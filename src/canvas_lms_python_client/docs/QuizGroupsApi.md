# canvas_lms_python_client.QuizGroupsApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quiz_groups_create**](QuizGroupsApi.md#quiz_groups_create) | **POST** /api/v1/courses/{course_id}/quizzes/{quiz_id}/groups | Create a question group
[**quiz_groups_destroy**](QuizGroupsApi.md#quiz_groups_destroy) | **DELETE** /api/v1/courses/{course_id}/quizzes/{quiz_id}/groups/{id} | Delete a question group
[**quiz_groups_index**](QuizGroupsApi.md#quiz_groups_index) | **GET** /api/v1/courses/{course_id}/quizzes/{quiz_id}/groups | List question groups in a quiz
[**quiz_groups_reorder**](QuizGroupsApi.md#quiz_groups_reorder) | **POST** /api/v1/courses/{course_id}/quizzes/{quiz_id}/groups/{id}/reorder | Reorder question groups
[**quiz_groups_show**](QuizGroupsApi.md#quiz_groups_show) | **GET** /api/v1/courses/{course_id}/quizzes/{quiz_id}/groups/{id} | Get a single quiz group
[**quiz_groups_update**](QuizGroupsApi.md#quiz_groups_update) | **PUT** /api/v1/courses/{course_id}/quizzes/{quiz_id}/groups/{id} | Update a question group


# **quiz_groups_create**
> quiz_groups_create(course_id, quiz_id, quiz_groups_create_request=quiz_groups_create_request)

Create a question group

Create a new question group for this quiz

<b>201 Created</b> response code is returned if the creation was successful.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.quiz_groups_create_request import QuizGroupsCreateRequest
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
    api_instance = canvas_lms_python_client.QuizGroupsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    quiz_id = 'quiz_id_example' # str | Scope response to quiz_id
    quiz_groups_create_request = canvas_lms_python_client.QuizGroupsCreateRequest() # QuizGroupsCreateRequest | Request body parameters (optional)

    try:
        # Create a question group
        await api_instance.quiz_groups_create(course_id, quiz_id, quiz_groups_create_request=quiz_groups_create_request)
    except Exception as e:
        print("Exception when calling QuizGroupsApi->quiz_groups_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **quiz_id** | **str**| Scope response to quiz_id | 
 **quiz_groups_create_request** | [**QuizGroupsCreateRequest**](QuizGroupsCreateRequest.md)| Request body parameters | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Create a question group |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quiz_groups_destroy**
> quiz_groups_destroy(course_id, id, quiz_id)

Delete a question group

Delete a question group

<b>204 No Content<b> response code is returned if the deletion was successful.

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
    api_instance = canvas_lms_python_client.QuizGroupsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    quiz_id = 'quiz_id_example' # str | Scope response to quiz_id

    try:
        # Delete a question group
        await api_instance.quiz_groups_destroy(course_id, id, quiz_id)
    except Exception as e:
        print("Exception when calling QuizGroupsApi->quiz_groups_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **quiz_id** | **str**| Scope response to quiz_id | 

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
**0** | Delete a question group |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quiz_groups_index**
> quiz_groups_index(course_id, quiz_id)

List question groups in a quiz

Returns a list of question groups in a quiz.

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
    api_instance = canvas_lms_python_client.QuizGroupsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    quiz_id = 'quiz_id_example' # str | Scope response to quiz_id

    try:
        # List question groups in a quiz
        await api_instance.quiz_groups_index(course_id, quiz_id)
    except Exception as e:
        print("Exception when calling QuizGroupsApi->quiz_groups_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **quiz_id** | **str**| Scope response to quiz_id | 

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
**0** | List question groups in a quiz |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quiz_groups_reorder**
> quiz_groups_reorder(course_id, id, quiz_id, quiz_groups_reorder_request=quiz_groups_reorder_request)

Reorder question groups

Change the order of the quiz questions within the group

<b>204 No Content<b> response code is returned if the reorder was successful.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.quiz_groups_reorder_request import QuizGroupsReorderRequest
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
    api_instance = canvas_lms_python_client.QuizGroupsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    quiz_id = 'quiz_id_example' # str | Scope response to quiz_id
    quiz_groups_reorder_request = canvas_lms_python_client.QuizGroupsReorderRequest() # QuizGroupsReorderRequest | Request body parameters (optional)

    try:
        # Reorder question groups
        await api_instance.quiz_groups_reorder(course_id, id, quiz_id, quiz_groups_reorder_request=quiz_groups_reorder_request)
    except Exception as e:
        print("Exception when calling QuizGroupsApi->quiz_groups_reorder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **quiz_id** | **str**| Scope response to quiz_id | 
 **quiz_groups_reorder_request** | [**QuizGroupsReorderRequest**](QuizGroupsReorderRequest.md)| Request body parameters | [optional] 

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
**0** | Reorder question groups |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quiz_groups_show**
> QuizGroup quiz_groups_show(course_id, id, quiz_id)

Get a single quiz group

Returns details of the quiz group with the given id.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.quiz_group import QuizGroup
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
    api_instance = canvas_lms_python_client.QuizGroupsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    quiz_id = 'quiz_id_example' # str | Scope response to quiz_id

    try:
        # Get a single quiz group
        api_response = await api_instance.quiz_groups_show(course_id, id, quiz_id)
        print("The response of QuizGroupsApi->quiz_groups_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuizGroupsApi->quiz_groups_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **quiz_id** | **str**| Scope response to quiz_id | 

### Return type

[**QuizGroup**](QuizGroup.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | QuizGroup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quiz_groups_update**
> quiz_groups_update(course_id, id, quiz_id, quiz_groups_update_request=quiz_groups_update_request)

Update a question group

Update a question group

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.quiz_groups_update_request import QuizGroupsUpdateRequest
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
    api_instance = canvas_lms_python_client.QuizGroupsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    quiz_id = 'quiz_id_example' # str | Scope response to quiz_id
    quiz_groups_update_request = canvas_lms_python_client.QuizGroupsUpdateRequest() # QuizGroupsUpdateRequest | Request body parameters (optional)

    try:
        # Update a question group
        await api_instance.quiz_groups_update(course_id, id, quiz_id, quiz_groups_update_request=quiz_groups_update_request)
    except Exception as e:
        print("Exception when calling QuizGroupsApi->quiz_groups_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **quiz_id** | **str**| Scope response to quiz_id | 
 **quiz_groups_update_request** | [**QuizGroupsUpdateRequest**](QuizGroupsUpdateRequest.md)| Request body parameters | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Update a question group |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

