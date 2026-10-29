# canvas_lms_python_client.SubAccountsApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sub_accounts_create**](SubAccountsApi.md#sub_accounts_create) | **POST** /api/v1/accounts/{account_id}/sub_accounts | Create a new sub-account
[**sub_accounts_destroy**](SubAccountsApi.md#sub_accounts_destroy) | **DELETE** /api/v1/accounts/{account_id}/sub_accounts/{id} | Delete a sub-account


# **sub_accounts_create**
> Account sub_accounts_create(account_id, sub_accounts_create_request=sub_accounts_create_request)

Create a new sub-account

Add a new sub-account to a given account.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.account import Account
from canvas_lms_python_client.models.sub_accounts_create_request import SubAccountsCreateRequest
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
    api_instance = canvas_lms_python_client.SubAccountsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    sub_accounts_create_request = canvas_lms_python_client.SubAccountsCreateRequest() # SubAccountsCreateRequest | Request body parameters (optional)

    try:
        # Create a new sub-account
        api_response = await api_instance.sub_accounts_create(account_id, sub_accounts_create_request=sub_accounts_create_request)
        print("The response of SubAccountsApi->sub_accounts_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubAccountsApi->sub_accounts_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **sub_accounts_create_request** | [**SubAccountsCreateRequest**](SubAccountsCreateRequest.md)| Request body parameters | [optional] 

### Return type

[**Account**](Account.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Account |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sub_accounts_destroy**
> Account sub_accounts_destroy(account_id, id)

Delete a sub-account

Cannot delete an account with active courses or active sub_accounts.
Cannot delete a root_account

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.account import Account
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
    api_instance = canvas_lms_python_client.SubAccountsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id

    try:
        # Delete a sub-account
        api_response = await api_instance.sub_accounts_destroy(account_id, id)
        print("The response of SubAccountsApi->sub_accounts_destroy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubAccountsApi->sub_accounts_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**Account**](Account.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Account |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

