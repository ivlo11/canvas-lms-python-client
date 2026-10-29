# canvas_lms_python_client.SisApiApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sis_api_sis_assignments**](SisApiApi.md#sis_api_sis_assignments) | **GET** /api/sis/accounts/{account_id}/assignments | Retrieve assignments enabled for grade export to SIS
[**sis_api_sis_assignments_for_courses**](SisApiApi.md#sis_api_sis_assignments_for_courses) | **GET** /api/sis/courses/{course_id}/assignments | Retrieve assignments enabled for grade export to SIS


# **sis_api_sis_assignments**
> sis_api_sis_assignments(account_id, course_id=course_id, starts_before=starts_before, ends_after=ends_after, include=include)

Retrieve assignments enabled for grade export to SIS

Retrieve a list of published assignments flagged as "post_to_sis".
See the Assignments API for more details on assignments.
Assignment group and section information are included for convenience.

Each section includes course information for the origin course and the
cross-listed course, if applicable. The `origin_course` is the course to
which the section belongs or the course from which the section was
cross-listed. Generally, the `origin_course` should be preferred when
performing integration work. The `xlist_course` is provided for consistency
and is only present when the section has been cross-listed.
See Sections API and Courses Api for me details.

The `override` is only provided if the Differentiated Assignments course
feature is turned on and the assignment has an override for that section.
When there is an override for the assignment the override object's
keys/values can be merged with the top level assignment object to create a
view of the assignment object specific to that section.
See Assignments api for more information on assignment overrides.

restricts to courses that start before this date (if they have a start date)
restricts to courses that end after this date (if they have an end date)
information to include.

  "student_overrides":: returns individual student override information

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
    api_instance = canvas_lms_python_client.SisApiApi(api_client)
    account_id = 'account_id_example' # str | The ID of the account to query.
    course_id = 56 # int | The ID of the course to query. (optional)
    starts_before = 'starts_before_example' # str | When searching on an account, (optional)
    ends_after = 'ends_after_example' # str | When searching on an account, (optional)
    include = 'include_example' # str | Array of additional (optional)

    try:
        # Retrieve assignments enabled for grade export to SIS
        await api_instance.sis_api_sis_assignments(account_id, course_id=course_id, starts_before=starts_before, ends_after=ends_after, include=include)
    except Exception as e:
        print("Exception when calling SisApiApi->sis_api_sis_assignments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The ID of the account to query. | 
 **course_id** | **int**| The ID of the course to query. | [optional] 
 **starts_before** | **str**| When searching on an account, | [optional] 
 **ends_after** | **str**| When searching on an account, | [optional] 
 **include** | **str**| Array of additional | [optional] 

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
**0** | Retrieve assignments enabled for grade export to SIS |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sis_api_sis_assignments_for_courses**
> sis_api_sis_assignments_for_courses(course_id, account_id=account_id, starts_before=starts_before, ends_after=ends_after, include=include)

Retrieve assignments enabled for grade export to SIS

Retrieve a list of published assignments flagged as "post_to_sis".
See the Assignments API for more details on assignments.
Assignment group and section information are included for convenience.

Each section includes course information for the origin course and the
cross-listed course, if applicable. The `origin_course` is the course to
which the section belongs or the course from which the section was
cross-listed. Generally, the `origin_course` should be preferred when
performing integration work. The `xlist_course` is provided for consistency
and is only present when the section has been cross-listed.
See Sections API and Courses Api for me details.

The `override` is only provided if the Differentiated Assignments course
feature is turned on and the assignment has an override for that section.
When there is an override for the assignment the override object's
keys/values can be merged with the top level assignment object to create a
view of the assignment object specific to that section.
See Assignments api for more information on assignment overrides.

restricts to courses that start before this date (if they have a start date)
restricts to courses that end after this date (if they have an end date)
information to include.

  "student_overrides":: returns individual student override information

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
    api_instance = canvas_lms_python_client.SisApiApi(api_client)
    course_id = 'course_id_example' # str | The ID of the course to query.
    account_id = 56 # int | The ID of the account to query. (optional)
    starts_before = 'starts_before_example' # str | When searching on an account, (optional)
    ends_after = 'ends_after_example' # str | When searching on an account, (optional)
    include = 'include_example' # str | Array of additional (optional)

    try:
        # Retrieve assignments enabled for grade export to SIS
        await api_instance.sis_api_sis_assignments_for_courses(course_id, account_id=account_id, starts_before=starts_before, ends_after=ends_after, include=include)
    except Exception as e:
        print("Exception when calling SisApiApi->sis_api_sis_assignments_for_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| The ID of the course to query. | 
 **account_id** | **int**| The ID of the account to query. | [optional] 
 **starts_before** | **str**| When searching on an account, | [optional] 
 **ends_after** | **str**| When searching on an account, | [optional] 
 **include** | **str**| Array of additional | [optional] 

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
**0** | Retrieve assignments enabled for grade export to SIS |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

