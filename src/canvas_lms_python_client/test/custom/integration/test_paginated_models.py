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
from canvas_lms_python_client.api.assignments_api_api import AssignmentsApiApi
from canvas_lms_python_client.api.authentication_audit_api_api import AuthenticationAuditApiApi
from canvas_lms_python_client.api.context_controls_api import ContextControlsApi
from canvas_lms_python_client.api.conversations_api import ConversationsApi
from canvas_lms_python_client.api.course_audit_api_api import CourseAuditApiApi
from canvas_lms_python_client.api.courses_api import CoursesApi
from canvas_lms_python_client.api.deployments_api import DeploymentsApi
from canvas_lms_python_client.api.grade_change_audit_api_api import GradeChangeAuditApiApi
from canvas_lms_python_client.api.grading_period_sets_api import GradingPeriodSetsApi
from canvas_lms_python_client.api.grading_periods_api import GradingPeriodsApi
from canvas_lms_python_client.api.lti_apps_api import LtiAppsApi
from canvas_lms_python_client.api.media_objects_api import MediaObjectsApi
from canvas_lms_python_client.api.pace_contexts_api_api import PaceContextsApiApi
from canvas_lms_python_client.api.poll_choices_api import PollChoicesApi
from canvas_lms_python_client.api.poll_sessions_api import PollSessionsApi
from canvas_lms_python_client.api.polls_api import PollsApi
from canvas_lms_python_client.api.pseudonyms_api import PseudonymsApi
from canvas_lms_python_client.api.quiz_submission_events_api_api import QuizSubmissionEventsApiApi
from canvas_lms_python_client.api.quiz_submissions_api_api import QuizSubmissionsApiApi
from canvas_lms_python_client.api.quizzes_api_api import QuizzesApiApi
from canvas_lms_python_client.api.registrations_api import RegistrationsApi
from canvas_lms_python_client.api.resource_links_api import ResourceLinksApi
from canvas_lms_python_client.api.role_overrides_api import RoleOverridesApi
from canvas_lms_python_client.api.rubrics_api_api import RubricsApiApi
from canvas_lms_python_client.api.submissions_api_api import SubmissionsApiApi
from canvas_lms_python_client.api.users_api import UsersApi
from canvas_lms_python_client.exceptions import ApiException
from canvas_lms_python_client.models.account import Account
from canvas_lms_python_client.models.account_calendar import AccountCalendar
from canvas_lms_python_client.models.account_calendars_api_index_response import (
    AccountCalendarsApiIndexResponse,
)
from canvas_lms_python_client.models.applied_pace import AppliedPace
from canvas_lms_python_client.models.appointment_group import AppointmentGroup
from canvas_lms_python_client.models.authentication_audit_api_for_account_response import (
    AuthenticationAuditApiForAccountResponse,
)
from canvas_lms_python_client.models.authentication_event import AuthenticationEvent
from canvas_lms_python_client.models.authentication_event_links import AuthenticationEventLinks
from canvas_lms_python_client.models.conversation_batch import ConversationBatch
from canvas_lms_python_client.models.course import Course
from canvas_lms_python_client.models.course_audit_api_for_account_response import (
    CourseAuditApiForAccountResponse,
)
from canvas_lms_python_client.models.course_event import CourseEvent
from canvas_lms_python_client.models.course_event_link import CourseEventLink
from canvas_lms_python_client.models.course_grading_period import CourseGradingPeriod
from canvas_lms_python_client.models.course_progress import CourseProgress
from canvas_lms_python_client.models.grade_change_audit_api_for_course_response import (
    GradeChangeAuditApiForCourseResponse,
)
from canvas_lms_python_client.models.grade_change_event import GradeChangeEvent
from canvas_lms_python_client.models.grade_change_event_links import GradeChangeEventLinks
from canvas_lms_python_client.models.grading_period import GradingPeriod
from canvas_lms_python_client.models.grading_period_sets import GradingPeriodSets
from canvas_lms_python_client.models.grading_period_sets_index_response import (
    GradingPeriodSetsIndexResponse,
)
from canvas_lms_python_client.models.group import Group
from canvas_lms_python_client.models.list_lti_registrations_response import (
    ListLtiRegistrationsResponse,
)
from canvas_lms_python_client.models.login import Login
from canvas_lms_python_client.models.lti_context_control import LtiContextControl
from canvas_lms_python_client.models.lti_deployment import LtiDeployment
from canvas_lms_python_client.models.lti_launch_definition import LtiLaunchDefinition
from canvas_lms_python_client.models.lti_registration import LtiRegistration
from canvas_lms_python_client.models.lti_registration_history_entry import (
    LtiRegistrationHistoryEntry,
)
from canvas_lms_python_client.models.lti_resource_link import LtiResourceLink
from canvas_lms_python_client.models.media_object import MediaObject
from canvas_lms_python_client.models.media_object_media_tracks_inner import (
    MediaObjectMediaTracksInner,
)
from canvas_lms_python_client.models.multiple_gradeable_student import MultipleGradeableStudent
from canvas_lms_python_client.models.pace_context import PaceContext
from canvas_lms_python_client.models.pace_contexts_api_index_response import (
    PaceContextsApiIndexResponse,
)
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
from canvas_lms_python_client.models.rubric_used_location import RubricUsedLocation
from canvas_lms_python_client.models.rubric_used_location_assignments_inner import (
    RubricUsedLocationAssignmentsInner,
)
from canvas_lms_python_client.models.user import User
from canvas_lms_python_client.models.user_progress import UserProgress

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


