"""
Every GET the seeded instance answers must parse through the generated client.

Runs as each role, and writes a report and audit evidence per role to
CANVAS_CONTRACT_OUTPUT (default build/contract). Failures name operations and error
kinds only, never values or tokens.
"""

import json
import os

import pytest

from .contract_runner import ContractRunner, discover_operations, write_result

ROLE_TOKENS = {
    "admin": "CANVAS_ADMIN_API_TOKEN",
    "teacher": "CANVAS_TEACHER_API_TOKEN",
    "observer": "CANVAS_API_TOKEN",
    "student": "CANVAS_STUDENT_API_TOKEN",
}
OUTPUT_DIRECTORY = os.getenv("CANVAS_CONTRACT_OUTPUT", "build/contract")


@pytest.mark.parametrize("role", sorted(ROLE_TOKENS))
async def test_every_get_parses(role):
    base_url = os.getenv("CANVAS_BASE_URL")
    token = os.getenv(ROLE_TOKENS[role])
    if not base_url or not token:
        pytest.skip(f"Contract test requires CANVAS_BASE_URL and {ROLE_TOKENS[role]} to be set")

    result = await ContractRunner(base_url, token, role).run(discover_operations())
    write_result(result, OUTPUT_DIRECTORY)

    assert not result.failures, f"{len(result.failures)} operations failed to parse as {role}:\n" + json.dumps(
        result.failures, indent=2, sort_keys=True
    )
