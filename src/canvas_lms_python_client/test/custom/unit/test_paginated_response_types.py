"""
Guard against paginated operations with no documented response type.

A ``*_paginated`` method whose ``_response_types_map`` is empty deserializes
every page to ``None`` and stops without yielding anything. Every such
operation must be listed in ``UNDOCUMENTED_PAGINATED_OPERATIONS``; the list
should only shrink as ``@returns`` annotations are added in canvas-lms.

A ``*_all`` item iterator is only generated when a page is a list; wrapper,
object and undocumented responses get ``*_paginated`` only.
"""

import importlib
import inspect
import json
import pathlib
import pkgutil
import re
import typing

import pytest

import canvas_lms_python_client.api
import canvas_lms_python_client.models

PAGINATED_SUFFIX = "_paginated"
ALL_SUFFIX = "_all"
MIN_PAGINATED_METHODS = 150

_EMPTY_TYPES_MAP = re.compile(
    r"_response_types_map\s*:\s*Dict\[str,\s*Optional\[str\]\]\s*=\s*\{\s*\}"
)

UNDOCUMENTED_PAGINATED_OPERATIONS: frozenset[str] = frozenset()


def _paginated_methods():
    """Yield (API class, operation name, function) for every ``*_paginated`` method."""
    package = canvas_lms_python_client.api
    for module_info in pkgutil.iter_modules(package.__path__):
        module = importlib.import_module(f"{package.__name__}.{module_info.name}")
        for _, cls in inspect.getmembers(module, inspect.isclass):
            if cls.__module__ != module.__name__:
                continue
            for name, func in inspect.getmembers(cls, inspect.isfunction):
                if name.endswith(PAGINATED_SUFFIX):
                    yield cls, name[: -len(PAGINATED_SUFFIX)], func


def _undocumented_operations():
    found = 0
    undocumented = set()
    for _, operation, func in _paginated_methods():
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


def _pages_are_lists(func):
    """True when ``func`` is annotated ``AsyncIterator[List[...]]``."""
    (page_type,) = typing.get_args(func.__annotations__["return"])
    return typing.get_origin(page_type) is list


def test_all_iterator_only_for_list_responses():
    """``<op>_all`` exists if and only if ``<op>_paginated`` yields list pages."""
    missing = []
    unexpected = []
    for cls, operation, func in _paginated_methods():
        has_all = hasattr(cls, operation + ALL_SUFFIX)
        if _pages_are_lists(func) and not has_all:
            missing.append(operation)
        elif not _pages_are_lists(func) and has_all:
            unexpected.append(operation)

    assert not missing, f"List-response operations missing {ALL_SUFFIX}: {sorted(missing)}"
    assert not unexpected, f"Non-list-response operations with {ALL_SUFFIX}: {sorted(unexpected)}"


# Paginated operation -> page item type (namespaced Lti::X models resolve)
LTI_LIST_ITEM_TYPES = {
    "deployments_list": "LtiDeployment",
    "deployments_list_controls": "LtiContextControl",
    "context_controls_index": "LtiDeployment",
    "lti_apps_launch_definitions": "LtiLaunchDefinition",
    "lti_apps_launch_definitions_for_accounts": "LtiLaunchDefinition",
    "resource_links_index": "LtiResourceLink",
    "registrations_history": "LtiRegistrationHistoryEntry",
}

# Paginated operation -> page item type, for models that were @object examples
# or named but undefined in canvas-lms
RETURN_MODEL_LIST_ITEM_TYPES = {
    "media_objects_index": "MediaObject",
    "media_objects_index_for_other": "MediaObject",
    "media_objects_index_for_courses": "MediaObject",
    "media_objects_index_for_groups": "MediaObject",
    "media_objects_index_by_media_attachments_for_courses": "MediaObject",
    "media_objects_index_by_media_attachments_for_groups": "MediaObject",
    "rubrics_api_used_locations": "RubricUsedLocation",
    "rubrics_api_used_locations_for_accounts": "RubricUsedLocation",
}


# Paginated operation -> page item type, for lists that had no @returns in
# canvas-lms
SIMPLE_LIST_ITEM_TYPES = {
    "pseudonyms_index": "Login",
    "pseudonyms_index_for_users": "Login",
    "conversations_batches": "ConversationBatch",
    "courses_bulk_user_progress": "UserProgress",
    "submissions_api_multiple_gradeable_students": "MultipleGradeableStudent",
}


def _page_item_type(func):
    (page_type,) = typing.get_args(func.__annotations__["return"])
    assert typing.get_origin(page_type) is list
    (item_type,) = typing.get_args(page_type)
    return item_type.__name__


