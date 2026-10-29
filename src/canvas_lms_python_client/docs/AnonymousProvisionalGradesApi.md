# canvas_lms_python_client.AnonymousProvisionalGradesApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**anonymous_provisional_grades_status**](AnonymousProvisionalGradesApi.md#anonymous_provisional_grades_status) | **GET** /api/v1/courses/{course_id}/assignments/{assignment_id}/anonymous_provisional_grades/status | Show provisional grade status for a student


# **anonymous_provisional_grades_status**
> anonymous_provisional_grades_status(assignment_id, course_id, anonymous_id=anonymous_id)

Show provisional grade status for a student

Determine whether or not the student's submission needs one or more provisional grades.

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
    api_instance = canvas_lms_python_client.AnonymousProvisionalGradesApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    course_id = 'course_id_example' # str | Scope response to course_id
    anonymous_id = 'anonymous_id_example' # str | The id of the student to show the status for (optional)

    try:
        # Show provisional grade status for a student
        await api_instance.anonymous_provisional_grades_status(assignment_id, course_id, anonymous_id=anonymous_id)
    except Exception as e:
        print("Exception when calling AnonymousProvisionalGradesApi->anonymous_provisional_grades_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **course_id** | **str**| Scope response to course_id | 
 **anonymous_id** | **str**| The id of the student to show the status for | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Show provisional grade status for a student |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

