# canvas_lms_python_client.ModerationSetApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**moderation_set_create**](ModerationSetApi.md#moderation_set_create) | **POST** /api/v1/courses/{course_id}/assignments/{assignment_id}/moderated_students | Select students for moderation
[**moderation_set_index**](ModerationSetApi.md#moderation_set_index) | **GET** /api/v1/courses/{course_id}/assignments/{assignment_id}/moderated_students | List students selected for moderation


# **moderation_set_create**
> List[User] moderation_set_create(assignment_id, course_id, moderation_set_create_request=moderation_set_create_request)

Select students for moderation

Returns an array of users that were selected for moderation

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.moderation_set_create_request import ModerationSetCreateRequest
from canvas_lms_python_client.models.user import User
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
    api_instance = canvas_lms_python_client.ModerationSetApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    course_id = 'course_id_example' # str | Scope response to course_id
    moderation_set_create_request = canvas_lms_python_client.ModerationSetCreateRequest() # ModerationSetCreateRequest | Request body parameters (optional)

    try:
        # Select students for moderation
        api_response = await api_instance.moderation_set_create(assignment_id, course_id, moderation_set_create_request=moderation_set_create_request)
        print("The response of ModerationSetApi->moderation_set_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModerationSetApi->moderation_set_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **course_id** | **str**| Scope response to course_id | 
 **moderation_set_create_request** | [**ModerationSetCreateRequest**](ModerationSetCreateRequest.md)| Request body parameters | [optional] 

### Return type

[**List[User]**](User.md)

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

# **moderation_set_index**
> List[User] moderation_set_index(assignment_id, course_id, page=page, per_page=per_page)

List students selected for moderation

Returns a paginated list of students selected for moderation

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.user import User
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
    api_instance = canvas_lms_python_client.ModerationSetApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    course_id = 'course_id_example' # str | Scope response to course_id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List students selected for moderation
        api_response = await api_instance.moderation_set_index(assignment_id, course_id, page=page, per_page=per_page)
        print("The response of ModerationSetApi->moderation_set_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModerationSetApi->moderation_set_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **course_id** | **str**| Scope response to course_id | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[User]**](User.md)

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

