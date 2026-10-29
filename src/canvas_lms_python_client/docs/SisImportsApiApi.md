# canvas_lms_python_client.SisImportsApiApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sis_imports_api_abort**](SisImportsApiApi.md#sis_imports_api_abort) | **PUT** /api/v1/accounts/{account_id}/sis_imports/{id}/abort | Abort SIS import
[**sis_imports_api_abort_all_pending**](SisImportsApiApi.md#sis_imports_api_abort_all_pending) | **PUT** /api/v1/accounts/{account_id}/sis_imports/abort_all_pending | Abort all pending SIS imports
[**sis_imports_api_create**](SisImportsApiApi.md#sis_imports_api_create) | **POST** /api/v1/accounts/{account_id}/sis_imports | Import SIS data
[**sis_imports_api_importing**](SisImportsApiApi.md#sis_imports_api_importing) | **GET** /api/v1/accounts/{account_id}/sis_imports/importing | Get the current importing SIS import
[**sis_imports_api_index**](SisImportsApiApi.md#sis_imports_api_index) | **GET** /api/v1/accounts/{account_id}/sis_imports | Get SIS import list
[**sis_imports_api_restore_states**](SisImportsApiApi.md#sis_imports_api_restore_states) | **PUT** /api/v1/accounts/{account_id}/sis_imports/{id}/restore_states | Restore workflow_states of SIS imported items
[**sis_imports_api_show**](SisImportsApiApi.md#sis_imports_api_show) | **GET** /api/v1/accounts/{account_id}/sis_imports/{id} | Get SIS import status


# **sis_imports_api_abort**
> SisImport sis_imports_api_abort(account_id, id)

Abort SIS import

Abort a SIS import that has not completed.

Aborting a sis batch that is running can take some time for every process to
see the abort event. Subsequent sis batches begin to process 10 minutes
after the abort to allow each process to clean up properly.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.sis_import import SisImport
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
    api_instance = canvas_lms_python_client.SisImportsApiApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id

    try:
        # Abort SIS import
        api_response = await api_instance.sis_imports_api_abort(account_id, id)
        print("The response of SisImportsApiApi->sis_imports_api_abort:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SisImportsApiApi->sis_imports_api_abort: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**SisImport**](SisImport.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | SisImport |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sis_imports_api_abort_all_pending**
> bool sis_imports_api_abort_all_pending(account_id)

Abort all pending SIS imports

Abort already created but not processed or processing SIS imports.

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
    api_instance = canvas_lms_python_client.SisImportsApiApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id

    try:
        # Abort all pending SIS imports
        api_response = await api_instance.sis_imports_api_abort_all_pending(account_id)
        print("The response of SisImportsApiApi->sis_imports_api_abort_all_pending:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SisImportsApiApi->sis_imports_api_abort_all_pending: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 

### Return type

**bool**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | boolean |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sis_imports_api_create**
> SisImport sis_imports_api_create(account_id, sis_imports_api_create_request=sis_imports_api_create_request)

Import SIS data

Import SIS data into Canvas. Must be on a root account with SIS imports
enabled.

For more information on the format that's expected here, please see the
"SIS CSV" section in the API docs.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.sis_import import SisImport
from canvas_lms_python_client.models.sis_imports_api_create_request import SisImportsApiCreateRequest
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
    api_instance = canvas_lms_python_client.SisImportsApiApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    sis_imports_api_create_request = canvas_lms_python_client.SisImportsApiCreateRequest() # SisImportsApiCreateRequest | Request body parameters (optional)

    try:
        # Import SIS data
        api_response = await api_instance.sis_imports_api_create(account_id, sis_imports_api_create_request=sis_imports_api_create_request)
        print("The response of SisImportsApiApi->sis_imports_api_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SisImportsApiApi->sis_imports_api_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **sis_imports_api_create_request** | [**SisImportsApiCreateRequest**](SisImportsApiCreateRequest.md)| Request body parameters | [optional] 

### Return type

[**SisImport**](SisImport.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | SisImport |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sis_imports_api_importing**
> SisImport sis_imports_api_importing(account_id)

Get the current importing SIS import

Returns the SIS imports that are currently processing for an account. If no
imports are running, will return an empty array.

Example:
  curl https://<canvas>/api/v1/accounts/<account_id>/sis_imports/importing \
    -H 'Authorization: Bearer <token>'

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.sis_import import SisImport
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
    api_instance = canvas_lms_python_client.SisImportsApiApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id

    try:
        # Get the current importing SIS import
        api_response = await api_instance.sis_imports_api_importing(account_id)
        print("The response of SisImportsApiApi->sis_imports_api_importing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SisImportsApiApi->sis_imports_api_importing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 

### Return type

[**SisImport**](SisImport.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | SisImport |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sis_imports_api_index**
> List[SisImport] sis_imports_api_index(account_id, created_since=created_since, created_before=created_before, workflow_state=workflow_state, page=page, per_page=per_page)

Get SIS import list

Returns the list of SIS imports for an account

Example:
  curl https://<canvas>/api/v1/accounts/<account_id>/sis_imports \
    -H 'Authorization: Bearer <token>'

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.sis_import import SisImport
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
    api_instance = canvas_lms_python_client.SisImportsApiApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    created_since = 'created_since_example' # str | If set, only shows imports created after the specified date (use ISO8601 format) (optional)
    created_before = 'created_before_example' # str | If set, only shows imports created before the specified date (use ISO8601 format) (optional)
    workflow_state = ['workflow_state_example'] # List[str] | If set, only returns imports that are in the given state. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # Get SIS import list
        api_response = await api_instance.sis_imports_api_index(account_id, created_since=created_since, created_before=created_before, workflow_state=workflow_state, page=page, per_page=per_page)
        print("The response of SisImportsApiApi->sis_imports_api_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SisImportsApiApi->sis_imports_api_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **created_since** | **str**| If set, only shows imports created after the specified date (use ISO8601 format) | [optional] 
 **created_before** | **str**| If set, only shows imports created before the specified date (use ISO8601 format) | [optional] 
 **workflow_state** | [**List[str]**](str.md)| If set, only returns imports that are in the given state. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[SisImport]**](SisImport.md)

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

# **sis_imports_api_restore_states**
> Progress sis_imports_api_restore_states(account_id, id, sis_imports_api_restore_states_request=sis_imports_api_restore_states_request)

Restore workflow_states of SIS imported items

This will restore the the workflow_state for all the items that changed
their workflow_state during the import being restored.
This will restore states for items imported with the following importers:
accounts.csv terms.csv courses.csv sections.csv group_categories.csv
groups.csv users.csv admins.csv
This also restores states for other items that changed during the import.
An example would be if an enrollment was deleted from a sis import and the
group_membership was also deleted as a result of the enrollment deletion,
both items would be restored when the sis batch is restored.

Restore data is retained for 30 days post-import. This endpoint is
unavailable after that time.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.progress import Progress
from canvas_lms_python_client.models.sis_imports_api_restore_states_request import SisImportsApiRestoreStatesRequest
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
    api_instance = canvas_lms_python_client.SisImportsApiApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id
    sis_imports_api_restore_states_request = canvas_lms_python_client.SisImportsApiRestoreStatesRequest() # SisImportsApiRestoreStatesRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/accounts/<account_id>/sis_imports/<sis_import_id>/restore_states \\   -H 'Authorization: Bearer <token>' ``` (optional)

    try:
        # Restore workflow_states of SIS imported items
        api_response = await api_instance.sis_imports_api_restore_states(account_id, id, sis_imports_api_restore_states_request=sis_imports_api_restore_states_request)
        print("The response of SisImportsApiApi->sis_imports_api_restore_states:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SisImportsApiApi->sis_imports_api_restore_states: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 
 **sis_imports_api_restore_states_request** | [**SisImportsApiRestoreStatesRequest**](SisImportsApiRestoreStatesRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/accounts/&lt;account_id&gt;/sis_imports/&lt;sis_import_id&gt;/restore_states \\   -H &#39;Authorization: Bearer &lt;token&gt;&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**Progress**](Progress.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Progress |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sis_imports_api_show**
> SisImport sis_imports_api_show(account_id, id)

Get SIS import status

Get the status of an already created SIS import.

  Examples:
    curl https://<canvas>/api/v1/accounts/<account_id>/sis_imports/<sis_import_id> \
        -H 'Authorization: Bearer <token>'

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.sis_import import SisImport
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
    api_instance = canvas_lms_python_client.SisImportsApiApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id

    try:
        # Get SIS import status
        api_response = await api_instance.sis_imports_api_show(account_id, id)
        print("The response of SisImportsApiApi->sis_imports_api_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SisImportsApiApi->sis_imports_api_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**SisImport**](SisImport.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | SisImport |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