def require_seeded(items: List[T], missing: str, seed_option: str) -> List[T]:
    """Skip, naming the missing data and the seed option that creates it."""
    if not items:
        pytest.skip(
            f"no {missing} found in the seeded Canvas instance (run the seed script with {seed_option})"
        )
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


async def test_course_media_objects_typed(canvas_admin_api_client):
    """Media objects were an @object example, so course listings were untyped."""
    api = MediaObjectsApi(canvas_admin_api_client)
    account = await root_account(canvas_admin_api_client)

    media_objects: List[MediaObject] = []
    for course in await account_courses(canvas_admin_api_client, account):
        # Listing media sources needs Kaltura, which the dev instance doesn't have
        media_objects = await collect(
            api.media_objects_index_for_courses_all(course_id=str(course.id), exclude=["sources"])
        )
        if media_objects:
            break
    require_seeded(media_objects, "course media object", "--media-objects")

    for media_object in media_objects:
        assert isinstance(media_object, MediaObject)
        assert media_object.media_id and media_object.media_type
        for track in media_object.media_tracks or []:
            assert isinstance(track, MediaObjectMediaTracksInner)
            assert track.locale


async def test_lti_registration_history_typed(canvas_admin_api_client):
    """Lti::RegistrationHistoryEntry had no @model, so history items were untyped."""
    account = await root_account(canvas_admin_api_client)
    api = RegistrationsApi(canvas_admin_api_client)

    entries: List[LtiRegistrationHistoryEntry] = []
    for registration in await lti_registrations(canvas_admin_api_client, account):
        entries += await collect(
            api.registrations_history_all(account_id=str(account.id), id=str(registration.id))
        )
    require(entries, "LTI registration history entry")

    for entry in entries:
        assert isinstance(entry, LtiRegistrationHistoryEntry)
        assert isinstance(entry.id, int)
        assert isinstance(entry.lti_registration_id, int)
        assert entry.update_type
        created_by = entry.created_by.actual_instance
        assert created_by == "Instructure" or isinstance(created_by, User)


