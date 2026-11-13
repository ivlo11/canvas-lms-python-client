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

Grade change and authentication pages type ``linked``. Course audit ``linked``
stays a mapping, because ``CourseEvent#linked_json`` stringifies its record ids,
which ``Course`` and ``User`` reject.

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
    Account,
    Assignment,
    AuthenticationEvent,
    AuthenticationEventLinks,
    AuthenticationLinkedRecords,
    Course,
    CourseEvent,
    CourseEventLink,
    GradeChangeEvent,
    GradeChangeEventLinks,
    GradeChangeLinkedRecords,
    Login,
    PageView,
    PageViewLinks,
    User,
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

# Event model -> (linked records model, linked list -> item model)
LINKED_RECORDS = {
    GradeChangeEvent: (
        GradeChangeLinkedRecords,
        {"page_views": PageView, "assignments": Assignment, "courses": Course, "users": User},
    ),
    AuthenticationEvent: (
        AuthenticationLinkedRecords,
        {"logins": Login, "accounts": Account, "users": User, "page_views": PageView},
    ),
}

TYPED_LINKED_OPERATIONS = sorted(op for op, spec in AUDIT_OPERATIONS.items() if spec[2] in LINKED_RECORDS)
UNTYPED_LINKED_OPERATIONS = sorted(op for op, spec in AUDIT_OPERATIONS.items() if spec[2] not in LINKED_RECORDS)

# What page_view_json sends; dev Canvas records no page views to capture
PAGE_VIEW = {
    "id": "3e246700-e305-0130-51de-02e33aa501ef",
    "session_id": "0ca9e5e58964bc58d4c1a0a8df509805",
    "url": "http://canvas.docker/courses/5/gradebook",
    "context_type": "Course",
    "asset_type": "Assignment",
    "controller": "gradebooks",
    "action": "update_submission",
    "interaction_seconds": 5.0,
    "created_at": "2026-11-03T03:44:39Z",
    "updated_at": "2026-11-03T03:44:39Z",
    "developer_key_id": None,
    "user_request": True,
    "render_time": 0.369,
    "user_agent": "Mozilla/5.0",
    "asset_user_access_id": None,
    "participated": True,
    "summarized": False,
    "http_method": "post",
    "remote_ip": "127.0.0.1",
    "contributed": False,
    "links": {"user": 167, "context": 5, "asset": 52, "real_user": None, "account": 1},
    "app_name": None,
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


@pytest.mark.parametrize("operation", TYPED_LINKED_OPERATIONS)
def test_empty_linked_has_unset_lists(operation):
    _, wrapper, event_model, _ = AUDIT_OPERATIONS[operation]
    linked_model, lists = LINKED_RECORDS[event_model]

    response = _deserialize({"links": {}, "events": [], "linked": {}}, wrapper)

    assert isinstance(response.linked, linked_model)
    assert all(getattr(response.linked, key) is None for key in lists)


@pytest.mark.parametrize("operation", TYPED_LINKED_OPERATIONS)
def test_linked_records_are_typed(operation):
    _, wrapper, event_model, page = AUDIT_OPERATIONS[operation]
    linked_model, lists = LINKED_RECORDS[event_model]

    linked = _deserialize(page, wrapper).linked

    assert isinstance(linked, linked_model)
    assert set(lists) == set(page["linked"])
    for key, item_model in lists.items():
        items = getattr(linked, key)
        assert all(isinstance(item, item_model) for item in items)
        assert [item.id for item in items] == [raw["id"] for raw in page["linked"][key]]


@pytest.mark.parametrize("operation", UNTYPED_LINKED_OPERATIONS)
def test_course_audit_linked_stays_a_mapping(operation):
    _, wrapper, _, page = AUDIT_OPERATIONS[operation]

    linked = _deserialize(page, wrapper).linked

    assert linked == page["linked"]
    assert isinstance(linked["users"][0]["id"], str)


def test_grade_change_event_links_resolve_in_linked():
    response = _deserialize(GRADE_CHANGE_PAGE, "GradeChangeAuditApiForCourseResponse")
    linked = response.linked
    user_ids = {user.id for user in linked.users}

    for event in response.events:
        assert event.links.assignment in {assignment.id for assignment in linked.assignments}
        assert event.links.course in {course.id for course in linked.courses}
        assert int(event.links.student) in user_ids
        assert event.links.grader is None or int(event.links.grader) in user_ids


def test_authentication_event_links_resolve_in_linked():
    response = _deserialize(AUTHENTICATION_PAGE, "AuthenticationAuditApiForUserResponse")
    linked = response.linked

    for event in response.events:
        assert event.links.login in {login.id for login in linked.logins}
        assert event.links.account in {account.id for account in linked.accounts}
        assert event.links.user in {user.id for user in linked.users}


@pytest.mark.parametrize("linked_model", [GradeChangeLinkedRecords, AuthenticationLinkedRecords])
def test_linked_page_view_is_typed(linked_model):
    page_view = linked_model.from_dict({"page_views": [PAGE_VIEW]}).page_views[0]

    assert isinstance(page_view, PageView)
    assert str(page_view.id) == PAGE_VIEW["id"]
    assert page_view.url == PAGE_VIEW["url"]
    assert page_view.session_id == PAGE_VIEW["session_id"]
    assert isinstance(page_view.links, PageViewLinks)
    assert page_view.links.user == PAGE_VIEW["links"]["user"]
    assert page_view.links.real_user is None


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
