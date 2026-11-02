"""
Guard against controller helper classes taking over API groups.

A class defined inside a Canvas controller (an error class or a
``Struct.new`` constant) used to rename that controller's operations after
itself and hide every action defined after it. These offline checks pin the
API classes and operations that were renamed or missing.
"""

import importlib
import inspect
import pkgutil

import pytest

import canvas_lms_python_client.api
from canvas_lms_python_client.api.collaborations_api import CollaborationsApi
from canvas_lms_python_client.api.external_tools_api import ExternalToolsApi
from canvas_lms_python_client.api.outcome_imports_api_api import OutcomeImportsApiApi
from canvas_lms_python_client.api.users_api import UsersApi

# Nested helper classes in Canvas controllers
HELPER_CLASS_NAMES = (
    "service_credentials",
    "bad_permission_setting_error",
    "record_already_exists",
    "metadata_sax_doc",
)


def _api_names():
    """Yield every API module, class and public method name."""
    package = canvas_lms_python_client.api
    for module_info in pkgutil.iter_modules(package.__path__):
        yield module_info.name
        module = importlib.import_module(f"{package.__name__}.{module_info.name}")
        for class_name, cls in inspect.getmembers(module, inspect.isclass):
            if cls.__module__ != module.__name__:
                continue
            yield class_name
            yield from (name for name, _ in inspect.getmembers(cls, inspect.isfunction) if not name.startswith("_"))


def _snake(name):
    return "".join(f"_{c.lower()}" if c.isupper() else c for c in name).lstrip("_")


def test_no_api_named_after_a_helper_class():
    named = sorted({name for name in _api_names() if any(helper in _snake(name) for helper in HELPER_CLASS_NAMES)})

    assert not named, f"API classes or operations named after a controller helper class: {named}"


@pytest.mark.parametrize(
    "operation",
    [
        "users_api_show",  # Show user details
        "users_create",  # Create a user
        "users_update",  # Edit a user
    ],
)
def test_users_actions_after_helper_class_exist(operation):
    assert callable(getattr(UsersApi, operation, None))


@pytest.mark.parametrize("api_cls", [ExternalToolsApi, CollaborationsApi, OutcomeImportsApiApi])
def test_previously_hidden_apis_have_operations(api_cls):
    operations = [name for name, _ in inspect.getmembers(api_cls, inspect.isfunction) if not name.startswith("_")]

    assert operations
