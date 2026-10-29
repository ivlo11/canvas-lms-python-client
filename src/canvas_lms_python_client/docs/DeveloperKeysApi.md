# canvas_lms_python_client.DeveloperKeysApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**developer_keys_create**](DeveloperKeysApi.md#developer_keys_create) | **POST** /api/v1/accounts/{account_id}/developer_keys | Create a Developer Key
[**developer_keys_destroy**](DeveloperKeysApi.md#developer_keys_destroy) | **DELETE** /api/v1/developer_keys/{id} | Delete a Developer Key
[**developer_keys_index**](DeveloperKeysApi.md#developer_keys_index) | **GET** /api/v1/accounts/{account_id}/developer_keys | List Developer Keys
[**developer_keys_lookup_utids**](DeveloperKeysApi.md#developer_keys_lookup_utids) | **GET** /api/v1/accounts/{account_id}/developer_keys/lookup_utids | Lookup LP API Registrations by Redirect URIs
[**developer_keys_update**](DeveloperKeysApi.md#developer_keys_update) | **PUT** /api/v1/developer_keys/{id} | Update a Developer Key


# **developer_keys_create**
> DeveloperKey developer_keys_create(account_id, developer_keys_create_request=developer_keys_create_request)

Create a Developer Key

Create a new Canvas API key. Creating an LTI 1.3 registration is not supported here and
should be done via the LTI Registration API.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.developer_key import DeveloperKey
from canvas_lms_python_client.models.developer_keys_create_request import DeveloperKeysCreateRequest
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
    api_instance = canvas_lms_python_client.DeveloperKeysApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    developer_keys_create_request = canvas_lms_python_client.DeveloperKeysCreateRequest() # DeveloperKeysCreateRequest | Request body parameters (optional)

    try:
        # Create a Developer Key
        api_response = await api_instance.developer_keys_create(account_id, developer_keys_create_request=developer_keys_create_request)
        print("The response of DeveloperKeysApi->developer_keys_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperKeysApi->developer_keys_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **developer_keys_create_request** | [**DeveloperKeysCreateRequest**](DeveloperKeysCreateRequest.md)| Request body parameters | [optional] 

### Return type

[**DeveloperKey**](DeveloperKey.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | DeveloperKey |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **developer_keys_destroy**
> DeveloperKey developer_keys_destroy(id)

Delete a Developer Key

Delete an existing Canvas API key. Deleting an LTI 1.3 registration should be done via the LTI Registration API.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.developer_key import DeveloperKey
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
    api_instance = canvas_lms_python_client.DeveloperKeysApi(api_client)
    id = 'id_example' # str | Scope response to id

    try:
        # Delete a Developer Key
        api_response = await api_instance.developer_keys_destroy(id)
        print("The response of DeveloperKeysApi->developer_keys_destroy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperKeysApi->developer_keys_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 

### Return type

[**DeveloperKey**](DeveloperKey.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | DeveloperKey |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **developer_keys_index**
> List[DeveloperKey] developer_keys_index(account_id, inherited=inherited, page=page, per_page=per_page)

List Developer Keys

List all developer keys created in the current account.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.developer_key import DeveloperKey
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
    api_instance = canvas_lms_python_client.DeveloperKeysApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    inherited = True # bool | Defaults to false. If true, lists keys inherited from Site Admin (and consortium parent account, if applicable). (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List Developer Keys
        api_response = await api_instance.developer_keys_index(account_id, inherited=inherited, page=page, per_page=per_page)
        print("The response of DeveloperKeysApi->developer_keys_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperKeysApi->developer_keys_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **inherited** | **bool**| Defaults to false. If true, lists keys inherited from Site Admin (and consortium parent account, if applicable). | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[DeveloperKey]**](DeveloperKey.md)

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

# **developer_keys_lookup_utids**
> List[object] developer_keys_lookup_utids(account_id, redirect_uris, sources=sources)

Lookup LP API Registrations by Redirect URIs

Returns a list of matching Unified Tool IDs (UTIDs) from Learn Platform
for the given redirect URIs.

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
    api_instance = canvas_lms_python_client.DeveloperKeysApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    redirect_uris = ['redirect_uris_example'] # List[str] | An array of redirect URI strings to match
    sources = ['sources_example'] # List[str] | An array of sources to look up the redirect URIs from. Possible values are `partner_provided` and `manual` (defaults to both). (optional)

    try:
        # Lookup LP API Registrations by Redirect URIs
        api_response = await api_instance.developer_keys_lookup_utids(account_id, redirect_uris, sources=sources)
        print("The response of DeveloperKeysApi->developer_keys_lookup_utids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperKeysApi->developer_keys_lookup_utids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **redirect_uris** | [**List[str]**](str.md)| An array of redirect URI strings to match | 
 **sources** | [**List[str]**](str.md)| An array of sources to look up the redirect URIs from. Possible values are &#x60;partner_provided&#x60; and &#x60;manual&#x60; (defaults to both). | [optional] 

### Return type

**List[object]**

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

# **developer_keys_update**
> DeveloperKey developer_keys_update(id, developer_keys_create_request=developer_keys_create_request)

Update a Developer Key

Update an existing Canvas API key. Updating an LTI 1.3 registration is not supported here and should
be done via the LTI Registration API.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.developer_key import DeveloperKey
from canvas_lms_python_client.models.developer_keys_create_request import DeveloperKeysCreateRequest
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
    api_instance = canvas_lms_python_client.DeveloperKeysApi(api_client)
    id = 'id_example' # str | Scope response to id
    developer_keys_create_request = canvas_lms_python_client.DeveloperKeysCreateRequest() # DeveloperKeysCreateRequest | Request body parameters (optional)

    try:
        # Update a Developer Key
        api_response = await api_instance.developer_keys_update(id, developer_keys_create_request=developer_keys_create_request)
        print("The response of DeveloperKeysApi->developer_keys_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperKeysApi->developer_keys_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **developer_keys_create_request** | [**DeveloperKeysCreateRequest**](DeveloperKeysCreateRequest.md)| Request body parameters | [optional] 

### Return type

[**DeveloperKey**](DeveloperKey.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | DeveloperKey |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

