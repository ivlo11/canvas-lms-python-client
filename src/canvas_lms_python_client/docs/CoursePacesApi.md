# canvas_lms_python_client.CoursePacesApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**course_paces_api_show**](CoursePacesApi.md#course_paces_api_show) | **GET** /api/v1/courses/{course_id}/course_pacing/{id} | Show a Course pace
[**course_paces_create**](CoursePacesApi.md#course_paces_create) | **POST** /api/v1/courses/{course_id}/course_pacing | Create a Course pace
[**course_paces_destroy**](CoursePacesApi.md#course_paces_destroy) | **DELETE** /api/v1/courses/{course_id}/course_pacing/{id} | Delete a Course pace
[**course_paces_update**](CoursePacesApi.md#course_paces_update) | **PUT** /api/v1/courses/{course_id}/course_pacing/{id} | Update a Course pace


# **course_paces_api_show**
> CoursePace course_paces_api_show(course_id, id, course_pace_id)

Show a Course pace

Returns a course pace for the course and pace id provided

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.course_pace import CoursePace
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
    api_instance = canvas_lms_python_client.CoursePacesApi(api_client)
    course_id = 'course_id_example' # str | The id of the course
    id = 'id_example' # str | Scope response to id
    course_pace_id = 56 # int | The id of the course_pace

    try:
        # Show a Course pace
        api_response = await api_instance.course_paces_api_show(course_id, id, course_pace_id)
        print("The response of CoursePacesApi->course_paces_api_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursePacesApi->course_paces_api_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| The id of the course | 
 **id** | **str**| Scope response to id | 
 **course_pace_id** | **int**| The id of the course_pace | 

### Return type

[**CoursePace**](CoursePace.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | CoursePace |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **course_paces_create**
> CoursePace course_paces_create(course_id, course_paces_create_request=course_paces_create_request)

Create a Course pace

Creates a new course pace with specified parameters.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.course_pace import CoursePace
from canvas_lms_python_client.models.course_paces_create_request import CoursePacesCreateRequest
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
    api_instance = canvas_lms_python_client.CoursePacesApi(api_client)
    course_id = 'course_id_example' # str | The id of the course
    course_paces_create_request = canvas_lms_python_client.CoursePacesCreateRequest() # CoursePacesCreateRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/courses/1/course_pacing \\   -X POST \\   -H 'Authorization: Bearer <token>' ``` (optional)

    try:
        # Create a Course pace
        api_response = await api_instance.course_paces_create(course_id, course_paces_create_request=course_paces_create_request)
        print("The response of CoursePacesApi->course_paces_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursePacesApi->course_paces_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| The id of the course | 
 **course_paces_create_request** | [**CoursePacesCreateRequest**](CoursePacesCreateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/courses/1/course_pacing \\   -X POST \\   -H &#39;Authorization: Bearer &lt;token&gt;&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**CoursePace**](CoursePace.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | CoursePace |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **course_paces_destroy**
> CoursePace course_paces_destroy(course_id, id, course_pace_id)

Delete a Course pace

Returns the updated course pace

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.course_pace import CoursePace
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
    api_instance = canvas_lms_python_client.CoursePacesApi(api_client)
    course_id = 'course_id_example' # str | The id of the course
    id = 'id_example' # str | Scope response to id
    course_pace_id = 56 # int | The id of the course_pace

    try:
        # Delete a Course pace
        api_response = await api_instance.course_paces_destroy(course_id, id, course_pace_id)
        print("The response of CoursePacesApi->course_paces_destroy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursePacesApi->course_paces_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| The id of the course | 
 **id** | **str**| Scope response to id | 
 **course_pace_id** | **int**| The id of the course_pace | 

### Return type

[**CoursePace**](CoursePace.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | CoursePace |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **course_paces_update**
> CoursePace course_paces_update(course_id, id, course_paces_update_request=course_paces_update_request)

Update a Course pace

Returns the updated course pace

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.course_pace import CoursePace
from canvas_lms_python_client.models.course_paces_update_request import CoursePacesUpdateRequest
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
    api_instance = canvas_lms_python_client.CoursePacesApi(api_client)
    course_id = 'course_id_example' # str | The id of the course
    id = 'id_example' # str | Scope response to id
    course_paces_update_request = canvas_lms_python_client.CoursePacesUpdateRequest() # CoursePacesUpdateRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/courses/1/course_pacing/1 \\   -X PUT \\   -H 'Authorization: Bearer <token>' ``` (optional)

    try:
        # Update a Course pace
        api_response = await api_instance.course_paces_update(course_id, id, course_paces_update_request=course_paces_update_request)
        print("The response of CoursePacesApi->course_paces_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursePacesApi->course_paces_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| The id of the course | 
 **id** | **str**| Scope response to id | 
 **course_paces_update_request** | [**CoursePacesUpdateRequest**](CoursePacesUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/courses/1/course_pacing/1 \\   -X PUT \\   -H &#39;Authorization: Bearer &lt;token&gt;&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**CoursePace**](CoursePace.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | CoursePace |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

