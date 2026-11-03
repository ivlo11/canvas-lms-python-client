# canvas_lms_python_client.GradeChangeAuditApiApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**grade_change_audit_api_for_assignment**](GradeChangeAuditApiApi.md#grade_change_audit_api_for_assignment) | **GET** /api/v1/audit/grade_change/assignments/{assignment_id} | Query by assignment
[**grade_change_audit_api_for_course**](GradeChangeAuditApiApi.md#grade_change_audit_api_for_course) | **GET** /api/v1/audit/grade_change/courses/{course_id} | Query by course
[**grade_change_audit_api_for_grader**](GradeChangeAuditApiApi.md#grade_change_audit_api_for_grader) | **GET** /api/v1/audit/grade_change/graders/{grader_id} | Query by grader
[**grade_change_audit_api_for_student**](GradeChangeAuditApiApi.md#grade_change_audit_api_for_student) | **GET** /api/v1/audit/grade_change/students/{student_id} | Query by student
[**grade_change_audit_api_query**](GradeChangeAuditApiApi.md#grade_change_audit_api_query) | **GET** /api/v1/audit/grade_change | Advanced query


# **grade_change_audit_api_for_assignment**
> GradeChangeAuditApiForAssignmentResponse grade_change_audit_api_for_assignment(assignment_id, start_time=start_time, end_time=end_time, page=page, per_page=per_page)

Query by assignment

List grade change events for a given assignment.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.grade_change_audit_api_for_assignment_response import GradeChangeAuditApiForAssignmentResponse
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
    api_instance = canvas_lms_python_client.GradeChangeAuditApiApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    start_time = 'start_time_example' # str | The beginning of the time range from which you want events. (optional)
    end_time = 'end_time_example' # str | The end of the time range from which you want events. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # Query by assignment
        api_response = await api_instance.grade_change_audit_api_for_assignment(assignment_id, start_time=start_time, end_time=end_time, page=page, per_page=per_page)
        print("The response of GradeChangeAuditApiApi->grade_change_audit_api_for_assignment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GradeChangeAuditApiApi->grade_change_audit_api_for_assignment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **start_time** | **str**| The beginning of the time range from which you want events. | [optional] 
 **end_time** | **str**| The end of the time range from which you want events. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**GradeChangeAuditApiForAssignmentResponse**](GradeChangeAuditApiForAssignmentResponse.md)

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

# **grade_change_audit_api_for_course**
> GradeChangeAuditApiForCourseResponse grade_change_audit_api_for_course(course_id, start_time=start_time, end_time=end_time, page=page, per_page=per_page)

Query by course

List grade change events for a given course.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.grade_change_audit_api_for_course_response import GradeChangeAuditApiForCourseResponse
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
    api_instance = canvas_lms_python_client.GradeChangeAuditApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    start_time = 'start_time_example' # str | The beginning of the time range from which you want events. (optional)
    end_time = 'end_time_example' # str | The end of the time range from which you want events. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # Query by course
        api_response = await api_instance.grade_change_audit_api_for_course(course_id, start_time=start_time, end_time=end_time, page=page, per_page=per_page)
        print("The response of GradeChangeAuditApiApi->grade_change_audit_api_for_course:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GradeChangeAuditApiApi->grade_change_audit_api_for_course: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **start_time** | **str**| The beginning of the time range from which you want events. | [optional] 
 **end_time** | **str**| The end of the time range from which you want events. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**GradeChangeAuditApiForCourseResponse**](GradeChangeAuditApiForCourseResponse.md)

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

# **grade_change_audit_api_for_grader**
> GradeChangeAuditApiForGraderResponse grade_change_audit_api_for_grader(grader_id, start_time=start_time, end_time=end_time, page=page, per_page=per_page)

Query by grader

List grade change events for a given grader.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.grade_change_audit_api_for_grader_response import GradeChangeAuditApiForGraderResponse
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
    api_instance = canvas_lms_python_client.GradeChangeAuditApiApi(api_client)
    grader_id = 'grader_id_example' # str | Scope response to grader_id
    start_time = 'start_time_example' # str | The beginning of the time range from which you want events. (optional)
    end_time = 'end_time_example' # str | The end of the time range from which you want events. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # Query by grader
        api_response = await api_instance.grade_change_audit_api_for_grader(grader_id, start_time=start_time, end_time=end_time, page=page, per_page=per_page)
        print("The response of GradeChangeAuditApiApi->grade_change_audit_api_for_grader:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GradeChangeAuditApiApi->grade_change_audit_api_for_grader: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grader_id** | **str**| Scope response to grader_id | 
 **start_time** | **str**| The beginning of the time range from which you want events. | [optional] 
 **end_time** | **str**| The end of the time range from which you want events. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**GradeChangeAuditApiForGraderResponse**](GradeChangeAuditApiForGraderResponse.md)

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

# **grade_change_audit_api_for_student**
> GradeChangeAuditApiForStudentResponse grade_change_audit_api_for_student(student_id, start_time=start_time, end_time=end_time, page=page, per_page=per_page)

Query by student

List grade change events for a given student.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.grade_change_audit_api_for_student_response import GradeChangeAuditApiForStudentResponse
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
    api_instance = canvas_lms_python_client.GradeChangeAuditApiApi(api_client)
    student_id = 'student_id_example' # str | Scope response to student_id
    start_time = 'start_time_example' # str | The beginning of the time range from which you want events. (optional)
    end_time = 'end_time_example' # str | The end of the time range from which you want events. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # Query by student
        api_response = await api_instance.grade_change_audit_api_for_student(student_id, start_time=start_time, end_time=end_time, page=page, per_page=per_page)
        print("The response of GradeChangeAuditApiApi->grade_change_audit_api_for_student:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GradeChangeAuditApiApi->grade_change_audit_api_for_student: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **student_id** | **str**| Scope response to student_id | 
 **start_time** | **str**| The beginning of the time range from which you want events. | [optional] 
 **end_time** | **str**| The end of the time range from which you want events. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**GradeChangeAuditApiForStudentResponse**](GradeChangeAuditApiForStudentResponse.md)

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

# **grade_change_audit_api_query**
> GradeChangeAuditApiQueryResponse grade_change_audit_api_query(course_id=course_id, assignment_id=assignment_id, student_id=student_id, grader_id=grader_id, start_time=start_time, end_time=end_time, page=page, per_page=per_page)

Advanced query

List grade change events satisfying all given parameters. Teachers may query for events in courses they teach.
Queries without +course_id+ or +assignment_id+ require account administrator rights.

At least one of +course_id+, +assignment_id+, +student_id+, or +grader_id+ must be specified.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.grade_change_audit_api_query_response import GradeChangeAuditApiQueryResponse
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
    api_instance = canvas_lms_python_client.GradeChangeAuditApiApi(api_client)
    course_id = 56 # int | Restrict query to events in the specified course. (optional)
    assignment_id = 56 # int | Restrict query to the given assignment. If \"override\" is given, query the course final grade override instead. (optional)
    student_id = 56 # int | User id of a student to search grading events for. (optional)
    grader_id = 56 # int | User id of a grader to search grading events for. (optional)
    start_time = 'start_time_example' # str | The beginning of the time range from which you want events. (optional)
    end_time = 'end_time_example' # str | The end of the time range from which you want events. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # Advanced query
        api_response = await api_instance.grade_change_audit_api_query(course_id=course_id, assignment_id=assignment_id, student_id=student_id, grader_id=grader_id, start_time=start_time, end_time=end_time, page=page, per_page=per_page)
        print("The response of GradeChangeAuditApiApi->grade_change_audit_api_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GradeChangeAuditApiApi->grade_change_audit_api_query: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **int**| Restrict query to events in the specified course. | [optional] 
 **assignment_id** | **int**| Restrict query to the given assignment. If \&quot;override\&quot; is given, query the course final grade override instead. | [optional] 
 **student_id** | **int**| User id of a student to search grading events for. | [optional] 
 **grader_id** | **int**| User id of a grader to search grading events for. | [optional] 
 **start_time** | **str**| The beginning of the time range from which you want events. | [optional] 
 **end_time** | **str**| The end of the time range from which you want events. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**GradeChangeAuditApiQueryResponse**](GradeChangeAuditApiQueryResponse.md)

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

