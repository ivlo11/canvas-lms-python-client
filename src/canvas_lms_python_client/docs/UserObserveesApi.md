# canvas_lms_python_client.UserObserveesApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_observees_create**](UserObserveesApi.md#user_observees_create) | **POST** /api/v1/users/{user_id}/observees | Add an observee with credentials
[**user_observees_destroy**](UserObserveesApi.md#user_observees_destroy) | **DELETE** /api/v1/users/{user_id}/observees/{observee_id} | Remove an observee
[**user_observees_index**](UserObserveesApi.md#user_observees_index) | **GET** /api/v1/users/{user_id}/observees | List linked observees
[**user_observees_observers**](UserObserveesApi.md#user_observees_observers) | **GET** /api/v1/users/{user_id}/observers | List linked observers
[**user_observees_show**](UserObserveesApi.md#user_observees_show) | **GET** /api/v1/users/{user_id}/observees/{observee_id} | Show an observee
[**user_observees_show_observer**](UserObserveesApi.md#user_observees_show_observer) | **GET** /api/v1/users/{user_id}/observers/{observer_id} | Show an observer
[**user_observees_update**](UserObserveesApi.md#user_observees_update) | **PUT** /api/v1/users/{user_id}/observees/{observee_id} | Add an observee


# **user_observees_create**
> User user_observees_create(user_id, user_observees_create_request=user_observees_create_request)

Add an observee with credentials

Register the given user to observe another user, given the observee's credentials.

*Note:* all users are allowed to add their own observees, given the observee's
credentials or access token are provided. Administrators can add observees given credentials, access token or
the {api:UserObserveesController#update observee's id}.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.user import User
from canvas_lms_python_client.models.user_observees_create_request import UserObserveesCreateRequest
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
    api_instance = canvas_lms_python_client.UserObserveesApi(api_client)
    user_id = 'user_id_example' # str | Scope response to user_id
    user_observees_create_request = canvas_lms_python_client.UserObserveesCreateRequest() # UserObserveesCreateRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/users/<user_id>/observees \\      -X POST \\      -H 'Authorization: Bearer <token>' \\      -F 'observee[unique_id]=UNIQUE_ID' \\      -F 'observee[password]=PASSWORD' ``` (optional)

    try:
        # Add an observee with credentials
        api_response = await api_instance.user_observees_create(user_id, user_observees_create_request=user_observees_create_request)
        print("The response of UserObserveesApi->user_observees_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserObserveesApi->user_observees_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Scope response to user_id | 
 **user_observees_create_request** | [**UserObserveesCreateRequest**](UserObserveesCreateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/users/&lt;user_id&gt;/observees \\      -X POST \\      -H &#39;Authorization: Bearer &lt;token&gt;&#39; \\      -F &#39;observee[unique_id]&#x3D;UNIQUE_ID&#39; \\      -F &#39;observee[password]&#x3D;PASSWORD&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**User**](User.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | User |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_observees_destroy**
> User user_observees_destroy(observee_id, user_id, root_account_id=root_account_id)

Remove an observee

Unregisters a user as being observed by the given user.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.user import User
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
    api_instance = canvas_lms_python_client.UserObserveesApi(api_client)
    observee_id = 'observee_id_example' # str | Scope response to observee_id
    user_id = 'user_id_example' # str | Scope response to user_id
    root_account_id = 56 # int | If specified, only removes the link for the given root account (optional)

    try:
        # Remove an observee
        api_response = await api_instance.user_observees_destroy(observee_id, user_id, root_account_id=root_account_id)
        print("The response of UserObserveesApi->user_observees_destroy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserObserveesApi->user_observees_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **observee_id** | **str**| Scope response to observee_id | 
 **user_id** | **str**| Scope response to user_id | 
 **root_account_id** | **int**| If specified, only removes the link for the given root account | [optional] 

### Return type

[**User**](User.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | User |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_observees_index**
> List[User] user_observees_index(user_id, include=include, page=page, per_page=per_page)

List linked observees

A paginated list of users that the given user is observing. This endpoint returns
users linked to the observer at the account level (such that the observer is automatically
enrolled in observees' courses); it doesn't return one-off observer enrollments from
individual courses.

*Note:* all users are allowed to list their own observees. Administrators can list
other users' observees.

The returned observees will include an attribute "observation_link_root_account_ids", a list
of ids for the root accounts the observer and observee are linked on. The observer will only be able to
observe in courses associated with these root accounts.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.user import User
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
    api_instance = canvas_lms_python_client.UserObserveesApi(api_client)
    user_id = 'user_id_example' # str | Scope response to user_id
    include = ['include_example'] # List[str] | - \"avatar_url\": Optionally include avatar_url. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List linked observees
        api_response = await api_instance.user_observees_index(user_id, include=include, page=page, per_page=per_page)
        print("The response of UserObserveesApi->user_observees_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserObserveesApi->user_observees_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Scope response to user_id | 
 **include** | [**List[str]**](str.md)| - \&quot;avatar_url\&quot;: Optionally include avatar_url. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[User]**](User.md)

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

# **user_observees_observers**
> List[User] user_observees_observers(user_id, include=include, page=page, per_page=per_page)

List linked observers

A paginated list of observers linked to a given user.

*Note:* all users are allowed to list their own observers. Administrators can list
other users' observers.

The returned observers will include an attribute "observation_link_root_account_ids", a list
of ids for the root accounts the observer and observee are linked on. The observer will only be able to
observe in courses associated with these root accounts.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.user import User
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
    api_instance = canvas_lms_python_client.UserObserveesApi(api_client)
    user_id = 'user_id_example' # str | Scope response to user_id
    include = ['include_example'] # List[str] | - \"avatar_url\": Optionally include avatar_url. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List linked observers
        api_response = await api_instance.user_observees_observers(user_id, include=include, page=page, per_page=per_page)
        print("The response of UserObserveesApi->user_observees_observers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserObserveesApi->user_observees_observers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Scope response to user_id | 
 **include** | [**List[str]**](str.md)| - \&quot;avatar_url\&quot;: Optionally include avatar_url. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[User]**](User.md)

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

# **user_observees_show**
> User user_observees_show(observee_id, user_id)

Show an observee

Gets information about an observed user.

*Note:* all users are allowed to view their own observees.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.user import User
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
    api_instance = canvas_lms_python_client.UserObserveesApi(api_client)
    observee_id = 'observee_id_example' # str | Scope response to observee_id
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # Show an observee
        api_response = await api_instance.user_observees_show(observee_id, user_id)
        print("The response of UserObserveesApi->user_observees_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserObserveesApi->user_observees_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **observee_id** | **str**| Scope response to observee_id | 
 **user_id** | **str**| Scope response to user_id | 

### Return type

[**User**](User.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | User |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_observees_show_observer**
> User user_observees_show_observer(observer_id, user_id)

Show an observer

Gets information about an observer.

*Note:* all users are allowed to view their own observers.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.user import User
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
    api_instance = canvas_lms_python_client.UserObserveesApi(api_client)
    observer_id = 'observer_id_example' # str | Scope response to observer_id
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # Show an observer
        api_response = await api_instance.user_observees_show_observer(observer_id, user_id)
        print("The response of UserObserveesApi->user_observees_show_observer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserObserveesApi->user_observees_show_observer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **observer_id** | **str**| Scope response to observer_id | 
 **user_id** | **str**| Scope response to user_id | 

### Return type

[**User**](User.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | User |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_observees_update**
> User user_observees_update(observee_id, user_id, user_observees_update_request=user_observees_update_request)

Add an observee

Registers a user as being observed by the given user.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.user import User
from canvas_lms_python_client.models.user_observees_update_request import UserObserveesUpdateRequest
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
    api_instance = canvas_lms_python_client.UserObserveesApi(api_client)
    observee_id = 'observee_id_example' # str | Scope response to observee_id
    user_id = 'user_id_example' # str | Scope response to user_id
    user_observees_update_request = canvas_lms_python_client.UserObserveesUpdateRequest() # UserObserveesUpdateRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/users/<user_id>/observees/<observee_id> \\      -X PUT \\      -H 'Authorization: Bearer <token>' ``` (optional)

    try:
        # Add an observee
        api_response = await api_instance.user_observees_update(observee_id, user_id, user_observees_update_request=user_observees_update_request)
        print("The response of UserObserveesApi->user_observees_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserObserveesApi->user_observees_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **observee_id** | **str**| Scope response to observee_id | 
 **user_id** | **str**| Scope response to user_id | 
 **user_observees_update_request** | [**UserObserveesUpdateRequest**](UserObserveesUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/users/&lt;user_id&gt;/observees/&lt;observee_id&gt; \\      -X PUT \\      -H &#39;Authorization: Bearer &lt;token&gt;&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**User**](User.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | User |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

