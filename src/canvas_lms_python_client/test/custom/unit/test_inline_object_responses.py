"""
Operations whose Canvas ``@returns`` is an inline object (``{ ... }``).

They used to be generated as ``List[object]``, so the client iterated the
JSON object and returned its key names. Each one now returns either a
wrapper model, when every documented entry is typeable, or the parsed
mapping (``object``), which keeps everything Canvas sent.
"""

import inspect
import json
import re

import pytest

from canvas_lms_python_client import api, models
from canvas_lms_python_client.api_client import ApiClient

_RESPONSE_TYPE = re.compile(r"_response_types_map[^{]*\{\s*'[^']+':\s*\"([^\"]+)\"")

# Operation -> (API class, return annotation of the plain method)
TYPED_OPERATIONS = {
    "account_calendars_api_index": ("AccountCalendarsApiApi", "AccountCalendarsApiIndexResponse"),
    "account_calendars_api_visible_calendars_count": (
        "AccountCalendarsApiApi",
        "AccountCalendarsApiVisibleCalendarsCountResponse",
    ),
    "content_shares_unread_count": ("ContentSharesApi", "ContentSharesUnreadCountResponse"),
    "career_experience_enabled": ("CareerExperienceApi", "CareerExperienceEnabledResponse"),
    "career_experience_switch_experience": ("CareerExperienceApi", "CareerExperienceSwitchExperienceResponse"),
    "career_experience_switch_role": ("CareerExperienceApi", "CareerExperienceSwitchRoleResponse"),
    "what_if_grades_api_update": ("WhatIfGradesApiApi", "WhatIfGradesApiUpdateResponse"),
    "what_if_grades_api_reset_for_student_course": (
        "WhatIfGradesApiApi",
        "WhatIfGradesApiResetForStudentCourseResponse",
    ),
    "communication_channels_delete_push_token": (
        "CommunicationChannelsApi",
        "CommunicationChannelsDeletePushTokenResponse",
    ),
    "discovery_pages_api_token": ("DiscoveryPagesApiApi", "DiscoveryPagesApiTokenResponse"),
}

# Operations whose inline object is untypeable ({Object} prose, a union or a
# nested object): they return the parsed JSON mapping
PLAIN_OBJECT_OPERATIONS = {
    "ai_conversations_active_conversation": "AiConversationsApi",
    "ai_conversations_create": "AiConversationsApi",
    "ai_conversations_create_feedback": "AiConversationsApi",
    "ai_conversations_delete_feedback": "AiConversationsApi",
    "ai_conversations_destroy": "AiConversationsApi",
    "ai_conversations_evaluation": "AiConversationsApi",
    "ai_conversations_post_message": "AiConversationsApi",
    "ai_conversations_show": "AiConversationsApi",
    "registrations_validate_lti_configuration": "RegistrationsApi",
    "registrations_check_domain_duplicates": "RegistrationsApi",
}

# Wrapper -> a response of its documented shape
_GRADES = {"current": {"grade": 92.5, "total": 18.5, "possible": 20}}
_SUBMISSION = {"id": 2, "student_entered_score": "18.5"}
WRAPPER_PAYLOADS = {
    "AccountCalendarsApiIndexResponse": {
        "account_calendars": [{"id": 1, "name": "Chemistry", "parent_account_id": None}],
        "total_results": 1,
    },
    "AccountCalendarsApiVisibleCalendarsCountResponse": {"count": 4},
    "ContentSharesUnreadCountResponse": {"unread_count": 2},
    "CareerExperienceEnabledResponse": {"enabled": True},
    "CareerExperienceSwitchExperienceResponse": {"experience": "career_learner"},
    "CareerExperienceSwitchRoleResponse": {"role": "learner"},
    "WhatIfGradesApiUpdateResponse": {"grades": [_GRADES], "submission": _SUBMISSION},
    "WhatIfGradesApiResetForStudentCourseResponse": {"grades": [_GRADES]},
    "CommunicationChannelsDeletePushTokenResponse": {"success": True},
    "DiscoveryPagesApiTokenResponse": {"token": "eyJhbGciOiJIUzI1NiJ9"},
}


