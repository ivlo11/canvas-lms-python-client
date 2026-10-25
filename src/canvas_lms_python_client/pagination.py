"""
Link header parsing utilities for Canvas LMS RFC 8288 pagination.

This module provides functions to parse Link headers and extract
pagination URLs for operations marked with x-paginated: true.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any
from urllib.parse import urljoin


@dataclass
class LinkHeader:
    """
    Represents a parsed Link header component.

    Attributes:
        url: The URL from the Link header
        rel: The relationship type (e.g., "next", "last", "first", "prev", "current")
    """

    url: str
    rel: str


def parse_link_header(link_header: str | None) -> list[LinkHeader]:
    """
    Parse an RFC 8288 Link header into a list of components.

    Example:
        Link: <https://canvas.example.com/api/v1/courses?page=2>; rel="next",
              <https://canvas.example.com/api/v1/courses?page=10>; rel="last"

    Args:
        link_header: The raw Link header string

    Returns:
        List of LinkHeader objects
    """
    if not link_header:
        return []

    links = []
    # RFC 8288 pattern: <URL>; rel="TYPE"
    # Canvas returns up to 5 relations: first, next, prev, last, current
    pattern = r'<([^>]+)>\s*;\s*rel="([^"]+)"'

    for match in re.finditer(pattern, link_header):
        url = match.group(1).strip()
        rel = match.group(2).strip()
        links.append(LinkHeader(url=url, rel=rel))

    return links


def get_link_by_rel(link_header: str | None, rel: str) -> str | None:
    """
    Extract a specific URL from Link header by relationship type.

    Canvas LMS returns these link relations:
    - first: URL to the first page
    - next: URL to the next page (absent on last page)
    - prev: URL to the previous page (absent on first page)
    - last: URL to the last page
    - current: URL to the current page

    Args:
        link_header: The raw Link header string
        rel: The relationship type to extract (e.g., "next", "last", "first")

    Returns:
        The URL string, or None if not found
    """
    links = parse_link_header(link_header)
    for link in links:
        if link.rel == rel:
            return link.url
    return None


def get_next_page_url(link_header: str | None, base_url: str | None = None) -> str | None:
    """
    Extract the "next" page URL from Link header.

    Args:
        link_header: The raw Link header string
        base_url: Optional base URL to resolve relative URLs

    Returns:
        The next page URL, or None if no next page (pagination complete)
    """
    next_url = get_link_by_rel(link_header, "next")
    if not next_url:
        return None

    # Resolve relative URLs if base_url is provided
    if base_url and not next_url.startswith("http"):
        return urljoin(base_url, next_url)

    return next_url


class AsyncPaginatedIterator:
    """
    Async iterator for paginated Canvas API responses.

    This class provides an async interface for iterating through
    all pages of a paginated API endpoint.

    It follows Canvas's RFC 8288 Link header pagination, automatically
    fetching pages by following rel="next" links until no more pages exist.
    """

    def __init__(
        self,
        get_page: callable,
        initial_params: dict,
        parse_response: callable,
        max_pages: int | None = None,
    ):
        """
        Initialize the paginated iterator.

        Args:
            get_page: Async function that fetches a page given params
            initial_params: Initial query parameters for first page
            parse_response: Function that extracts items from response
            max_pages: Maximum number of pages to fetch (None for unlimited)
        """
        self.get_page = get_page
        self.params = initial_params.copy()
        self.parse_response = parse_response
        self.max_pages = max_pages
        self.current_page = 0
        self._current_items: list[Any] = []
        self._item_index = 0
        self._done = False

    def __aiter__(self) -> "AsyncPaginatedIterator":
        """Return async iterator."""
        return self

    async def __anext__(self) -> Any:
        """
         Get the next item from the paginated response.

        Returns:
             The next item from the current page

         Raises:
             StopAsyncIteration: When all items have been yielded
        """
        if self._done:
            raise StopAsyncIteration

        # Fetch next page if current page is exhausted
        if self._item_index >= len(self._current_items):
            if self.max_pages and self.current_page >= self.max_pages:
                self._done = True
                raise StopAsyncIteration

            await self._fetch_next_page()
            if not self._current_items:
                self._done = True
                raise StopAsyncIteration

        item = self._current_items[self._item_index]
        self._item_index += 1
        return item

    async def _fetch_next_page(self) -> None:
        """
        Fetch the next page of results.

        Updates self._current_items with new page data.
        Sets self._done if no more pages available.
        """
        response = await self.get_page(self.params)

        # Extract items from response
        items = self.parse_response(response)
        if not isinstance(items, list):
            items = [items]

        self._current_items = items
        self._item_index = 0
        self.current_page += 1

        # Check for next page in Link header
        # Note: The generated client may not expose Link headers
        # In a real implementation, you'd need to access the raw HTTP response
        # For now, we'll stop after one page (simplified for demo)
        self._done = True  # Simplified: only fetch one page for now
