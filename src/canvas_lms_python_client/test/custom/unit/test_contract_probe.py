"""Offline checks that the contract probe finds GETs and records no values."""

import json

from canvas_lms_python_client.test.custom.integration.contract_runner import (
    RoleResult,
    build_record,
    collect_fields,
    discover_operations,
    key_name,
    skip_reason,
    write_result,
)

RECORD_KEYS = {"route", "method", "status", "role", "container", "api", "string_ids", "fields"}


def test_discovers_only_gets():
    operations = {operation.name: operation for operation in discover_operations()}

    assert operations["tabs_index"].route == "/api/v1/accounts/{account_id}/tabs"
    assert "tabs_update" not in operations


def test_record_holds_names_and_types_only():
    body = [{"name": "secret-name", "token": "secret-token", "score": 1.5, "tags": ["secret-tag"], "user": {"id": 42}}]

    record = build_record("/api/v1/things", 200, "student", body)

    assert set(record) == RECORD_KEYS
    assert record["container"] == "list"
    assert record["fields"]["[].token"] == ["string"]
    assert record["fields"]["[].score"] == ["number"]
    assert record["fields"]["[].tags[]"] == ["string"]
    assert record["fields"]["[].user.id"] == ["integer"]
    serialized = json.dumps(record)
    assert "secret" not in serialized
    assert "42" not in serialized


def test_keys_that_may_be_data_are_hidden():
    for key in ("1234", "someone@example.com", "a1b2c3d4e5f60718293a", "x" * 65):
        assert key_name(key) == "*"
    assert key_name("group_weight") == "group_weight"


def test_booleans_are_not_integers():
    fields = {}
    collect_fields({"flag": True}, "", fields)

    assert fields == {"flag": {"boolean"}}


def test_session_token_download_and_launch_routes_are_skipped():
    assert skip_reason("/api/v1/login/session_token") == "session"
    assert skip_reason("/api/v1/users/{id}/tokens") == "token"
    assert skip_reason("/api/v1/files/{id}/download") == "download"
    assert skip_reason("/api/v1/accounts/{id}/external_tools/sessionless_launch") == "session"
    assert skip_reason("/api/v1/courses/{course_id}/lti_launch") == "launch"
    assert skip_reason("/api/v1/courses/{course_id}/assignments") is None


def test_written_output_has_no_values(tmp_path):
    result = RoleResult("student")
    result.outcomes = {"a": "parsed", "b": "skipped:no_data:id", "c": "http_403", "d": "parse_failure"}
    result.failures = {"d": ["response.0.score:int_type"]}
    result.records = [build_record("/api/v1/things", 200, "student", {"secret": "secret-value"})]

    write_result(result, tmp_path)

    report = json.loads((tmp_path / "contract-student.json").read_text())
    assert report["counts"] == {"parsed": 1, "skipped": 1, "http_error": 1, "parse_failure": 1}
    lines = (tmp_path / "probes-student.jsonl").read_text().splitlines()
    assert set(json.loads(lines[0])) == RECORD_KEYS
    assert "secret-value" not in lines[0]