async def test_rubric_used_locations_typed(canvas_admin_api_client):
    """Used locations named an undefined model and returned one object per page."""
    api = RubricsApiApi(canvas_admin_api_client)
    account = await root_account(canvas_admin_api_client)

    locations: List[RubricUsedLocation] = []
    for course in await account_courses(canvas_admin_api_client, account):
        course_id = str(course.id)
        for rubric in await collect(api.rubrics_api_index_for_courses_all(course_id=course_id)):
            locations = await collect(
                api.rubrics_api_used_locations_all(course_id=course_id, id=str(rubric.id))
            )
            if locations:
                break
        if locations:
            break
    require_seeded(locations, "rubric used in a course", "--rubric-locations")

    for location in locations:
        assert isinstance(location, RubricUsedLocation)
        assert isinstance(location.id, int)
        assert location.name
        assert isinstance(location.concluded, bool)
        for assignment in location.assignments:
            assert isinstance(assignment, RubricUsedLocationAssignmentsInner)
            assert isinstance(assignment.id, int)
            assert assignment.title


async def first_page(iterator: AsyncIterator[T]) -> T:
    """The first page of a `_paginated` iterator."""
    async for page in iterator:
        return page
    raise AssertionError("no page returned")


async def test_course_audit_pages_typed(canvas_admin_api_client):
    """Course audit pages were deserialized as event lists and always failed."""
    account = await root_account(canvas_admin_api_client)
    page = await first_page(
        CourseAuditApiApi(canvas_admin_api_client).course_audit_api_for_account_paginated(account_id=str(account.id))
    )

    assert isinstance(page, CourseAuditApiForAccountResponse)
    events = require_seeded(page.events, "course audit event", "--audit-events")
    assert_typed(events, CourseEvent, id_type=str)
    for event in events:
        assert isinstance(event.links, CourseEventLink)
        assert isinstance(event.links.course, str) and event.links.course
        assert isinstance(event.event_data, dict)


async def test_grade_change_audit_pages_typed(canvas_admin_api_client):
    """Grade change audit pages were deserialized as event lists and always failed."""
    api = GradeChangeAuditApiApi(canvas_admin_api_client)
    account = await root_account(canvas_admin_api_client)

    events: List[GradeChangeEvent] = []
    for course in await account_courses(canvas_admin_api_client, account):
        page = await first_page(api.grade_change_audit_api_for_course_paginated(course_id=str(course.id)))
        assert isinstance(page, GradeChangeAuditApiForCourseResponse)
        events = page.events or []
        if events:
            break
    require(events, "grade change event in any root account course")

    assert_typed(events, GradeChangeEvent, id_type=str)
    for event in events:
        assert isinstance(event.version_number, int)
        assert isinstance(event.links, GradeChangeEventLinks)
        assert isinstance(event.links.student, str)
        assert event.links.grader is None or isinstance(event.links.grader, str)


async def test_authentication_audit_pages_typed(canvas_admin_api_client):
    """Authentication audit operations had no response type and returned nothing."""
    account = await root_account(canvas_admin_api_client)
    page = await first_page(
        AuthenticationAuditApiApi(canvas_admin_api_client).authentication_audit_api_for_account_paginated(
            account_id=str(account.id)
        )
    )

    assert isinstance(page, AuthenticationAuditApiForAccountResponse)
    events = require_seeded(page.events, "authentication event", "--audit-events")
    assert_typed(events, AuthenticationEvent, id_type=str)
    for event in events:
        assert event.event_type in ("login", "logout")
        assert isinstance(event.links, AuthenticationEventLinks)
        assert isinstance(event.links.user, int)


async def test_logins_typed(canvas_admin_api_client):
    """List user logins had no @returns, so login pages were untyped."""
    api = PseudonymsApi(canvas_admin_api_client)

    # The account listing has only the caller's logins in that account
    account_logins: List[Login] = []
    for account in await collect(AccountsApi(canvas_admin_api_client).accounts_index_all()):
        account_logins += await collect(api.pseudonyms_index_all(account_id=str(account.id)))
    user_logins = await collect(api.pseudonyms_index_for_users_all(user_id="self"))

    require(account_logins, "login for the admin in any of its accounts")
    require(user_logins, "login for the admin")

    for login in account_logins + user_logins:
        assert isinstance(login, Login)
        assert isinstance(login.id, int)
        assert isinstance(login.user_id, int)
        assert isinstance(login.account_id, int)
        assert login.unique_id


