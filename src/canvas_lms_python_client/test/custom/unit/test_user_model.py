"""
Deserialize show user details responses captured from a seeded Canvas.

``fixtures/users/users_self.json`` holds ``GET /api/v1/users/:id?include[]=uuid&include[]=last_login``
as the observer, the student and the second admin reading ``self``, and as the
second admin reading the student. If ``User`` loses the fields the operation
always sends (``permissions``, ``effective_locale``) or its ``uuid``, the values
Canvas sent are dropped and these assertions fail.
"""

import json
import pathlib

import pytest

from canvas_lms_python_client.models import User

FIXTURE = pathlib.Path(__file__).parent / "fixtures" / "users" / "users_self.json"

PAYLOAD = json.loads(FIXTURE.read_text())


def test_fixture_covers_self_and_another_user():
    assert sum("effective_locale" in item for item in PAYLOAD) == 3
    assert any("effective_locale" not in item for item in PAYLOAD)


@pytest.mark.parametrize("item", PAYLOAD, ids=lambda item: f"user-{item['id']}")
def test_user_keeps_show_user_details_fields(item):
    user = User.from_dict(item)

    assert user.id == item["id"]
    assert user.name == item["name"]
    assert user.uuid == item["uuid"]
    assert user.permissions == item["permissions"]
    assert user.permissions["can_update_name"] == item["permissions"]["can_update_name"]
    assert user.effective_locale == item.get("effective_locale")
