"""
Integration tests for paginated operations typed by `@returns` annotations.

These endpoints need account-admin permissions, so they run with
CANVAS_ADMIN_API_TOKEN against a seeded Canvas instance:

    pdm run pytest --integration -m integration

Tests skip, naming the missing data, when the instance has nothing to list.

Wrapped list endpoints (e.g. polls) have no `_all`; their tests iterate
`_paginated` and check each page is the wrapper model.
"""

from typing import AsyncIterator, Awaitable, Callable, List, Optional, TypeVar

import pytest

from canvas_lms_python_client.api.account_calendars_api_api import AccountCalendarsApiApi
from canvas_lms_python_client.api.accounts_api import AccountsApi
from canvas_lms_python_client.api.appointment_groups_api import AppointmentGroupsApi
from canvas_lms_python_client.api.context_controls_api import ContextControlsApi
from canvas_lms_python_client.api.courses_api import CoursesApi
from canvas_lms_python_client.api.deployments_api import DeploymentsApi
from canvas_lms_python_client.api.grading_period_sets_api import GradingPeriodSetsApi
from canvas_lms_python_client.api.grading_periods_api import GradingPeriodsApi
from canvas_lms_python_client.api.lti_apps_api import LtiAppsApi
from canvas_lms_python_client.api.poll_choices_api import PollChoicesApi
from canvas_lms_python_client.api.poll_sessions_api import PollSessionsApi
from canvas_lms_python_client.api.polls_api import PollsApi
from canvas_lms_python_client.api.quiz_submission_events_api_api import QuizSubmissionEventsApiApi
from canvas_lms_python_client.api.quiz_submissions_api_api import QuizSubmissionsApiApi
from canvas_lms_python_client.api.quizzes_api_api import QuizzesApiApi
from canvas_lms_python_client.api.registrations_api import RegistrationsApi
from canvas_lms_python_client.api.resource_links_api import ResourceLinksApi
from canvas_lms_python_client.api.role_overrides_api import RoleOverridesApi
from canvas_lms_python_client.api.rubrics_api_api import RubricsApiApi
from canvas_lms_python_client.api.users_api import UsersApi
from canvas_lms_python_client.exceptions import ApiException
from canvas_lms_python_client.models.account import Account
from canvas_lms_python_client.models.account_calendar import AccountCalendar
from canvas_lms_python_client.models.account_calendars_api_index_response import (
    AccountCalendarsApiIndexResponse,
)
from canvas_lms_python_client.models.appointment_group import AppointmentGroup
from canvas_lms_python_client.models.course import Course
from canvas_lms_python_client.models.course_grading_period import CourseGradingPeriod
from canvas_lms_python_client.models.grading_period import GradingPeriod
from canvas_lms_python_client.models.grading_period_sets import GradingPeriodSets
from canvas_lms_python_client.models.grading_period_sets_index_response import (
    GradingPeriodSetsIndexResponse,
)
from canvas_lms_python_client.models.group import Group
from canvas_lms_python_client.models.list_lti_registrations_response import (
    ListLtiRegistrationsResponse,
)
from canvas_lms_python_client.models.lti_context_control import LtiContextControl
from canvas_lms_python_client.models.lti_deployment import LtiDeployment
from canvas_lms_python_client.models.lti_launch_definition import LtiLaunchDefinition
from canvas_lms_python_client.models.lti_registration import LtiRegistration
from canvas_lms_python_client.models.lti_resource_link import LtiResourceLink
from canvas_lms_python_client.models.poll import Poll
from canvas_lms_python_client.models.poll_choice import PollChoice
from canvas_lms_python_client.models.poll_choices_index_response import PollChoicesIndexResponse
from canvas_lms_python_client.models.poll_session import PollSession
from canvas_lms_python_client.models.poll_sessions_index_response import PollSessionsIndexResponse
from canvas_lms_python_client.models.poll_submission import PollSubmission
from canvas_lms_python_client.models.polls_index_response import PollsIndexResponse
from canvas_lms_python_client.models.quiz_submission import QuizSubmission
from canvas_lms_python_client.models.quiz_submission_event import QuizSubmissionEvent
from canvas_lms_python_client.models.quiz_submission_events_api_index_response import (
    QuizSubmissionEventsApiIndexResponse,
)
from canvas_lms_python_client.models.quiz_submissions_api_index_response import (
    QuizSubmissionsApiIndexResponse,
)
from canvas_lms_python_client.models.role import Role
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


