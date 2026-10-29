# canvas_lms_python_client.ScopesApiApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**scopes_api_index**](ScopesApiApi.md#scopes_api_index) | **GET** /api/v1/accounts/{account_id}/scopes | List scopes


# **scopes_api_index**
> List[Scope] scopes_api_index(account_id, group_by=group_by)

List scopes

A list of scopes that can be applied to developer keys and access tokens.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.scope import Scope
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
    api_instance = canvas_lms_python_client.ScopesApiApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    group_by = 'group_by_example' # str | The attribute to group the scopes by. By default no grouping is done. (optional)

    try:
        # List scopes
        api_response = await api_instance.scopes_api_index(account_id, group_by=group_by)
        print("The response of ScopesApiApi->scopes_api_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScopesApiApi->scopes_api_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **group_by** | **str**| The attribute to group the scopes by. By default no grouping is done. | [optional] 

### Return type

[**List[Scope]**](Scope.md)

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

