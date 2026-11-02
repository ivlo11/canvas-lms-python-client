"""
Pytest configuration and fixtures for canvas-python-client tests.
"""

import os
import pathlib

import pytest

from canvas_lms_python_client.api_client import ApiClient
from canvas_lms_python_client.configuration import Configuration


def pytest_addoption(parser):
    """Register the --integration option."""
    parser.addoption(
        "--integration",
        action="store_true",
        default=False,
        help="run integration tests against a live Canvas instance",
    )


INTEGRATION_DIR = pathlib.Path(__file__).parent / "integration"


def pytest_collection_modifyitems(config, items):
    """
    Mark every test under custom/integration as an integration test, then
    skip integration-marked tests unless --integration is passed.
    """
    for item in items:
        if item.path.is_relative_to(INTEGRATION_DIR):
            item.add_marker(pytest.mark.integration)
    if config.getoption("--integration"):
        return
    skip_integration = pytest.mark.skip(reason="use --integration to run")
    for item in items:
        if "integration" in item.keywords:
            item.add_marker(skip_integration)


@pytest.fixture(scope="session")
def canvas_base_url() -> str | None:
    """
    Canvas base URL from environment.

    Set CANVAS_BASE_URL environment variable for integration tests.
    """
    return os.getenv("CANVAS_BASE_URL")


@pytest.fixture(scope="session")
def canvas_api_token() -> str | None:
    """
    Canvas API token from environment.

    Set CANVAS_API_TOKEN environment variable for integration tests.
    """
    return os.getenv("CANVAS_API_TOKEN")


@pytest.fixture
async def skip_integration_tests(canvas_base_url, canvas_api_token):
    """
    Skip integration tests if Canvas credentials are not configured.

    Usage in test:
        @pytest.mark.integration
        async def test_something(skip_integration_tests):
            # Your integration test code
    """
    if not canvas_base_url or not canvas_api_token:
        pytest.skip("Integration tests require CANVAS_BASE_URL and CANVAS_API_TOKEN")


@pytest.fixture
async def canvas_api_client(canvas_base_url, canvas_api_token):
    """
    Authenticated async ApiClient for integration tests.

    Skips the test when CANVAS_BASE_URL or CANVAS_API_TOKEN is unset.
    The client session is closed when the test finishes.
    """
    missing = [
        name
        for name, value in (
            ("CANVAS_BASE_URL", canvas_base_url),
            ("CANVAS_API_TOKEN", canvas_api_token),
        )
        if not value
    ]
    if missing:
        pytest.skip(f"Integration tests require {', '.join(missing)} to be set")

    config = Configuration(host=canvas_base_url, access_token=canvas_api_token)
    async with ApiClient(config) as client:
        yield client


@pytest.fixture(scope="session")
def canvas_admin_api_token() -> str | None:
    """
    Canvas account admin API token from environment.

    Set CANVAS_ADMIN_API_TOKEN environment variable for admin-scoped integration tests.
    """
    return os.getenv("CANVAS_ADMIN_API_TOKEN")


@pytest.fixture
async def canvas_admin_api_client(canvas_base_url, canvas_admin_api_token):
    """
    Authenticated async ApiClient for admin-scoped integration tests.

    Skips the test when CANVAS_BASE_URL or CANVAS_ADMIN_API_TOKEN is unset.
    The client session is closed when the test finishes.
    """
    missing = [
        name
        for name, value in (
            ("CANVAS_BASE_URL", canvas_base_url),
            ("CANVAS_ADMIN_API_TOKEN", canvas_admin_api_token),
        )
        if not value
    ]
    if missing:
        pytest.skip(f"Integration tests require {', '.join(missing)} to be set")

    config = Configuration(host=canvas_base_url, access_token=canvas_admin_api_token)
    async with ApiClient(config) as client:
        yield client


@pytest.fixture(scope="session")
def canvas_student_api_token() -> str | None:
    """
    Canvas student API token from environment.

    Set CANVAS_STUDENT_API_TOKEN environment variable for student-scoped integration tests.
    """
    return os.getenv("CANVAS_STUDENT_API_TOKEN")


@pytest.fixture
async def canvas_student_api_client(canvas_base_url, canvas_student_api_token):
    """
    Authenticated async ApiClient for student-scoped integration tests.

    Skips the test when CANVAS_BASE_URL or CANVAS_STUDENT_API_TOKEN is unset.
    The client session is closed when the test finishes.
    """
    missing = [
        name
        for name, value in (
            ("CANVAS_BASE_URL", canvas_base_url),
            ("CANVAS_STUDENT_API_TOKEN", canvas_student_api_token),
        )
        if not value
    ]
    if missing:
        pytest.skip(f"Integration tests require {', '.join(missing)} to be set")

    config = Configuration(host=canvas_base_url, access_token=canvas_student_api_token)
    async with ApiClient(config) as client:
        yield client


@pytest.fixture
def sample_link_header():
    """Sample Canvas Link header for testing."""
    return (
        '<https://canvas.example.com/api/v1/courses?page=1>; rel="first", '
        '<https://canvas.example.com/api/v1/courses?page=2>; rel="next", '
        '<https://canvas.example.com/api/v1/courses?page=3>; rel="prev", '
        '<https://canvas.example.com/api/v1/courses?page=10>; rel="last", '
        '<https://canvas.example.com/api/v1/courses?page=3>; rel="current"'
    )


@pytest.fixture
def sample_next_link_header():
    """Sample Canvas Link header with only next link."""
    return '<https://canvas.example.com/api/v1/courses?page=2>; rel="next"'


@pytest.fixture
def sample_last_link_header():
    """Sample Canvas Link header from last page (no next link)."""
    return '<https://canvas.example.com/api/v1/courses?page=1>; rel="prev","last"'


# Async test configuration
def pytest_configure(config):
    """Configure pytest for async tests."""
    config.addinivalue_line(
        "markers", "integration: mark test as integration test (requires Canvas instance)"
    )
