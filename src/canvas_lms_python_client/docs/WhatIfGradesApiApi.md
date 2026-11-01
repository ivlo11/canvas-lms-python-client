# canvas_lms_python_client.WhatIfGradesApiApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**what_if_grades_api_reset_for_student_course**](WhatIfGradesApiApi.md#what_if_grades_api_reset_for_student_course) | **PUT** /api/v1/courses/{course_id}/what_if_grades/reset | Reset the what-if scores for the current user for an entire course and recalculate grades
[**what_if_grades_api_update**](WhatIfGradesApiApi.md#what_if_grades_api_update) | **PUT** /api/v1/submissions/{id}/what_if_grades | Update a submission&#39;s what-if score and calculate grades


# **what_if_grades_api_reset_for_student_course**
> WhatIfGradesApiResetForStudentCourseResponse what_if_grades_api_reset_for_student_course(course_id)

Reset the what-if scores for the current user for an entire course and recalculate grades

Resets all what-if scores for a student in a course and recalculates grades.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.what_if_grades_api_reset_for_student_course_response import WhatIfGradesApiResetForStudentCourseResponse
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
    api_instance = canvas_lms_python_client.WhatIfGradesApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id

    try:
        # Reset the what-if scores for the current user for an entire course and recalculate grades
        api_response = await api_instance.what_if_grades_api_reset_for_student_course(course_id)
        print("The response of WhatIfGradesApiApi->what_if_grades_api_reset_for_student_course:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WhatIfGradesApiApi->what_if_grades_api_reset_for_student_course: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 

### Return type

[**WhatIfGradesApiResetForStudentCourseResponse**](WhatIfGradesApiResetForStudentCourseResponse.md)

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

# **what_if_grades_api_update**
> WhatIfGradesApiUpdateResponse what_if_grades_api_update(id, what_if_grades_api_update_request=what_if_grades_api_update_request)

Update a submission's what-if score and calculate grades

Enter a what if score for a submission and receive the calculated grades
Grade calculation is a costly operation, so this API should be used sparingly

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.what_if_grades_api_update_request import WhatIfGradesApiUpdateRequest
from canvas_lms_python_client.models.what_if_grades_api_update_response import WhatIfGradesApiUpdateResponse
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
    api_instance = canvas_lms_python_client.WhatIfGradesApiApi(api_client)
    id = 'id_example' # str | Scope response to id
    what_if_grades_api_update_request = canvas_lms_python_client.WhatIfGradesApiUpdateRequest() # WhatIfGradesApiUpdateRequest | Request body parameters (optional)

    try:
        # Update a submission's what-if score and calculate grades
        api_response = await api_instance.what_if_grades_api_update(id, what_if_grades_api_update_request=what_if_grades_api_update_request)
        print("The response of WhatIfGradesApiApi->what_if_grades_api_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WhatIfGradesApiApi->what_if_grades_api_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **what_if_grades_api_update_request** | [**WhatIfGradesApiUpdateRequest**](WhatIfGradesApiUpdateRequest.md)| Request body parameters | [optional] 

### Return type

[**WhatIfGradesApiUpdateResponse**](WhatIfGradesApiUpdateResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

