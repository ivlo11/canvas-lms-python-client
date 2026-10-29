# canvas_lms_python_client.RubricAssociationsApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rubric_associations_create**](RubricAssociationsApi.md#rubric_associations_create) | **POST** /api/v1/courses/{course_id}/rubric_associations | Create a RubricAssociation
[**rubric_associations_destroy**](RubricAssociationsApi.md#rubric_associations_destroy) | **DELETE** /api/v1/courses/{course_id}/rubric_associations/{id} | Delete a RubricAssociation
[**rubric_associations_update**](RubricAssociationsApi.md#rubric_associations_update) | **PUT** /api/v1/courses/{course_id}/rubric_associations/{id} | Update a RubricAssociation


# **rubric_associations_create**
> RubricAssociation rubric_associations_create(course_id, rubric_associations_create_request=rubric_associations_create_request)

Create a RubricAssociation

Returns the rubric with the given id.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.rubric_association import RubricAssociation
from canvas_lms_python_client.models.rubric_associations_create_request import RubricAssociationsCreateRequest
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
    api_instance = canvas_lms_python_client.RubricAssociationsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    rubric_associations_create_request = canvas_lms_python_client.RubricAssociationsCreateRequest() # RubricAssociationsCreateRequest | Request body parameters (optional)

    try:
        # Create a RubricAssociation
        api_response = await api_instance.rubric_associations_create(course_id, rubric_associations_create_request=rubric_associations_create_request)
        print("The response of RubricAssociationsApi->rubric_associations_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RubricAssociationsApi->rubric_associations_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **rubric_associations_create_request** | [**RubricAssociationsCreateRequest**](RubricAssociationsCreateRequest.md)| Request body parameters | [optional] 

### Return type

[**RubricAssociation**](RubricAssociation.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | RubricAssociation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rubric_associations_destroy**
> RubricAssociation rubric_associations_destroy(course_id, id)

Delete a RubricAssociation

Delete the RubricAssociation with the given ID

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.rubric_association import RubricAssociation
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
    api_instance = canvas_lms_python_client.RubricAssociationsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id

    try:
        # Delete a RubricAssociation
        api_response = await api_instance.rubric_associations_destroy(course_id, id)
        print("The response of RubricAssociationsApi->rubric_associations_destroy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RubricAssociationsApi->rubric_associations_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**RubricAssociation**](RubricAssociation.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | RubricAssociation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rubric_associations_update**
> RubricAssociation rubric_associations_update(course_id, id, rubric_associations_create_request=rubric_associations_create_request)

Update a RubricAssociation

Returns the rubric with the given id.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.rubric_association import RubricAssociation
from canvas_lms_python_client.models.rubric_associations_create_request import RubricAssociationsCreateRequest
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
    api_instance = canvas_lms_python_client.RubricAssociationsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | The id of the RubricAssociation to update
    rubric_associations_create_request = canvas_lms_python_client.RubricAssociationsCreateRequest() # RubricAssociationsCreateRequest | Request body parameters (optional)

    try:
        # Update a RubricAssociation
        api_response = await api_instance.rubric_associations_update(course_id, id, rubric_associations_create_request=rubric_associations_create_request)
        print("The response of RubricAssociationsApi->rubric_associations_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RubricAssociationsApi->rubric_associations_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| The id of the RubricAssociation to update | 
 **rubric_associations_create_request** | [**RubricAssociationsCreateRequest**](RubricAssociationsCreateRequest.md)| Request body parameters | [optional] 

### Return type

[**RubricAssociation**](RubricAssociation.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | RubricAssociation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

