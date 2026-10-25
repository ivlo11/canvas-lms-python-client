"""
Pytest configuration and fixtures for canvas-python-client tests.
"""

import os

import pytest


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