async def test_conversation_batches_typed(canvas_admin_api_client):
    """Get running batches had no @returns, so batch pages were untyped.

    Canvas lists only the caller's batches. ``--conversation-batch`` seeds one
    for Seeded Admin 2, so run this with that admin's token to exercise it.
    """
    batches = await collect(ConversationsApi(canvas_admin_api_client).conversations_batches_all())
    require_seeded(batches, "running conversation batch for the caller", "--conversation-batch")

    for batch in batches:
        assert isinstance(batch, ConversationBatch)
        assert isinstance(batch.id, int)
        assert batch.workflow_state
        assert isinstance(batch.completion, float)
        assert isinstance(batch.recipient_count, int)
        assert isinstance(batch.message, dict)


async def test_bulk_user_progress_typed(canvas_admin_api_client):
    """Bulk user progress had no @returns, so progress pages were untyped."""
    api = CoursesApi(canvas_admin_api_client)
    account = await root_account(canvas_admin_api_client)

    progress: List[UserProgress] = []
    for course in await account_courses(canvas_admin_api_client, account):
        try:
            progress = await collect(api.courses_bulk_user_progress_all(course_id=str(course.id)))
        except ApiException as error:
            if error.status == 400:  # the course isn't module based
                continue
            raise
        if progress:
            break
    require_seeded(progress, "module progress", "--module-progress")

    for item in progress:
        assert isinstance(item, UserProgress)
        assert isinstance(item.id, int)
        assert item.display_name
        assert isinstance(item.progress, CourseProgress)


async def test_multiple_gradeable_students_typed(canvas_admin_api_client):
    """List multiple assignments gradeable students had no @returns."""
    api = SubmissionsApiApi(canvas_admin_api_client)
    account = await root_account(canvas_admin_api_client)

    students: List[MultipleGradeableStudent] = []
    for course in await account_courses(canvas_admin_api_client, account):
        course_id = str(course.id)
        assignments = await collect(
            AssignmentsApiApi(canvas_admin_api_client).assignments_api_index_all(
                course_id=course_id
            )
        )
        if len(assignments) < 2:
            continue
        students = await collect(
            api.submissions_api_multiple_gradeable_students_all(
                course_id=course_id,
                assignment_ids=[str(assignment.id) for assignment in assignments[:2]],
            )
        )
        if students:
            break
    require(students, "gradeable student in a course with two assignments")

    for student in students:
        assert isinstance(student, MultipleGradeableStudent)
        assert isinstance(student.id, int)
        assert student.display_name
        assert all(isinstance(assignment_id, int) for assignment_id in student.assignment_ids)


@pytest.mark.parametrize("context_type", ["course", "student_enrollment"])
async def test_pace_contexts_pages_typed(canvas_admin_api_client, context_type):
    """List all pace contexts had no @returns, so pace context pages were untyped."""
    api = PaceContextsApiApi(canvas_admin_api_client)
    account = await root_account(canvas_admin_api_client)

    pages: List[PaceContextsApiIndexResponse] = []
    contexts: List[PaceContext] = []
    for course in await account_courses(canvas_admin_api_client, account):
        try:
            pages = await collect(
                api.pace_contexts_api_index_paginated(course_id=str(course.id), type=context_type)
            )
        except ApiException as error:
            if error.status == 404:  # course pacing is off for this course
                continue
            raise
        contexts = wrapped_items(pages, PaceContextsApiIndexResponse, "pace_contexts")
        if contexts:
            break
    require_seeded(contexts, f"{context_type} pace context", "--course-pacing")

    for page in pages:
        assert isinstance(page.total_entries, int)
    for context in contexts:
        assert isinstance(context, PaceContext)
        assert isinstance(context.item_id, int)
        assert context.name and context.type
        if context.applied_pace is not None:
            assert isinstance(context.applied_pace, AppliedPace)
            assert isinstance(context.applied_pace.duration, int)
