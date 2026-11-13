# canvas_lms_python_client.AccountNotificationsApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_notifications_create**](AccountNotificationsApi.md#account_notifications_create) | **POST** /api/v1/accounts/{account_id}/account_notifications | Create a global notification
[**account_notifications_show**](AccountNotificationsApi.md#account_notifications_show) | **GET** /api/v1/accounts/{account_id}/account_notifications/{id} | Show a global notification
[**account_notifications_update**](AccountNotificationsApi.md#account_notifications_update) | **PUT** /api/v1/accounts/{account_id}/account_notifications/{id} | Update a global notification
[**account_notifications_user_close_notification**](AccountNotificationsApi.md#account_notifications_user_close_notification) | **DELETE** /api/v1/accounts/{account_id}/account_notifications/{id} | Close notification for user. Destroy notification for admin
[**account_notifications_user_index**](AccountNotificationsApi.md#account_notifications_user_index) | **GET** /api/v1/accounts/{account_id}/account_notifications | Index of active global notification for the user


# **account_notifications_create**
> AccountNotification account_notifications_create(account_id, account_notifications_create_request=account_notifications_create_request)

Create a global notification

Create and return a new global notification for an account.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.account_notification import AccountNotification
from canvas_lms_python_client.models.account_notifications_create_request import AccountNotificationsCreateRequest
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
    api_instance = canvas_lms_python_client.AccountNotificationsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    account_notifications_create_request = canvas_lms_python_client.AccountNotificationsCreateRequest() # AccountNotificationsCreateRequest | Request body parameters  **Example Request:** ``` curl -X POST -H 'Authorization: Bearer <token>' \\ https://<canvas>/api/v1/accounts/2/account_notifications \\ -d 'account_notification[subject]=New notification' \\ -d 'account_notification[start_at]=2014-01-01T00:00:00Z' \\ -d 'account_notification[end_at]=2014-02-01T00:00:00Z' \\ -d 'account_notification[message]=This is a global notification' ``` (optional)

    try:
        # Create a global notification
        api_response = await api_instance.account_notifications_create(account_id, account_notifications_create_request=account_notifications_create_request)
        print("The response of AccountNotificationsApi->account_notifications_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountNotificationsApi->account_notifications_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **account_notifications_create_request** | [**AccountNotificationsCreateRequest**](AccountNotificationsCreateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl -X POST -H &#39;Authorization: Bearer &lt;token&gt;&#39; \\ https://&lt;canvas&gt;/api/v1/accounts/2/account_notifications \\ -d &#39;account_notification[subject]&#x3D;New notification&#39; \\ -d &#39;account_notification[start_at]&#x3D;2014-01-01T00:00:00Z&#39; \\ -d &#39;account_notification[end_at]&#x3D;2014-02-01T00:00:00Z&#39; \\ -d &#39;account_notification[message]&#x3D;This is a global notification&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**AccountNotification**](AccountNotification.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | AccountNotification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_notifications_show**
> AccountNotification account_notifications_show(account_id, id)

Show a global notification

Returns a global notification for the current user
A notification that has been closed by the user will not be returned

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.account_notification import AccountNotification
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
    api_instance = canvas_lms_python_client.AccountNotificationsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id

    try:
        # Show a global notification
        api_response = await api_instance.account_notifications_show(account_id, id)
        print("The response of AccountNotificationsApi->account_notifications_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountNotificationsApi->account_notifications_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**AccountNotification**](AccountNotification.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | AccountNotification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_notifications_update**
> AccountNotification account_notifications_update(account_id, id, account_notifications_update_request=account_notifications_update_request)

Update a global notification

Update global notification for an account.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.account_notification import AccountNotification
from canvas_lms_python_client.models.account_notifications_update_request import AccountNotificationsUpdateRequest
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
    api_instance = canvas_lms_python_client.AccountNotificationsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id
    account_notifications_update_request = canvas_lms_python_client.AccountNotificationsUpdateRequest() # AccountNotificationsUpdateRequest | Request body parameters  **Example Request:** ``` curl -X PUT -H 'Authorization: Bearer <token>' \\ https://<canvas>/api/v1/accounts/2/account_notifications/1 \\ -d 'account_notification[subject]=New notification' \\ -d 'account_notification[start_at]=2014-01-01T00:00:00Z' \\ -d 'account_notification[end_at]=2014-02-01T00:00:00Z' \\ -d 'account_notification[message]=This is a global notification' ``` (optional)

    try:
        # Update a global notification
        api_response = await api_instance.account_notifications_update(account_id, id, account_notifications_update_request=account_notifications_update_request)
        print("The response of AccountNotificationsApi->account_notifications_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountNotificationsApi->account_notifications_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 
 **account_notifications_update_request** | [**AccountNotificationsUpdateRequest**](AccountNotificationsUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl -X PUT -H &#39;Authorization: Bearer &lt;token&gt;&#39; \\ https://&lt;canvas&gt;/api/v1/accounts/2/account_notifications/1 \\ -d &#39;account_notification[subject]&#x3D;New notification&#39; \\ -d &#39;account_notification[start_at]&#x3D;2014-01-01T00:00:00Z&#39; \\ -d &#39;account_notification[end_at]&#x3D;2014-02-01T00:00:00Z&#39; \\ -d &#39;account_notification[message]&#x3D;This is a global notification&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**AccountNotification**](AccountNotification.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | AccountNotification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_notifications_user_close_notification**
> AccountNotification account_notifications_user_close_notification(account_id, id, remove=remove)

Close notification for user. Destroy notification for admin

If the current user no longer wants to see this account notification, it can be closed with this call.
This affects the current user only.

If the current user is an admin and they pass a remove parameter with a value of "true", the account notification
will be destroyed. This affects all users.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.account_notification import AccountNotification
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
    api_instance = canvas_lms_python_client.AccountNotificationsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id
    remove = True # bool | Destroy the account notification. (optional)

    try:
        # Close notification for user. Destroy notification for admin
        api_response = await api_instance.account_notifications_user_close_notification(account_id, id, remove=remove)
        print("The response of AccountNotificationsApi->account_notifications_user_close_notification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountNotificationsApi->account_notifications_user_close_notification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 
 **remove** | **bool**| Destroy the account notification. | [optional] 

### Return type

[**AccountNotification**](AccountNotification.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | AccountNotification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_notifications_user_index**
> List[AccountNotification] account_notifications_user_index(account_id, include_past=include_past, include_all=include_all, show_is_closed=show_is_closed)

Index of active global notification for the user

Returns a list of all global notifications in the account for the current user
Any notifications that have been closed by the user will not be returned, unless
a include_past parameter is passed in as true. Admins can request all global
notifications for the account by passing in an include_all parameter.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.account_notification import AccountNotification
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
    api_instance = canvas_lms_python_client.AccountNotificationsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    include_past = True # bool | Include past and dismissed global announcements. (optional)
    include_all = True # bool | Include all global announcements, regardless of user's role or availability date. Only available to account admins. (optional)
    show_is_closed = True # bool | Include a flag for each notification indicating whether it has been read by the user. (optional)

    try:
        # Index of active global notification for the user
        api_response = await api_instance.account_notifications_user_index(account_id, include_past=include_past, include_all=include_all, show_is_closed=show_is_closed)
        print("The response of AccountNotificationsApi->account_notifications_user_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountNotificationsApi->account_notifications_user_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **include_past** | **bool**| Include past and dismissed global announcements. | [optional] 
 **include_all** | **bool**| Include all global announcements, regardless of user&#39;s role or availability date. Only available to account admins. | [optional] 
 **show_is_closed** | **bool**| Include a flag for each notification indicating whether it has been read by the user. | [optional] 

### Return type

[**List[AccountNotification]**](AccountNotification.md)

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

