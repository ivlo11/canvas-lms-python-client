# Canvas LMS Python Client

Async Python client library for Canvas LMS API with automatic Link header pagination support.

**Generated from** [Canvas LMS OpenAPI specification](https://github.com/instructure/canvas-lms)

> **Note:** This client is auto-generated from Canvas's OpenAPI spec, ensuring it includes all current endpoints and stays in sync as Canvas adds new features.

## Features

- ✅ **Full-coverage client** - Generated from spec, includes all Canvas API endpoints
- ✅ **Async/await support** - Built with asyncio for Home Assistant integration
- ✅ **Link header pagination** - Automatic handling of Canvas's RFC 8288 pagination
- ✅ **Type-safe** - Pydantic v2 models with full type hints
- ✅ **Up-to-date** - Regenerates automatically when Canvas's spec changes

## Installation

```bash
pdm add "git+https://github.com/ivlo11/canvas-lms-python-client"
```

### Development Installation

```bash
git clone https://github.com/ivlo11/canvas-lms-python-client
pdm install -G dev
```

## Quick Start

In your own code, to use this library to connect and interact with canvas-lms-python-client,
you can run the following:

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.account import Account
from canvas_lms_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://canvas.instructure.com
# See configuration.py for a list of all supported configuration parameters.
configuration = canvas_lms_python_client.Configuration(
    host = "https://canvas.instructure.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (token): bearer
configuration = canvas_lms_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with canvas_lms_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = canvas_lms_python_client.AccountsApi(api_client)
    page = 1 # int | The page number to return. Defaults to 1. (optional)
    per_page = 50 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List accounts for course admins
        api_response = await api_instance.accounts_course_accounts(page=page, per_page=per_page)
        print("The response of AccountsApi->accounts_course_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->accounts_course_accounts: %s\n" % e)

    try:
        # List accounts for course admins
        async for page in api_instance.accounts_course_accounts_paginated(page=page, per_page=per_page)
            print(f"Fetched {len(page)} items")
            for item in page:
                print(f"{item.name} (ID: {item.id})")
    except Exception as e:
        print("Exception when calling AccountsApi->accounts_course_accounts_paginated: %s\n" % e)
```

## Pagination

Canvas uses [RFC 8288 Link headers](https://www.rfc-editor.org/rfc/rfc8288) for pagination. Operations marked with `x-paginated: true` in the spec generate both regular and paginated methods:

### Paginated Method (Recommended)

```python
# Enter a context with an instance of the API client
async with canvas_lms_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = canvas_lms_python_client.AccountsApi(api_client)
    page = 1 # int | The page number to return. Defaults to 1. (optional)
    per_page = 50 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List accounts for course admins
        async for page in api_instance.accounts_course_accounts_paginated(page=page, per_page=per_page)
            print(f"Fetched {len(page)} items")
            for item in page:
                print(f"{item.name} (ID: {item.id})")
    except Exception as e:
        print("Exception when calling AccountsApi->accounts_course_accounts_paginated: %s\n" % e)
```

### Single Page (For Testing)

```python
# Enter a context with an instance of the API client
async with canvas_lms_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = canvas_lms_python_client.AccountsApi(api_client)
    page = 1 # int | The page number to return. Defaults to 1. (optional)
    per_page = 50 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List accounts for course admins
        api_response = await api_instance.accounts_course_accounts(page=page, per_page=per_page)
        print("The response of AccountsApi->accounts_course_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->accounts_course_accounts: %s\n" % e)

```

### All Items

Operations whose pages are lists also generate `<operation>_all`, which yields each item across all pages:

```python
async for account in api_instance.accounts_course_accounts_all(per_page=50):
    print(account.name)
```

### Wrapped List Responses

Some Canvas endpoints wrap each page in an object, for example `{"polls": [...]}`. For these, `_paginated` yields one wrapper model per page (such as `PollsResponse`), and no `_all` method is generated. Read the list attribute from each page:

```python
async for page in polls_api.polls_index_paginated(per_page=50):
    for poll in page.polls or []:
        print(poll.question)
```

### List Query Parameters

List query parameters are sent in Canvas's bracket form, one `name[]=value` pair per value. Argument names are unchanged:

```python
# GET /api/v1/accounts/1/courses?include[]=term&include[]=teachers
await accounts_api.accounts_courses_api(account_id="1", include=["term", "teachers"])
```

Earlier versions sent `include=term&include=teachers`, which Canvas ignored or rejected. List filters such as `include`, `enrollment_type`, `context_codes` and `placements` now take effect, so calls that pass them may return different results than before.

### Breaking Changes

`<operation>_all` is now generated only for operations whose response is a list. It was removed from every paginated operation whose response is a wrapper model (e.g. `polls_index`, `terms_api_index`, `registrations_list`), an untyped object (`rubrics_api_used_locations`), or undocumented. On those operations it yielded either nothing or one whole wrapper per page. Iterate `<operation>_paginated` instead and read the wrapper's list attribute, as shown above.

Model field types now match what Canvas sends:
- `Poll`, `PollChoice`, `PollSession` and `PollSubmission` ids (`id` and every `*_id`) are strings, because Canvas's polling endpoints always send ids as strings. `PollSession.poll_submissions` is a list, and `PollChoice.poll_id` is optional.
- `QuizSubmission.score`, `kept_score`, `score_before_regrade`, `fudge_points` and `Quiz.points_possible` accept floats.
- `LtiLaunchDefinition.definition_id` is an integer, and `LtiOverlayVersion.diff` is a list of change tuples (`["~", "title", "old", "new"]`).
- `created_by` / `updated_by` on `LtiRegistration`, `LtiRegistrationAccountBinding` and `LtiOverlayVersion` are a `LtiRegistrationCreatedBy` wrapper. Its `actual_instance` is a `User`, or the string `"Instructure"` when Canvas hides a site admin.

LTI operations whose Canvas docs name a namespaced model (`Lti::…`) now return that model instead of a dict. Use attributes (`deployment.context_id`) instead of keys (`deployment["context_id"]`):
- Paginated lists (`_paginated` pages, and `_all` items):
  - `deployments_list` and `context_controls_index` → `List[LtiDeployment]` (`context_controls_index` groups the controls by deployment, under `context_controls`)
  - `deployments_list_controls` → `List[LtiContextControl]`
  - `lti_apps_launch_definitions` and `lti_apps_launch_definitions_for_accounts` → `List[LtiLaunchDefinition]`
  - `resource_links_index` → `List[LtiResourceLink]`
- Context controls: `context_controls_create`, `context_controls_show`, `context_controls_update` and `context_controls_delete` → `LtiContextControl`; `context_controls_create_many` → `List[LtiContextControl]`
- Deployments: `deployments_create`, `deployments_show` and `deployments_destroy` → `LtiDeployment`
- Registrations:
  - `registrations_create`, `registrations_show`, `registrations_update`, `registrations_destroy`, `registrations_show_by_client_id`, `registrations_show_by_utid`, `registrations_install_status`, `registrations_reset`, `registrations_install_from_template` and `registrations_apply_registration_update_request` → `LtiRegistration`
  - `registrations_bind` and `registrations_unbind` → `LtiRegistrationAccountBinding`
  - `registrations_overlay_history` → `List[LtiOverlayVersion]`
- Resource links: `resource_links_create`, `resource_links_show`, `resource_links_update` and `resource_links_destroy` → `LtiResourceLink`; `resource_links_bulk_create` → `List[LtiResourceLink]`

`registrations_history`, `registrations_show_registration_update_request` and `registrations_latest_registration_update_request` still return untyped objects, because Canvas documents no model for them.

### Link Header Relations

Canvas returns five link relations in the Link header:

- `rel="first"` - First page URL
- `rel="next"` - Next page URL (absent on last page)
- `rel="prev"` - Previous page URL (absent on first page)
- `rel="last"` - Last page URL
- `rel="current"` - Current page URL

The `_paginated` methods use `rel="next"` automatically. If you need access to specific relations:

```python
from canvas_lms_python_client.pagination import get_link_by_rel


async with canvas_lms_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = canvas_lms_python_client.AccountsApi(api_client)
    
    try:
        # List accounts for course admins
        api_response = await api_instance.accounts_course_accounts_with_http_info(page=page, per_page=per_page)
        link_header = api_response.headers.get('Link', '')
        
        last_url = get_link_by_rel(link_header, 'last')
        prev_url = get_link_by_rel(link_header, 'prev')
        
        print(f"Last Page: {last_url})")
        print(f"Previous Page: {prev_url})")
    except Exception as e:
        print("Exception when calling AccountsApi->accounts_course_accounts: %s\n" % e)

```

## Pagination Utilities

Direct access to Link header parsing utilities:

```python
from canvas_lms_python_client.pagination import (
    parse_link_header,
    get_link_by_rel,
    get_next_page_url,
)

# Parse all links from header
links = parse_link_header(
    '<https://canvas.instructure.com/api/v1/courses?page=2>; rel="next", '
    '<https://canvas.instructure.com/api/v1/courses?page=10>; rel="last"'
)

for link in links:
    print(f"{link.rel}: {link.url}")

# Get specific relation
next_url = get_link_by_rel(link_header, 'next')
last_url = get_link_by_rel(link_header, 'last')
```

## Configuration

### API Token

Generate an API token from Canvas:
1. Log in to Canvas
2. Go to "Account" → "Settings"
3. Scroll to "Approved Integrations"
4. Click "+ New Access Token"
5. Enter a purpose and create the token

### Python Environment

```bash
# Python 3.11+
python3 --version

# Install dependencies
pdm install

# Development dependencies
pdm install -G dev
```

## Testing

```bash
# Run all tests
pdm run pytest -v

# Run with coverage
pdm run pytest --cov=canvas_python_client --cov-report=html

# Run specific test
pdm run pytest test/test_pagination.py -v
```

### Integration Tests

Integration tests are marked `@pytest.mark.integration` and are skipped unless
`--integration` is passed. They require a Canvas instance and are written against the
seeded dockerized canvas-lms, so `CANVAS_API_TOKEN` must belong to a seeded **observer**
user (one linked to at least one observee with courses and assignments). If either
variable is unset, the integration tests are skipped with a reason naming it.

Some endpoints (account rubrics, account LTI launch definitions, manageable appointment
groups) cannot be read by an observer. Those admin-scoped tests use `CANVAS_ADMIN_API_TOKEN`,
a token for a seeded account admin, with the same `CANVAS_BASE_URL`. When it is unset, only
the admin-scoped tests are skipped (with a reason naming it); the observer tests still run.
Tests that need seeded data the instance does not have are skipped with a reason naming the
missing data.

```bash
# Start the seeded canvas-lms (from the canvas-lms repo)
docker compose up -d

# Run the integration tests as the observer
export CANVAS_BASE_URL="http://canvas.docker"
export CANVAS_API_TOKEN="observer-access-token"
export CANVAS_ADMIN_API_TOKEN="admin-access-token"  # optional
pdm run pytest --integration -m integration
```

## Configuration

### Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `CANVAS_BASE_URL` | Canvas instance URL | Yes | - |
| `CANVAS_API_TOKEN` | Canvas API token | Yes | - |
| `CANVAS_ADMIN_API_TOKEN` | Seeded account admin's API token, for admin-scoped integration tests (skipped when unset) | No | - |

## Development

### File Ownership

**Generated by OpenAPI Generator** (overwritten on regeneration):
- `src/canvas_lms_python_client/api/*.py`
- `src/canvas_lms_python_client/docs/*.py`
- `src/canvas_lms_python_client/models/*.py`
- `src/canvas_lms_python_client/test/*.py`
- `src/canvas_lms_python_client/api_client.py`
- `src/canvas_lms_python_client/api_response.py`
- `src/canvas_lms_python_client/configuration.py`
- `src/canvas_lms_python_client/exceptions.py`
- `src/canvas_lms_python_client/rest.py`

**Custom, never overwritten**:
- `src/canvas_lms_python_client/test/conftest.py`
- `src/canvas_lms_python_client/test/test_pagination.py`
- `src/canvas_lms_python_client/test/test_integration_observees.py`
- `src/canvas_lms_python_client/test/test_paginated_response_types.py`
- `src/canvas_lms_python_client/test/test_integration_paginated_models.py`
- `src/canvas_lms_python_client/test/test_lti_model_payloads.py`
- `src/canvas_lms_python_client/test/test_list_query_params.py`
- `src/canvas_lms_python_client/test/test_api_operation_coverage.py`
- `src/canvas_lms_python_client/test/fixtures/` (captured Canvas responses for offline tests)
- `src/canvas_lms_python_client/pagination.py`
- `src/.openapi-generator-ignore`

## License

MIT License - see [LICENSE](LICENSE) file.

## References

- [Canvas LMS API Documentation](https://canvas.instructure.com/doc/api/index.html)
- [Canvas LMS Repository](https://github.com/instructure/canvas-lms)
- [RFC 8288 (Web Linking)](https://www.rfc-editor.org/rfc/rfc8288)
- [OpenAPI Generator](https://openapi-generator.tech/)

## Troubleshooting

### Import Errors

Ensure you're using Python 3.11+:

```bash
python3 --version  # Should be 3.11 or higher
```

## Contributing

When contributing tests:
1. Follow TDD - write failing test first
2. Watch it fail for the expected reason
3. Implement minimal code to pass
4. Run full test suite: `pdm run pytest`

## Support

For issues related to:
- **Client generation**: Open an issue in this repository
- **Canvas API behavior**: Check [Canvas LMS documentation](https://canvas.instructure.com/doc/api/index.html)
- **Home Assistant integration**: See [Home Assistant Developer Docs](https://developers.home-assistant.io/)
