"""
Deserialize planner items and todo items, the student dashboard feeds.

List planner items and the two todo item operations had no response type, so
their pages were untyped and they had no ``*_all`` iterator. A planner item's
envelope is typed, but ``plannable`` (its fields depend on ``plannable_type``)
and ``submissions`` (``false`` or a status object) keep what Canvas sent.

The fixtures in ``fixtures/planner/`` were captured from a seeded Canvas
(``--todo-items``: course 2, teacher 7, student 8, assignment 260):

- ``student_planner.json``: the student's ``GET /api/v1/planner/items`` over
  the seeded range (a planner note with an override, and the assignment)
- ``observer_planner.json``: the observer's ``GET /api/v1/users/168/planner/items``
  (first two items)
- ``student_todo.json``: the student's ``GET /api/v1/users/self/todo``
  (the seeded assignment and one other)
- ``course_todo.json``: the teacher's ``GET /api/v1/courses/2/todo``
  (grading items)
"""

import inspect
import json
import pathlib
import typing
from datetime import datetime

import pytest

from canvas_lms_python_client import api
from canvas_lms_python_client.api_client import ApiClient
from canvas_lms_python_client.models import Assignment, PlannerItem, PlannerOverride, Quiz, TodoItem

FIXTURES = pathlib.Path(__file__).parent / "fixtures" / "planner"


def _load(name):
    return json.loads((FIXTURES / f"{name}.json").read_text())


STUDENT_PLANNER = _load("student_planner")
OBSERVER_PLANNER = _load("observer_planner")
PLANNER_ITEMS = STUDENT_PLANNER + OBSERVER_PLANNER
STUDENT_TODO = _load("student_todo")
COURSE_TODO = _load("course_todo")
TODO_ITEMS = STUDENT_TODO + COURSE_TODO

# Operation -> (API class, item model)
OPERATIONS = {
    "planner_index": ("PlannerApi", PlannerItem),
    "planner_index_for_users": ("PlannerApi", PlannerItem),
    "users_todo_items": ("UsersApi", TodoItem),
    "courses_todo_items": ("CoursesApi", TodoItem),
}


def _deserialize(payload, response_type):
    return ApiClient().deserialize(json.dumps(payload), response_type, "application/json")


def _parse_datetime(value):
    return None if value is None else datetime.fromisoformat(value)


def _item_id(item):
    return f"{item.get('plannable_type') or item['type']}-{item.get('plannable_id') or item['assignment']['id']}"


def test_fixtures_have_data():
    assert {item["plannable_type"] for item in STUDENT_PLANNER} == {"assignment", "planner_note"}
    assert {type(item["submissions"]) for item in STUDENT_PLANNER} == {bool, dict}
    assert {item["type"] for item in STUDENT_TODO} == {"submitting"}
    assert {item["type"] for item in COURSE_TODO} == {"grading"}


@pytest.mark.parametrize("operation", sorted(OPERATIONS))
def test_operation_pages_are_item_lists(operation):
    api_class, model = OPERATIONS[operation]
    api_type = getattr(api, api_class)

    paginated = getattr(api_type, f"{operation}_paginated")
    (page_type,) = typing.get_args(paginated.__annotations__["return"])
    assert typing.get_args(page_type) == (model,)

    all_items = inspect.signature(getattr(api_type, f"{operation}_all"))
    assert model.__name__ in str(all_items.return_annotation)


@pytest.mark.parametrize("payload", [PLANNER_ITEMS, TODO_ITEMS], ids=["planner", "todo"])
def test_page_deserializes(payload):
    model = PlannerItem if payload is PLANNER_ITEMS else TodoItem

    items = _deserialize(payload, f"List[{model.__name__}]")

    assert len(items) == len(payload)
    assert all(isinstance(item, model) for item in items)


@pytest.mark.parametrize("item", PLANNER_ITEMS, ids=_item_id)
def test_planner_item_envelope_is_typed(item):
    planner_item = PlannerItem.from_dict(item)

    assert planner_item.plannable_id == item["plannable_id"]
    assert isinstance(planner_item.plannable_id, int)
    assert planner_item.plannable_type == item["plannable_type"]
    assert planner_item.plannable_date == _parse_datetime(item["plannable_date"])
    assert planner_item.course_id == item.get("course_id")
    assert planner_item.html_url == item.get("html_url")
    assert planner_item.new_activity is item["new_activity"]
    # Untyped: kept as Canvas sent them
    assert planner_item.plannable == item["plannable"]
    assert planner_item.submissions == item["submissions"]
    assert planner_item.plannable["id"] == item["plannable_id"]


def test_planner_note_has_typed_override():
    item = next(item for item in STUDENT_PLANNER if item["plannable_type"] == "planner_note")

    planner_item = PlannerItem.from_dict(item)

    assert planner_item.submissions is False
    assert isinstance(planner_item.planner_override, PlannerOverride)
    assert planner_item.planner_override.id == item["planner_override"]["id"]
    assert planner_item.planner_override.marked_complete is False
    assert planner_item.course_id is None


def test_assignment_submissions_are_a_mapping():
    item = next(item for item in STUDENT_PLANNER if item["plannable_type"] == "assignment")

    planner_item = PlannerItem.from_dict(item)

    assert planner_item.planner_override is None
    assert planner_item.submissions == item["submissions"]
    assert planner_item.submissions["submitted"] is False
    assert planner_item.context_image is None


@pytest.mark.parametrize("item", TODO_ITEMS, ids=_item_id)
def test_todo_item_has_typed_assignment(item):
    todo_item = TodoItem.from_dict(item)

    assert todo_item.type == item["type"]
    assert todo_item.course_id == item["course_id"]
    assert todo_item.ignore == item["ignore"]
    assert todo_item.html_url == item["html_url"]
    assert todo_item.quiz is None
    assert isinstance(todo_item.assignment, Assignment)
    assert todo_item.assignment.id == item["assignment"]["id"]
    assert todo_item.assignment.due_at == _parse_datetime(item["assignment"]["due_at"])


@pytest.mark.parametrize("item", COURSE_TODO, ids=_item_id)
def test_grading_todo_item_has_count(item):
    todo_item = TodoItem.from_dict(item)

    assert todo_item.needs_grading_count == item["needs_grading_count"]
    assert isinstance(todo_item.needs_grading_count, int)


def test_quiz_todo_item_has_typed_quiz():
    """Quizzes due soon carry ``quiz`` (``quiz_json``) instead of ``assignment``."""
    item = {key: value for key, value in STUDENT_TODO[0].items() if key != "assignment"}
    item["quiz"] = {"id": 5, "title": "Seeded quiz", "quiz_type": "assignment", "points_possible": 10.0}

    todo_item = TodoItem.from_dict(item)

    assert todo_item.assignment is None
    assert isinstance(todo_item.quiz, Quiz)
    assert todo_item.quiz.id == 5
