# canvas_lms_python_client.ModuleAssignmentOverridesApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**module_assignment_overrides_bulk_update**](ModuleAssignmentOverridesApi.md#module_assignment_overrides_bulk_update) | **PUT** /api/v1/courses/{course_id}/modules/{context_module_id}/assignment_overrides | Update a module&#39;s overrides
[**module_assignment_overrides_index**](ModuleAssignmentOverridesApi.md#module_assignment_overrides_index) | **GET** /api/v1/courses/{course_id}/modules/{context_module_id}/assignment_overrides | List a module&#39;s overrides


# **module_assignment_overrides_bulk_update**
> module_assignment_overrides_bulk_update(context_module_id, course_id, module_assignment_overrides_bulk_update_request=module_assignment_overrides_bulk_update_request)

Update a module's overrides

Accepts a list of overrides and applies them to the ContextModule. Returns 204 No Content response
code if successful.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.module_assignment_overrides_bulk_update_request import ModuleAssignmentOverridesBulkUpdateRequest
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
    api_instance = canvas_lms_python_client.ModuleAssignmentOverridesApi(api_client)
    context_module_id = 'context_module_id_example' # str | Scope response to context_module_id
    course_id = 'course_id_example' # str | Scope response to course_id
    module_assignment_overrides_bulk_update_request = canvas_lms_python_client.ModuleAssignmentOverridesBulkUpdateRequest() # ModuleAssignmentOverridesBulkUpdateRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/courses/:course_id/modules/:context_module_id/assignment_overrides \\   -X PUT \\   -H 'Authorization: Bearer <token>' \\   -H 'Content-Type: application/json' \\   -d '{         \"overrides\": [           {             \"id\": 212,             \"course_section_id\": 3564           },           {             \"id\": 56,             \"group_id\": 7809           },           {             \"title\": \"an assignment override\",             \"student_ids\": [1, 2, 3]           }         ]       }' ``` (optional)

    try:
        # Update a module's overrides
        await api_instance.module_assignment_overrides_bulk_update(context_module_id, course_id, module_assignment_overrides_bulk_update_request=module_assignment_overrides_bulk_update_request)
    except Exception as e:
        print("Exception when calling ModuleAssignmentOverridesApi->module_assignment_overrides_bulk_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context_module_id** | **str**| Scope response to context_module_id | 
 **course_id** | **str**| Scope response to course_id | 
 **module_assignment_overrides_bulk_update_request** | [**ModuleAssignmentOverridesBulkUpdateRequest**](ModuleAssignmentOverridesBulkUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/courses/:course_id/modules/:context_module_id/assignment_overrides \\   -X PUT \\   -H &#39;Authorization: Bearer &lt;token&gt;&#39; \\   -H &#39;Content-Type: application/json&#39; \\   -d &#39;{         \&quot;overrides\&quot;: [           {             \&quot;id\&quot;: 212,             \&quot;course_section_id\&quot;: 3564           },           {             \&quot;id\&quot;: 56,             \&quot;group_id\&quot;: 7809           },           {             \&quot;title\&quot;: \&quot;an assignment override\&quot;,             \&quot;student_ids\&quot;: [1, 2, 3]           }         ]       }&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Update a module&#39;s overrides |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **module_assignment_overrides_index**
> List[ModuleAssignmentOverride] module_assignment_overrides_index(context_module_id, course_id, page=page, per_page=per_page)

List a module's overrides

Returns a paginated list of AssignmentOverrides that apply to the ContextModule.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.module_assignment_override import ModuleAssignmentOverride
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
    api_instance = canvas_lms_python_client.ModuleAssignmentOverridesApi(api_client)
    context_module_id = 'context_module_id_example' # str | Scope response to context_module_id
    course_id = 'course_id_example' # str | Scope response to course_id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List a module's overrides
        api_response = await api_instance.module_assignment_overrides_index(context_module_id, course_id, page=page, per_page=per_page)
        print("The response of ModuleAssignmentOverridesApi->module_assignment_overrides_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModuleAssignmentOverridesApi->module_assignment_overrides_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context_module_id** | **str**| Scope response to context_module_id | 
 **course_id** | **str**| Scope response to course_id | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[ModuleAssignmentOverride]**](ModuleAssignmentOverride.md)

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

