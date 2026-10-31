"""
Guard against paginated operations with no documented response type.

A ``*_paginated`` method whose ``_response_types_map`` is empty deserializes
every page to ``None`` and stops without yielding anything. Every such
operation must be listed in ``UNDOCUMENTED_PAGINATED_OPERATIONS``; the list
should only shrink as ``@returns`` annotations are added in canvas-lms.
"""

import importlib
import inspect
import pkgutil
import re

import canvas_lms_python_client.api

PAGINATED_SUFFIX = "_paginated"
MIN_PAGINATED_METHODS = 150

_EMPTY_TYPES_MAP = re.compile(
    r"_response_types_map\s*:\s*Dict\[str,\s*Optional\[str\]\]\s*=\s*\{\s*\}"
)

UNDOCUMENTED_PAGINATED_OPERATIONS = frozenset(
    {
        "authentication_audit_api_for_account",
        "authentication_audit_api_for_login",
        "authentication_audit_api_for_user",
        "conversations_batches",
        "courses_bulk_user_progress",
        "courses_todo_items",
        "discussion_topics_api_entries",
        "discussion_topics_api_entries_for_groups",
        "discussion_topics_api_entry_list",
        "discussion_topics_api_entry_list_for_groups",
        "discussion_topics_api_replies",
        "discussion_topics_api_replies_for_groups",
        "grading_period_sets_index",
        "outcome_results_index",
        "pace_contexts_api_index",
        "planner_index",
        "planner_index_for_users",
        "poll_choices_index",
        "poll_sessions_closed",
        "poll_sessions_index",
        "poll_sessions_opened",
        "polls_index",
        "pseudonyms_index",
        "pseudonyms_index_for_users",
        "quiz_ip_filters_index",
        "quiz_submission_events_api_index",
        "quiz_submissions_api_index",
        "search_all_courses",
        "search_recipients",
        "search_recipients_for_other",
        "service_credentials_todo_items",
        "submissions_api_multiple_gradeable_students",
    }
)


def _paginated_methods():
    """Yield (operation name, function) for every generated ``*_paginated`` method."""
    package = canvas_lms_python_client.api
    for module_info in pkgutil.iter_modules(package.__path__):
        module = importlib.import_module(f"{package.__name__}.{module_info.name}")
        for _, cls in inspect.getmembers(module, inspect.isclass):
            if cls.__module__ != module.__name__:
                continue
            for name, func in inspect.getmembers(cls, inspect.isfunction):
                if name.endswith(PAGINATED_SUFFIX):
                    yield name[: -len(PAGINATED_SUFFIX)], func


def _undocumented_operations():
    found = 0
    undocumented = set()
    for operation, func in _paginated_methods():
        found += 1
        if _EMPTY_TYPES_MAP.search(inspect.getsource(func)):
            undocumented.add(operation)
    return found, undocumented


def test_paginated_operations_have_response_types():
    """Every paginated operation has a response type unless allowlisted."""
    found, undocumented = _undocumented_operations()

    assert found >= MIN_PAGINATED_METHODS, (
        f"Only {found} *_paginated methods found; the generated method "
        "format may have changed and the scan no longer matches."
    )

    unlisted = sorted(undocumented - UNDOCUMENTED_PAGINATED_OPERATIONS)
    stale = sorted(UNDOCUMENTED_PAGINATED_OPERATIONS - undocumented)
    assert not unlisted, (
        "Paginated operations with no response type (add @returns in "
        f"canvas-lms or allowlist them): {unlisted}"
    )
    assert not stale, (
        "Allowlisted operations now have a response type; remove them from "
        f"UNDOCUMENTED_PAGINATED_OPERATIONS: {stale}"
    )
