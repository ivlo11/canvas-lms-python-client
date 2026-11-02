"""
Check that list query parameters go out in Canvas's bracket form.

Canvas reads list query parameters only as ``name[]=a&name[]=b``. Sent as
``name=a&name=b`` it ignores the filter or fails the request, so these tests
build the request URL offline and check the wire names.
"""

from urllib.parse import parse_qsl, urlsplit

from canvas_lms_python_client.api.lti_apps_api import LtiAppsApi
from canvas_lms_python_client.api_client import ApiClient
from canvas_lms_python_client.configuration import Configuration


def launch_definitions_query(**params):
    api = LtiAppsApi(ApiClient(Configuration(host="http://canvas.test")))
    args = {
        "course_id": "8",
        "placements": None,
        "only_visible": None,
        "include_context_name": None,
        "page": None,
        "per_page": None,
        "_request_auth": None,
        "_content_type": None,
        "_headers": None,
        "_host_index": 0,
    }
    _method, url, *_ = api._lti_apps_launch_definitions_serialize(**{**args, **params})
    return parse_qsl(urlsplit(url).query)


def test_list_values_repeat_with_brackets():
    query = launch_definitions_query(placements=["course_navigation", "account_navigation"])

    assert query == [
        ("placements[]", "course_navigation"),
        ("placements[]", "account_navigation"),
    ]


def test_single_value_list_keeps_brackets():
    query = launch_definitions_query(placements=["course_navigation"])

    assert query == [("placements[]", "course_navigation")]


def test_scalar_params_stay_unbracketed():
    query = launch_definitions_query(placements=["course_navigation"], per_page=50)

    assert query == [("placements[]", "course_navigation"), ("per_page", "50")]
