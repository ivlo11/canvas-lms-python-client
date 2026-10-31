"""
Integration tests for paginated operations typed by `@returns` annotations.

These endpoints need account-admin permissions, so they run with
CANVAS_ADMIN_API_TOKEN against a seeded Canvas instance:

    pdm run pytest --integration -m integration

Tests skip, naming the missing data, when the instance has nothing to list.
"""

from typing import AsyncIterator, Awaitable, Callable, List, Optional, TypeVar

import pytest

from canvas_lms_python_client.api.accounts_api import AccountsApi
from canvas_lms_python_client.api.appointment_groups_api import AppointmentGroupsApi
from canvas_lms_python_client.api.lti_apps_api import LtiAppsApi
from canvas_lms_python_client.api.rubrics_api_api import RubricsApiApi
from canvas_lms_python_client.models.account import Account
from canvas_lms_python_client.models.appointment_group import AppointmentGroup
from canvas_lms_python_client.models.course import Course
from canvas_lms_python_client.models.group import Group
from canvas_lms_python_client.models.rubric import Rubric
from canvas_lms_python_client.models.user import User

pytestmark = pytest.mark.integration

T = TypeVar("T")

LAUNCH_PLACEMENTS = [
    "account_navigation",
    "assignment_selection",
    "course_navigation",
    "editor_button",
    "link_selection",
    "resource_selection",
]


async def collect(iterator: AsyncIterator[T]) -> List[T]:
    """Collect every item from an `_all` iterator into a list."""
    return [item async for item in iterator]


def require(items: List[T], missing: str) -> List[T]:
    """Skip the test, naming the missing data, when a listing is empty."""
    if not items:
        pytest.skip(f"no {missing} found in the seeded Canvas instance")
    return items


def assert_typed(items: List[object], model: type) -> None:
    for item in items:
        assert isinstance(item, model)
        assert isinstance(item.id, int)


async def assert_pages_match(
    items: List[object], list_page: Callable[[Optional[int]], Awaitable[List[object]]]
) -> None:
    """Re-list with per_page=1 and compare ids when the listing spans 2+ items."""
    if len(items) < 2:
        return
    paged_ids = [item.id for item in await list_page(1)]
    assert len(paged_ids) == len(set(paged_ids)), "duplicate items across pages"
    assert set(paged_ids) == {item.id for item in items}


async def root_account(api_client) -> Account:
    """The admin's first account (its root account)."""
    accounts = await collect(AccountsApi(api_client).accounts_index_all())
    return require(accounts, "account visible to the admin")[0]


async def account_courses(api_client, account: Account) -> List[Course]:
    return await collect(
        AccountsApi(api_client).accounts_courses_api_all(account_id=str(account.id))
    )


async def test_account_rubrics_typed(canvas_admin_api_client):
    api = RubricsApiApi(canvas_admin_api_client)
    account_id = str((await root_account(canvas_admin_api_client)).id)

    async def list_rubrics(per_page: Optional[int] = None) -> List[Rubric]:
        return await collect(api.rubrics_api_index_all(account_id=account_id, per_page=per_page))

    rubrics = require(await list_rubrics(), "rubric in the root account")

    assert_typed(rubrics, Rubric)
    await assert_pages_match(rubrics, list_rubrics)


async def test_course_rubrics_typed(canvas_admin_api_client):
    api = RubricsApiApi(canvas_admin_api_client)
    account = await root_account(canvas_admin_api_client)

    rubrics: List[Rubric] = []
    for course in await account_courses(canvas_admin_api_client, account):
        course_id = str(course.id)
        rubrics = await collect(api.rubrics_api_index_for_courses_all(course_id=course_id))
        if rubrics:
            break
    require(rubrics, "rubric in any root account course")

    async def list_rubrics(per_page: Optional[int] = None) -> List[Rubric]:
        return await collect(
            api.rubrics_api_index_for_courses_all(course_id=course_id, per_page=per_page)
        )

    assert_typed(rubrics, Rubric)
    await assert_pages_match(rubrics, list_rubrics)


async def list_manageable_groups(api_client, per_page: Optional[int] = None):
    return await collect(
        AppointmentGroupsApi(api_client).appointment_groups_index_all(
            scope="manageable", per_page=per_page
        )
    )


async def test_appointment_groups_typed(canvas_admin_api_client):
    async def list_groups(per_page: Optional[int] = None) -> List[AppointmentGroup]:
        return await list_manageable_groups(canvas_admin_api_client, per_page)

    groups = require(await list_groups(), "manageable appointment group")

    assert_typed(groups, AppointmentGroup)
    await assert_pages_match(groups, list_groups)


async def test_appointment_group_participants_typed(canvas_admin_api_client):
    api = AppointmentGroupsApi(canvas_admin_api_client)
    groups = require(
        await list_manageable_groups(canvas_admin_api_client), "manageable appointment group"
    )
    group_id = str(groups[0].id)

    users = await collect(api.appointment_groups_users_all(id=group_id))
    student_groups = await collect(api.appointment_groups_groups_all(id=group_id))

    if groups[0].participant_type == "Group":
        assert users == []
        participants, model = student_groups, Group
    else:
        assert student_groups == []
        participants, model = users, User
    require(participants, f"{model.__name__} participant in appointment group {group_id}")
    assert_typed(participants, model)


def assert_launch_definitions(definitions: List[object]) -> None:
    for definition in definitions:
        assert isinstance(definition, dict)
        assert "definition_type" in definition
        assert "definition_id" in definition


async def test_course_launch_definitions_yield_items(canvas_admin_api_client):
    api = LtiAppsApi(canvas_admin_api_client)
    account = await root_account(canvas_admin_api_client)

    definitions: List[object] = []
    for course in await account_courses(canvas_admin_api_client, account):
        definitions = await collect(
            api.lti_apps_launch_definitions_all(
                course_id=str(course.id), placements=LAUNCH_PLACEMENTS
            )
        )
        if definitions:
            break
    require(definitions, "LTI tool with a launch placement in any root account course")

    assert_launch_definitions(definitions)


async def test_account_launch_definitions_yield_items(canvas_admin_api_client):
    account = await root_account(canvas_admin_api_client)

    definitions = await collect(
        LtiAppsApi(canvas_admin_api_client).lti_apps_launch_definitions_for_accounts_all(
            account_id=str(account.id), placements=LAUNCH_PLACEMENTS
        )
    )
    require(definitions, "LTI tool with a launch placement in the root account")

    assert_launch_definitions(definitions)
