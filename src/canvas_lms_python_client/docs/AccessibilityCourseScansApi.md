# canvas_lms_python_client.AccessibilityCourseScansApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accessibility_course_scans_create**](AccessibilityCourseScansApi.md#accessibility_course_scans_create) | **POST** /api/v1/users/{user_id}/educator_accessibility_course_scan | Trigger accessibility course scan


# **accessibility_course_scans_create**
> Progress accessibility_course_scans_create(user_id)

Trigger accessibility course scan

Queues a background job that scans all a11y-enabled courses where the
user has an active teacher or designer enrollment. Idempotent — if a
scan is already queued or running, the existing Progress is returned.

Requires the educator_dashboard feature flag on the root account and
a11y_checker_account_statistics on site admin.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.progress import Progress
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
    api_instance = canvas_lms_python_client.AccessibilityCourseScansApi(api_client)
    user_id = 'user_id_example' # str | The ID of the user, or \"self\" for the current user. The requesting user may only trigger a scan for themselves.

    try:
        # Trigger accessibility course scan
        api_response = await api_instance.accessibility_course_scans_create(user_id)
        print("The response of AccessibilityCourseScansApi->accessibility_course_scans_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessibilityCourseScansApi->accessibility_course_scans_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the user, or \&quot;self\&quot; for the current user. The requesting user may only trigger a scan for themselves. | 

### Return type

[**Progress**](Progress.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Progress |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