def assert_typed(items: List[object], model: type, id_type: type = int) -> None:
    for item in items:
        assert isinstance(item, model)
        assert isinstance(item.id, id_type)


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
        assert isinstance(definition, LtiLaunchDefinition)
        assert definition.definition_type
        assert isinstance(definition.definition_id, int)


async def test_course_launch_definitions_yield_items(canvas_admin_api_client):
    api = LtiAppsApi(canvas_admin_api_client)
    account = await root_account(canvas_admin_api_client)

    definitions: List[LtiLaunchDefinition] = []
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


async def test_include_list_filter_applies(canvas_admin_api_client):
    """include=["term"] is sent as include[]=term, so Canvas embeds each course's term."""
    account = await root_account(canvas_admin_api_client)
    api = AccountsApi(canvas_admin_api_client)
    account_id = str(account.id)

    plain = require(
        await collect(api.accounts_courses_api_all(account_id=account_id)),
        "course in the root account",
    )
    with_term = await collect(api.accounts_courses_api_all(account_id=account_id, include=["term"]))

    assert all(course.term is None for course in plain)
    assert with_term and all(course.term is not None for course in with_term)


async def lti_registrations(api_client, account: Account) -> List[LtiRegistration]:
    pages = await collect(
        RegistrationsApi(api_client).registrations_list_paginated(account_id=str(account.id))
    )
    return wrapped_items(pages, ListLtiRegistrationsResponse, "data")


async def lti_deployments(api_client) -> List[tuple]:
    """(account id, registration id, deployment) for every visible deployment."""
    account = await root_account(api_client)
    account_id = str(account.id)
    api = DeploymentsApi(api_client)

    found = []
    for registration in await lti_registrations(api_client, account):
        registration_id = str(registration.id)
        deployments = await collect(
            api.deployments_list_all(account_id=account_id, registration_id=registration_id)
        )
        found.extend((account_id, registration_id, deployment) for deployment in deployments)
    return require(found, "LTI deployment in the root account")


async def test_lti_deployments_typed(canvas_admin_api_client):
    deployments = [d for _, _, d in await lti_deployments(canvas_admin_api_client)]

    assert_typed(deployments, LtiDeployment)


async def test_lti_deployment_show_typed(canvas_admin_api_client):
    account_id, registration_id, listed = (await lti_deployments(canvas_admin_api_client))[0]

    deployment = await DeploymentsApi(canvas_admin_api_client).deployments_show(
        account_id=account_id, registration_id=registration_id, id=str(listed.id)
    )

    assert isinstance(deployment, LtiDeployment)
    assert deployment.id == listed.id


async def test_lti_deployment_controls_typed(canvas_admin_api_client):
    api = DeploymentsApi(canvas_admin_api_client)

    controls: List[LtiContextControl] = []
    for account_id, registration_id, deployment in await lti_deployments(canvas_admin_api_client):
        controls = await collect(
            api.deployments_list_controls_all(
                account_id=account_id, registration_id=registration_id, id=str(deployment.id)
            )
        )
        if controls:
            break
    require(controls, "context control on any LTI deployment")

    assert_typed(controls, LtiContextControl)


async def test_lti_account_context_controls_typed(canvas_admin_api_client):
    """The account's context controls are listed grouped by deployment."""
    api = ContextControlsApi(canvas_admin_api_client)
    account = await root_account(canvas_admin_api_client)

    deployments: List[LtiDeployment] = []
    for registration in await lti_registrations(canvas_admin_api_client, account):
        deployments = await collect(
            api.context_controls_index_all(
                account_id=str(account.id), registration_id=str(registration.id)
            )
        )
        if deployments:
            break
    controls = [c for deployment in deployments for c in deployment.context_controls or []]
    require(controls, "context control for any LTI registration")

    assert_typed(deployments, LtiDeployment)
    assert_typed(controls, LtiContextControl)


