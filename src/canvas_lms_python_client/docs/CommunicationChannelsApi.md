# canvas_lms_python_client.CommunicationChannelsApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**communication_channels_create**](CommunicationChannelsApi.md#communication_channels_create) | **POST** /api/v1/users/{user_id}/communication_channels | Create a communication channel
[**communication_channels_delete_push_token**](CommunicationChannelsApi.md#communication_channels_delete_push_token) | **DELETE** /api/v1/users/self/communication_channels/push | Delete a push notification endpoint
[**communication_channels_destroy**](CommunicationChannelsApi.md#communication_channels_destroy) | **DELETE** /api/v1/users/{user_id}/communication_channels/{id} | Delete a communication channel
[**communication_channels_destroy_for_users**](CommunicationChannelsApi.md#communication_channels_destroy_for_users) | **DELETE** /api/v1/users/{user_id}/communication_channels/{type}/{address} | Delete a communication channel
[**communication_channels_index**](CommunicationChannelsApi.md#communication_channels_index) | **GET** /api/v1/users/{user_id}/communication_channels | List user communication channels


# **communication_channels_create**
> CommunicationChannel communication_channels_create(user_id, communication_channels_create_request=communication_channels_create_request)

Create a communication channel

Creates a new communication channel for the specified user.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.communication_channel import CommunicationChannel
from canvas_lms_python_client.models.communication_channels_create_request import CommunicationChannelsCreateRequest
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
    api_instance = canvas_lms_python_client.CommunicationChannelsApi(api_client)
    user_id = 'user_id_example' # str | Scope response to user_id
    communication_channels_create_request = canvas_lms_python_client.CommunicationChannelsCreateRequest() # CommunicationChannelsCreateRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/users/1/communication_channels \\      -H 'Authorization: Bearer <token>' \\      -d 'communication_channel[address]=new@example.com' \\      -d 'communication_channel[type]=email' \\ ``` (optional)

    try:
        # Create a communication channel
        api_response = await api_instance.communication_channels_create(user_id, communication_channels_create_request=communication_channels_create_request)
        print("The response of CommunicationChannelsApi->communication_channels_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunicationChannelsApi->communication_channels_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Scope response to user_id | 
 **communication_channels_create_request** | [**CommunicationChannelsCreateRequest**](CommunicationChannelsCreateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/users/1/communication_channels \\      -H &#39;Authorization: Bearer &lt;token&gt;&#39; \\      -d &#39;communication_channel[address]&#x3D;new@example.com&#39; \\      -d &#39;communication_channel[type]&#x3D;email&#39; \\ &#x60;&#x60;&#x60; | [optional] 

### Return type

[**CommunicationChannel**](CommunicationChannel.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | CommunicationChannel |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **communication_channels_delete_push_token**
> CommunicationChannelsDeletePushTokenResponse communication_channels_delete_push_token()

Delete a push notification endpoint

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.communication_channels_delete_push_token_response import CommunicationChannelsDeletePushTokenResponse
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
    api_instance = canvas_lms_python_client.CommunicationChannelsApi(api_client)

    try:
        # Delete a push notification endpoint
        api_response = await api_instance.communication_channels_delete_push_token()
        print("The response of CommunicationChannelsApi->communication_channels_delete_push_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunicationChannelsApi->communication_channels_delete_push_token: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CommunicationChannelsDeletePushTokenResponse**](CommunicationChannelsDeletePushTokenResponse.md)

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

# **communication_channels_destroy**
> CommunicationChannel communication_channels_destroy(id, user_id)

Delete a communication channel

Delete an existing communication channel.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.communication_channel import CommunicationChannel
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
    api_instance = canvas_lms_python_client.CommunicationChannelsApi(api_client)
    id = 'id_example' # str | Scope response to id
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # Delete a communication channel
        api_response = await api_instance.communication_channels_destroy(id, user_id)
        print("The response of CommunicationChannelsApi->communication_channels_destroy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunicationChannelsApi->communication_channels_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **user_id** | **str**| Scope response to user_id | 

### Return type

[**CommunicationChannel**](CommunicationChannel.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | CommunicationChannel |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **communication_channels_destroy_for_users**
> CommunicationChannel communication_channels_destroy_for_users(address, type, user_id)

Delete a communication channel

Delete an existing communication channel.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.communication_channel import CommunicationChannel
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
    api_instance = canvas_lms_python_client.CommunicationChannelsApi(api_client)
    address = 'address_example' # str | Scope response to address
    type = 'type_example' # str | Scope response to type
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # Delete a communication channel
        api_response = await api_instance.communication_channels_destroy_for_users(address, type, user_id)
        print("The response of CommunicationChannelsApi->communication_channels_destroy_for_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunicationChannelsApi->communication_channels_destroy_for_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Scope response to address | 
 **type** | **str**| Scope response to type | 
 **user_id** | **str**| Scope response to user_id | 

### Return type

[**CommunicationChannel**](CommunicationChannel.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | CommunicationChannel |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **communication_channels_index**
> List[CommunicationChannel] communication_channels_index(user_id, page=page, per_page=per_page)

List user communication channels

Returns a paginated list of communication channels for the specified user,
sorted by position.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.communication_channel import CommunicationChannel
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
    api_instance = canvas_lms_python_client.CommunicationChannelsApi(api_client)
    user_id = 'user_id_example' # str | Scope response to user_id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List user communication channels
        api_response = await api_instance.communication_channels_index(user_id, page=page, per_page=per_page)
        print("The response of CommunicationChannelsApi->communication_channels_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunicationChannelsApi->communication_channels_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Scope response to user_id | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[CommunicationChannel]**](CommunicationChannel.md)

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

