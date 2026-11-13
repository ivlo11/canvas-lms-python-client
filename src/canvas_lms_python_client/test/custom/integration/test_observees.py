"""
Integration tests for the observer -> observees -> courses -> assignments and
submissions flow.

Run against a seeded Canvas instance with a token belonging to an observer user:

    pdm run pytest --integration -m integration
"""

from collections import Counter
from typing import AsyncIterator, List, TypeVar

import pytest

from canvas_lms_python_client.api.assignments_api_api import AssignmentsApiApi
from canvas_lms_python_client.api.courses_api import CoursesApi
from canvas_lms_python_client.api.submissions_api_api import SubmissionsApiApi
from canvas_lms_python_client.api.user_observees_api import UserObserveesApi
from canvas_lms_python_client.models.assignment import Assignment
from canvas_lms_python_client.models.course import Course
from canvas_lms_python_client.models.submission import Submission
from canvas_lms_python_client.models.user import User

pytestmark = pytest.mark.integration

WORKFLOW_STATES = {"graded", "submitted", "unsubmitted", "pending_review"}

T = TypeVar("T")


async def collect(iterator: AsyncIterator[T]) -> List[T]:
    """Collect every item from an `_all` iterator into a list."""
    return [item async for item in iterator]


async def list_observees(api_client, per_page: int | None = None) -> List[User]:
    """List the authenticated observer's observees across all pages."""
    return await collect(
        UserObserveesApi(api_client).user_observees_index_all(user_id="self", per_page=per_page)
    )


async def list_courses(api_client, observee: User) -> List[Course]:
    """List an observee's courses across all pages."""
    return await collect(CoursesApi(api_client).courses_user_index_all(user_id=str(observee.id)))


async def test_observer_lists_observees(canvas_api_client):
    observees = await list_observees(canvas_api_client)

    assert observees, "observer has no observees"
    for observee in observees:
        assert isinstance(observee, User)
        assert isinstance(observee.id, int)
        assert observee.name


async def test_observees_pagination(canvas_api_client):
    default_ids = [o.id for o in await list_observees(canvas_api_client)]
    if len(default_ids) < 2:
        pytest.skip("observer needs at least 2 observees to exercise multi-page results")

    paged_ids = [o.id for o in await list_observees(canvas_api_client, per_page=1)]

    assert len(paged_ids) == len(set(paged_ids)), "duplicate observees across pages"
    assert set(paged_ids) == set(default_ids)


async def test_observee_courses(canvas_api_client):
    observees = await list_observees(canvas_api_client)
    assert observees, "observer has no observees"

    total_courses = 0
    for observee in observees:
        courses = await list_courses(canvas_api_client, observee)
        for course in courses:
            assert isinstance(course, Course)
            assert isinstance(course.id, int)
        total_courses += len(courses)

    assert total_courses > 0, "observer has observees but none have courses"


async def test_observee_course_assignments(canvas_api_client):
    observees = await list_observees(canvas_api_client)
    assert observees, "observer has no observees"

    assignments_api = AssignmentsApiApi(canvas_api_client)
    total_courses = 0
    total_assignments = 0
    for observee in observees:
        courses = await list_courses(canvas_api_client, observee)
        total_courses += len(courses)
        for course in courses:
            assignments = await collect(
                assignments_api.assignments_api_user_index_all(
                    user_id=str(observee.id), course_id=str(course.id)
                )
            )
            for assignment in assignments:
                assert isinstance(assignment, Assignment)
                assert isinstance(assignment.id, int)
                assert assignment.course_id == course.id
            total_assignments += len(assignments)

    assert total_courses > 0, "observer has observees but none have courses"
    assert total_assignments > 0, "observees have courses but none have assignments"


async def test_observee_submission_workflow_states(canvas_api_client):
    observees = await list_observees(canvas_api_client)
    assert observees, "observer has no observees"

    submissions_api = SubmissionsApiApi(canvas_api_client)
    counts = {}
    for observee in observees:
        submissions = []
        for course in await list_courses(canvas_api_client, observee):
            # A small page size spreads each course's submissions over several pages
            submissions += await collect(
                submissions_api.submissions_api_for_students_all(
                    course_id=str(course.id), student_ids=[str(observee.id)], per_page=10
                )
            )
        for submission in submissions:
            assert isinstance(submission, Submission)
            assert isinstance(submission.id, int)
            assert submission.user_id == observee.id
        ids = [s.id for s in submissions]
        assert len(ids) == len(set(ids)), f"duplicate submissions for observee {observee.id}"

        counts[observee.id] = Counter(s.workflow_state for s in submissions)
        assert sum(counts[observee.id].values()) == len(submissions)
        assert set(counts[observee.id]) <= WORKFLOW_STATES

    for observee_id, state_counts in counts.items():
        print(f"observee {observee_id}: {dict(state_counts)}")
    if not any(len(state_counts) >= 2 for state_counts in counts.values()):
        pytest.skip("no observee has submissions in more than one state")
