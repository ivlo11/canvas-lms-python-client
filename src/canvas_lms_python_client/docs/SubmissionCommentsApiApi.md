# canvas_lms_python_client.SubmissionCommentsApiApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**submission_comments_api_create_file**](SubmissionCommentsApiApi.md#submission_comments_api_create_file) | **POST** /api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/comments/files | Upload a file
[**submission_comments_api_destroy**](SubmissionCommentsApiApi.md#submission_comments_api_destroy) | **DELETE** /api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/comments/{id} | Delete a submission comment
[**submission_comments_api_update**](SubmissionCommentsApiApi.md#submission_comments_api_update) | **PUT** /api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/comments/{id} | Edit a submission comment


# **submission_comments_api_create_file**
> submission_comments_api_create_file(assignment_id, course_id, user_id)

Upload a file

Upload a file to attach to a submission comment

See the {file:file.file_uploads.html File Upload Documentation} for details on the file upload workflow.

The final step of the file upload workflow will return the attachment data,
including the new file id. The caller can then PUT the file_id to the
submission API to attach it to a comment

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
    api_instance = canvas_lms_python_client.SubmissionCommentsApiApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    course_id = 'course_id_example' # str | Scope response to course_id
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # Upload a file
        await api_instance.submission_comments_api_create_file(assignment_id, course_id, user_id)
    except Exception as e:
        print("Exception when calling SubmissionCommentsApiApi->submission_comments_api_create_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **course_id** | **str**| Scope response to course_id | 
 **user_id** | **str**| Scope response to user_id | 

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
**0** | Upload a file |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submission_comments_api_destroy**
> SubmissionComment submission_comments_api_destroy(assignment_id, course_id, id, user_id)

Delete a submission comment

Delete the given submission comment.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.submission_comment import SubmissionComment
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
    api_instance = canvas_lms_python_client.SubmissionCommentsApiApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # Delete a submission comment
        api_response = await api_instance.submission_comments_api_destroy(assignment_id, course_id, id, user_id)
        print("The response of SubmissionCommentsApiApi->submission_comments_api_destroy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubmissionCommentsApiApi->submission_comments_api_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **user_id** | **str**| Scope response to user_id | 

### Return type

[**SubmissionComment**](SubmissionComment.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | SubmissionComment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submission_comments_api_update**
> SubmissionComment submission_comments_api_update(assignment_id, course_id, id, user_id, submission_comments_api_update_request=submission_comments_api_update_request)

Edit a submission comment

Edit the given submission comment.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.submission_comment import SubmissionComment
from canvas_lms_python_client.models.submission_comments_api_update_request import SubmissionCommentsApiUpdateRequest
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
    api_instance = canvas_lms_python_client.SubmissionCommentsApiApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    user_id = 'user_id_example' # str | Scope response to user_id
    submission_comments_api_update_request = canvas_lms_python_client.SubmissionCommentsApiUpdateRequest() # SubmissionCommentsApiUpdateRequest | Request body parameters (optional)

    try:
        # Edit a submission comment
        api_response = await api_instance.submission_comments_api_update(assignment_id, course_id, id, user_id, submission_comments_api_update_request=submission_comments_api_update_request)
        print("The response of SubmissionCommentsApiApi->submission_comments_api_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubmissionCommentsApiApi->submission_comments_api_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **user_id** | **str**| Scope response to user_id | 
 **submission_comments_api_update_request** | [**SubmissionCommentsApiUpdateRequest**](SubmissionCommentsApiUpdateRequest.md)| Request body parameters | [optional] 

### Return type

[**SubmissionComment**](SubmissionComment.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | SubmissionComment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

