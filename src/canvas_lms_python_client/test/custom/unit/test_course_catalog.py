"""
Deserialize the public course catalog (``GET /api/v1/search/all_courses``).

``fixtures/catalog/all_courses.json`` was captured from the seeded Canvas with
the admin token, after ``--contract-data`` turned the catalog on. Canvas renders
``Course#as_json``: each item wraps the raw course record in a ``course`` key, so
a ``Course`` model would find none of its fields there.

If the docs miss a column the catalog returns, or the ``course`` key stops
resolving to ``CatalogCourse``, these assertions fail.
"""

import json
import pathlib
from datetime import datetime

from canvas_lms_python_client.api_client import ApiClient
from canvas_lms_python_client.models import CatalogCourse, CatalogCourseEntry

FIXTURE = pathlib.Path(__file__).parent / "fixtures" / "catalog" / "all_courses.json"

PAYLOAD = json.loads(FIXTURE.read_text())


def _entries():
    return ApiClient().deserialize(json.dumps(PAYLOAD), "List[CatalogCourseEntry]", "application/json")


def test_catalog_items_are_typed_entries():
    entries = _entries()

    assert len(entries) == len(PAYLOAD)
    for entry, item in zip(entries, PAYLOAD):
        assert isinstance(entry, CatalogCourseEntry)
        assert isinstance(entry.course, CatalogCourse)
        for field in ("id", "name", "workflow_state"):
            assert getattr(entry.course, field) == item["course"][field], field
        assert entry.course.created_at == datetime.fromisoformat(item["course"]["created_at"])


def test_every_returned_column_is_a_field():
    for item in PAYLOAD:
        assert set(item["course"]) - set(CatalogCourse.model_fields) == set()


def test_internal_looking_columns_are_kept():
    for entry, item in zip(_entries(), PAYLOAD):
        record = item["course"]
        assert entry.course.settings == record["settings"]
        assert entry.course.stuck_sis_fields == record["stuck_sis_fields"]
        assert entry.course.self_enrollment_code == record["self_enrollment_code"]
        assert entry.course.sis_source_id == record["sis_source_id"]


def test_null_only_columns_deserialize_as_none():
    for entry, item in zip(_entries(), PAYLOAD):
        for field in ("start_at", "conclude_at", "public_description", "self_enrollment_code"):
            assert item["course"][field] is None, field
            assert getattr(entry.course, field) is None, field
