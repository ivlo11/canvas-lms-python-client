# canvas_lms_python_client.ContextControlsApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**context_controls_create**](ContextControlsApi.md#context_controls_create) | **POST** /api/v1/accounts/{account_id}/lti_registrations/{registration_id}/controls | Create LTI Context Control
[**context_controls_create_many**](ContextControlsApi.md#context_controls_create_many) | **POST** /api/v1/accounts/{account_id}/lti_registrations/{registration_id}/controls/bulk | Bulk Create LTI Context Controls
[**context_controls_delete**](ContextControlsApi.md#context_controls_delete) | **DELETE** /api/v1/accounts/{account_id}/lti_registrations/{registration_id}/controls/{id} | Delete a Context Control
[**context_controls_index**](ContextControlsApi.md#context_controls_index) | **GET** /api/v1/accounts/{account_id}/lti_registrations/{registration_id}/controls | List All Context Controls
[**context_controls_show**](ContextControlsApi.md#context_controls_show) | **GET** /api/v1/accounts/{account_id}/lti_registrations/{registration_id}/controls/{id} | Show LTI Context Control
[**context_controls_update**](ContextControlsApi.md#context_controls_update) | **PUT** /api/v1/accounts/{account_id}/lti_registrations/{registration_id}/controls/{id} | Modify a Context Control


# **context_controls_create**
> object context_controls_create(account_id, registration_id, context_controls_create_request=context_controls_create_request)

Create LTI Context Control

Create a new LTI ContextControl for the specified LTI registration in this context.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.context_controls_create_request import ContextControlsCreateRequest
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
    api_instance = canvas_lms_python_client.ContextControlsApi(api_client)
    account_id = 'account_id_example' # str | ID of the account
    registration_id = 'registration_id_example' # str | Scope response to registration_id
    context_controls_create_request = canvas_lms_python_client.ContextControlsCreateRequest() # ContextControlsCreateRequest | Request body parameters  **Example Request:** ``` curl -X POST 'https://<canvas>/api/v1/accounts/<account_id>/lti_registrations/<registration_id>/controls' \\      -H \"Authorization: Bearer <token>\" \\      -d '{             \"account_id\": 1,             \"deployment_id\": 1,             \"available\": true          }' ``` (optional)

    try:
        # Create LTI Context Control
        api_response = await api_instance.context_controls_create(account_id, registration_id, context_controls_create_request=context_controls_create_request)
        print("The response of ContextControlsApi->context_controls_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContextControlsApi->context_controls_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of the account | 
 **registration_id** | **str**| Scope response to registration_id | 
 **context_controls_create_request** | [**ContextControlsCreateRequest**](ContextControlsCreateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl -X POST &#39;https://&lt;canvas&gt;/api/v1/accounts/&lt;account_id&gt;/lti_registrations/&lt;registration_id&gt;/controls&#39; \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; \\      -d &#39;{             \&quot;account_id\&quot;: 1,             \&quot;deployment_id\&quot;: 1,             \&quot;available\&quot;: true          }&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

**object**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Lti::ContextControl |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **context_controls_create_many**
> object context_controls_create_many(account_id, registration_id, context_controls_create_many_request=context_controls_create_many_request)

Bulk Create LTI Context Controls

Create up to 100 new LTI ContextControls for the specified LTI registration in this context.
Control parameters are sent as a JSON array of objects, each with the same parameters as the Create LTI Context Control endpoint.
Note that if a control already exists for the specified context and deployment, it will be updated instead of created.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.context_controls_create_many_request import ContextControlsCreateManyRequest
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
    api_instance = canvas_lms_python_client.ContextControlsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    registration_id = 'registration_id_example' # str | Scope response to registration_id
    context_controls_create_many_request = canvas_lms_python_client.ContextControlsCreateManyRequest() # ContextControlsCreateManyRequest | Request body parameters  **Example Request:** ``` curl -X POST 'https://<canvas>/api/v1/accounts/<account_id>/lti_registrations/<registration_id>/controls' \\      -H \"Authorization: Bearer <token>\" \\      --json '[ \\                { \"account_id\": 1, \"available\": false }, \\                { \"course_id\": 1, \"deployment_id\": 1 }, \\                { \"account_id\": 1, \"deployment_id\": 2 } \\              ]' ``` (optional)

    try:
        # Bulk Create LTI Context Controls
        api_response = await api_instance.context_controls_create_many(account_id, registration_id, context_controls_create_many_request=context_controls_create_many_request)
        print("The response of ContextControlsApi->context_controls_create_many:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContextControlsApi->context_controls_create_many: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **registration_id** | **str**| Scope response to registration_id | 
 **context_controls_create_many_request** | [**ContextControlsCreateManyRequest**](ContextControlsCreateManyRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl -X POST &#39;https://&lt;canvas&gt;/api/v1/accounts/&lt;account_id&gt;/lti_registrations/&lt;registration_id&gt;/controls&#39; \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; \\      --json &#39;[ \\                { \&quot;account_id\&quot;: 1, \&quot;available\&quot;: false }, \\                { \&quot;course_id\&quot;: 1, \&quot;deployment_id\&quot;: 1 }, \\                { \&quot;account_id\&quot;: 1, \&quot;deployment_id\&quot;: 2 } \\              ]&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

**object**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Lti::ContextControl |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **context_controls_delete**
> object context_controls_delete(account_id, id, registration_id)

Delete a Context Control

Deletes a context control. Returns the control that is now deleted.

Note: Deleting the "primary" control for a deployment (the control associated with the context
where the deployment is installed) is not allowed and will return an error. This prevents
situations where a deployment cannot be managed from the Apps page.

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
    api_instance = canvas_lms_python_client.ContextControlsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id
    registration_id = 'registration_id_example' # str | Scope response to registration_id

    try:
        # Delete a Context Control
        api_response = await api_instance.context_controls_delete(account_id, id, registration_id)
        print("The response of ContextControlsApi->context_controls_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContextControlsApi->context_controls_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 
 **registration_id** | **str**| Scope response to registration_id | 

### Return type

**object**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Lti::ContextControl |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **context_controls_index**
> List[object] context_controls_index(account_id, registration_id, page=page, per_page=per_page)

List All Context Controls

List all LTI ContextControls for the given LTI Registration.
These controls are partitioned by LTI Deployment, and have added
calculated fields for display in the Canvas UI.

This endpoint is used to populate the Availability page for an LTI Registration
and may not be useful for general API Usage. For listing all ContextControls
for a given Deployment, see the LTI Deployments - List Controls for Deployment endpoint.

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
    api_instance = canvas_lms_python_client.ContextControlsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    registration_id = 'registration_id_example' # str | Scope response to registration_id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List All Context Controls
        api_response = await api_instance.context_controls_index(account_id, registration_id, page=page, per_page=per_page)
        print("The response of ContextControlsApi->context_controls_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContextControlsApi->context_controls_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **registration_id** | **str**| Scope response to registration_id | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

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

# **context_controls_show**
> object context_controls_show(account_id, id, registration_id)

Show LTI Context Control

Display details of the specified LTI ContextControl for the specified LTI registration in this context.

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
    api_instance = canvas_lms_python_client.ContextControlsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id
    registration_id = 'registration_id_example' # str | Scope response to registration_id

    try:
        # Show LTI Context Control
        api_response = await api_instance.context_controls_show(account_id, id, registration_id)
        print("The response of ContextControlsApi->context_controls_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContextControlsApi->context_controls_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 
 **registration_id** | **str**| Scope response to registration_id | 

### Return type

**object**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Lti::ContextControl |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **context_controls_update**
> object context_controls_update(account_id, id, registration_id, context_controls_update_request=context_controls_update_request)

Modify a Context Control

Changes the availability of a context control. This endpoint can only be used
to change the availability of a context control; no other attributes about the
control (such as which course or account it belongs to) can be changed here.
To change those values, the control should be deleted and a new one created
instead.

Returns the context control with its new availability value applied.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.context_controls_update_request import ContextControlsUpdateRequest
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
    api_instance = canvas_lms_python_client.ContextControlsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id
    registration_id = 'registration_id_example' # str | Scope response to registration_id
    context_controls_update_request = canvas_lms_python_client.ContextControlsUpdateRequest() # ContextControlsUpdateRequest | Request body parameters  **Example Request:** ``` curl \"https://<canvas>/api/v1/accounts/<account_id>/lti_registrations/<registration_id>/controls/<id>\" \\      -X PUT \\      -F \"available=true\" \\      -H \"Authorization: Bearer <token>\" ``` (optional)

    try:
        # Modify a Context Control
        api_response = await api_instance.context_controls_update(account_id, id, registration_id, context_controls_update_request=context_controls_update_request)
        print("The response of ContextControlsApi->context_controls_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContextControlsApi->context_controls_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 
 **registration_id** | **str**| Scope response to registration_id | 
 **context_controls_update_request** | [**ContextControlsUpdateRequest**](ContextControlsUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl \&quot;https://&lt;canvas&gt;/api/v1/accounts/&lt;account_id&gt;/lti_registrations/&lt;registration_id&gt;/controls/&lt;id&gt;\&quot; \\      -X PUT \\      -F \&quot;available&#x3D;true\&quot; \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; &#x60;&#x60;&#x60; | [optional] 

### Return type

**object**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Lti::ContextControl |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

