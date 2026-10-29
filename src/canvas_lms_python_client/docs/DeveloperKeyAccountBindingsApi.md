# canvas_lms_python_client.DeveloperKeyAccountBindingsApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**developer_key_account_bindings_create_or_update**](DeveloperKeyAccountBindingsApi.md#developer_key_account_bindings_create_or_update) | **POST** /api/v1/accounts/{account_id}/developer_keys/{developer_key_id}/developer_key_account_bindings | Create a Developer Key Account Binding


# **developer_key_account_bindings_create_or_update**
> DeveloperKeyAccountBinding developer_key_account_bindings_create_or_update(account_id, developer_key_id, developer_key_account_bindings_create_or_update_request=developer_key_account_bindings_create_or_update_request)

Create a Developer Key Account Binding

Create a new Developer Key Account Binding. The developer key specified
in the request URL must be available in the requested account or the
requested account's account chain. If the binding already exists for the
specified account/key combination it will be updated.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.developer_key_account_binding import DeveloperKeyAccountBinding
from canvas_lms_python_client.models.developer_key_account_bindings_create_or_update_request import DeveloperKeyAccountBindingsCreateOrUpdateRequest
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
    api_instance = canvas_lms_python_client.DeveloperKeyAccountBindingsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    developer_key_id = 'developer_key_id_example' # str | Scope response to developer_key_id
    developer_key_account_bindings_create_or_update_request = canvas_lms_python_client.DeveloperKeyAccountBindingsCreateOrUpdateRequest() # DeveloperKeyAccountBindingsCreateOrUpdateRequest | Request body parameters (optional)

    try:
        # Create a Developer Key Account Binding
        api_response = await api_instance.developer_key_account_bindings_create_or_update(account_id, developer_key_id, developer_key_account_bindings_create_or_update_request=developer_key_account_bindings_create_or_update_request)
        print("The response of DeveloperKeyAccountBindingsApi->developer_key_account_bindings_create_or_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperKeyAccountBindingsApi->developer_key_account_bindings_create_or_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **developer_key_id** | **str**| Scope response to developer_key_id | 
 **developer_key_account_bindings_create_or_update_request** | [**DeveloperKeyAccountBindingsCreateOrUpdateRequest**](DeveloperKeyAccountBindingsCreateOrUpdateRequest.md)| Request body parameters | [optional] 

### Return type

[**DeveloperKeyAccountBinding**](DeveloperKeyAccountBinding.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | DeveloperKeyAccountBinding |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