async def test_lti_resource_links_typed(canvas_admin_api_client):
    api = ResourceLinksApi(canvas_admin_api_client)
    account = await root_account(canvas_admin_api_client)

    links: List[LtiResourceLink] = []
    for course in await account_courses(canvas_admin_api_client, account):
        links = await collect(api.resource_links_index_all(course_id=str(course.id)))
        if links:
            break
    require(links, "LTI resource link in any root account course")

    assert_typed(links, LtiResourceLink)


def wrapped_items(pages: List[object], wrapper: type, key: str) -> List[object]:
    """Assert each page is ``wrapper`` and return the items under ``key``."""
    items: List[object] = []
    for page in pages:
        assert isinstance(page, wrapper)
        items.extend(getattr(page, key) or [])
    return items


async def admin_polls(api_client) -> List[Poll]:
    """Polls owned by the admin (Canvas only lists the caller's own polls)."""
    pages = await collect(PollsApi(api_client).polls_index_paginated())
    return require(wrapped_items(pages, PollsIndexResponse, "polls"), "poll owned by the admin")


async def test_polls_pages_typed(canvas_admin_api_client):
    polls = await admin_polls(canvas_admin_api_client)

    # Polling endpoints send every id as a string
    assert_typed(polls, Poll, id_type=str)


async def test_poll_choices_pages_typed(canvas_admin_api_client):
    api = PollChoicesApi(canvas_admin_api_client)

    choices: List[object] = []
    for poll in await admin_polls(canvas_admin_api_client):
        pages = await collect(api.poll_choices_index_paginated(poll_id=poll.id))
        choices = wrapped_items(pages, PollChoicesIndexResponse, "poll_choices")
        if choices:
            break
    require(choices, "poll choice in any admin poll")

    assert_typed(choices, PollChoice, id_type=str)


async def test_poll_sessions_pages_typed(canvas_admin_api_client):
    api = PollSessionsApi(canvas_admin_api_client)

    sessions: List[PollSession] = []
    for poll in await admin_polls(canvas_admin_api_client):
        pages = await collect(api.poll_sessions_index_paginated(poll_id=poll.id))
        sessions = wrapped_items(pages, PollSessionsIndexResponse, "poll_sessions")
        if any(session.poll_submissions for session in sessions):
            break
    submissions = [s for session in sessions for s in session.poll_submissions or []]
    require(submissions, "poll session with submissions in any admin poll")

    assert_typed(sessions, PollSession, id_type=str)
    assert_typed(submissions, PollSubmission, id_type=str)


async def test_quiz_submissions_pages_typed(canvas_admin_api_client):
    account = await root_account(canvas_admin_api_client)
    quizzes_api = QuizzesApiApi(canvas_admin_api_client)
    submissions_api = QuizSubmissionsApiApi(canvas_admin_api_client)

    submissions: List[object] = []
    for course in await account_courses(canvas_admin_api_client, account):
        course_id = str(course.id)
        for quiz in await collect(quizzes_api.quizzes_api_index_all(course_id=course_id)):
            pages = await collect(
                submissions_api.quiz_submissions_api_index_paginated(
                    course_id=course_id, quiz_id=str(quiz.id)
                )
            )
            submissions = wrapped_items(pages, QuizSubmissionsApiIndexResponse, "quiz_submissions")
            if submissions:
                break
        if submissions:
            break
    require(submissions, "quiz submission in any root account course")

    assert_typed(submissions, QuizSubmission)