def test_lti_list_pages_are_typed():
    paginated = {operation: func for _, operation, func in _paginated_methods()}

    item_types = {operation: _page_item_type(paginated[operation]) for operation in LTI_LIST_ITEM_TYPES}

    assert item_types == LTI_LIST_ITEM_TYPES


def test_return_model_list_pages_are_typed():
    paginated = {operation: func for _, operation, func in _paginated_methods()}

    item_types = {
        operation: _page_item_type(paginated[operation]) for operation in RETURN_MODEL_LIST_ITEM_TYPES
    }

    assert item_types == RETURN_MODEL_LIST_ITEM_TYPES


def test_simple_list_pages_are_typed():
    paginated = {operation: func for _, operation, func in _paginated_methods()}

    item_types = {operation: _page_item_type(paginated[operation]) for operation in SIMPLE_LIST_ITEM_TYPES}

    assert item_types == SIMPLE_LIST_ITEM_TYPES


# List key -> (item model, minimal valid item)
_WRAPPED_ITEMS = {
    "account_calendars": ("AccountCalendar", {"id": 1, "name": "Chemistry"}),
    "assignment_extensions": ("AssignmentExtension", {"assignment_id": 1, "user_id": 2}),
    "grading_period_sets": ("GradingPeriodSets", {"id": "1", "title": "Fall"}),
    "grading_periods": (
        "GradingPeriod",
        {"id": "1", "start_date": "2026-01-01T00:00:00Z", "end_date": "2026-06-01T00:00:00Z"},
    ),
    "outcome_results": ("OutcomeResult", {"id": 1}),
    "pace_contexts": ("PaceContext", {"name": "Biology 101", "type": "Course", "item_id": 1}),
    "poll_choices": ("PollChoice", {"id": "1", "text": "Yes"}),
    "poll_sessions": ("PollSession", {"id": "1", "poll_id": "2", "course_id": "3"}),
    "poll_submissions": ("PollSubmission", {"id": "1", "poll_choice_id": "2"}),
    "polls": ("Poll", {"id": "1", "question": "Pizza?"}),
    "quiz_extensions": ("QuizExtension", {"quiz_id": 1, "user_id": 2}),
    "quiz_groups": ("QuizGroup", {"id": 1, "quiz_id": 2}),
    "quiz_ip_filters": ("QuizIPFilter", {"name": "Lab", "account": "School", "filter": "10.0.0.0/8"}),
    "quiz_statistics": ("QuizStatistics", {"id": 1, "quiz_id": 2}),
    "quiz_submission_questions": ("QuizSubmissionQuestion", {"id": 1}),
    "quiz_submission_events": ("QuizSubmissionEvent", {"id": "1", "event_type": "page_blurred"}),
    "quiz_submissions": ("QuizSubmission", {"id": 1, "quiz_id": 2}),
    "results": ("Result", {"id": "1"}),
}

# Wrapper model (named after its controller and action) -> its list key
_WRAPPER_KEYS = {
    "AccountCalendarsApiIndexResponse": "account_calendars",
    "AssignmentExtensionsCreateResponse": "assignment_extensions",
    "CourseQuizExtensionsCreateResponse": "quiz_extensions",
    "GradingPeriodSetsIndexResponse": "grading_period_sets",
    "GradingPeriodsBatchUpdateResponse": "grading_periods",
    "GradingPeriodsIndexResponse": "grading_periods",
    "GradingPeriodsShowResponse": "grading_periods",
    "GradingPeriodsUpdateResponse": "grading_periods",
    "OutcomeResultsIndexResponse": "outcome_results",
    "PaceContextsApiIndexResponse": "pace_contexts",
    "PollChoicesCreateResponse": "poll_choices",
    "PollChoicesIndexResponse": "poll_choices",
    "PollChoicesShowResponse": "poll_choices",
    "PollChoicesUpdateResponse": "poll_choices",
    "PollSessionsCloseResponse": "poll_sessions",
    "PollSessionsClosedResponse": "poll_sessions",
    "PollSessionsCreateResponse": "poll_sessions",
    "PollSessionsIndexResponse": "poll_sessions",
    "PollSessionsOpenResponse": "poll_sessions",
    "PollSessionsOpenedResponse": "poll_sessions",
    "PollSessionsShowResponse": "poll_sessions",
    "PollSessionsUpdateResponse": "poll_sessions",
    "PollSubmissionsCreateResponse": "poll_submissions",
    "PollSubmissionsShowResponse": "poll_submissions",
    "PollsCreateResponse": "polls",
    "PollsIndexResponse": "polls",
    "PollsShowResponse": "polls",
    "PollsUpdateResponse": "polls",
    "QuizExtensionsCreateResponse": "quiz_extensions",
    "QuizGroupsCreateResponse": "quiz_groups",
    "QuizGroupsIndexResponse": "quiz_groups",
    "QuizGroupsUpdateResponse": "quiz_groups",
    "QuizIpFiltersIndexResponse": "quiz_ip_filters",
    "QuizStatisticsIndexResponse": "quiz_statistics",
    "QuizSubmissionEventsApiIndexResponse": "quiz_submission_events",
    "QuizSubmissionQuestionsIndexResponse": "quiz_submission_questions",
    "QuizSubmissionsApiCompleteResponse": "quiz_submissions",
    "QuizSubmissionsApiCreateResponse": "quiz_submissions",
    "QuizSubmissionsApiIndexResponse": "quiz_submissions",
    "QuizSubmissionsApiShowResponse": "quiz_submissions",
    "QuizSubmissionsApiSubmissionResponse": "quiz_submissions",
    "QuizzesQuizSubmissionsUpdateResponse": "quiz_submissions",
    "ResultsCreateResponse": "results",
    "ResultsIndexResponse": "results",
}

