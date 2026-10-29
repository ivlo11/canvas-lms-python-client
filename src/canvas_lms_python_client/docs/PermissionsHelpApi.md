# canvas_lms_python_client.PermissionsHelpApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**permissions_help_groups**](PermissionsHelpApi.md#permissions_help_groups) | **GET** /api/v1/permissions/groups | Retrieve permission groups
[**permissions_help_help**](PermissionsHelpApi.md#permissions_help_help) | **GET** /api/v1/permissions/{context_type}/{permission}/help | Get help text for permissions


# **permissions_help_groups**
> permissions_help_groups()

Retrieve permission groups

Retrieve information about groups of granular permissions

The return value is a dictionary of permission group keys to objects
containing +label+ and +subtitle+ keys.

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
    api_instance = canvas_lms_python_client.PermissionsHelpApi(api_client)

    try:
        # Retrieve permission groups
        await api_instance.permissions_help_groups()
    except Exception as e:
        print("Exception when calling PermissionsHelpApi->permissions_help_groups: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**0** | Retrieve permission groups |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permissions_help_help**
> PermissionHelpText permissions_help_help(context_type, permission)

Get help text for permissions

these actions access only static (but localized) information about permissions,
but require a logged-in user to mitigate possible abuse
Retrieve information about what Canvas permissions do and considerations for their use.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.permission_help_text import PermissionHelpText
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
    api_instance = canvas_lms_python_client.PermissionsHelpApi(api_client)
    context_type = 'context_type_example' # str | Scope response to context_type
    permission = 'permission_example' # str | Scope response to permission

    try:
        # Get help text for permissions
        api_response = await api_instance.permissions_help_help(context_type, permission)
        print("The response of PermissionsHelpApi->permissions_help_help:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionsHelpApi->permissions_help_help: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context_type** | **str**| Scope response to context_type | 
 **permission** | **str**| Scope response to permission | 

### Return type

[**PermissionHelpText**](PermissionHelpText.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | PermissionHelpText |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

