# canvas_lms_python_client.GradebookHistoryApiApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gradebook_history_api_day_details**](GradebookHistoryApiApi.md#gradebook_history_api_day_details) | **GET** /api/v1/courses/{course_id}/gradebook_history/{date} | Details for a given date in gradebook history for this course
[**gradebook_history_api_days**](GradebookHistoryApiApi.md#gradebook_history_api_days) | **GET** /api/v1/courses/{course_id}/gradebook_history/days | Days in gradebook history for this course
[**gradebook_history_api_feed**](GradebookHistoryApiApi.md#gradebook_history_api_feed) | **GET** /api/v1/courses/{course_id}/gradebook_history/feed | List uncollated submission versions
[**gradebook_history_api_submissions**](GradebookHistoryApiApi.md#gradebook_history_api_submissions) | **GET** /api/v1/courses/{course_id}/gradebook_history/{date}/graders/{grader_id}/assignments/{assignment_id}/submissions | Lists submissions


# **gradebook_history_api_day_details**
> List[Grader] gradebook_history_api_day_details(course_id, var_date)

Details for a given date in gradebook history for this course

Returns the graders who worked on this day, along with the assignments they worked on.
More details can be obtained by selecting a grader and assignment and calling the
'submissions' api endpoint for a given date.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.grader import Grader
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
    api_instance = canvas_lms_python_client.GradebookHistoryApiApi(api_client)
    course_id = 'course_id_example' # str | The id of the contextual course for this API call
    var_date = 'var_date_example' # str | The date for which you would like to see detailed information

    try:
        # Details for a given date in gradebook history for this course
        api_response = await api_instance.gradebook_history_api_day_details(course_id, var_date)
        print("The response of GradebookHistoryApiApi->gradebook_history_api_day_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GradebookHistoryApiApi->gradebook_history_api_day_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| The id of the contextual course for this API call | 
 **var_date** | **str**| The date for which you would like to see detailed information | 

### Return type

[**List[Grader]**](Grader.md)

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

# **gradebook_history_api_days**
> List[Day] gradebook_history_api_days(course_id)

Days in gradebook history for this course

Returns a map of dates to grader/assignment groups

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.day import Day
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
    api_instance = canvas_lms_python_client.GradebookHistoryApiApi(api_client)
    course_id = 'course_id_example' # str | The id of the contextual course for this API call

    try:
        # Days in gradebook history for this course
        api_response = await api_instance.gradebook_history_api_days(course_id)
        print("The response of GradebookHistoryApiApi->gradebook_history_api_days:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GradebookHistoryApiApi->gradebook_history_api_days: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| The id of the contextual course for this API call | 

### Return type

[**List[Day]**](Day.md)

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

# **gradebook_history_api_feed**
> List[SubmissionVersion] gradebook_history_api_feed(course_id, assignment_id=assignment_id, user_id=user_id, ascending=ascending, page=page, per_page=per_page)

List uncollated submission versions

Gives a paginated, uncollated list of submission versions for all matching
submissions in the context. This SubmissionVersion objects will not include
the +new_grade+ or +previous_grade+ keys, only the +grade+; same for
+graded_at+ and +grader+.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.submission_version import SubmissionVersion
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
    api_instance = canvas_lms_python_client.GradebookHistoryApiApi(api_client)
    course_id = 'course_id_example' # str | The id of the contextual course for this API call
    assignment_id = 56 # int | The ID of the assignment for which you want to see submissions. If absent, versions of submissions from any assignment in the course are included. (optional)
    user_id = 56 # int | The ID of the user for which you want to see submissions. If absent, versions of submissions from any user in the course are included. (optional)
    ascending = True # bool | Returns submission versions in ascending date order (oldest first). If absent, returns submission versions in descending date order (newest first). (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List uncollated submission versions
        api_response = await api_instance.gradebook_history_api_feed(course_id, assignment_id=assignment_id, user_id=user_id, ascending=ascending, page=page, per_page=per_page)
        print("The response of GradebookHistoryApiApi->gradebook_history_api_feed:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GradebookHistoryApiApi->gradebook_history_api_feed: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| The id of the contextual course for this API call | 
 **assignment_id** | **int**| The ID of the assignment for which you want to see submissions. If absent, versions of submissions from any assignment in the course are included. | [optional] 
 **user_id** | **int**| The ID of the user for which you want to see submissions. If absent, versions of submissions from any user in the course are included. | [optional] 
 **ascending** | **bool**| Returns submission versions in ascending date order (oldest first). If absent, returns submission versions in descending date order (newest first). | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[SubmissionVersion]**](SubmissionVersion.md)

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

# **gradebook_history_api_submissions**
> List[SubmissionHistory] gradebook_history_api_submissions(assignment_id, course_id, var_date, grader_id)

Lists submissions

Gives a nested list of submission versions

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.submission_history import SubmissionHistory
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
    api_instance = canvas_lms_python_client.GradebookHistoryApiApi(api_client)
    assignment_id = 'assignment_id_example' # str | The ID of the assignment for which you want to see submissions
    course_id = 'course_id_example' # str | The id of the contextual course for this API call
    var_date = 'var_date_example' # str | The date for which you would like to see submissions
    grader_id = 'grader_id_example' # str | The ID of the grader for which you want to see submissions

    try:
        # Lists submissions
        api_response = await api_instance.gradebook_history_api_submissions(assignment_id, course_id, var_date, grader_id)
        print("The response of GradebookHistoryApiApi->gradebook_history_api_submissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GradebookHistoryApiApi->gradebook_history_api_submissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| The ID of the assignment for which you want to see submissions | 
 **course_id** | **str**| The id of the contextual course for this API call | 
 **var_date** | **str**| The date for which you would like to see submissions | 
 **grader_id** | **str**| The ID of the grader for which you want to see submissions | 

### Return type

[**List[SubmissionHistory]**](SubmissionHistory.md)

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