# Wrapper model -> (list key, item model, minimal valid item)
WRAPPED_LIST_RESPONSES = {wrapper: (key, *_WRAPPED_ITEMS[key]) for wrapper, key in _WRAPPER_KEYS.items()}


@pytest.mark.parametrize("wrapper_name", sorted(WRAPPED_LIST_RESPONSES))
def test_wrapper_page_deserializes_items(wrapper_name):
    """A wrapped page deserializes its list key into item models."""
    key, item_name, item = WRAPPED_LIST_RESPONSES[wrapper_name]
    wrapper_cls = getattr(canvas_lms_python_client.models, wrapper_name)
    item_cls = getattr(canvas_lms_python_client.models, item_name)

    page = wrapper_cls.from_json(json.dumps({key: [item]}))

    assert isinstance(page, wrapper_cls)
    items = getattr(page, key)
    assert isinstance(items, list) and len(items) == 1
    assert isinstance(items[0], item_cls)


@pytest.mark.parametrize("wrapper_name", sorted(WRAPPED_LIST_RESPONSES))
def test_wrapper_page_without_key(wrapper_name):
    """A page that omits the wrapper key deserializes with the attribute unset."""
    key, _, _ = WRAPPED_LIST_RESPONSES[wrapper_name]
    wrapper_cls = getattr(canvas_lms_python_client.models, wrapper_name)

    page = wrapper_cls.from_json("{}")

    assert isinstance(page, wrapper_cls)
    assert getattr(page, key) is None


# Items as Canvas sends them (captured from the seeded instance). Polling
# endpoints stringify every id; quiz scores and points are floats.
_POLL_SUBMISSION = {
    "id": "1",
    "poll_session_id": "2",
    "poll_choice_id": "4",
    "user_id": "281",
    "created_at": "2026-10-31T22:53:34-06:00",
}
_POLL_SESSION = {
    "id": "2",
    "is_published": True,
    "course_id": "7",
    "course_section_id": "7",
    "created_at": "2026-11-01T04:53:34Z",
    "poll_id": "2",
    "has_submitted": False,
    "poll_submissions": [_POLL_SUBMISSION],
    "has_public_results": False,
    "results": {"6": 1, "5": 1, "4": 1},
}
LIVE_ITEMS = {
    "poll": (
        "Poll",
        {
            "id": "2",
            "question": "Which topic should we review next?",
            "description": None,
            "created_at": "2026-11-01T04:53:34Z",
            "total_results": {"6": 1, "5": 1, "4": 1},
            "user_id": "1",
        },
    ),
    "poll_choice": (
        "PollChoice",
        {"id": "4", "text": "Review the readings", "position": 0, "is_correct": True},
    ),
    "poll_session": ("PollSession", _POLL_SESSION),
    "poll_session_no_submissions": ("PollSession", {**_POLL_SESSION, "poll_submissions": []}),
    "poll_submission": ("PollSubmission", _POLL_SUBMISSION),
    "quiz_submission": (
        "QuizSubmission",
        {
            "id": 6,
            "user_id": 281,
            "submission_id": 10152,
            "quiz_id": 2,
            "quiz_points_possible": 10.0,
            "quiz_version": 2,
            "attempt": 1,
            "extra_attempts": None,
            "extra_time": None,
            "manually_unlocked": None,
            "started_at": "2026-11-01T04:53:36Z",
            "finished_at": "2026-11-01T04:53:36Z",
            "end_at": None,
            "fudge_points": None,
            "kept_score": 0.0,
            "score": 0.0,
            "score_before_regrade": None,
            "has_seen_results": False,
            "workflow_state": "complete",
            "time_spent": 0,
            "attempts_left": 0,
            "overdue_and_needs_submission": False,
        },
    ),
    "quiz_submission_fractional": (
        "QuizSubmission",
        {"id": 7, "quiz_id": 2, "score": 7.5, "kept_score": 7.5, "fudge_points": 0.5},
    ),
    "quiz": (
        "Quiz",
        {
            "id": 2,
            "title": "Checkpoint Quiz",
            "quiz_type": "assignment",
            "assignment_group_id": 5,
            "time_limit": None,
            "shuffle_answers": False,
            "scoring_policy": "keep_highest",
            "allowed_attempts": 1,
            "question_count": 1,
            "points_possible": 10.0,
            "published": True,
            "due_at": None,
        },
    ),
}


