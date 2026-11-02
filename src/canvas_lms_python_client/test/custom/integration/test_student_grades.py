"""
Integration tests for a student listing their own courses with computed grades.

Run against a seeded Canvas instance with a token belonging to a student user
(printed by the seed script's ``--tokens`` option):

    CANVAS_STUDENT_API_TOKEN=... pdm run pytest --integration -m integration
"""

import pytest

from canvas_lms_python_client.api.courses_api import CoursesApi
from canvas_lms_python_client.api.users_api import UsersApi
from canvas_lms_python_client.models.course import Course

pytestmark = pytest.mark.integration

# Canvas's default grading scheme
DEFAULT_SCHEME_LETTERS = {"A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F"}


async def test_student_courses_computed_grades(canvas_student_api_client):
    # users_api_show is untyped (@returns Schemas::Docs::User), so it's a dict
    student = await UsersApi(canvas_student_api_client).users_api_show(id="self")
    student_id = student["id"]
    courses = [
        course
        async for course in CoursesApi(canvas_student_api_client).courses_index_all(
            include=["total_scores"], per_page=10
        )
    ]

    assert courses, "student has no courses"

    graded = []
    for course in courses:
        assert isinstance(course, Course)
        enrollments = [
            enrollment
            for enrollment in course.enrollments or []
            if enrollment.type == "student" and enrollment.user_id == student_id
        ]
        for enrollment in enrollments:
            score, grade = enrollment.computed_current_score, enrollment.computed_current_grade
            assert score is None or isinstance(score, float)
            assert grade is None or (isinstance(grade, str) and grade)
            if enrollment.grades and enrollment.grades.current_score is not None and score is not None:
                assert enrollment.grades.current_score == score
            print(f"\n{course.name} ({course.id}): grade {grade}, score {score}")
            if grade is not None:
                graded.append((course, grade, score))

    if not graded:
        pytest.skip("no seeded course uses a grading scheme (run the seed script with --grading-scheme)")
    assert any(grade in DEFAULT_SCHEME_LETTERS for _, grade, _ in graded)
    assert all(isinstance(score, float) for _, _, score in graded)
