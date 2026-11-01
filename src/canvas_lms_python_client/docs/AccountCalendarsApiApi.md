# canvas_lms_python_client.AccountCalendarsApiApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_calendars_api_all_calendars**](AccountCalendarsApiApi.md#account_calendars_api_all_calendars) | **GET** /api/v1/accounts/{account_id}/account_calendars | List all account calendars
[**account_calendars_api_bulk_update**](AccountCalendarsApiApi.md#account_calendars_api_bulk_update) | **PUT** /api/v1/accounts/{account_id}/account_calendars | Update several calendars
[**account_calendars_api_index**](AccountCalendarsApiApi.md#account_calendars_api_index) | **GET** /api/v1/account_calendars | List available account calendars
[**account_calendars_api_show**](AccountCalendarsApiApi.md#account_calendars_api_show) | **GET** /api/v1/account_calendars/{account_id} | Get a single account calendar
[**account_calendars_api_update**](AccountCalendarsApiApi.md#account_calendars_api_update) | **PUT** /api/v1/account_calendars/{account_id} | Update a calendar
[**account_calendars_api_visible_calendars_count**](AccountCalendarsApiApi.md#account_calendars_api_visible_calendars_count) | **GET** /api/v1/accounts/{account_id}/visible_calendars_count | Count of all visible account calendars


# **account_calendars_api_all_calendars**
> List[AccountCalendar] account_calendars_api_all_calendars(account_id, search_term=search_term, filter=filter, page=page, per_page=per_page)

List all account calendars

Returns a paginated list of account calendars for the provided account and
its first level of sub-accounts. Includes hidden calendars in the response.
Requires the `manage_account_calendar_visibility` permission.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.account_calendar import AccountCalendar
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
    api_instance = canvas_lms_python_client.AccountCalendarsApiApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    search_term = 'search_term_example' # str | When included, searches all descendent accounts of provided account for the term. Returns matching results. Term must be at least 2 characters. Can be combined with a filter value. (optional)
    filter = 'filter_example' # str | When included, only returns calendars that are either visible or hidden. Can be combined with a search term. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List all account calendars
        api_response = await api_instance.account_calendars_api_all_calendars(account_id, search_term=search_term, filter=filter, page=page, per_page=per_page)
        print("The response of AccountCalendarsApiApi->account_calendars_api_all_calendars:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountCalendarsApiApi->account_calendars_api_all_calendars: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **search_term** | **str**| When included, searches all descendent accounts of provided account for the term. Returns matching results. Term must be at least 2 characters. Can be combined with a filter value. | [optional] 
 **filter** | **str**| When included, only returns calendars that are either visible or hidden. Can be combined with a search term. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[AccountCalendar]**](AccountCalendar.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_calendars_api_bulk_update**
> account_calendars_api_bulk_update(account_id)

Update several calendars

Set visibility and/or auto_subscribe on many calendars simultaneously. Requires
the `manage_account_calendar_visibility` permission on the account.

Accepts a JSON array of objects containing 2-3 keys each: `id`
(the account's id, required), `visible` (a boolean indicating whether
the account calendar is visible), and `auto_subscribe` (a boolean indicating
whether users should see these events in their calendar without manually
subscribing).

Returns the count of updated accounts.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
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
    api_instance = canvas_lms_python_client.AccountCalendarsApiApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id

    try:
        # Update several calendars
        await api_instance.account_calendars_api_bulk_update(account_id)
    except Exception as e:
        print("Exception when calling AccountCalendarsApiApi->account_calendars_api_bulk_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Update several calendars |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_calendars_api_index**
> AccountCalendarsApiIndexResponse account_calendars_api_index(search_term=search_term, page=page, per_page=per_page)

List available account calendars

Returns a paginated list of account calendars available to the current user.
Includes visible account calendars where the user has an account association.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.account_calendars_api_index_response import AccountCalendarsApiIndexResponse
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
    api_instance = canvas_lms_python_client.AccountCalendarsApiApi(api_client)
    search_term = 'search_term_example' # str | When included, searches available account calendars for the term. Returns matching results. Term must be at least 2 characters. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List available account calendars
        api_response = await api_instance.account_calendars_api_index(search_term=search_term, page=page, per_page=per_page)
        print("The response of AccountCalendarsApiApi->account_calendars_api_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountCalendarsApiApi->account_calendars_api_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_term** | **str**| When included, searches available account calendars for the term. Returns matching results. Term must be at least 2 characters. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**AccountCalendarsApiIndexResponse**](AccountCalendarsApiIndexResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_calendars_api_show**
> AccountCalendar account_calendars_api_show(account_id)

Get a single account calendar

Get details about a specific account calendar.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.account_calendar import AccountCalendar
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
    api_instance = canvas_lms_python_client.AccountCalendarsApiApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id

    try:
        # Get a single account calendar
        api_response = await api_instance.account_calendars_api_show(account_id)
        print("The response of AccountCalendarsApiApi->account_calendars_api_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountCalendarsApiApi->account_calendars_api_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 

### Return type

[**AccountCalendar**](AccountCalendar.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | AccountCalendar |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_calendars_api_update**
> AccountCalendar account_calendars_api_update(account_id, account_calendars_api_update_request=account_calendars_api_update_request)

Update a calendar

Set an account calendar's visibility and auto_subscribe values. Requires the
`manage_account_calendar_visibility` permission on the account.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.account_calendar import AccountCalendar
from canvas_lms_python_client.models.account_calendars_api_update_request import AccountCalendarsApiUpdateRequest
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
    api_instance = canvas_lms_python_client.AccountCalendarsApiApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    account_calendars_api_update_request = canvas_lms_python_client.AccountCalendarsApiUpdateRequest() # AccountCalendarsApiUpdateRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/account_calendars/204 \\   -X PUT \\   -H 'Authorization: Bearer <token>' \\   -d 'visible=false' \\   -d 'auto_subscribe=false' ``` (optional)

    try:
        # Update a calendar
        api_response = await api_instance.account_calendars_api_update(account_id, account_calendars_api_update_request=account_calendars_api_update_request)
        print("The response of AccountCalendarsApiApi->account_calendars_api_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountCalendarsApiApi->account_calendars_api_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **account_calendars_api_update_request** | [**AccountCalendarsApiUpdateRequest**](AccountCalendarsApiUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/account_calendars/204 \\   -X PUT \\   -H &#39;Authorization: Bearer &lt;token&gt;&#39; \\   -d &#39;visible&#x3D;false&#39; \\   -d &#39;auto_subscribe&#x3D;false&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**AccountCalendar**](AccountCalendar.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | AccountCalendar |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_calendars_api_visible_calendars_count**
> AccountCalendarsApiVisibleCalendarsCountResponse account_calendars_api_visible_calendars_count(account_id)

Count of all visible account calendars

Returns the number of visible account calendars.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.account_calendars_api_visible_calendars_count_response import AccountCalendarsApiVisibleCalendarsCountResponse
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
    api_instance = canvas_lms_python_client.AccountCalendarsApiApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id

    try:
        # Count of all visible account calendars
        api_response = await api_instance.account_calendars_api_visible_calendars_count(account_id)
        print("The response of AccountCalendarsApiApi->account_calendars_api_visible_calendars_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountCalendarsApiApi->account_calendars_api_visible_calendars_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 

### Return type

[**AccountCalendarsApiVisibleCalendarsCountResponse**](AccountCalendarsApiVisibleCalendarsCountResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

