"""
Deserialize audit log pages, which are compound documents.

The course, grade change and authentication audit APIs return
``{"links": {...}, "events": [...], "linked": {...}}``. The course and grade
change operations were documented as event lists and failed on every page;
the authentication operations had no response type and returned ``None``.

The fixtures in ``fixtures/audit/`` were captured as an account admin from a
seeded Canvas (``--audit-events``):

- ``course.json``: ``GET /api/v1/audit/course/courses/5``
- ``grade_change.json``: ``GET /api/v1/audit/grade_change/courses/5``
- ``authentication.json``: ``GET /api/v1/audit/authentication/users/392``
  (the seeded second admin)

If an operation goes back to a list or untyped response, or an event model
loses a field or its Canvas type, these assertions fail.
"""

import inspect
import json
import pathlib
import re
from datetime import datetime

import pytest

from canvas_lms_python_client import api
from canvas_lms_python_client.api_client import ApiClient
from canvas_lms_python_client.models import (
    AuthenticationEvent,
    AuthenticationEventLinks,
    CourseEvent,
    CourseEventLink,
    GradeChangeEvent,
    GradeChangeEventLinks,
)

FIXTURES = pathlib.Path(__file__).parent / "fixtures" / "audit"

_RESPONSE_TYPE = re.compile(r"_response_types_map[^{]*\{\s*'[^']+':\s*\"([^\"]+)\"")


def _load(name):
    return json.loads((FIXTURES / f"{name}.json").read_text())


COURSE_PAGE = _load("course")
GRADE_CHANGE_PAGE = _load("grade_change")
AUTHENTICATION_PAGE = _load("authentication")

# Operation -> (API class, wrapper, event model, captured page)
AUDIT_OPERATIONS = {
    "course_audit_api_for_course": ("CourseAuditApiApi", "CourseAuditApiForCourseResponse", CourseEvent, COURSE_PAGE),
    "course_audit_api_for_account": ("CourseAuditApiApi", "CourseAuditApiForAccountResponse", CourseEvent, COURSE_PAGE),
    "grade_change_audit_api_for_assignment": (
        "GradeChangeAuditApiApi",
        "GradeChangeAuditApiForAssignmentResponse",
        GradeChangeEvent,
        GRADE_CHANGE_PAGE,
    ),
    "grade_change_audit_api_for_course": (
        "GradeChangeAuditApiApi",
        "GradeChangeAuditApiForCourseResponse",
        GradeChangeEvent,
        GRADE_CHANGE_PAGE,
    ),
    "grade_change_audit_api_for_student": (
        "GradeChangeAuditApiApi",
        "GradeChangeAuditApiForStudentResponse",
        GradeChangeEvent,
        GRADE_CHANGE_PAGE,
    ),
    "grade_change_audit_api_for_grader": (
        "GradeChangeAuditApiApi",
        "GradeChangeAuditApiForGraderResponse",
        GradeChangeEvent,
        GRADE_CHANGE_PAGE,
    ),
    "grade_change_audit_api_query": (
        "GradeChangeAuditApiApi",
        "GradeChangeAuditApiQueryResponse",
        GradeChangeEvent,
        GRADE_CHANGE_PAGE,
    ),
    "authentication_audit_api_for_account": (
        "AuthenticationAuditApiApi",
        "AuthenticationAuditApiForAccountResponse",
        AuthenticationEvent,
        AUTHENTICATION_PAGE,
    ),
    "authentication_audit_api_for_login": (
        "AuthenticationAuditApiApi",
        "AuthenticationAuditApiForLoginResponse",
        AuthenticationEvent,
        AUTHENTICATION_PAGE,
    ),
    "authentication_audit_api_for_user": (
        "AuthenticationAuditApiApi",
        "AuthenticationAuditApiForUserResponse",
        AuthenticationEvent,
        AUTHENTICATION_PAGE,
    ),
}


def _response_type(api_class, operation):
    source = inspect.getsource(getattr(getattr(api, api_class), operation))
    match = _RESPONSE_TYPE.search(source)
    assert match, f"{api_class}.{operation} has no response type"
    return match.group(1)


def _deserialize(payload, response_type):
    return ApiClient().deserialize(json.dumps(payload), response_type, "application/json")


def _parse_datetime(value):
    return None if value is None else datetime.fromisoformat(value)


def test_fixtures_have_data():
    for page in (COURSE_PAGE, GRADE_CHANGE_PAGE, AUTHENTICATION_PAGE):
        assert set(page) == {"links", "events", "linked"}
        assert page["events"]
    assert any(event["links"]["grader"] for event in GRADE_CHANGE_PAGE["events"])


