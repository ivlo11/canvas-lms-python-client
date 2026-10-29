# canvas_lms_python_client.SubmissionsApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**submissions_create**](SubmissionsApi.md#submissions_create) | **POST** /api/v1/courses/{course_id}/assignments/{assignment_id}/submissions | Submit an assignment
[**submissions_create_for_sections**](SubmissionsApi.md#submissions_create_for_sections) | **POST** /api/v1/sections/{section_id}/assignments/{assignment_id}/submissions | Submit an assignment


# **submissions_create**
> submissions_create(assignment_id, course_id, submissions_create_request=submissions_create_request)

Submit an assignment

Make a submission for an assignment. You must be actively enrolled as a student in
the course/section to do this. Concluded and pending enrollments are not permitted.

All online turn-in submission types are supported in this API. However,
there are a few things that are not yet supported:

* Files can be submitted based on a file ID of a user or group file or through the {api:SubmissionsApiController#create_file file upload API}. However, there is no API yet for listing the user and group files.
* Media comments can be submitted, however, there is no API yet for creating a media comment to submit.
* Integration with Google Docs is not yet supported.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.submissions_create_request import SubmissionsCreateRequest
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
    api_instance = canvas_lms_python_client.SubmissionsApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    course_id = 'course_id_example' # str | Scope response to course_id
    submissions_create_request = canvas_lms_python_client.SubmissionsCreateRequest() # SubmissionsCreateRequest | Request body parameters (optional)

    try:
        # Submit an assignment
        await api_instance.submissions_create(assignment_id, course_id, submissions_create_request=submissions_create_request)
    except Exception as e:
        print("Exception when calling SubmissionsApi->submissions_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **course_id** | **str**| Scope response to course_id | 
 **submissions_create_request** | [**SubmissionsCreateRequest**](SubmissionsCreateRequest.md)| Request body parameters | [optional] 

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
**0** | Submit an assignment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submissions_create_for_sections**
> submissions_create_for_sections(assignment_id, section_id, submissions_create_request=submissions_create_request)

Submit an assignment

Make a submission for an assignment. You must be actively enrolled as a student in
the course/section to do this. Concluded and pending enrollments are not permitted.

All online turn-in submission types are supported in this API. However,
there are a few things that are not yet supported:

* Files can be submitted based on a file ID of a user or group file or through the {api:SubmissionsApiController#create_file file upload API}. However, there is no API yet for listing the user and group files.
* Media comments can be submitted, however, there is no API yet for creating a media comment to submit.
* Integration with Google Docs is not yet supported.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.submissions_create_request import SubmissionsCreateRequest
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
    api_instance = canvas_lms_python_client.SubmissionsApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    section_id = 'section_id_example' # str | Scope response to section_id
    submissions_create_request = canvas_lms_python_client.SubmissionsCreateRequest() # SubmissionsCreateRequest | Request body parameters (optional)

    try:
        # Submit an assignment
        await api_instance.submissions_create_for_sections(assignment_id, section_id, submissions_create_request=submissions_create_request)
    except Exception as e:
        print("Exception when calling SubmissionsApi->submissions_create_for_sections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **section_id** | **str**| Scope response to section_id | 
 **submissions_create_request** | [**SubmissionsCreateRequest**](SubmissionsCreateRequest.md)| Request body parameters | [optional] 

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
**0** | Submit an assignment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

