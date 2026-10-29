# canvas_lms_python_client.CommMessagesApiApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**comm_messages_api_index**](CommMessagesApiApi.md#comm_messages_api_index) | **GET** /api/v1/comm_messages | List of CommMessages for a user


# **comm_messages_api_index**
> List[CommMessage] comm_messages_api_index(user_id, start_time=start_time, end_time=end_time, page=page, per_page=per_page)

List of CommMessages for a user

Retrieve a paginated list of messages sent to a user.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.comm_message import CommMessage
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
    api_instance = canvas_lms_python_client.CommMessagesApiApi(api_client)
    user_id = 'user_id_example' # str | The user id for whom you want to retrieve CommMessages
    start_time = 'start_time_example' # str | The beginning of the time range you want to retrieve message from. Up to a year prior to the current date is available. (optional)
    end_time = 'end_time_example' # str | The end of the time range you want to retrieve messages for. Up to a year prior to the current date is available. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List of CommMessages for a user
        api_response = await api_instance.comm_messages_api_index(user_id, start_time=start_time, end_time=end_time, page=page, per_page=per_page)
        print("The response of CommMessagesApiApi->comm_messages_api_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommMessagesApiApi->comm_messages_api_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user id for whom you want to retrieve CommMessages | 
 **start_time** | **str**| The beginning of the time range you want to retrieve message from. Up to a year prior to the current date is available. | [optional] 
 **end_time** | **str**| The end of the time range you want to retrieve messages for. Up to a year prior to the current date is available. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[CommMessage]**](CommMessage.md)

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

