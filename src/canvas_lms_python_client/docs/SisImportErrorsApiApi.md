# canvas_lms_python_client.SisImportErrorsApiApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sis_import_errors_api_index**](SisImportErrorsApiApi.md#sis_import_errors_api_index) | **GET** /api/v1/accounts/{account_id}/sis_imports/{id}/errors | Get SIS import error list
[**sis_import_errors_api_index_for_accounts**](SisImportErrorsApiApi.md#sis_import_errors_api_index_for_accounts) | **GET** /api/v1/accounts/{account_id}/sis_import_errors | Get SIS import error list


# **sis_import_errors_api_index**
> List[SisImportError] sis_import_errors_api_index(account_id, id, failure=failure, page=page, per_page=per_page)

Get SIS import error list

Returns the list of SIS import errors for an account or a SIS import. Import
errors are only stored for 30 days.

Example:
  curl 'https://<canvas>/api/v1/accounts/<account_id>/sis_imports/<id>/sis_import_errors' \
    -H "Authorization: Bearer <token>"

Example:
  curl 'https://<canvas>/api/v1/accounts/<account_id>/sis_import_errors' \
    -H "Authorization: Bearer <token>"

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.sis_import_error import SisImportError
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
    api_instance = canvas_lms_python_client.SisImportErrorsApiApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id
    failure = True # bool | If set, only shows errors on a sis import that would cause a failure. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # Get SIS import error list
        api_response = await api_instance.sis_import_errors_api_index(account_id, id, failure=failure, page=page, per_page=per_page)
        print("The response of SisImportErrorsApiApi->sis_import_errors_api_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SisImportErrorsApiApi->sis_import_errors_api_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 
 **failure** | **bool**| If set, only shows errors on a sis import that would cause a failure. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[SisImportError]**](SisImportError.md)

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

# **sis_import_errors_api_index_for_accounts**
> List[SisImportError] sis_import_errors_api_index_for_accounts(account_id, failure=failure, page=page, per_page=per_page)

Get SIS import error list

Returns the list of SIS import errors for an account or a SIS import. Import
errors are only stored for 30 days.

Example:
  curl 'https://<canvas>/api/v1/accounts/<account_id>/sis_imports/<id>/sis_import_errors' \
    -H "Authorization: Bearer <token>"

Example:
  curl 'https://<canvas>/api/v1/accounts/<account_id>/sis_import_errors' \
    -H "Authorization: Bearer <token>"

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.sis_import_error import SisImportError
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
    api_instance = canvas_lms_python_client.SisImportErrorsApiApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    failure = True # bool | If set, only shows errors on a sis import that would cause a failure. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # Get SIS import error list
        api_response = await api_instance.sis_import_errors_api_index_for_accounts(account_id, failure=failure, page=page, per_page=per_page)
        print("The response of SisImportErrorsApiApi->sis_import_errors_api_index_for_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SisImportErrorsApiApi->sis_import_errors_api_index_for_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **failure** | **bool**| If set, only shows errors on a sis import that would cause a failure. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[SisImportError]**](SisImportError.md)

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

