# canvas_lms_python_client.DeploymentsApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deployments_create**](DeploymentsApi.md#deployments_create) | **POST** /api/v1/accounts/{account_id}/lti_registrations/{registration_id}/deployments | Create LTI Deployment
[**deployments_destroy**](DeploymentsApi.md#deployments_destroy) | **DELETE** /api/v1/accounts/{account_id}/lti_registrations/{registration_id}/deployments/{id} | Delete LTI Deployment
[**deployments_list**](DeploymentsApi.md#deployments_list) | **GET** /api/v1/accounts/{account_id}/lti_registrations/{registration_id}/deployments | List LTI Deployments
[**deployments_list_controls**](DeploymentsApi.md#deployments_list_controls) | **GET** /api/v1/accounts/{account_id}/lti_registrations/{registration_id}/deployments/{id}/controls | List LTI Context Controls
[**deployments_show**](DeploymentsApi.md#deployments_show) | **GET** /api/v1/accounts/{account_id}/lti_registrations/{registration_id}/deployments/{id} | Show LTI Deployment


# **deployments_create**
> LtiDeployment deployments_create(account_id, registration_id, deployments_create_request=deployments_create_request)

Create LTI Deployment

Create a new deployment for the specified LTI registration for the given context.
If no context is specified, the deployment will be created in the root account.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.deployments_create_request import DeploymentsCreateRequest
from canvas_lms_python_client.models.lti_deployment import LtiDeployment
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
    api_instance = canvas_lms_python_client.DeploymentsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    registration_id = 'registration_id_example' # str | Scope response to registration_id
    deployments_create_request = canvas_lms_python_client.DeploymentsCreateRequest() # DeploymentsCreateRequest | Request body parameters  **Example Request:** ``` curl -X POST 'https://<canvas>/api/v1/accounts/<account_id>/lti_registrations/<registration_id>/deployments' \\      -H \"Authorization: Bearer <token>\" ``` (optional)

    try:
        # Create LTI Deployment
        api_response = await api_instance.deployments_create(account_id, registration_id, deployments_create_request=deployments_create_request)
        print("The response of DeploymentsApi->deployments_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeploymentsApi->deployments_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **registration_id** | **str**| Scope response to registration_id | 
 **deployments_create_request** | [**DeploymentsCreateRequest**](DeploymentsCreateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl -X POST &#39;https://&lt;canvas&gt;/api/v1/accounts/&lt;account_id&gt;/lti_registrations/&lt;registration_id&gt;/deployments&#39; \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**LtiDeployment**](LtiDeployment.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Lti::Deployment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deployments_destroy**
> LtiDeployment deployments_destroy(account_id, id, registration_id)

Delete LTI Deployment

Delete the specified deployment for the specified LTI tool in this context.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.lti_deployment import LtiDeployment
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
    api_instance = canvas_lms_python_client.DeploymentsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id
    registration_id = 'registration_id_example' # str | Scope response to registration_id

    try:
        # Delete LTI Deployment
        api_response = await api_instance.deployments_destroy(account_id, id, registration_id)
        print("The response of DeploymentsApi->deployments_destroy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeploymentsApi->deployments_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 
 **registration_id** | **str**| Scope response to registration_id | 

### Return type

[**LtiDeployment**](LtiDeployment.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Lti::Deployment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deployments_list**
> List[LtiDeployment] deployments_list(account_id, registration_id, page=page, per_page=per_page)

List LTI Deployments

List all deployments available for the specified LTI registration.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.lti_deployment import LtiDeployment
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
    api_instance = canvas_lms_python_client.DeploymentsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    registration_id = 'registration_id_example' # str | Scope response to registration_id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List LTI Deployments
        api_response = await api_instance.deployments_list(account_id, registration_id, page=page, per_page=per_page)
        print("The response of DeploymentsApi->deployments_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeploymentsApi->deployments_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **registration_id** | **str**| Scope response to registration_id | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[LtiDeployment]**](LtiDeployment.md)

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

# **deployments_list_controls**
> List[LtiContextControl] deployments_list_controls(account_id, id, registration_id, page=page, per_page=per_page)

List LTI Context Controls

List all context controls for the specified deployment. Context Controls are used to manage
LTI tool availability in contexts across Canvas.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.lti_context_control import LtiContextControl
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
    api_instance = canvas_lms_python_client.DeploymentsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id
    registration_id = 'registration_id_example' # str | Scope response to registration_id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List LTI Context Controls
        api_response = await api_instance.deployments_list_controls(account_id, id, registration_id, page=page, per_page=per_page)
        print("The response of DeploymentsApi->deployments_list_controls:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeploymentsApi->deployments_list_controls: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 
 **registration_id** | **str**| Scope response to registration_id | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[LtiContextControl]**](LtiContextControl.md)

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

# **deployments_show**
> LtiDeployment deployments_show(account_id, id, registration_id)

Show LTI Deployment

Display details of the specified deployment for the specified LTI registration in this context.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.lti_deployment import LtiDeployment
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
    api_instance = canvas_lms_python_client.DeploymentsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id
    registration_id = 'registration_id_example' # str | Scope response to registration_id

    try:
        # Show LTI Deployment
        api_response = await api_instance.deployments_show(account_id, id, registration_id)
        print("The response of DeploymentsApi->deployments_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeploymentsApi->deployments_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 
 **registration_id** | **str**| Scope response to registration_id | 

### Return type

[**LtiDeployment**](LtiDeployment.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Lti::Deployment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

