# canvas_lms_python_client.DisablePostToSisApiApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**disable_post_to_sis_api_disable_post_to_sis**](DisablePostToSisApiApi.md#disable_post_to_sis_api_disable_post_to_sis) | **PUT** /api/sis/courses/{course_id}/disable_post_to_sis | Disable assignments currently enabled for grade export to SIS


# **disable_post_to_sis_api_disable_post_to_sis**
> disable_post_to_sis_api_disable_post_to_sis(course_id, disable_post_to_sis_api_disable_post_to_sis_request=disable_post_to_sis_api_disable_post_to_sis_request)

Disable assignments currently enabled for grade export to SIS

Disable all assignments flagged as "post_to_sis", with the option of making it
specific to a grading period, in a course.

On success, the response will be 204 No Content with an empty body.

On failure, the response will be 400 Bad Request with a body of a specific
message.

For disabling assignments in a specific grading period

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.disable_post_to_sis_api_disable_post_to_sis_request import DisablePostToSisApiDisablePostToSisRequest
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
    api_instance = canvas_lms_python_client.DisablePostToSisApiApi(api_client)
    course_id = 'course_id_example' # str | The ID of the course.
    disable_post_to_sis_api_disable_post_to_sis_request = canvas_lms_python_client.DisablePostToSisApiDisablePostToSisRequest() # DisablePostToSisApiDisablePostToSisRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/sis/courses/<course_id>/disable_post_to_sis' \\      -X PUT \\      -H \"Authorization: Bearer <token>\" \\      -H \"Content-Length: 0\" ``` (optional)

    try:
        # Disable assignments currently enabled for grade export to SIS
        await api_instance.disable_post_to_sis_api_disable_post_to_sis(course_id, disable_post_to_sis_api_disable_post_to_sis_request=disable_post_to_sis_api_disable_post_to_sis_request)
    except Exception as e:
        print("Exception when calling DisablePostToSisApiApi->disable_post_to_sis_api_disable_post_to_sis: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| The ID of the course. | 
 **disable_post_to_sis_api_disable_post_to_sis_request** | [**DisablePostToSisApiDisablePostToSisRequest**](DisablePostToSisApiDisablePostToSisRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/sis/courses/&lt;course_id&gt;/disable_post_to_sis&#39; \\      -X PUT \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; \\      -H \&quot;Content-Length: 0\&quot; &#x60;&#x60;&#x60; | [optional] 

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
**0** | Disable assignments currently enabled for grade export to SIS |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