def _method(api_class, operation):
    return getattr(getattr(api, api_class), operation)


def _response_type(api_class, operation):
    match = _RESPONSE_TYPE.search(inspect.getsource(_method(api_class, operation)))
    assert match, f"{api_class}.{operation} has no response type"
    return match.group(1)


def _deserialize(payload, response_type):
    return ApiClient().deserialize(json.dumps(payload), response_type, "application/json")


def test_every_typed_operation_has_a_payload():
    assert sorted(WRAPPER_PAYLOADS) == sorted(wrapper for _, wrapper in TYPED_OPERATIONS.values())


@pytest.mark.parametrize("operation", sorted(TYPED_OPERATIONS))
def test_typed_operation_returns_its_wrapper(operation):
    api_class, wrapper = TYPED_OPERATIONS[operation]

    assert _method(api_class, operation).__annotations__["return"] is getattr(models, wrapper)
    assert _response_type(api_class, operation) == wrapper


@pytest.mark.parametrize("operation", sorted(PLAIN_OBJECT_OPERATIONS))
def test_plain_object_operation_returns_object(operation):
    assert _method(PLAIN_OBJECT_OPERATIONS[operation], operation).__annotations__["return"] is object


@pytest.mark.parametrize("operation", sorted(PLAIN_OBJECT_OPERATIONS))
def test_plain_object_operation_keeps_the_mapping(operation):
    """The regression: a JSON object used to come back as a list of its keys."""
    payload = {"a": 1, "b": [2]}

    result = _deserialize(payload, _response_type(PLAIN_OBJECT_OPERATIONS[operation], operation))

    assert result == payload


@pytest.mark.parametrize("wrapper", sorted(WRAPPER_PAYLOADS))
def test_wrapper_deserializes_documented_shape(wrapper):
    payload = WRAPPER_PAYLOADS[wrapper]

    result = _deserialize(payload, wrapper)

    assert isinstance(result, getattr(models, wrapper))
    assert result.to_dict() == payload


def test_account_calendars_page_is_typed():
    page = _deserialize(WRAPPER_PAYLOADS["AccountCalendarsApiIndexResponse"], "AccountCalendarsApiIndexResponse")

    assert all(isinstance(item, models.AccountCalendar) for item in page.account_calendars)
    assert page.total_results == 1


def test_what_if_grades_are_typed():
    result = _deserialize(WRAPPER_PAYLOADS["WhatIfGradesApiUpdateResponse"], "WhatIfGradesApiUpdateResponse")

    assert all(isinstance(item, models.Grades) for item in result.grades)
    assert isinstance(result.submission, models.WhatIfSubmission)


@pytest.mark.parametrize(
    ("wrapper", "key", "value"),
    [
        ("CommunicationChannelsDeletePushTokenResponse", "success", True),
        ("DiscoveryPagesApiTokenResponse", "token", "eyJhbGciOiJIUzI1NiJ9"),
        ("CareerExperienceSwitchExperienceResponse", "experience", "career_learner"),
    ],
)
def test_literal_and_primitive_entries_keep_their_type(wrapper, key, value):
    result = _deserialize({key: value}, wrapper)

    assert getattr(result, key) == value
    assert type(getattr(result, key)) is type(value)


@pytest.mark.parametrize("wrapper", sorted(WRAPPER_PAYLOADS))
def test_wrapper_with_omitted_keys(wrapper):
    """Canvas may omit any documented key; its attribute is then unset."""
    result = _deserialize({}, wrapper)

    assert isinstance(result, getattr(models, wrapper))
    assert all(getattr(result, key) is None for key in WRAPPER_PAYLOADS[wrapper])
