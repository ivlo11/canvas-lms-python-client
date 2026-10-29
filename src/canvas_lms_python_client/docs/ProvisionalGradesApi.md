# canvas_lms_python_client.ProvisionalGradesApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**provisional_grades_bulk_select**](ProvisionalGradesApi.md#provisional_grades_bulk_select) | **PUT** /api/v1/courses/{course_id}/assignments/{assignment_id}/provisional_grades/bulk_select | Bulk select provisional grades
[**provisional_grades_publish**](ProvisionalGradesApi.md#provisional_grades_publish) | **POST** /api/v1/courses/{course_id}/assignments/{assignment_id}/provisional_grades/publish | Publish provisional grades for an assignment
[**provisional_grades_select**](ProvisionalGradesApi.md#provisional_grades_select) | **PUT** /api/v1/courses/{course_id}/assignments/{assignment_id}/provisional_grades/{provisional_grade_id}/select | Select provisional grade
[**provisional_grades_status**](ProvisionalGradesApi.md#provisional_grades_status) | **GET** /api/v1/courses/{course_id}/assignments/{assignment_id}/provisional_grades/status | Show provisional grade status for a student


# **provisional_grades_bulk_select**
> provisional_grades_bulk_select(assignment_id, course_id)

Bulk select provisional grades

Choose which provisional grades will be received by associated students for an assignment.
The caller must be the final grader for the assignment or an admin with :select_final_grade rights.

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
    api_instance = canvas_lms_python_client.ProvisionalGradesApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    course_id = 'course_id_example' # str | Scope response to course_id

    try:
        # Bulk select provisional grades
        await api_instance.provisional_grades_bulk_select(assignment_id, course_id)
    except Exception as e:
        print("Exception when calling ProvisionalGradesApi->provisional_grades_bulk_select: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **course_id** | **str**| Scope response to course_id | 

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
**0** | Bulk select provisional grades |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **provisional_grades_publish**
> provisional_grades_publish(assignment_id, course_id)

Publish provisional grades for an assignment

Publish the selected provisional grade for all submissions to an assignment.
Use the "Select provisional grade" endpoint to choose which provisional grade to publish
for a particular submission.

Students not in the moderation set will have their one and only provisional grade published.

WARNING: This is irreversible. This will overwrite existing grades in the gradebook.

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
    api_instance = canvas_lms_python_client.ProvisionalGradesApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    course_id = 'course_id_example' # str | Scope response to course_id

    try:
        # Publish provisional grades for an assignment
        await api_instance.provisional_grades_publish(assignment_id, course_id)
    except Exception as e:
        print("Exception when calling ProvisionalGradesApi->provisional_grades_publish: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **course_id** | **str**| Scope response to course_id | 

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
**0** | Publish provisional grades for an assignment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **provisional_grades_select**
> provisional_grades_select(assignment_id, course_id, provisional_grade_id)

Select provisional grade

Choose which provisional grade the student should receive for a submission.
The caller must be the final grader for the assignment or an admin with :select_final_grade rights.

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
    api_instance = canvas_lms_python_client.ProvisionalGradesApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    course_id = 'course_id_example' # str | Scope response to course_id
    provisional_grade_id = 'provisional_grade_id_example' # str | Scope response to provisional_grade_id

    try:
        # Select provisional grade
        await api_instance.provisional_grades_select(assignment_id, course_id, provisional_grade_id)
    except Exception as e:
        print("Exception when calling ProvisionalGradesApi->provisional_grades_select: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **course_id** | **str**| Scope response to course_id | 
 **provisional_grade_id** | **str**| Scope response to provisional_grade_id | 

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
**0** | Select provisional grade |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **provisional_grades_status**
> provisional_grades_status(assignment_id, course_id, student_id=student_id)

Show provisional grade status for a student

Tell whether the student's submission needs one or more provisional grades.

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
    api_instance = canvas_lms_python_client.ProvisionalGradesApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    course_id = 'course_id_example' # str | Scope response to course_id
    student_id = 56 # int | The id of the student to show the status for (optional)

    try:
        # Show provisional grade status for a student
        await api_instance.provisional_grades_status(assignment_id, course_id, student_id=student_id)
    except Exception as e:
        print("Exception when calling ProvisionalGradesApi->provisional_grades_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **course_id** | **str**| Scope response to course_id | 
 **student_id** | **int**| The id of the student to show the status for | [optional] 

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

