"""
Deserialize discussion entry and recipient lists, which had no @returns in canvas-lms.

The fixtures in ``fixtures/discussions/`` were captured from a seeded Canvas
(``--discussion-entries``):

- ``topic_entries.json``: ``GET /api/v1/courses/:id/discussion_topics/:id/entries``
  (a root entry with an attachment and a recent reply), as a seeded account admin
- ``entry_replies.json``: ``GET .../entries/:id/replies``, as a seeded account admin
- ``entry_list.json``: ``GET .../entry_list?ids[]=…`` with the root, the reply and a
  deleted entry, as a seeded account admin
- ``user_recipients.json``: ``GET /api/v1/search/recipients?search=a``, as a seeded
  account admin (users only; the admin has no enrollments)
- ``context_recipients.json``: ``GET /api/v1/search/recipients?type=context&search=``,
  as the seeded student

If these models lose a field, or the operations go back to untyped responses,
these assertions fail.
"""

import importlib
import json
import pathlib
import typing
from datetime import datetime

import pytest

from canvas_lms_python_client.models import DiscussionEntry, Recipient

FIXTURES = pathlib.Path(__file__).parent / "fixtures" / "discussions"


def _load(name):
    return json.loads((FIXTURES / f"{name}.json").read_text())


def _parse_datetime(value):
    return None if value is None else datetime.fromisoformat(value)


TOPIC_ENTRIES = _load("topic_entries")
ENTRY_REPLIES = _load("entry_replies")
ENTRY_LIST = _load("entry_list")
USER_RECIPIENTS = _load("user_recipients")
CONTEXT_RECIPIENTS = _load("context_recipients")

ALL_ENTRIES = TOPIC_ENTRIES + ENTRY_REPLIES + ENTRY_LIST

# Paginated operation -> page item type
LIST_ITEM_TYPES = {
    "discussion_topics_api.DiscussionTopicsApiApi": {
        "discussion_topics_api_entries": "DiscussionEntry",
        "discussion_topics_api_entries_for_groups": "DiscussionEntry",
        "discussion_topics_api_entry_list": "DiscussionEntry",
        "discussion_topics_api_entry_list_for_groups": "DiscussionEntry",
        "discussion_topics_api_replies": "DiscussionEntry",
        "discussion_topics_api_replies_for_groups": "DiscussionEntry",
    },
    "search.SearchApi": {
        "search_recipients": "Recipient",
        "search_recipients_for_other": "Recipient",
    },
}


def _api_class(path):
    module_name, class_name = path.rsplit(".", 1)
    module = importlib.import_module(f"canvas_lms_python_client.api.{module_name}_api")
    return getattr(module, class_name)


def _item_type(func):
    (iterator_item,) = typing.get_args(func.__annotations__["return"])
    return iterator_item.__name__


@pytest.mark.parametrize("path", LIST_ITEM_TYPES)
def test_all_iterators_yield_models(path):
    cls = _api_class(path)

    item_types = {
        operation: _item_type(getattr(cls, f"{operation}_all"))
        for operation in LIST_ITEM_TYPES[path]
    }

    assert item_types == LIST_ITEM_TYPES[path]


def test_fixtures_have_data():
    root = TOPIC_ENTRIES[0]
    assert root["recent_replies"] and root["attachment"]
    assert ENTRY_REPLIES[0]["parent_id"] == root["id"]
    assert any(entry.get("deleted") for entry in ENTRY_LIST)
    assert all(isinstance(item["id"], int) for item in USER_RECIPIENTS)
    assert all(
        item["type"] == "context" and isinstance(item["id"], str) for item in CONTEXT_RECIPIENTS
    )
    assert USER_RECIPIENTS and CONTEXT_RECIPIENTS


def assert_entry_matches(entry, item):
    assert isinstance(entry, DiscussionEntry)
    assert entry.id == item["id"]
    assert entry.parent_id == item["parent_id"]
    assert entry.user_id == item.get("user_id")
    assert entry.user_name == item.get("user_name")
    assert entry.message == item.get("message")
    assert entry.deleted == item.get("deleted")
    assert entry.created_at == _parse_datetime(item["created_at"])
    assert entry.updated_at == _parse_datetime(item["updated_at"])
    assert entry.read_state == item["read_state"]
    assert entry.forced_read_state is item["forced_read_state"]
    assert entry.user == item["user"]
    assert entry.attachment == item.get("attachment")
    assert entry.attachments == item.get("attachments")
    assert entry.has_more_replies == item.get("has_more_replies")
    assert len(entry.recent_replies or []) == len(item.get("recent_replies", []))
    for reply, reply_item in zip(entry.recent_replies or [], item.get("recent_replies", [])):
        assert_entry_matches(reply, reply_item)


@pytest.mark.parametrize("item", ALL_ENTRIES, ids=lambda item: f"entry-{item['id']}")
def test_discussion_entry_keeps_canvas_fields(item):
    assert_entry_matches(DiscussionEntry.from_dict(item), item)


def test_root_entry_has_typed_replies_and_attachment():
    root = DiscussionEntry.from_dict(TOPIC_ENTRIES[0])

    assert root.recent_replies and all(
        isinstance(reply, DiscussionEntry) for reply in root.recent_replies
    )
    assert root.recent_replies[0].parent_id == root.id
    assert root.attachment["id"] and root.attachment["display_name"]


def test_deleted_entry_has_no_message():
    (deleted,) = [DiscussionEntry.from_dict(item) for item in ENTRY_LIST if item.get("deleted")]

    assert deleted.deleted is True
    assert deleted.message is None and deleted.user_id is None


def test_nested_recent_replies_deserialize():
    """recent_replies refers to DiscussionEntry itself, so two levels parse."""
    reply = {**ENTRY_REPLIES[0], "recent_replies": [ENTRY_REPLIES[0]], "has_more_replies": False}
    root = {**TOPIC_ENTRIES[0], "recent_replies": [reply]}

    entry = DiscussionEntry.from_dict(root)

    assert isinstance(entry.recent_replies[0].recent_replies[0], DiscussionEntry)
    assert DiscussionEntry.from_dict(entry.to_dict()) == entry


@pytest.mark.parametrize(
    "item", USER_RECIPIENTS + CONTEXT_RECIPIENTS, ids=lambda item: f"recipient-{item['id']}"
)
def test_recipient_keeps_canvas_fields(item):
    recipient = Recipient.from_dict(item)

    assert isinstance(recipient, Recipient)
    assert recipient.id == item["id"]
    assert type(recipient.id) is type(item["id"])
    assert recipient.name == item["name"]
    assert recipient.avatar_url == item["avatar_url"]
    assert recipient.full_name == item.get("full_name")
    assert recipient.pronouns == item.get("pronouns")
    assert recipient.common_courses == item.get("common_courses")
    assert recipient.common_groups == item.get("common_groups")
    assert recipient.type == item.get("type")
    assert recipient.user_count == item.get("user_count")
    assert recipient.item_count == item.get("item_count")
    assert recipient.permissions == item.get("permissions")
    assert recipient.context_name == item.get("context_name")


def test_synthetic_context_recipient_has_item_count():
    """Sub-contexts such as course_5_groups carry item_count instead of user_count."""
    recipient = Recipient.from_dict(
        {
            "id": "course_2_groups",
            "name": "Student Groups",
            "avatar_url": "http://canvas.docker/images/messages/avatar-group-50.png",
            "type": "context",
            "item_count": 2,
            "context_name": "Advanced Pokeball Mechanics",
        }
    )

    assert recipient.id == "course_2_groups"
    assert recipient.item_count == 2 and recipient.user_count is None
