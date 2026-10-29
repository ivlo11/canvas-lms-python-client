# canvas_lms_python_client.RubricsApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rubrics_create**](RubricsApi.md#rubrics_create) | **POST** /api/v1/courses/{course_id}/rubrics | Create a single rubric
[**rubrics_destroy**](RubricsApi.md#rubrics_destroy) | **DELETE** /api/v1/courses/{course_id}/rubrics/{id} | Delete a single
[**rubrics_update**](RubricsApi.md#rubrics_update) | **PUT** /api/v1/courses/{course_id}/rubrics/{id} | Update a single rubric


# **rubrics_create**
> rubrics_create(course_id, rubrics_create_request=rubrics_create_request)

Create a single rubric

Returns the rubric with the given id.

Unfortunately this endpoint does not return a standard Rubric object,
instead it returns a hash that looks like
  { 'rubric': Rubric, 'rubric_association': RubricAssociation }

This may eventually be deprecated in favor of a more standardized return
value, but that is not currently planned.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.rubrics_create_request import RubricsCreateRequest
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
    api_instance = canvas_lms_python_client.RubricsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    rubrics_create_request = canvas_lms_python_client.RubricsCreateRequest() # RubricsCreateRequest | Request body parameters (optional)

    try:
        # Create a single rubric
        await api_instance.rubrics_create(course_id, rubrics_create_request=rubrics_create_request)
    except Exception as e:
        print("Exception when calling RubricsApi->rubrics_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **rubrics_create_request** | [**RubricsCreateRequest**](RubricsCreateRequest.md)| Request body parameters | [optional] 

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
**0** | Create a single rubric |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rubrics_destroy**
> Rubric rubrics_destroy(course_id, id)

Delete a single

Deletes a Rubric and removes all RubricAssociations.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.rubric import Rubric
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
    api_instance = canvas_lms_python_client.RubricsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id

    try:
        # Delete a single
        api_response = await api_instance.rubrics_destroy(course_id, id)
        print("The response of RubricsApi->rubrics_destroy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RubricsApi->rubrics_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**Rubric**](Rubric.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Rubric |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rubrics_update**
> rubrics_update(course_id, id, rubrics_update_request=rubrics_update_request)

Update a single rubric

Returns the rubric with the given id.

Unfortunately this endpoint does not return a standard Rubric object,
instead it returns a hash that looks like
  { 'rubric': Rubric, 'rubric_association': RubricAssociation }

This may eventually be deprecated in favor of a more standardized return
value, but that is not currently planned.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.rubrics_update_request import RubricsUpdateRequest
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
    api_instance = canvas_lms_python_client.RubricsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | The id of the rubric
    rubrics_update_request = canvas_lms_python_client.RubricsUpdateRequest() # RubricsUpdateRequest | Request body parameters (optional)

    try:
        # Update a single rubric
        await api_instance.rubrics_update(course_id, id, rubrics_update_request=rubrics_update_request)
    except Exception as e:
        print("Exception when calling RubricsApi->rubrics_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| The id of the rubric | 
 **rubrics_update_request** | [**RubricsUpdateRequest**](RubricsUpdateRequest.md)| Request body parameters | [optional] 

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
**0** | Update a single rubric |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

