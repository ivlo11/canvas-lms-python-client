# canvas_lms_python_client.PollChoicesApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**poll_choices_create**](PollChoicesApi.md#poll_choices_create) | **POST** /api/v1/polls/{poll_id}/poll_choices | Create a single poll choice
[**poll_choices_destroy**](PollChoicesApi.md#poll_choices_destroy) | **DELETE** /api/v1/polls/{poll_id}/poll_choices/{id} | Delete a poll choice
[**poll_choices_index**](PollChoicesApi.md#poll_choices_index) | **GET** /api/v1/polls/{poll_id}/poll_choices | List poll choices in a poll
[**poll_choices_show**](PollChoicesApi.md#poll_choices_show) | **GET** /api/v1/polls/{poll_id}/poll_choices/{id} | Get a single poll choice
[**poll_choices_update**](PollChoicesApi.md#poll_choices_update) | **PUT** /api/v1/polls/{poll_id}/poll_choices/{id} | Update a single poll choice


# **poll_choices_create**
> PollChoicesCreateResponse poll_choices_create(poll_id, poll_choices_create_request=poll_choices_create_request)

Create a single poll choice

Create a new poll choice for this poll

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.poll_choices_create_request import PollChoicesCreateRequest
from canvas_lms_python_client.models.poll_choices_create_response import PollChoicesCreateResponse
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
    api_instance = canvas_lms_python_client.PollChoicesApi(api_client)
    poll_id = 'poll_id_example' # str | Scope response to poll_id
    poll_choices_create_request = canvas_lms_python_client.PollChoicesCreateRequest() # PollChoicesCreateRequest | Request body parameters (optional)

    try:
        # Create a single poll choice
        api_response = await api_instance.poll_choices_create(poll_id, poll_choices_create_request=poll_choices_create_request)
        print("The response of PollChoicesApi->poll_choices_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PollChoicesApi->poll_choices_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **poll_id** | **str**| Scope response to poll_id | 
 **poll_choices_create_request** | [**PollChoicesCreateRequest**](PollChoicesCreateRequest.md)| Request body parameters | [optional] 

### Return type

[**PollChoicesCreateResponse**](PollChoicesCreateResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Create a single poll choice |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **poll_choices_destroy**
> poll_choices_destroy(id, poll_id)

Delete a poll choice

<b>204 No Content</b> response code is returned if the deletion was successful.

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
    api_instance = canvas_lms_python_client.PollChoicesApi(api_client)
    id = 'id_example' # str | Scope response to id
    poll_id = 'poll_id_example' # str | Scope response to poll_id

    try:
        # Delete a poll choice
        await api_instance.poll_choices_destroy(id, poll_id)
    except Exception as e:
        print("Exception when calling PollChoicesApi->poll_choices_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **poll_id** | **str**| Scope response to poll_id | 

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
**0** | Delete a poll choice |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **poll_choices_index**
> PollChoicesIndexResponse poll_choices_index(poll_id, page=page, per_page=per_page)

List poll choices in a poll

Returns the paginated list of PollChoices in this poll.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.poll_choices_index_response import PollChoicesIndexResponse
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
    api_instance = canvas_lms_python_client.PollChoicesApi(api_client)
    poll_id = 'poll_id_example' # str | Scope response to poll_id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List poll choices in a poll
        api_response = await api_instance.poll_choices_index(poll_id, page=page, per_page=per_page)
        print("The response of PollChoicesApi->poll_choices_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PollChoicesApi->poll_choices_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **poll_id** | **str**| Scope response to poll_id | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**PollChoicesIndexResponse**](PollChoicesIndexResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | List poll choices in a poll |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **poll_choices_show**
> PollChoicesShowResponse poll_choices_show(id, poll_id)

Get a single poll choice

Returns the poll choice with the given id

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.poll_choices_show_response import PollChoicesShowResponse
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
    api_instance = canvas_lms_python_client.PollChoicesApi(api_client)
    id = 'id_example' # str | Scope response to id
    poll_id = 'poll_id_example' # str | Scope response to poll_id

    try:
        # Get a single poll choice
        api_response = await api_instance.poll_choices_show(id, poll_id)
        print("The response of PollChoicesApi->poll_choices_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PollChoicesApi->poll_choices_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **poll_id** | **str**| Scope response to poll_id | 

### Return type

[**PollChoicesShowResponse**](PollChoicesShowResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Get a single poll choice |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **poll_choices_update**
> PollChoicesUpdateResponse poll_choices_update(id, poll_id, poll_choices_update_request=poll_choices_update_request)

Update a single poll choice

Update an existing poll choice for this poll

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.poll_choices_update_request import PollChoicesUpdateRequest
from canvas_lms_python_client.models.poll_choices_update_response import PollChoicesUpdateResponse
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
    api_instance = canvas_lms_python_client.PollChoicesApi(api_client)
    id = 'id_example' # str | Scope response to id
    poll_id = 'poll_id_example' # str | Scope response to poll_id
    poll_choices_update_request = canvas_lms_python_client.PollChoicesUpdateRequest() # PollChoicesUpdateRequest | Request body parameters (optional)

    try:
        # Update a single poll choice
        api_response = await api_instance.poll_choices_update(id, poll_id, poll_choices_update_request=poll_choices_update_request)
        print("The response of PollChoicesApi->poll_choices_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PollChoicesApi->poll_choices_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **poll_id** | **str**| Scope response to poll_id | 
 **poll_choices_update_request** | [**PollChoicesUpdateRequest**](PollChoicesUpdateRequest.md)| Request body parameters | [optional] 

### Return type

[**PollChoicesUpdateResponse**](PollChoicesUpdateResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Update a single poll choice |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