@pytest.mark.parametrize("operation", sorted(AUDIT_OPERATIONS))
def test_page_deserializes_to_its_wrapper(operation):
    api_class, wrapper, event_model, page = AUDIT_OPERATIONS[operation]
    assert _response_type(api_class, operation) == wrapper

    response = _deserialize(page, wrapper)

    assert type(response).__name__ == wrapper
    assert response.links == page["links"]
    assert response.linked == page["linked"]
    assert len(response.events) == len(page["events"])
    assert all(isinstance(event, event_model) for event in response.events)


@pytest.mark.parametrize("operation", sorted(AUDIT_OPERATIONS))
def test_paginated_yields_wrapper_pages_and_no_all(operation):
    api_class, wrapper, _, _ = AUDIT_OPERATIONS[operation]
    api_type = getattr(api, api_class)

    paginated = inspect.signature(getattr(api_type, f"{operation}_paginated"))
    assert wrapper in str(paginated.return_annotation)
    assert not hasattr(api_type, f"{operation}_all")


@pytest.mark.parametrize("operation", sorted(AUDIT_OPERATIONS))
def test_empty_page(operation):
    api_class, wrapper, _, _ = AUDIT_OPERATIONS[operation]

    response = _deserialize({"links": {}, "events": [], "linked": {}}, wrapper)

    assert response.events == []


@pytest.mark.parametrize("item", COURSE_PAGE["events"], ids=lambda item: item["id"])
def test_course_event_links_are_strings(item):
    event = CourseEvent.from_dict(item)

    assert event.id == item["id"]
    assert event.event_type == item["event_type"]
    assert event.created_at == _parse_datetime(item["created_at"])
    assert event.event_data == item["event_data"]
    assert isinstance(event.links, CourseEventLink)
    for key in ("course", "user", "page_view", "sis_batch"):
        assert getattr(event.links, key) == item["links"][key]
        assert isinstance(getattr(event.links, key), str)


def test_copied_to_course_event():
    """Copy and reset events add integer course ids to links, with empty event data."""
    item = {
        "id": "a8c2f1d0-1111-4b1a-9a7e-000000000001",
        "created_at": "2026-11-03T03:44:39Z",
        "event_type": "copied_to",
        "event_source": "manual",
        "event_data": {},
        "links": {"copied_to": 12, "course": "5", "page_view": "", "user": "392", "sis_batch": ""},
    }

    links = CourseEvent.from_dict(item).links

    assert links.copied_to == 12
    assert links.course == "5"
    assert links.sis_batch == ""


def test_reset_from_course_event():
    item = {
        "id": "a8c2f1d0-1111-4b1a-9a7e-000000000002",
        "created_at": "2026-11-03T03:44:39Z",
        "event_type": "reset_from",
        "event_source": "manual",
        "event_data": {},
        "links": {"reset_from": 11, "course": "5", "page_view": "", "user": "392", "sis_batch": ""},
    }

    assert CourseEvent.from_dict(item).links.reset_from == 11


@pytest.mark.parametrize("item", GRADE_CHANGE_PAGE["events"], ids=lambda item: item["id"])
def test_grade_change_event_keeps_canvas_types(item):
    event = GradeChangeEvent.from_dict(item)

    assert event.id == item["id"]
    assert event.version_number == item["version_number"]
    assert isinstance(event.version_number, int)
    assert event.points_possible_before == item["points_possible_before"]
    assert event.points_possible_after == item["points_possible_after"]
    assert event.grade_after == item["grade_after"]
    assert event.excused_after is item["excused_after"]
    assert isinstance(event.links, GradeChangeEventLinks)
    assert event.links.course == item["links"]["course"]
    assert event.links.assignment == item["links"]["assignment"]
    assert event.links.student == item["links"]["student"]
    assert event.links.grader == item["links"]["grader"]


def test_override_grade_event():
    """Override grade events add course_override_grade, and current_grade adds grade_current."""
    item = dict(GRADE_CHANGE_PAGE["events"][0])
    item.update(grade_current="B+", course_override_grade=True, links={**item["links"], "assignment": None})

    event = GradeChangeEvent.from_dict(item)

    assert event.course_override_grade is True
    assert event.grade_current == "B+"
    assert event.links.assignment is None


@pytest.mark.parametrize("item", AUTHENTICATION_PAGE["events"], ids=lambda item: item["id"])
def test_authentication_event_keeps_canvas_fields(item):
    event = AuthenticationEvent.from_dict(item)

    assert event.id == item["id"]
    assert event.event_type == item["event_type"]
    assert event.created_at == _parse_datetime(item["created_at"])
    assert isinstance(event.links, AuthenticationEventLinks)
    assert event.links.login == item["links"]["login"]
    assert event.links.account == item["links"]["account"]
    assert event.links.user == item["links"]["user"]
    assert event.links.page_view == item["links"]["page_view"]