@pytest.mark.parametrize("case", sorted(LIVE_ITEMS))
def test_live_item_deserializes(case):
    """Items shaped like Canvas's real responses deserialize without error."""
    model_name, item = LIVE_ITEMS[case]
    model_cls = getattr(canvas_lms_python_client.models, model_name)

    model = model_cls.from_json(json.dumps(item))

    assert isinstance(model, model_cls)
    assert model.id == item["id"]


def test_live_poll_session_submissions_are_typed():
    """A poll session's submissions deserialize as a list of PollSubmission."""
    session = canvas_lms_python_client.models.PollSession.from_json(json.dumps(_POLL_SESSION))

    assert [type(s).__name__ for s in session.poll_submissions] == ["PollSubmission"]
    assert session.poll_submissions[0].poll_choice_id == "4"


# Pages captured from the seeded instance as an account admin: a weighted
# grading period set (fractional weights, string ids), its account's grading
# periods, a course with include[]=grading_periods (integer ids), and an
# audited quiz submission's events
_FIXTURES = pathlib.Path(__file__).parent / "fixtures" / "grading_periods"


def _fixture(name):
    return json.loads((_FIXTURES / f"{name}.json").read_text())


def test_grading_period_sets_page_keeps_canvas_types():
    payload = _fixture("grading_period_sets")
    page = canvas_lms_python_client.models.GradingPeriodSetsIndexResponse.from_dict(payload)

    assert len(page.grading_period_sets) == len(payload["grading_period_sets"])
    for grading_period_set, item in zip(page.grading_period_sets, payload["grading_period_sets"]):
        assert isinstance(grading_period_set, canvas_lms_python_client.models.GradingPeriodSets)
        assert grading_period_set.id == item["id"]
        assert grading_period_set.account_id == item["account_id"]
        assert grading_period_set.permissions == item["permissions"]
        assert [p.id for p in grading_period_set.grading_periods] == [p["id"] for p in item["grading_periods"]]
        assert [p.weight for p in grading_period_set.grading_periods] == [p["weight"] for p in item["grading_periods"]]


def test_grading_period_set_create_returns_one_set():
    item = _fixture("grading_period_sets")["grading_period_sets"][0]
    response = canvas_lms_python_client.models.GradingPeriodSetsCreateResponse.from_dict(
        {"grading_period_set": item}
    )

    assert isinstance(response.grading_period_set, canvas_lms_python_client.models.GradingPeriodSets)
    assert response.grading_period_set.title == item["title"]


def test_grading_periods_page_keeps_canvas_types():
    payload = _fixture("grading_periods")
    page = canvas_lms_python_client.models.GradingPeriodsIndexResponse.from_dict(payload)

    for grading_period, item in zip(page.grading_periods, payload["grading_periods"], strict=True):
        assert grading_period.id == item["id"]
        assert grading_period.grading_period_group_id == item["grading_period_group_id"]
        assert isinstance(grading_period.weight, float)
        assert grading_period.weight == item["weight"]
        assert grading_period.is_closed == item["is_closed"]


def test_course_include_grading_periods_are_typed():
    payload = _fixture("course_include_grading_periods")
    course = canvas_lms_python_client.models.Course.from_dict(payload)

    assert [type(p).__name__ for p in course.grading_periods] == ["CourseGradingPeriod"] * len(
        payload["grading_periods"]
    )
    for grading_period, item in zip(course.grading_periods, payload["grading_periods"], strict=True):
        assert grading_period.id == item["id"]
        assert isinstance(grading_period.id, int)
        assert grading_period.workflow_state == item["workflow_state"]


def test_quiz_submission_events_keep_every_event_data_shape():
    payload = _fixture("quiz_submission_events")
    page = canvas_lms_python_client.models.QuizSubmissionEventsApiIndexResponse.from_dict(payload)

    events = page.quiz_submission_events
    assert [e.id for e in events] == [e["id"] for e in payload["quiz_submission_events"]]
    assert [e.event_data for e in events] == [e["event_data"] for e in payload["quiz_submission_events"]]
    shapes = {type(e.event_data).__name__ for e in events}
    assert {"list", "dict", "NoneType"} <= shapes
