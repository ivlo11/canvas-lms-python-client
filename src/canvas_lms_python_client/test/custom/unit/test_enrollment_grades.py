"""
Deserialize a seeded student's course enrollments and grades captured from Canvas.

Both fixtures were captured with an account admin's token, so they carry the
``unposted_*`` fields that only teachers, TAs and admins see:

- ``fixtures/enrollments/courses_total_scores.json`` is
  ``GET /api/v1/users/:id/courses?include[]=total_scores&include[]=current_grading_period_scores``.
- ``fixtures/enrollments/enrollments_with_grades.json`` is
  ``GET /api/v1/courses/:id/enrollments?user_id=:id``, whose items carry ``grades``.

If ``Enrollment`` drops the ``computed_*`` fields, types a score as a string, or
``Grade`` is replaced by another ``@model`` named ``Grade``, these assertions fail.
"""

import json
import pathlib

import pytest

from canvas_lms_python_client.models import Course, Enrollment, Grade

FIXTURES = pathlib.Path(__file__).parent / "fixtures" / "enrollments"

COURSES = json.loads((FIXTURES / "courses_total_scores.json").read_text())
ENROLLMENTS = json.loads((FIXTURES / "enrollments_with_grades.json").read_text())

COURSE_ENROLLMENTS = [enrollment for course in COURSES for enrollment in course["enrollments"]]

SCORE_FIELDS = [
    "computed_current_score",
    "computed_final_score",
    "unposted_current_score",
    "unposted_final_score",
    "current_period_computed_current_score",
    "current_period_computed_final_score",
    "current_period_unposted_current_score",
    "current_period_unposted_final_score",
]

GRADE_FIELDS = [
    "computed_current_grade",
    "computed_final_grade",
    "unposted_current_grade",
    "unposted_final_grade",
    "current_period_computed_current_grade",
    "current_period_computed_final_grade",
    "current_period_unposted_current_grade",
    "current_period_unposted_final_grade",
]


def test_fixtures_have_a_letter_grade_and_unposted_scores():
    assert any(item["computed_current_grade"] for item in COURSE_ENROLLMENTS)
    assert all(isinstance(item["unposted_final_score"], float) for item in COURSE_ENROLLMENTS)


@pytest.mark.parametrize("item", COURSES, ids=lambda item: f"course-{item['id']}")
def test_course_with_total_scores_deserializes(item):
    course = Course.from_dict(item)

    assert course.id == item["id"]
    assert len(course.enrollments) == len(item["enrollments"])


@pytest.mark.parametrize("item", COURSE_ENROLLMENTS, ids=lambda item: f"user-{item['user_id']}")
def test_course_enrollment_keeps_scores_and_grades(item):
    enrollment = Enrollment.from_dict(item)

    for field in SCORE_FIELDS:
        value = getattr(enrollment, field)
        assert value == item[field], field
        assert value is None or isinstance(value, float), field
    for field in GRADE_FIELDS:
        assert getattr(enrollment, field) == item[field], field


@pytest.mark.parametrize("item", ENROLLMENTS, ids=lambda item: f"enrollment-{item['id']}")
def test_enrollment_grades_use_the_enrollment_grade_model(item):
    enrollment = Enrollment.from_dict(item)

    assert isinstance(enrollment.grades, Grade)
    assert enrollment.grades.html_url == item["grades"]["html_url"]
    assert enrollment.grades.current_grade == item["grades"]["current_grade"]
    assert enrollment.grades.current_score == item["grades"]["current_score"]
    assert enrollment.grades.final_score == item["grades"]["final_score"]
    assert enrollment.grades.unposted_current_score == item["grades"]["unposted_current_score"]
