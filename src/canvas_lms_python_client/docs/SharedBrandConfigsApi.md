# canvas_lms_python_client.SharedBrandConfigsApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**shared_brand_configs_create**](SharedBrandConfigsApi.md#shared_brand_configs_create) | **POST** /api/v1/accounts/{account_id}/shared_brand_configs | Share a BrandConfig (Theme)
[**shared_brand_configs_destroy**](SharedBrandConfigsApi.md#shared_brand_configs_destroy) | **DELETE** /api/v1/shared_brand_configs/{id} | Un-share a BrandConfig (Theme)
[**shared_brand_configs_update**](SharedBrandConfigsApi.md#shared_brand_configs_update) | **PUT** /api/v1/accounts/{account_id}/shared_brand_configs/{id} | Update a shared theme


# **shared_brand_configs_create**
> SharedBrandConfig shared_brand_configs_create(account_id, shared_brand_configs_create_request=shared_brand_configs_create_request)

Share a BrandConfig (Theme)

Create a SharedBrandConfig, which will give the given brand_config a name
and make it available to other users of this account.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.shared_brand_config import SharedBrandConfig
from canvas_lms_python_client.models.shared_brand_configs_create_request import SharedBrandConfigsCreateRequest
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
    api_instance = canvas_lms_python_client.SharedBrandConfigsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    shared_brand_configs_create_request = canvas_lms_python_client.SharedBrandConfigsCreateRequest() # SharedBrandConfigsCreateRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/accounts/<account_id>/shared_brand_configs' \\      -X POST \\      -F 'shared_brand_config[name]=Crimson and Gold Theme' \\      -F 'shared_brand_config[brand_config_md5]=a1f113321fa024e7a14cb0948597a2a4' \\      -H \"Authorization: Bearer <token>\" ``` (optional)

    try:
        # Share a BrandConfig (Theme)
        api_response = await api_instance.shared_brand_configs_create(account_id, shared_brand_configs_create_request=shared_brand_configs_create_request)
        print("The response of SharedBrandConfigsApi->shared_brand_configs_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharedBrandConfigsApi->shared_brand_configs_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **shared_brand_configs_create_request** | [**SharedBrandConfigsCreateRequest**](SharedBrandConfigsCreateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/accounts/&lt;account_id&gt;/shared_brand_configs&#39; \\      -X POST \\      -F &#39;shared_brand_config[name]&#x3D;Crimson and Gold Theme&#39; \\      -F &#39;shared_brand_config[brand_config_md5]&#x3D;a1f113321fa024e7a14cb0948597a2a4&#39; \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**SharedBrandConfig**](SharedBrandConfig.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | SharedBrandConfig |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shared_brand_configs_destroy**
> SharedBrandConfig shared_brand_configs_destroy(id)

Un-share a BrandConfig (Theme)

Delete a SharedBrandConfig, which will unshare it so you nor anyone else in
your account will see it as an option to pick from.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.shared_brand_config import SharedBrandConfig
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
    api_instance = canvas_lms_python_client.SharedBrandConfigsApi(api_client)
    id = 'id_example' # str | Scope response to id

    try:
        # Un-share a BrandConfig (Theme)
        api_response = await api_instance.shared_brand_configs_destroy(id)
        print("The response of SharedBrandConfigsApi->shared_brand_configs_destroy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharedBrandConfigsApi->shared_brand_configs_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 

### Return type

[**SharedBrandConfig**](SharedBrandConfig.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | SharedBrandConfig |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shared_brand_configs_update**
> SharedBrandConfig shared_brand_configs_update(account_id, id)

Update a shared theme

Update the specified shared_brand_config with a new name or to point to a new brand_config.
Uses same parameters as create.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.shared_brand_config import SharedBrandConfig
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
    api_instance = canvas_lms_python_client.SharedBrandConfigsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id

    try:
        # Update a shared theme
        api_response = await api_instance.shared_brand_configs_update(account_id, id)
        print("The response of SharedBrandConfigsApi->shared_brand_configs_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharedBrandConfigsApi->shared_brand_configs_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**SharedBrandConfig**](SharedBrandConfig.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | SharedBrandConfig |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

