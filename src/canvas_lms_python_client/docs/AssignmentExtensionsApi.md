# canvas_lms_python_client.AssignmentExtensionsApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assignment_extensions_create**](AssignmentExtensionsApi.md#assignment_extensions_create) | **POST** /api/v1/courses/{course_id}/assignments/{assignment_id}/extensions | Set extensions for student assignment submissions


# **assignment_extensions_create**
> assignment_extensions_create(assignment_id, course_id, assignment_extensions_create_request=assignment_extensions_create_request)

Set extensions for student assignment submissions

<b>Responses</b>

* <b>200 OK</b> if the request was successful
* <b>403 Forbidden</b> if you are not allowed to extend assignments for this course
* <b>400 Bad Request</b> if any of the extensions are invalid

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.assignment_extensions_create_request import AssignmentExtensionsCreateRequest
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
    api_instance = canvas_lms_python_client.AssignmentExtensionsApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    course_id = 'course_id_example' # str | Scope response to course_id
    assignment_extensions_create_request = canvas_lms_python_client.AssignmentExtensionsCreateRequest() # AssignmentExtensionsCreateRequest | Request body parameters  **Example Request:** ``` {   \"assignment_extensions\": [{     \"user_id\": 3,     \"extra_attempts\": 2   },{     \"user_id\": 2,     \"extra_attempts\": 2   }] } ``` (optional)

    try:
        # Set extensions for student assignment submissions
        await api_instance.assignment_extensions_create(assignment_id, course_id, assignment_extensions_create_request=assignment_extensions_create_request)
    except Exception as e:
        print("Exception when calling AssignmentExtensionsApi->assignment_extensions_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **course_id** | **str**| Scope response to course_id | 
 **assignment_extensions_create_request** | [**AssignmentExtensionsCreateRequest**](AssignmentExtensionsCreateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; {   \&quot;assignment_extensions\&quot;: [{     \&quot;user_id\&quot;: 3,     \&quot;extra_attempts\&quot;: 2   },{     \&quot;user_id\&quot;: 2,     \&quot;extra_attempts\&quot;: 2   }] } &#x60;&#x60;&#x60; | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Set extensions for student assignment submissions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

