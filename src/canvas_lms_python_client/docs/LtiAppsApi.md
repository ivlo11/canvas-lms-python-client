# canvas_lms_python_client.LtiAppsApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lti_apps_launch_definitions**](LtiAppsApi.md#lti_apps_launch_definitions) | **GET** /api/v1/courses/{course_id}/lti_apps/launch_definitions | List LTI Launch Definitions
[**lti_apps_launch_definitions_for_accounts**](LtiAppsApi.md#lti_apps_launch_definitions_for_accounts) | **GET** /api/v1/accounts/{account_id}/lti_apps/launch_definitions | List LTI Launch Definitions


# **lti_apps_launch_definitions**
> lti_apps_launch_definitions(course_id, placements=placements, only_visible=only_visible, include_context_name=include_context_name, page=page, per_page=per_page)

List LTI Launch Definitions

List all tools available in this context for the given placements, in the form of Launch Definitions.
Used primarily by the Canvas frontend. API users should consider using the External Tools API instead.
This endpoint is cached for 10 minutes!

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
    api_instance = canvas_lms_python_client.LtiAppsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    placements = ['placements_example'] # List[str] | The placements to return launch definitions for. If not provided, an empty list will be returned. (optional)
    only_visible = True # bool | If true, only return launch definitions that are visible to the current user. Defaults to true. (optional)
    include_context_name = True # bool | If true, includes the deployment context name (account or course) of the tool definition in the response. This helps distinguish between tools with identical names deployed at different levels of the context hierarchy. Defaults to false. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List LTI Launch Definitions
        await api_instance.lti_apps_launch_definitions(course_id, placements=placements, only_visible=only_visible, include_context_name=include_context_name, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling LtiAppsApi->lti_apps_launch_definitions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **placements** | [**List[str]**](str.md)| The placements to return launch definitions for. If not provided, an empty list will be returned. | [optional] 
 **only_visible** | **bool**| If true, only return launch definitions that are visible to the current user. Defaults to true. | [optional] 
 **include_context_name** | **bool**| If true, includes the deployment context name (account or course) of the tool definition in the response. This helps distinguish between tools with identical names deployed at different levels of the context hierarchy. Defaults to false. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

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
**0** | List LTI Launch Definitions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lti_apps_launch_definitions_for_accounts**
> lti_apps_launch_definitions_for_accounts(account_id, placements=placements, only_visible=only_visible, include_context_name=include_context_name, page=page, per_page=per_page)

List LTI Launch Definitions

List all tools available in this context for the given placements, in the form of Launch Definitions.
Used primarily by the Canvas frontend. API users should consider using the External Tools API instead.
This endpoint is cached for 10 minutes!

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
    api_instance = canvas_lms_python_client.LtiAppsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    placements = ['placements_example'] # List[str] | The placements to return launch definitions for. If not provided, an empty list will be returned. (optional)
    only_visible = True # bool | If true, only return launch definitions that are visible to the current user. Defaults to true. (optional)
    include_context_name = True # bool | If true, includes the deployment context name (account or course) of the tool definition in the response. This helps distinguish between tools with identical names deployed at different levels of the context hierarchy. Defaults to false. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List LTI Launch Definitions
        await api_instance.lti_apps_launch_definitions_for_accounts(account_id, placements=placements, only_visible=only_visible, include_context_name=include_context_name, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling LtiAppsApi->lti_apps_launch_definitions_for_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **placements** | [**List[str]**](str.md)| The placements to return launch definitions for. If not provided, an empty list will be returned. | [optional] 
 **only_visible** | **bool**| If true, only return launch definitions that are visible to the current user. Defaults to true. | [optional] 
 **include_context_name** | **bool**| If true, includes the deployment context name (account or course) of the tool definition in the response. This helps distinguish between tools with identical names deployed at different levels of the context hierarchy. Defaults to false. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

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
**0** | List LTI Launch Definitions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

