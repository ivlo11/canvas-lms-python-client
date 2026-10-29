# canvas_lms_python_client.QuizzesApiApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quizzes_api_create**](QuizzesApiApi.md#quizzes_api_create) | **POST** /api/v1/courses/{course_id}/quizzes | Create a quiz
[**quizzes_api_destroy**](QuizzesApiApi.md#quizzes_api_destroy) | **DELETE** /api/v1/courses/{course_id}/quizzes/{id} | Delete a quiz
[**quizzes_api_index**](QuizzesApiApi.md#quizzes_api_index) | **GET** /api/v1/courses/{course_id}/quizzes | List quizzes in a course
[**quizzes_api_index_for_courses**](QuizzesApiApi.md#quizzes_api_index_for_courses) | **GET** /api/v1/courses/{course_id}/all_quizzes | List quizzes in a course
[**quizzes_api_reorder**](QuizzesApiApi.md#quizzes_api_reorder) | **POST** /api/v1/courses/{course_id}/quizzes/{id}/reorder | Reorder quiz items
[**quizzes_api_show**](QuizzesApiApi.md#quizzes_api_show) | **GET** /api/v1/courses/{course_id}/quizzes/{id} | Get a single quiz
[**quizzes_api_update**](QuizzesApiApi.md#quizzes_api_update) | **PUT** /api/v1/courses/{course_id}/quizzes/{id} | Edit a quiz
[**quizzes_api_validate_access_code**](QuizzesApiApi.md#quizzes_api_validate_access_code) | **POST** /api/v1/courses/{course_id}/quizzes/{id}/validate_access_code | Validate quiz access code


# **quizzes_api_create**
> Quiz quizzes_api_create(course_id, quizzes_api_create_request=quizzes_api_create_request)

Create a quiz

Create a new quiz for this course.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.quiz import Quiz
from canvas_lms_python_client.models.quizzes_api_create_request import QuizzesApiCreateRequest
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
    api_instance = canvas_lms_python_client.QuizzesApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    quizzes_api_create_request = canvas_lms_python_client.QuizzesApiCreateRequest() # QuizzesApiCreateRequest | Request body parameters (optional)

    try:
        # Create a quiz
        api_response = await api_instance.quizzes_api_create(course_id, quizzes_api_create_request=quizzes_api_create_request)
        print("The response of QuizzesApiApi->quizzes_api_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuizzesApiApi->quizzes_api_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **quizzes_api_create_request** | [**QuizzesApiCreateRequest**](QuizzesApiCreateRequest.md)| Request body parameters | [optional] 

### Return type

[**Quiz**](Quiz.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Quiz |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quizzes_api_destroy**
> Quiz quizzes_api_destroy(course_id, id)

Delete a quiz

Deletes a quiz and returns the deleted quiz object.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.quiz import Quiz
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
    api_instance = canvas_lms_python_client.QuizzesApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id

    try:
        # Delete a quiz
        api_response = await api_instance.quizzes_api_destroy(course_id, id)
        print("The response of QuizzesApiApi->quizzes_api_destroy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuizzesApiApi->quizzes_api_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**Quiz**](Quiz.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Quiz |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quizzes_api_index**
> List[Quiz] quizzes_api_index(course_id, search_term=search_term, page=page, per_page=per_page)

List quizzes in a course

Returns the paginated list of Quizzes in this course.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.quiz import Quiz
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
    api_instance = canvas_lms_python_client.QuizzesApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    search_term = 'search_term_example' # str | The partial title of the quizzes to match and return. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List quizzes in a course
        api_response = await api_instance.quizzes_api_index(course_id, search_term=search_term, page=page, per_page=per_page)
        print("The response of QuizzesApiApi->quizzes_api_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuizzesApiApi->quizzes_api_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **search_term** | **str**| The partial title of the quizzes to match and return. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[Quiz]**](Quiz.md)

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

# **quizzes_api_index_for_courses**
> List[Quiz] quizzes_api_index_for_courses(course_id, search_term=search_term, page=page, per_page=per_page)

List quizzes in a course

Returns the paginated list of Quizzes in this course.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.quiz import Quiz
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
    api_instance = canvas_lms_python_client.QuizzesApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    search_term = 'search_term_example' # str | The partial title of the quizzes to match and return. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List quizzes in a course
        api_response = await api_instance.quizzes_api_index_for_courses(course_id, search_term=search_term, page=page, per_page=per_page)
        print("The response of QuizzesApiApi->quizzes_api_index_for_courses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuizzesApiApi->quizzes_api_index_for_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **search_term** | **str**| The partial title of the quizzes to match and return. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[Quiz]**](Quiz.md)

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

# **quizzes_api_reorder**
> quizzes_api_reorder(course_id, id, quizzes_api_reorder_request=quizzes_api_reorder_request)

Reorder quiz items

Change order of the quiz questions or groups within the quiz

<b>204 No Content</b> response code is returned if the reorder was successful.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.quizzes_api_reorder_request import QuizzesApiReorderRequest
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
    api_instance = canvas_lms_python_client.QuizzesApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    quizzes_api_reorder_request = canvas_lms_python_client.QuizzesApiReorderRequest() # QuizzesApiReorderRequest | Request body parameters (optional)

    try:
        # Reorder quiz items
        await api_instance.quizzes_api_reorder(course_id, id, quizzes_api_reorder_request=quizzes_api_reorder_request)
    except Exception as e:
        print("Exception when calling QuizzesApiApi->quizzes_api_reorder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **quizzes_api_reorder_request** | [**QuizzesApiReorderRequest**](QuizzesApiReorderRequest.md)| Request body parameters | [optional] 

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
**0** | Reorder quiz items |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quizzes_api_show**
> Quiz quizzes_api_show(course_id, id)

Get a single quiz

Returns the quiz with the given id.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.quiz import Quiz
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
    api_instance = canvas_lms_python_client.QuizzesApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id

    try:
        # Get a single quiz
        api_response = await api_instance.quizzes_api_show(course_id, id)
        print("The response of QuizzesApiApi->quizzes_api_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuizzesApiApi->quizzes_api_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**Quiz**](Quiz.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Quiz |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quizzes_api_update**
> Quiz quizzes_api_update(course_id, id, quizzes_api_update_request=quizzes_api_update_request)

Edit a quiz

Modify an existing quiz. See the documentation for quiz creation.

Additional arguments:

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.quiz import Quiz
from canvas_lms_python_client.models.quizzes_api_update_request import QuizzesApiUpdateRequest
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
    api_instance = canvas_lms_python_client.QuizzesApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    quizzes_api_update_request = canvas_lms_python_client.QuizzesApiUpdateRequest() # QuizzesApiUpdateRequest | Request body parameters (optional)

    try:
        # Edit a quiz
        api_response = await api_instance.quizzes_api_update(course_id, id, quizzes_api_update_request=quizzes_api_update_request)
        print("The response of QuizzesApiApi->quizzes_api_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuizzesApiApi->quizzes_api_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **quizzes_api_update_request** | [**QuizzesApiUpdateRequest**](QuizzesApiUpdateRequest.md)| Request body parameters | [optional] 

### Return type

[**Quiz**](Quiz.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Quiz |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quizzes_api_validate_access_code**
> bool quizzes_api_validate_access_code(course_id, id, quizzes_api_validate_access_code_request=quizzes_api_validate_access_code_request)

Validate quiz access code

Accepts an access code and returns a boolean indicating whether that access code is correct

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.quizzes_api_validate_access_code_request import QuizzesApiValidateAccessCodeRequest
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
    api_instance = canvas_lms_python_client.QuizzesApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    quizzes_api_validate_access_code_request = canvas_lms_python_client.QuizzesApiValidateAccessCodeRequest() # QuizzesApiValidateAccessCodeRequest | Request body parameters (optional)

    try:
        # Validate quiz access code
        api_response = await api_instance.quizzes_api_validate_access_code(course_id, id, quizzes_api_validate_access_code_request=quizzes_api_validate_access_code_request)
        print("The response of QuizzesApiApi->quizzes_api_validate_access_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuizzesApiApi->quizzes_api_validate_access_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **quizzes_api_validate_access_code_request** | [**QuizzesApiValidateAccessCodeRequest**](QuizzesApiValidateAccessCodeRequest.md)| Request body parameters | [optional] 

### Return type

**bool**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | boolean |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