async def test_quiz_submission_events_pages_typed(canvas_admin_api_client):
    """Events were untyped, and their event_data is a list, an object or null."""
    account = await root_account(canvas_admin_api_client)
    quizzes_api = QuizzesApiApi(canvas_admin_api_client)
    submissions_api = QuizSubmissionsApiApi(canvas_admin_api_client)
    events_api = QuizSubmissionEventsApiApi(canvas_admin_api_client)

    events: List[object] = []
    for course in await account_courses(canvas_admin_api_client, account):
        course_id = str(course.id)
        for quiz in await collect(quizzes_api.quizzes_api_index_all(course_id=course_id)):
            pages = await collect(
                submissions_api.quiz_submissions_api_index_paginated(course_id=course_id, quiz_id=str(quiz.id))
            )
            for submission in wrapped_items(pages, QuizSubmissionsApiIndexResponse, "quiz_submissions"):
                try:
                    event_pages = await collect(
                        events_api.quiz_submission_events_api_index_paginated(
                            course_id=course_id, quiz_id=str(quiz.id), id=str(submission.id)
                        )
                    )
                except ApiException as error:
                    if error.status == 400:  # quiz log auditing is off for this course
                        break
                    raise
                events = wrapped_items(event_pages, QuizSubmissionEventsApiIndexResponse, "quiz_submission_events")
                if {type(e.event_data) for e in events} >= {list, dict, type(None)}:
                    break
            if events:
                break
        if events:
            break
    require(events, "audited quiz submission with events in any root account course (run the seed script with --audit-data)")

    assert_typed(events, QuizSubmissionEvent, id_type=str)
    assert {type(e.event_data) for e in events} >= {list, dict, type(None)}


async def test_grading_period_sets_pages_typed(canvas_admin_api_client):
    """Grading period set pages were untyped."""
    account = await root_account(canvas_admin_api_client)
    pages = await collect(
        GradingPeriodSetsApi(canvas_admin_api_client).grading_period_sets_index_paginated(account_id=str(account.id))
    )

    sets = wrapped_items(pages, GradingPeriodSetsIndexResponse, "grading_period_sets")
    assert_typed(require(sets, "grading period set (run the seed script with --audit-data)"), GradingPeriodSets, str)
    periods = [p for s in sets for p in s.grading_periods or []]
    assert_typed(require(periods, "grading period in a set"), GradingPeriod, str)


async def test_grading_periods_index_typed(canvas_admin_api_client):
    """Grading period ids are strings and weights can be fractional."""
    account = await root_account(canvas_admin_api_client)
    page = await GradingPeriodsApi(canvas_admin_api_client).grading_periods_index(account_id=str(account.id))

    periods = require(page.grading_periods or [], "grading period in the root account")
    assert_typed(periods, GradingPeriod, str)
    assert all(p.weight is None or isinstance(p.weight, (int, float)) for p in periods)


async def test_course_include_grading_periods_typed(canvas_admin_api_client):
    """A course's included grading periods have integer ids, unlike GradingPeriod."""
    account = await root_account(canvas_admin_api_client)
    courses_api = CoursesApi(canvas_admin_api_client)

    periods: List[object] = []
    for listed in await account_courses(canvas_admin_api_client, account):
        course = await courses_api.courses_show(id=str(listed.id), include=["grading_periods"])
        assert isinstance(course, Course)
        periods = course.grading_periods or []
        if periods:
            break
    require(periods, "course whose term has grading periods")

    assert_typed(periods, CourseGradingPeriod)


async def test_users_and_roles_pages_typed(canvas_admin_api_client):
    """Users and roles were misnamed under a controller helper class and untyped."""
    users = [
        user
        async for page in UsersApi(canvas_admin_api_client).users_api_index_paginated(account_id="self")
        for user in page
    ]
    roles = [
        role
        async for page in RoleOverridesApi(canvas_admin_api_client).role_overrides_api_index_paginated(
            account_id="self"
        )
        for role in page
    ]

    assert_typed(require(users, "user in the admin's account"), User)
    assert_typed(require(roles, "role in the admin's account"), Role)


async def test_users_api_show_self_is_typed(canvas_api_client):
    """Show user details documented @returns Schemas::Docs::User and was untyped."""
    observer = await UsersApi(canvas_api_client).users_api_show(id="self")

    assert isinstance(observer, User)
    assert isinstance(observer.id, int)
    assert observer.name


async def test_account_calendars_pages_typed(canvas_admin_api_client):
    """Account calendar pages were lists of the wrapper's key names."""
    pages = await collect(
        AccountCalendarsApiApi(canvas_admin_api_client).account_calendars_api_index_paginated(per_page=1)
    )

    for page in pages:
        assert isinstance(page.total_results, int)
    calendars = wrapped_items(pages, AccountCalendarsApiIndexResponse, "account_calendars")
    assert_typed(require(calendars, "account calendar visible to the admin"), AccountCalendar)
    assert len(calendars) == pages[0].total_results
