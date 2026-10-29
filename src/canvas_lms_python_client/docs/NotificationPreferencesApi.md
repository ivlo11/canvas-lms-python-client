# canvas_lms_python_client.NotificationPreferencesApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**notification_preferences_category_index**](NotificationPreferencesApi.md#notification_preferences_category_index) | **GET** /api/v1/users/{user_id}/communication_channels/{communication_channel_id}/notification_preference_categories | List of preference categories
[**notification_preferences_index**](NotificationPreferencesApi.md#notification_preferences_index) | **GET** /api/v1/users/{user_id}/communication_channels/{communication_channel_id}/notification_preferences | List preferences
[**notification_preferences_index_for_users**](NotificationPreferencesApi.md#notification_preferences_index_for_users) | **GET** /api/v1/users/{user_id}/communication_channels/{type}/{address}/notification_preferences | List preferences
[**notification_preferences_show**](NotificationPreferencesApi.md#notification_preferences_show) | **GET** /api/v1/users/{user_id}/communication_channels/{communication_channel_id}/notification_preferences/{notification} | Get a preference
[**notification_preferences_show_for_users**](NotificationPreferencesApi.md#notification_preferences_show_for_users) | **GET** /api/v1/users/{user_id}/communication_channels/{type}/{address}/notification_preferences/{notification} | Get a preference
[**notification_preferences_update**](NotificationPreferencesApi.md#notification_preferences_update) | **PUT** /api/v1/users/self/communication_channels/{communication_channel_id}/notification_preferences/{notification} | Update a preference
[**notification_preferences_update_all**](NotificationPreferencesApi.md#notification_preferences_update_all) | **PUT** /api/v1/users/self/communication_channels/{communication_channel_id}/notification_preferences | Update multiple preferences
[**notification_preferences_update_all_for_self**](NotificationPreferencesApi.md#notification_preferences_update_all_for_self) | **PUT** /api/v1/users/self/communication_channels/{type}/{address}/notification_preferences | Update multiple preferences
[**notification_preferences_update_for_self**](NotificationPreferencesApi.md#notification_preferences_update_for_self) | **PUT** /api/v1/users/self/communication_channels/{type}/{address}/notification_preferences/{notification} | Update a preference
[**notification_preferences_update_preferences_by_category**](NotificationPreferencesApi.md#notification_preferences_update_preferences_by_category) | **PUT** /api/v1/users/self/communication_channels/{communication_channel_id}/notification_preference_categories/{category} | Update preferences by category


# **notification_preferences_category_index**
> notification_preferences_category_index(communication_channel_id, user_id)

List of preference categories

Fetch all notification preference categories for the given communication channel

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
    api_instance = canvas_lms_python_client.NotificationPreferencesApi(api_client)
    communication_channel_id = 'communication_channel_id_example' # str | Scope response to communication_channel_id
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # List of preference categories
        await api_instance.notification_preferences_category_index(communication_channel_id, user_id)
    except Exception as e:
        print("Exception when calling NotificationPreferencesApi->notification_preferences_category_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **communication_channel_id** | **str**| Scope response to communication_channel_id | 
 **user_id** | **str**| Scope response to user_id | 

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
**0** | List of preference categories |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notification_preferences_index**
> List[NotificationPreference] notification_preferences_index(communication_channel_id, user_id)

List preferences

Fetch all preferences for the given communication channel

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.notification_preference import NotificationPreference
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
    api_instance = canvas_lms_python_client.NotificationPreferencesApi(api_client)
    communication_channel_id = 'communication_channel_id_example' # str | Scope response to communication_channel_id
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # List preferences
        api_response = await api_instance.notification_preferences_index(communication_channel_id, user_id)
        print("The response of NotificationPreferencesApi->notification_preferences_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationPreferencesApi->notification_preferences_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **communication_channel_id** | **str**| Scope response to communication_channel_id | 
 **user_id** | **str**| Scope response to user_id | 

### Return type

[**List[NotificationPreference]**](NotificationPreference.md)

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

# **notification_preferences_index_for_users**
> List[NotificationPreference] notification_preferences_index_for_users(address, type, user_id)

List preferences

Fetch all preferences for the given communication channel

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.notification_preference import NotificationPreference
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
    api_instance = canvas_lms_python_client.NotificationPreferencesApi(api_client)
    address = 'address_example' # str | Scope response to address
    type = 'type_example' # str | Scope response to type
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # List preferences
        api_response = await api_instance.notification_preferences_index_for_users(address, type, user_id)
        print("The response of NotificationPreferencesApi->notification_preferences_index_for_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationPreferencesApi->notification_preferences_index_for_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Scope response to address | 
 **type** | **str**| Scope response to type | 
 **user_id** | **str**| Scope response to user_id | 

### Return type

[**List[NotificationPreference]**](NotificationPreference.md)

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

# **notification_preferences_show**
> NotificationPreference notification_preferences_show(communication_channel_id, notification, user_id)

Get a preference

Fetch the preference for the given notification for the given communication channel

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.notification_preference import NotificationPreference
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
    api_instance = canvas_lms_python_client.NotificationPreferencesApi(api_client)
    communication_channel_id = 'communication_channel_id_example' # str | Scope response to communication_channel_id
    notification = 'notification_example' # str | Scope response to notification
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # Get a preference
        api_response = await api_instance.notification_preferences_show(communication_channel_id, notification, user_id)
        print("The response of NotificationPreferencesApi->notification_preferences_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationPreferencesApi->notification_preferences_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **communication_channel_id** | **str**| Scope response to communication_channel_id | 
 **notification** | **str**| Scope response to notification | 
 **user_id** | **str**| Scope response to user_id | 

### Return type

[**NotificationPreference**](NotificationPreference.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | NotificationPreference |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notification_preferences_show_for_users**
> NotificationPreference notification_preferences_show_for_users(address, notification, type, user_id)

Get a preference

Fetch the preference for the given notification for the given communication channel

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.notification_preference import NotificationPreference
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
    api_instance = canvas_lms_python_client.NotificationPreferencesApi(api_client)
    address = 'address_example' # str | Scope response to address
    notification = 'notification_example' # str | Scope response to notification
    type = 'type_example' # str | Scope response to type
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # Get a preference
        api_response = await api_instance.notification_preferences_show_for_users(address, notification, type, user_id)
        print("The response of NotificationPreferencesApi->notification_preferences_show_for_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationPreferencesApi->notification_preferences_show_for_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Scope response to address | 
 **notification** | **str**| Scope response to notification | 
 **type** | **str**| Scope response to type | 
 **user_id** | **str**| Scope response to user_id | 

### Return type

[**NotificationPreference**](NotificationPreference.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | NotificationPreference |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notification_preferences_update**
> notification_preferences_update(communication_channel_id, notification, notification_preferences_update_request=notification_preferences_update_request)

Update a preference

Change the preference for a single notification for a single communication channel

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.notification_preferences_update_request import NotificationPreferencesUpdateRequest
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
    api_instance = canvas_lms_python_client.NotificationPreferencesApi(api_client)
    communication_channel_id = 'communication_channel_id_example' # str | Scope response to communication_channel_id
    notification = 'notification_example' # str | Scope response to notification
    notification_preferences_update_request = canvas_lms_python_client.NotificationPreferencesUpdateRequest() # NotificationPreferencesUpdateRequest | Request body parameters (optional)

    try:
        # Update a preference
        await api_instance.notification_preferences_update(communication_channel_id, notification, notification_preferences_update_request=notification_preferences_update_request)
    except Exception as e:
        print("Exception when calling NotificationPreferencesApi->notification_preferences_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **communication_channel_id** | **str**| Scope response to communication_channel_id | 
 **notification** | **str**| Scope response to notification | 
 **notification_preferences_update_request** | [**NotificationPreferencesUpdateRequest**](NotificationPreferencesUpdateRequest.md)| Request body parameters | [optional] 

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
**0** | Update a preference |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notification_preferences_update_all**
> notification_preferences_update_all(communication_channel_id, notification_preferences_update_all_request=notification_preferences_update_all_request)

Update multiple preferences

Change the preferences for multiple notifications for a single communication channel at once

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.notification_preferences_update_all_request import NotificationPreferencesUpdateAllRequest
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
    api_instance = canvas_lms_python_client.NotificationPreferencesApi(api_client)
    communication_channel_id = 'communication_channel_id_example' # str | Scope response to communication_channel_id
    notification_preferences_update_all_request = canvas_lms_python_client.NotificationPreferencesUpdateAllRequest() # NotificationPreferencesUpdateAllRequest | Request body parameters (optional)

    try:
        # Update multiple preferences
        await api_instance.notification_preferences_update_all(communication_channel_id, notification_preferences_update_all_request=notification_preferences_update_all_request)
    except Exception as e:
        print("Exception when calling NotificationPreferencesApi->notification_preferences_update_all: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **communication_channel_id** | **str**| Scope response to communication_channel_id | 
 **notification_preferences_update_all_request** | [**NotificationPreferencesUpdateAllRequest**](NotificationPreferencesUpdateAllRequest.md)| Request body parameters | [optional] 

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
**0** | Update multiple preferences |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notification_preferences_update_all_for_self**
> notification_preferences_update_all_for_self(address, type, notification_preferences_update_all_request=notification_preferences_update_all_request)

Update multiple preferences

Change the preferences for multiple notifications for a single communication channel at once

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.notification_preferences_update_all_request import NotificationPreferencesUpdateAllRequest
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
    api_instance = canvas_lms_python_client.NotificationPreferencesApi(api_client)
    address = 'address_example' # str | Scope response to address
    type = 'type_example' # str | Scope response to type
    notification_preferences_update_all_request = canvas_lms_python_client.NotificationPreferencesUpdateAllRequest() # NotificationPreferencesUpdateAllRequest | Request body parameters (optional)

    try:
        # Update multiple preferences
        await api_instance.notification_preferences_update_all_for_self(address, type, notification_preferences_update_all_request=notification_preferences_update_all_request)
    except Exception as e:
        print("Exception when calling NotificationPreferencesApi->notification_preferences_update_all_for_self: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Scope response to address | 
 **type** | **str**| Scope response to type | 
 **notification_preferences_update_all_request** | [**NotificationPreferencesUpdateAllRequest**](NotificationPreferencesUpdateAllRequest.md)| Request body parameters | [optional] 

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
**0** | Update multiple preferences |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notification_preferences_update_for_self**
> notification_preferences_update_for_self(address, notification, type, notification_preferences_update_request=notification_preferences_update_request)

Update a preference

Change the preference for a single notification for a single communication channel

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.notification_preferences_update_request import NotificationPreferencesUpdateRequest
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
    api_instance = canvas_lms_python_client.NotificationPreferencesApi(api_client)
    address = 'address_example' # str | Scope response to address
    notification = 'notification_example' # str | Scope response to notification
    type = 'type_example' # str | Scope response to type
    notification_preferences_update_request = canvas_lms_python_client.NotificationPreferencesUpdateRequest() # NotificationPreferencesUpdateRequest | Request body parameters (optional)

    try:
        # Update a preference
        await api_instance.notification_preferences_update_for_self(address, notification, type, notification_preferences_update_request=notification_preferences_update_request)
    except Exception as e:
        print("Exception when calling NotificationPreferencesApi->notification_preferences_update_for_self: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Scope response to address | 
 **notification** | **str**| Scope response to notification | 
 **type** | **str**| Scope response to type | 
 **notification_preferences_update_request** | [**NotificationPreferencesUpdateRequest**](NotificationPreferencesUpdateRequest.md)| Request body parameters | [optional] 

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
**0** | Update a preference |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notification_preferences_update_preferences_by_category**
> notification_preferences_update_preferences_by_category(category, communication_channel_id, notification_preferences_update_preferences_by_category_request=notification_preferences_update_preferences_by_category_request)

Update preferences by category

Change the preferences for multiple notifications based on the category for a single communication channel

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.notification_preferences_update_preferences_by_category_request import NotificationPreferencesUpdatePreferencesByCategoryRequest
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
    api_instance = canvas_lms_python_client.NotificationPreferencesApi(api_client)
    category = 'category_example' # str | The name of the category. Must be parameterized (e.g. The category \"Course Content\" should be \"course_content\")
    communication_channel_id = 'communication_channel_id_example' # str | Scope response to communication_channel_id
    notification_preferences_update_preferences_by_category_request = canvas_lms_python_client.NotificationPreferencesUpdatePreferencesByCategoryRequest() # NotificationPreferencesUpdatePreferencesByCategoryRequest | Request body parameters (optional)

    try:
        # Update preferences by category
        await api_instance.notification_preferences_update_preferences_by_category(category, communication_channel_id, notification_preferences_update_preferences_by_category_request=notification_preferences_update_preferences_by_category_request)
    except Exception as e:
        print("Exception when calling NotificationPreferencesApi->notification_preferences_update_preferences_by_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**| The name of the category. Must be parameterized (e.g. The category \&quot;Course Content\&quot; should be \&quot;course_content\&quot;) | 
 **communication_channel_id** | **str**| Scope response to communication_channel_id | 
 **notification_preferences_update_preferences_by_category_request** | [**NotificationPreferencesUpdatePreferencesByCategoryRequest**](NotificationPreferencesUpdatePreferencesByCategoryRequest.md)| Request body parameters | [optional] 

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
**0** | Update preferences by category |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

