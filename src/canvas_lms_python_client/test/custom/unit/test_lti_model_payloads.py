"""
Deserialize LTI responses captured from a seeded Canvas into their models.

Each fixture in ``fixtures/lti`` is the JSON an account admin received from
the matching operation. A model whose field types differ from what Canvas
sends raises a ``ValidationError`` here instead of in a caller's code.
"""

import json
import pathlib

import pytest

from canvas_lms_python_client.models import (
    LtiContextControl,
    LtiDeployment,
    LtiLaunchDefinition,
    LtiOverlayVersion,
    LtiRegistration,
    LtiRegistrationAccountBinding,
    LtiResourceLink,
    User,
)

FIXTURES = pathlib.Path(__file__).parent / "fixtures" / "lti"

# Fixture -> (model, whether the response is a list of it)
PAYLOADS = {
    "deployments_list": (LtiDeployment, True),
    "deployments_show": (LtiDeployment, False),
    "deployments_list_controls": (LtiContextControl, True),
    "context_controls_index": (LtiDeployment, True),
    "context_controls_show": (LtiContextControl, False),
    "lti_apps_launch_definitions": (LtiLaunchDefinition, True),
    "registrations_show": (LtiRegistration, False),
    "registrations_overlay_history": (LtiOverlayVersion, True),
    "resource_links_index": (LtiResourceLink, True),
    "resource_links_show": (LtiResourceLink, False),
}


def _load(name):
    return json.loads((FIXTURES / f"{name}.json").read_text())


def _deserialize(name):
    model_cls, is_list = PAYLOADS[name]
    payload = _load(name)
    if is_list:
        assert payload, f"{name}.json is an empty list"
        return [model_cls.from_dict(item) for item in payload]
    return model_cls.from_dict(payload)


def test_every_fixture_has_a_model():
    assert sorted(p.stem for p in FIXTURES.glob("*.json")) == sorted(PAYLOADS)


@pytest.mark.parametrize("name", sorted(PAYLOADS))
def test_payload_deserializes(name):
    """The captured response deserializes into its model without error."""
    model_cls, is_list = PAYLOADS[name]
    result = _deserialize(name)

    items = result if is_list else [result]
    payload = _load(name) if is_list else [_load(name)]
    assert all(isinstance(item, model_cls) for item in items)
    if "id" in model_cls.model_fields:
        assert [item.id for item in items] == [item["id"] for item in payload]


def test_launch_definition_ids_are_integers():
    (definition,) = _deserialize("lti_apps_launch_definitions")

    assert definition.definition_type == "ContextExternalTool"
    assert isinstance(definition.definition_id, int)
    assert definition.definition_id == _load("lti_apps_launch_definitions")[0]["definition_id"]


def test_context_controls_index_groups_controls_by_deployment():
    deployments = _deserialize("context_controls_index")

    controls = [control for deployment in deployments for control in deployment.context_controls]
    assert controls
    assert all(isinstance(control, LtiContextControl) for control in controls)


def test_registration_created_by_instructure_is_a_string():
    registration = _deserialize("registrations_show")

    assert registration.created_by.actual_instance == "Instructure"
    assert registration.updated_by.actual_instance == "Instructure"
    assert registration.account_binding.created_by.actual_instance == "Instructure"


def test_account_binding_deserializes():
    binding = LtiRegistrationAccountBinding.from_dict(_load("registrations_show")["account_binding"])

    assert binding.workflow_state == "on"
    assert binding.created_by.actual_instance == "Instructure"


def test_account_binding_created_by_a_user_is_a_user():
    """A binding created by a non-site-admin carries a user, not a string."""
    user = _load("context_controls_show")["created_by"]
    binding = dict(_load("registrations_show")["account_binding"], created_by=user)

    created_by = LtiRegistrationAccountBinding.from_dict(binding).created_by.actual_instance

    assert isinstance(created_by, User)
    assert created_by.id == user["id"]


def test_overlay_version_diff_keeps_mixed_tuples():
    (version,) = _deserialize("registrations_overlay_history")

    assert version.diff == _load("registrations_overlay_history")[0]["diff"]
    assert version.created_by.actual_instance == "Instructure"
