"""
Deserialize a learning object dates response with a peer review sub-assignment.

``fixtures/learning_object_dates/date_details.json`` is shaped like
``GET /api/v1/courses/:course_id/assignments/:assignment_id/date_details``. It
was built by hand from the ``LearningObjectDates`` and ``AssignmentOverride``
``@model`` docs, because the seeded Canvas has no peer review sub-assignment
(it needs the hidden ``peer_review_allocation_and_grading`` flag), so it is not
verified against a live response.

If ``peer_review_sub_assignment`` (or ``User.permissions``) becomes an untyped
mapping again because nested object properties are dropped, these assertions fail.
"""

import json
import pathlib
import typing
from datetime import datetime

from canvas_lms_python_client.models import (
    AssignmentOverride,
    LearningObjectDates,
    LearningObjectDatesPeerReviewSubAssignment,
    User,
    UserPermissions,
)

FIXTURE = pathlib.Path(__file__).parent / "fixtures" / "learning_object_dates" / "date_details.json"

PAYLOAD = json.loads(FIXTURE.read_text())


def test_peer_review_sub_assignment_is_typed():
    dates = LearningObjectDates.from_dict(PAYLOAD)
    expected = PAYLOAD["peer_review_sub_assignment"]
    sub_assignment = dates.peer_review_sub_assignment

    assert isinstance(sub_assignment, LearningObjectDatesPeerReviewSubAssignment)
    assert sub_assignment.id == expected["id"]
    for field in ("due_at", "unlock_at", "lock_at"):
        assert getattr(sub_assignment, field) == datetime.fromisoformat(expected[field]), field
    assert sub_assignment.only_visible_to_overrides is expected["only_visible_to_overrides"]
    assert sub_assignment.visible_to_everyone is expected["visible_to_everyone"]


def test_peer_review_overrides_are_assignment_overrides():
    sub_assignment = LearningObjectDates.from_dict(PAYLOAD).peer_review_sub_assignment
    expected = PAYLOAD["peer_review_sub_assignment"]["overrides"]

    assert len(sub_assignment.overrides) == len(expected)
    for override, item in zip(sub_assignment.overrides, expected):
        assert isinstance(override, AssignmentOverride)
        assert override.id == item["id"]
        assert override.student_ids == item["student_ids"]
        assert override.due_at == datetime.fromisoformat(item["due_at"])


def _annotation_types(model, field):
    annotation = model.model_fields[field].annotation
    return [arg for arg in typing.get_args(annotation) if arg is not type(None)] or [annotation]


def test_nested_object_properties_are_models_not_dicts():
    assert _annotation_types(User, "permissions") == [UserPermissions]
    assert _annotation_types(LearningObjectDates, "peer_review_sub_assignment") == [
        LearningObjectDatesPeerReviewSubAssignment
    ]
