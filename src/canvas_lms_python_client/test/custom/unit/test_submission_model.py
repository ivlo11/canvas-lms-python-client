"""
Deserialize an observee's submissions captured from a seeded Canvas.

``fixtures/submissions/observee_submissions.json`` is what an observer received
from ``GET /api/v1/courses/:course_id/students/submissions`` for one observee.
If ``Submission`` loses fields again (for example, when another ``@model``
named ``Submission`` replaces the full one), the values Canvas sent are dropped
and these assertions fail.
"""

import json
import pathlib
from datetime import datetime

import pytest

from canvas_lms_python_client.models import Submission

FIXTURE = pathlib.Path(__file__).parent / "fixtures" / "submissions" / "observee_submissions.json"

PAYLOAD = json.loads(FIXTURE.read_text())


def _parse_datetime(value):
    return None if value is None else datetime.fromisoformat(value)


def test_fixture_covers_every_workflow_state():
    assert {item["workflow_state"] for item in PAYLOAD} == {
        "graded",
        "submitted",
        "unsubmitted",
        "pending_review",
    }


@pytest.mark.parametrize("item", PAYLOAD, ids=lambda item: f"submission-{item['id']}")
def test_submission_keeps_canvas_fields(item):
    submission = Submission.from_dict(item)

    assert submission.id == item["id"]
    assert submission.workflow_state == item["workflow_state"]
    assert submission.assignment_id == item["assignment_id"]
    assert submission.user_id == item["user_id"]
    assert submission.submitted_at == _parse_datetime(item["submitted_at"])
    assert submission.grade == item.get("grade")
