# canvas_lms_python_client.CourseNicknamesApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**course_nicknames_clear**](CourseNicknamesApi.md#course_nicknames_clear) | **DELETE** /api/v1/users/self/course_nicknames | Clear course nicknames
[**course_nicknames_delete**](CourseNicknamesApi.md#course_nicknames_delete) | **DELETE** /api/v1/users/self/course_nicknames/{course_id} | Remove course nickname
[**course_nicknames_index**](CourseNicknamesApi.md#course_nicknames_index) | **GET** /api/v1/users/self/course_nicknames | List course nicknames
[**course_nicknames_show**](CourseNicknamesApi.md#course_nicknames_show) | **GET** /api/v1/users/self/course_nicknames/{course_id} | Get course nickname
[**course_nicknames_update**](CourseNicknamesApi.md#course_nicknames_update) | **PUT** /api/v1/users/self/course_nicknames/{course_id} | Set course nickname


# **course_nicknames_clear**
> CourseNicknamesClearResponse course_nicknames_clear()

Clear course nicknames

Remove all stored course nicknames.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.course_nicknames_clear_response import CourseNicknamesClearResponse
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
    api_instance = canvas_lms_python_client.CourseNicknamesApi(api_client)

    try:
        # Clear course nicknames
        api_response = await api_instance.course_nicknames_clear()
        print("The response of CourseNicknamesApi->course_nicknames_clear:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseNicknamesApi->course_nicknames_clear: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CourseNicknamesClearResponse**](CourseNicknamesClearResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | CourseNicknamesClearResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **course_nicknames_delete**
> CourseNickname course_nicknames_delete(course_id)

Remove course nickname

Remove the nickname for the given course.
Subsequent course API calls will return the actual name for the course.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.course_nickname import CourseNickname
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
    api_instance = canvas_lms_python_client.CourseNicknamesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id

    try:
        # Remove course nickname
        api_response = await api_instance.course_nicknames_delete(course_id)
        print("The response of CourseNicknamesApi->course_nicknames_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseNicknamesApi->course_nicknames_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 

### Return type

[**CourseNickname**](CourseNickname.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | CourseNickname |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **course_nicknames_index**
> List[CourseNickname] course_nicknames_index(page=page, per_page=per_page)

List course nicknames

Returns all course nicknames you have set.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.course_nickname import CourseNickname
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
    api_instance = canvas_lms_python_client.CourseNicknamesApi(api_client)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List course nicknames
        api_response = await api_instance.course_nicknames_index(page=page, per_page=per_page)
        print("The response of CourseNicknamesApi->course_nicknames_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseNicknamesApi->course_nicknames_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[CourseNickname]**](CourseNickname.md)

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

# **course_nicknames_show**
> CourseNickname course_nicknames_show(course_id)

Get course nickname

Returns the nickname for a specific course.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.course_nickname import CourseNickname
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
    api_instance = canvas_lms_python_client.CourseNicknamesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id

    try:
        # Get course nickname
        api_response = await api_instance.course_nicknames_show(course_id)
        print("The response of CourseNicknamesApi->course_nicknames_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseNicknamesApi->course_nicknames_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 

### Return type

[**CourseNickname**](CourseNickname.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | CourseNickname |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **course_nicknames_update**
> CourseNickname course_nicknames_update(course_id, course_nicknames_update_request=course_nicknames_update_request)

Set course nickname

Set a nickname for the given course. This will replace the course's name
in output of API calls you make subsequently, as well as in selected
places in the Canvas web user interface.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.course_nickname import CourseNickname
from canvas_lms_python_client.models.course_nicknames_update_request import CourseNicknamesUpdateRequest
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
    api_instance = canvas_lms_python_client.CourseNicknamesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    course_nicknames_update_request = canvas_lms_python_client.CourseNicknamesUpdateRequest() # CourseNicknamesUpdateRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/users/self/course_nicknames/<course_id> \\   -X PUT \\   -F 'nickname=Physics' \\   -H 'Authorization: Bearer <token>' ``` (optional)

    try:
        # Set course nickname
        api_response = await api_instance.course_nicknames_update(course_id, course_nicknames_update_request=course_nicknames_update_request)
        print("The response of CourseNicknamesApi->course_nicknames_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseNicknamesApi->course_nicknames_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **course_nicknames_update_request** | [**CourseNicknamesUpdateRequest**](CourseNicknamesUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/users/self/course_nicknames/&lt;course_id&gt; \\   -X PUT \\   -F &#39;nickname&#x3D;Physics&#39; \\   -H &#39;Authorization: Bearer &lt;token&gt;&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**CourseNickname**](CourseNickname.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | CourseNickname |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

