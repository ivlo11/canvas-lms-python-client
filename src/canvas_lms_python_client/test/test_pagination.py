"""
Tests for Canvas LMS Link header pagination utilities.
"""

import pytest

from canvas_lms_python_client.pagination import (
    LinkHeader,
    get_link_by_rel,
    get_next_page_url,
    parse_link_header,
)


@pytest.mark.parametrize(
    "link_header,expected_count",
    [
        ('<https://api.example.com/page1>; rel="next"', 1),
        (
            '<https://api.example.com/page1>; rel="next", <https://api.example.com/page2>; rel="last"',
            2,
        ),
        (
            '<https://api.example.com/page1>; rel="first", <https://api.example.com/page2>; rel="next", <https://api.example.com/page3>; rel="prev", <https://api.example.com/page4>; rel="last", <https://api.example.com/page5>; rel="current"',
            5,
        ),
        ("", 0),
    ],
)
def test_parse_link_header_count(link_header, expected_count):
    """Test parsing link header returns correct number of links."""
    links = parse_link_header(link_header)
    assert len(links) == expected_count


@pytest.mark.parametrize(
    "link_header,expected_links",
    [
        (
            '<https://api.example.com/page1>; rel="next"',
            [LinkHeader(url="https://api.example.com/page1", rel="next")],
        ),
        (
            '<https://api.example.com/page1>; rel="next", <https://api.example.com/page2>; rel="last"',
            [
                LinkHeader(url="https://api.example.com/page1", rel="next"),
                LinkHeader(url="https://api.example.com/page2", rel="last"),
            ],
        ),
    ],
)
def test_parse_link_header_content(link_header, expected_links):
    """Test parsing link header returns correct LinkHeader objects."""
    links = parse_link_header(link_header)
    assert links == expected_links


def test_parse_link_header_empty():
    """Test parsing empty link header returns empty list."""
    links = parse_link_header("")
    assert links == []


def test_parse_link_header_none():
    """Test parsing None link header returns empty list."""
    links = parse_link_header(None)
    assert links == []


def test_parse_link_header_none_string():
    """Test parsing 'None' string link header returns empty list."""
    links = parse_link_header(None)
    assert links == []


@pytest.mark.parametrize(
    "link_header,rel,expected_url",
    [
        ('<https://api.example.com/page1>; rel="next"', "next", "https://api.example.com/page1"),
        (
            '<https://api.example.com/page1>; rel="next", <https://api.example.com/page2>; rel="last"',
            "last",
            "https://api.example.com/page2",
        ),
        (
            '<https://api.example.com/page1>; rel="next", <https://api.example.com/page2>; rel="last"',
            "next",
            "https://api.example.com/page1",
        ),
        ('<https://api.example.com/page1>; rel="next"', "last", None),
        (
            '<https://api.example.com/page1>; rel="next", <https://api.example.com/page2>; rel="last"',
            "prev",
            None,
        ),
    ],
)
def test_get_link_by_rel(link_header, rel, expected_url):
    """Test extracting specific relation from link header."""
    url = get_link_by_rel(link_header, rel)
    assert url == expected_url, f"Expected {expected_url}, got {url}"


def test_get_link_by_rel_canvas_style():
    """Test extracting all Canvas link relations."""
    link_header = (
        '<https://canvas.example.com/api/v1/courses?page=1>; rel="first", '
        '<https://canvas.example.com/api/v1/courses?page=2>; rel="next", '
        '<https://canvas.example.com/api/v1/courses?page=3>; rel="prev", '
        '<https://canvas.example.com/api/v1/courses?page=10>; rel="last", '
        '<https://canvas.example.com/api/v1/courses?page=3>; rel="current"'
    )

    assert (
        get_link_by_rel(link_header, "first") == "https://canvas.example.com/api/v1/courses?page=1"
    )
    assert (
        get_link_by_rel(link_header, "next") == "https://canvas.example.com/api/v1/courses?page=2"
    )
    assert (
        get_link_by_rel(link_header, "prev") == "https://canvas.example.com/api/v1/courses?page=3"
    )
    assert (
        get_link_by_rel(link_header, "last") == "https://canvas.example.com/api/v1/courses?page=10"
    )
    assert (
        get_link_by_rel(link_header, "current")
        == "https://canvas.example.com/api/v1/courses?page=3"
    )


def test_get_next_page_url():
    """Test extracting next page URL."""
    link_header = '<https://canvas.example.com/api/v1/courses?page=2>; rel="next"'
    next_url = get_next_page_url(link_header)
    assert next_url == "https://canvas.example.com/api/v1/courses?page=2"


def test_get_next_page_url_none():
    """Test extracting next page URL when no next link exists."""
    link_header = '<https://canvas.example.com/api/v1/courses?page=1>; rel="last"'
    next_url = get_next_page_url(link_header)
    assert next_url is None


def test_get_next_page_url_multiple_links():
    """Test extracting next page URL from multiple links."""
    link_header = (
        '<https://canvas.example.com/api/v1/courses?page=1>; rel="first", '
        '<https://canvas.example.com/api/v1/courses?page=2>; rel="next", '
        '<https://canvas.example.com/api/v1/courses?page=10>; rel="last"'
    )
    next_url = get_next_page_url(link_header)
    assert next_url == "https://canvas.example.com/api/v1/courses?page=2"
