"""
Deserialize list responses that had no @returns in canvas-lms.

The fixtures in ``fixtures/simple_lists/`` were captured as a seeded account
admin from a seeded Canvas (``--module-progress``, ``--course-pacing`` and
``--conversation-batch``):

- ``logins.json``: ``GET /api/v1/users/:id/logins`` for two seeded users
- ``conversation_batches.json``: ``GET /api/v1/conversations/batches``
- ``bulk_user_progress.json``: ``GET /api/v1/courses/:id/bulk_user_progress``
- ``gradeable_students.json``: ``GET /api/v1/courses/:id/assignments/gradeable_students``
  with two ``assignment_ids[]``
- ``pace_contexts_course.json`` and ``pace_contexts_student_enrollment.json``:
  ``GET /api/v1/courses/:id/pace_contexts`` with ``type=course`` and
  ``type=student_enrollment``

If one of these models loses a field, or the operations go back to untyped
responses, these assertions fail.
"""

import json
import pathlib
from datetime import datetime

import pytest

from canvas_lms_python_client.models import (
    AppliedPace,
    ConversationBatch,
    CourseProgress,
    Login,
    MultipleGradeableStudent,
    PaceContext,
    PaceContextsApiIndexResponse,
    UserProgress,
)

FIXTURES = pathlib.Path(__file__).parent / "fixtures" / "simple_lists"


def _load(name):
    return json.loads((FIXTURES / f"{name}.json").read_text())


def _parse_datetime(value):
    return None if value is None else datetime.fromisoformat(value)


USER_DISPLAY_FIELDS = ["id", "anonymous_id", "display_name", "avatar_image_url", "html_url", "pronouns"]


@pytest.mark.parametrize("item", _load("logins"), ids=lambda item: f"login-{item['id']}")
def test_login_keeps_canvas_fields(item):
    login = Login.from_dict(item)

    for field in ["id", "user_id", "account_id", "unique_id", "workflow_state", "authentication_provider_id"]:
        assert getattr(login, field) == item[field], field
    assert login.created_at == _parse_datetime(item["created_at"])


def test_conversation_batch_keeps_canvas_fields():
    (item,) = _load("conversation_batches")

    batch = ConversationBatch.from_dict(item)

    assert batch.id == item["id"]
    assert batch.workflow_state == item["workflow_state"]
    assert batch.completion == item["completion"]
    assert batch.recipient_count == item["recipient_count"]
    assert batch.tags == item["tags"]
    assert batch.message == item["message"]


@pytest.mark.parametrize("item", _load("bulk_user_progress"), ids=lambda item: f"user-{item['id']}")
def test_user_progress_keeps_canvas_fields(item):
    progress = UserProgress.from_dict(item)

    for field in USER_DISPLAY_FIELDS:
        assert getattr(progress, field) == item[field], field
    assert isinstance(progress.progress, CourseProgress)
    assert progress.progress.requirement_count == item["progress"]["requirement_count"]
    assert progress.progress.requirement_completed_count == item["progress"]["requirement_completed_count"]
    assert progress.progress.completed_at == _parse_datetime(item["progress"]["completed_at"])


def test_user_progress_accepts_a_progress_error():
    """Canvas sends {error: {message}} as progress when it can't be evaluated."""
    item = dict(_load("bulk_user_progress")[0], progress={"error": {"message": "unavailable"}})

    progress = UserProgress.from_dict(item)

    assert isinstance(progress.progress, CourseProgress)
    assert progress.progress.requirement_count is None


@pytest.mark.parametrize("item", _load("gradeable_students"), ids=lambda item: f"student-{item['id']}")
def test_gradeable_student_keeps_canvas_fields(item):
    student = MultipleGradeableStudent.from_dict(item)

    for field in USER_DISPLAY_FIELDS:
        assert getattr(student, field) == item[field], field
    assert student.assignment_ids == item["assignment_ids"]
    assert all(isinstance(assignment_id, int) for assignment_id in student.assignment_ids)


@pytest.mark.parametrize("name", ["pace_contexts_course", "pace_contexts_student_enrollment"])
def test_pace_contexts_page_keeps_canvas_fields(name):
    payload = _load(name)

    page = PaceContextsApiIndexResponse.from_dict(payload)

    assert page.total_entries == payload["total_entries"]
    assert len(page.pace_contexts) == len(payload["pace_contexts"])
    for context, item in zip(page.pace_contexts, payload["pace_contexts"]):
        assert isinstance(context, PaceContext)
        for field in ["name", "type", "item_id", "associated_section_count", "associated_student_count", "on_pace"]:
            assert getattr(context, field) == item[field], field
        assert isinstance(context.applied_pace, AppliedPace)
        assert context.applied_pace.name == item["applied_pace"]["name"]
        assert context.applied_pace.type == item["applied_pace"]["type"]
        assert context.applied_pace.duration == item["applied_pace"]["duration"]
        assert context.applied_pace.last_modified == _parse_datetime(item["applied_pace"]["last_modified"])
