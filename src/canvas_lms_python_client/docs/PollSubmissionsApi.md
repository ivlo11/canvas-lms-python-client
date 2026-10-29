# canvas_lms_python_client.PollSubmissionsApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**poll_submissions_create**](PollSubmissionsApi.md#poll_submissions_create) | **POST** /api/v1/polls/{poll_id}/poll_sessions/{poll_session_id}/poll_submissions | Create a single poll submission
[**poll_submissions_show**](PollSubmissionsApi.md#poll_submissions_show) | **GET** /api/v1/polls/{poll_id}/poll_sessions/{poll_session_id}/poll_submissions/{id} | Get a single poll submission


# **poll_submissions_create**
> poll_submissions_create(poll_id, poll_session_id, poll_submissions_create_request=poll_submissions_create_request)

Create a single poll submission

Create a new poll submission for this poll session

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.poll_submissions_create_request import PollSubmissionsCreateRequest
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
    api_instance = canvas_lms_python_client.PollSubmissionsApi(api_client)
    poll_id = 'poll_id_example' # str | Scope response to poll_id
    poll_session_id = 'poll_session_id_example' # str | Scope response to poll_session_id
    poll_submissions_create_request = canvas_lms_python_client.PollSubmissionsCreateRequest() # PollSubmissionsCreateRequest | Request body parameters (optional)

    try:
        # Create a single poll submission
        await api_instance.poll_submissions_create(poll_id, poll_session_id, poll_submissions_create_request=poll_submissions_create_request)
    except Exception as e:
        print("Exception when calling PollSubmissionsApi->poll_submissions_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **poll_id** | **str**| Scope response to poll_id | 
 **poll_session_id** | **str**| Scope response to poll_session_id | 
 **poll_submissions_create_request** | [**PollSubmissionsCreateRequest**](PollSubmissionsCreateRequest.md)| Request body parameters | [optional] 

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
**0** | Create a single poll submission |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **poll_submissions_show**
> poll_submissions_show(id, poll_id, poll_session_id)

Get a single poll submission

Returns the poll submission with the given id

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
    api_instance = canvas_lms_python_client.PollSubmissionsApi(api_client)
    id = 'id_example' # str | Scope response to id
    poll_id = 'poll_id_example' # str | Scope response to poll_id
    poll_session_id = 'poll_session_id_example' # str | Scope response to poll_session_id

    try:
        # Get a single poll submission
        await api_instance.poll_submissions_show(id, poll_id, poll_session_id)
    except Exception as e:
        print("Exception when calling PollSubmissionsApi->poll_submissions_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **poll_id** | **str**| Scope response to poll_id | 
 **poll_session_id** | **str**| Scope response to poll_session_id | 

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
**0** | Get a single poll submission |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

