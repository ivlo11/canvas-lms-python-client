# canvas_lms_python_client.RegistrationsApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**registrations_apply_registration_update_request**](RegistrationsApi.md#registrations_apply_registration_update_request) | **PUT** /api/v1/accounts/{account_id}/lti_registrations/{id}/update_requests/{update_request_id}/apply | Apply LTI Registration Update Requst
[**registrations_bind**](RegistrationsApi.md#registrations_bind) | **POST** /api/v1/accounts/{account_id}/lti_registrations/{id}/bind | Bind an LTI Registration to a Root Account
[**registrations_check_domain_duplicates**](RegistrationsApi.md#registrations_check_domain_duplicates) | **GET** /api/v1/accounts/{account_id}/lti_registrations/check_domain_duplicates | Check for Duplicate Domains
[**registrations_context_search**](RegistrationsApi.md#registrations_context_search) | **GET** /api/v1/accounts/{account_id}/lti_registrations/{registration_id}/deployments/{deployment_id}/context_search | Search for Accounts and Courses
[**registrations_create**](RegistrationsApi.md#registrations_create) | **POST** /api/v1/accounts/{account_id}/lti_registrations | Create an LTI Registration
[**registrations_destroy**](RegistrationsApi.md#registrations_destroy) | **DELETE** /api/v1/accounts/{account_id}/lti_registrations/{id} | Delete an LTI Registration
[**registrations_history**](RegistrationsApi.md#registrations_history) | **GET** /api/v1/accounts/{account_id}/lti_registrations/{id}/history | Get LTI Registration History
[**registrations_install_from_template**](RegistrationsApi.md#registrations_install_from_template) | **POST** /api/v1/accounts/{account_id}/lti_registrations/{id}/install_from_template | Install an LTI Registration from a Template
[**registrations_install_status**](RegistrationsApi.md#registrations_install_status) | **GET** /api/v1/accounts/{account_id}/lti_registrations/install_status/{client_id} | Check LTI Registration Install Status
[**registrations_latest_registration_update_request**](RegistrationsApi.md#registrations_latest_registration_update_request) | **GET** /api/v1/accounts/{account_id}/lti_registrations/{id}/latest_update_request | Get Latest LTI Registration Update Request
[**registrations_list**](RegistrationsApi.md#registrations_list) | **GET** /api/v1/accounts/{account_id}/lti_registrations | List LTI Registrations in an account
[**registrations_overlay_history**](RegistrationsApi.md#registrations_overlay_history) | **GET** /api/v1/accounts/{account_id}/lti_registrations/{id}/overlay_history | Get LTI Registration Overlay History
[**registrations_reset**](RegistrationsApi.md#registrations_reset) | **PUT** /api/v1/accounts/{account_id}/lti_registrations/{id}/reset | Reset an LTI Registration to Defaults
[**registrations_show**](RegistrationsApi.md#registrations_show) | **GET** /api/v1/accounts/{account_id}/lti_registrations/{id} | Show an LTI Registration
[**registrations_show_by_client_id**](RegistrationsApi.md#registrations_show_by_client_id) | **GET** /api/v1/accounts/{account_id}/lti_registration_by_client_id/{client_id} | Show an LTI Registration (via the client_id)
[**registrations_show_by_utid**](RegistrationsApi.md#registrations_show_by_utid) | **GET** /api/v1/accounts/{account_id}/lti_registrations/by_utid/{utid} | Get LTI Registration by Unified Tool ID
[**registrations_show_registration_update_request**](RegistrationsApi.md#registrations_show_registration_update_request) | **GET** /api/v1/accounts/{account_id}/lti_registrations/{id}/update_requests/{update_request_id} | Get LTI Registration Update Request
[**registrations_unbind**](RegistrationsApi.md#registrations_unbind) | **DELETE** /api/v1/accounts/{account_id}/lti_registrations/{id}/bind | Remove an Inherited LTI Registration
[**registrations_update**](RegistrationsApi.md#registrations_update) | **PUT** /api/v1/accounts/{account_id}/lti_registrations/{id} | Update an LTI Registration
[**registrations_validate_lti_configuration**](RegistrationsApi.md#registrations_validate_lti_configuration) | **POST** /api/v1/accounts/{account_id}/lti_registrations/configuration/validate | Validate LtiConfiguration


# **registrations_apply_registration_update_request**
> object registrations_apply_registration_update_request(account_id, id, update_request_id, registrations_apply_registration_update_request_request=registrations_apply_registration_update_request_request)

Apply LTI Registration Update Requst

Applies a registration update request to an existing registration,
replacing the existing configuration and overlay with the new values.
If the request is rejected, marks it as rejected without applying changes.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.registrations_apply_registration_update_request_request import RegistrationsApplyRegistrationUpdateRequestRequest
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
    api_instance = canvas_lms_python_client.RegistrationsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | The id of the registration to update.
    update_request_id = 'update_request_id_example' # str | The id of the registration update request to apply.
    registrations_apply_registration_update_request_request = canvas_lms_python_client.RegistrationsApplyRegistrationUpdateRequestRequest() # RegistrationsApplyRegistrationUpdateRequestRequest | Request body parameters  **Example Request:** ``` curl -X POST 'https://<canvas>/api/v1/accounts/<account_id>/lti_registrations/:id/update_requests/:update_request_id/apply' \\      -d '{\"overlay\": <LtiConfigurationOverlay>, \"accepted\": boolean}' \\      -H \"Content-Type: application/json\" \\      -H \"Authorization: Bearer <token>\" ``` (optional)

    try:
        # Apply LTI Registration Update Requst
        api_response = await api_instance.registrations_apply_registration_update_request(account_id, id, update_request_id, registrations_apply_registration_update_request_request=registrations_apply_registration_update_request_request)
        print("The response of RegistrationsApi->registrations_apply_registration_update_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistrationsApi->registrations_apply_registration_update_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| The id of the registration to update. | 
 **update_request_id** | **str**| The id of the registration update request to apply. | 
 **registrations_apply_registration_update_request_request** | [**RegistrationsApplyRegistrationUpdateRequestRequest**](RegistrationsApplyRegistrationUpdateRequestRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl -X POST &#39;https://&lt;canvas&gt;/api/v1/accounts/&lt;account_id&gt;/lti_registrations/:id/update_requests/:update_request_id/apply&#39; \\      -d &#39;{\&quot;overlay\&quot;: &lt;LtiConfigurationOverlay&gt;, \&quot;accepted\&quot;: boolean}&#39; \\      -H \&quot;Content-Type: application/json\&quot; \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; &#x60;&#x60;&#x60; | [optional] 

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
**0** | Lti::Registration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registrations_bind**
> object registrations_bind(account_id, id, registrations_bind_request=registrations_bind_request)

Bind an LTI Registration to a Root Account

Enable or disable the specified LTI registration for the specified root account.
To enable an inherited registration (eg from Site Admin), pass the registration's global ID.

Only allowed for root accounts.

<b>Specifics for centrally-managed/federated consortia:</b>
Child root accounts may not bind inherited registrations.
For parent root account, binding also applies to all child root accounts.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.registrations_bind_request import RegistrationsBindRequest
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
    api_instance = canvas_lms_python_client.RegistrationsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id
    registrations_bind_request = canvas_lms_python_client.RegistrationsBindRequest() # RegistrationsBindRequest | Request body parameters  **Example Request:** ``` This would enable the specified LTI registration for the specified account curl -X POST 'https://<canvas>/api/v1/accounts/<account_id>/lti_registrations/<registration_id>/bind' \\      -H \"Authorization: Bearer <token>\" \\      -H \"Content-Type: application/json\" \\      -d '{\"workflow_state\": \"on\"}' ``` (optional)

    try:
        # Bind an LTI Registration to a Root Account
        api_response = await api_instance.registrations_bind(account_id, id, registrations_bind_request=registrations_bind_request)
        print("The response of RegistrationsApi->registrations_bind:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistrationsApi->registrations_bind: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 
 **registrations_bind_request** | [**RegistrationsBindRequest**](RegistrationsBindRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; This would enable the specified LTI registration for the specified account curl -X POST &#39;https://&lt;canvas&gt;/api/v1/accounts/&lt;account_id&gt;/lti_registrations/&lt;registration_id&gt;/bind&#39; \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; \\      -H \&quot;Content-Type: application/json\&quot; \\      -d &#39;{\&quot;workflow_state\&quot;: \&quot;on\&quot;}&#39; &#x60;&#x60;&#x60; | [optional] 

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
**0** | Lti::RegistrationAccountBinding |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registrations_check_domain_duplicates**
> List[object] registrations_check_domain_duplicates(account_id, domain)

Check for Duplicate Domains

Checks if any existing LTI registrations in the account have the same domain
as the provided domain. This includes registrations owned by the account,
Site Admin registrations forced on, and inherited registrations that are enabled.
This is a utility endpoint for the LTI registration UI to warn administrators
about potential conflicts.

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
    api_instance = canvas_lms_python_client.RegistrationsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    domain = 'domain_example' # str | The domain to check for duplicates.

    try:
        # Check for Duplicate Domains
        api_response = await api_instance.registrations_check_domain_duplicates(account_id, domain)
        print("The response of RegistrationsApi->registrations_check_domain_duplicates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistrationsApi->registrations_check_domain_duplicates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **domain** | **str**| The domain to check for duplicates. | 

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

# **registrations_context_search**
> ContextSearchResponse registrations_context_search(account_id, deployment_id, registration_id, only_children_of=only_children_of, search_term=search_term)

Search for Accounts and Courses

This is a utility endpoint used by the Canvas Apps UI and may not serve general use cases.

Search for accounts and courses that match the search term on name, SIS id, or course code.
Returns all matching accounts and courses, including those nested in sub-accounts.
Returns bare-bones data about each account and course, and only up to 20 of each.
Used to populate the search dropdowns when managing LTI registration availability.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.context_search_response import ContextSearchResponse
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
    api_instance = canvas_lms_python_client.RegistrationsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    deployment_id = 'deployment_id_example' # str | Scope response to deployment_id
    registration_id = 'registration_id_example' # str | Scope response to registration_id
    only_children_of = 'only_children_of_example' # str | Account ID. If provided, only searches within this account and only returns direct children of this account. (optional)
    search_term = 'search_term_example' # str | String to search for in account names, SIS ids, or course codes. (optional)

    try:
        # Search for Accounts and Courses
        api_response = await api_instance.registrations_context_search(account_id, deployment_id, registration_id, only_children_of=only_children_of, search_term=search_term)
        print("The response of RegistrationsApi->registrations_context_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistrationsApi->registrations_context_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **deployment_id** | **str**| Scope response to deployment_id | 
 **registration_id** | **str**| Scope response to registration_id | 
 **only_children_of** | **str**| Account ID. If provided, only searches within this account and only returns direct children of this account. | [optional] 
 **search_term** | **str**| String to search for in account names, SIS ids, or course codes. | [optional] 

### Return type

[**ContextSearchResponse**](ContextSearchResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ContextSearchResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registrations_create**
> object registrations_create(account_id, registrations_create_request=registrations_create_request)

Create an LTI Registration

Create a new LTI Registration, as well as an associated Tool Configuration, Developer Key, and Registration Account
binding.
To install/create using Dynamic Registration, please use the
{file:file.registration.html Dynamic Registration API}.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.registrations_create_request import RegistrationsCreateRequest
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
    api_instance = canvas_lms_python_client.RegistrationsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    registrations_create_request = canvas_lms_python_client.RegistrationsCreateRequest() # RegistrationsCreateRequest | Request body parameters  **Example Request:** ``` This would create a new LTI Registration, as well as an associated Developer Key and LTI Tool Configuration.  curl -X POST 'https://<canvas>/api/v1/accounts/<account_id>/lti_registrations' \\     -H \"Authorization: Bearer <token>\" \\     -H \"Content-Type: application/json\" \\     -d '{           \"vendor\": \"Example\",           \"name\": \"An Example Tool\",           \"admin_nickname\": \"A Great LTI Tool\",           \"configuration\": {             \"title\": \"Sample Tool\",             \"description\": \"A sample LTI tool\",             \"target_link_uri\": \"https://example.com/launch\",             \"oidc_initiation_url\": \"https://example.com/oidc\",             \"redirect_uris\": [\"https://example.com/redirect\"],             \"scopes\": [\"https://purl.imsglobal.org/spec/lti-ags/scope/lineitem\"],             \"placements\": [               {                 \"placement\": \"course_navigation\",                 \"enabled\": true               }             ],             \"launch_settings\": {}           }         }' ``` (optional)

    try:
        # Create an LTI Registration
        api_response = await api_instance.registrations_create(account_id, registrations_create_request=registrations_create_request)
        print("The response of RegistrationsApi->registrations_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistrationsApi->registrations_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **registrations_create_request** | [**RegistrationsCreateRequest**](RegistrationsCreateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; This would create a new LTI Registration, as well as an associated Developer Key and LTI Tool Configuration.  curl -X POST &#39;https://&lt;canvas&gt;/api/v1/accounts/&lt;account_id&gt;/lti_registrations&#39; \\     -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; \\     -H \&quot;Content-Type: application/json\&quot; \\     -d &#39;{           \&quot;vendor\&quot;: \&quot;Example\&quot;,           \&quot;name\&quot;: \&quot;An Example Tool\&quot;,           \&quot;admin_nickname\&quot;: \&quot;A Great LTI Tool\&quot;,           \&quot;configuration\&quot;: {             \&quot;title\&quot;: \&quot;Sample Tool\&quot;,             \&quot;description\&quot;: \&quot;A sample LTI tool\&quot;,             \&quot;target_link_uri\&quot;: \&quot;https://example.com/launch\&quot;,             \&quot;oidc_initiation_url\&quot;: \&quot;https://example.com/oidc\&quot;,             \&quot;redirect_uris\&quot;: [\&quot;https://example.com/redirect\&quot;],             \&quot;scopes\&quot;: [\&quot;https://purl.imsglobal.org/spec/lti-ags/scope/lineitem\&quot;],             \&quot;placements\&quot;: [               {                 \&quot;placement\&quot;: \&quot;course_navigation\&quot;,                 \&quot;enabled\&quot;: true               }             ],             \&quot;launch_settings\&quot;: {}           }         }&#39; &#x60;&#x60;&#x60; | [optional] 

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
**0** | Lti::Registration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registrations_destroy**
> object registrations_destroy(account_id, id)

Delete an LTI Registration

Remove the specified LTI registration

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
    api_instance = canvas_lms_python_client.RegistrationsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id

    try:
        # Delete an LTI Registration
        api_response = await api_instance.registrations_destroy(account_id, id)
        print("The response of RegistrationsApi->registrations_destroy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistrationsApi->registrations_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 

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
**0** | Lti::Registration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registrations_history**
> List[object] registrations_history(account_id, id, page=page, per_page=per_page)

Get LTI Registration History

Returns the history entries for the specified LTI registration.
This endpoint provides comprehensive change tracking for all fields associated
with the registration, including registration fields, developer key changes,
internal configuration changes, and overlay changes. Supports pagination using the `page` and `per_page` parameters.
The default page size is 10.

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
    api_instance = canvas_lms_python_client.RegistrationsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # Get LTI Registration History
        api_response = await api_instance.registrations_history(account_id, id, page=page, per_page=per_page)
        print("The response of RegistrationsApi->registrations_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistrationsApi->registrations_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 
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

# **registrations_install_from_template**
> object registrations_install_from_template(account_id, id)

Install an LTI Registration from a Template

This endpoint installs a local copy of a "template" LTI registration from Site Admin into the specified account.
The local copy can then be customized for the account without affecting the template registration.

Only allowed for root accounts and for registrations from Site Admin marked as templates.

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
    api_instance = canvas_lms_python_client.RegistrationsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id

    try:
        # Install an LTI Registration from a Template
        api_response = await api_instance.registrations_install_from_template(account_id, id)
        print("The response of RegistrationsApi->registrations_install_from_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistrationsApi->registrations_install_from_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 

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
**0** | Lti::Registration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registrations_install_status**
> object registrations_install_status(account_id, client_id)

Check LTI Registration Install Status

Returns the local installation status for a Site Admin LTI registration.
If the developer key's registration is in Site Admin, returns the local copy
in the current account (if installed). If the registration is already in the
current account, returns it directly.

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
    api_instance = canvas_lms_python_client.RegistrationsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    client_id = 'client_id_example' # str | Scope response to client_id

    try:
        # Check LTI Registration Install Status
        api_response = await api_instance.registrations_install_status(account_id, client_id)
        print("The response of RegistrationsApi->registrations_install_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistrationsApi->registrations_install_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **client_id** | **str**| Scope response to client_id | 

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
**0** | Lti::Registration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registrations_latest_registration_update_request**
> object registrations_latest_registration_update_request(account_id, id)

Get Latest LTI Registration Update Request

Retrieves the most recent update request for a registration, regardless of its status.
Returns 404 if there are no update requests for this registration.

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
    api_instance = canvas_lms_python_client.RegistrationsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | The id of the registration.

    try:
        # Get Latest LTI Registration Update Request
        api_response = await api_instance.registrations_latest_registration_update_request(account_id, id)
        print("The response of RegistrationsApi->registrations_latest_registration_update_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistrationsApi->registrations_latest_registration_update_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| The id of the registration. | 

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
**0** | Lti::RegistrationUpdateRequest |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registrations_list**
> ListLtiRegistrationsResponse registrations_list(account_id, per_page=per_page, page=page, sort=sort, dir=dir, include=include)

List LTI Registrations in an account

Returns all LTI registrations in the specified account.
Includes registrations created in this account, those set to 'allow' from a
parent root account (like Site Admin) and 'on' for this account,
and those enabled 'on' at the parent root account level.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.list_lti_registrations_response import ListLtiRegistrationsResponse
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
    api_instance = canvas_lms_python_client.RegistrationsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    per_page = 56 # int | The number of registrations to return per page. Defaults to 15. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    sort = 'sort_example' # str | The field to sort by. Choices are: name, nickname, lti_version, installed, installed_by, updated_by, updated, and on. Defaults to installed. (optional)
    dir = 'dir_example' # str | The order to sort the given column by. Defaults to desc. (optional)
    include = ['include_example'] # List[str] | Array of additional data to include. Always includes [account_binding].  \"account_binding\":: the registration's binding to the given account \"configuration\":: the registration's Canvas-style tool configuration, without any overlays applied. \"overlaid_configuration\":: the registration's Canvas-style tool configuration, with all overlays applied. \"overlay\":: the registration's admin-defined configuration overlay (optional)

    try:
        # List LTI Registrations in an account
        api_response = await api_instance.registrations_list(account_id, per_page=per_page, page=page, sort=sort, dir=dir, include=include)
        print("The response of RegistrationsApi->registrations_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistrationsApi->registrations_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **per_page** | **int**| The number of registrations to return per page. Defaults to 15. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **sort** | **str**| The field to sort by. Choices are: name, nickname, lti_version, installed, installed_by, updated_by, updated, and on. Defaults to installed. | [optional] 
 **dir** | **str**| The order to sort the given column by. Defaults to desc. | [optional] 
 **include** | [**List[str]**](str.md)| Array of additional data to include. Always includes [account_binding].  \&quot;account_binding\&quot;:: the registration&#39;s binding to the given account \&quot;configuration\&quot;:: the registration&#39;s Canvas-style tool configuration, without any overlays applied. \&quot;overlaid_configuration\&quot;:: the registration&#39;s Canvas-style tool configuration, with all overlays applied. \&quot;overlay\&quot;:: the registration&#39;s admin-defined configuration overlay | [optional] 

### Return type

[**ListLtiRegistrationsResponse**](ListLtiRegistrationsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ListLtiRegistrationsResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registrations_overlay_history**
> List[object] registrations_overlay_history(account_id, id, limit=limit)

Get LTI Registration Overlay History

Returns the overlay history items for the specified LTI registration.

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
    api_instance = canvas_lms_python_client.RegistrationsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id
    limit = 56 # int | The maximum number of history items to return. Defaults to 10. Maximum allowed is 100. (optional)

    try:
        # Get LTI Registration Overlay History
        api_response = await api_instance.registrations_overlay_history(account_id, id, limit=limit)
        print("The response of RegistrationsApi->registrations_overlay_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistrationsApi->registrations_overlay_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 
 **limit** | **int**| The maximum number of history items to return. Defaults to 10. Maximum allowed is 100. | [optional] 

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

# **registrations_reset**
> object registrations_reset(account_id, id)

Reset an LTI Registration to Defaults

Reset the specified LTI registration to its default settings in this context. This removes all customizations
that were present in the overlay associated with this context.

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
    api_instance = canvas_lms_python_client.RegistrationsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id

    try:
        # Reset an LTI Registration to Defaults
        api_response = await api_instance.registrations_reset(account_id, id)
        print("The response of RegistrationsApi->registrations_reset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistrationsApi->registrations_reset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 

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
**0** | Lti::Registration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registrations_show**
> object registrations_show(account_id, id, include=include)

Show an LTI Registration

Return details about the specified LTI registration, including the
configuration and account binding.

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
    api_instance = canvas_lms_python_client.RegistrationsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id
    include = ['include_example'] # List[str] | Array of additional data to include. Always includes [account_binding configuration].  \"account_binding\":: the registration's binding to the given account \"configuration\":: the registration's Canvas-style tool configuration, without any overlays applied. \"overlaid_configuration\":: the registration's Canvas-style tool configuration, with all overlays applied. \"overlaid_legacy_configuration\":: the registration's legacy-style configuration, with all overlays applied. \"overlay\":: the registration's admin-defined configuration overlay \"overlay_versions\":: the registration's overlay's edit history (optional)

    try:
        # Show an LTI Registration
        api_response = await api_instance.registrations_show(account_id, id, include=include)
        print("The response of RegistrationsApi->registrations_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistrationsApi->registrations_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 
 **include** | [**List[str]**](str.md)| Array of additional data to include. Always includes [account_binding configuration].  \&quot;account_binding\&quot;:: the registration&#39;s binding to the given account \&quot;configuration\&quot;:: the registration&#39;s Canvas-style tool configuration, without any overlays applied. \&quot;overlaid_configuration\&quot;:: the registration&#39;s Canvas-style tool configuration, with all overlays applied. \&quot;overlaid_legacy_configuration\&quot;:: the registration&#39;s legacy-style configuration, with all overlays applied. \&quot;overlay\&quot;:: the registration&#39;s admin-defined configuration overlay \&quot;overlay_versions\&quot;:: the registration&#39;s overlay&#39;s edit history | [optional] 

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
**0** | Lti::Registration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registrations_show_by_client_id**
> object registrations_show_by_client_id(account_id, client_id)

Show an LTI Registration (via the client_id)

Returns details about the specified LTI registration, including the
configuration and account binding.

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
    api_instance = canvas_lms_python_client.RegistrationsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    client_id = 'client_id_example' # str | Scope response to client_id

    try:
        # Show an LTI Registration (via the client_id)
        api_response = await api_instance.registrations_show_by_client_id(account_id, client_id)
        print("The response of RegistrationsApi->registrations_show_by_client_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistrationsApi->registrations_show_by_client_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **client_id** | **str**| Scope response to client_id | 

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
**0** | Lti::Registration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registrations_show_by_utid**
> object registrations_show_by_utid(account_id, utid)

Get LTI Registration by Unified Tool ID

Returns an LTI registration by looking up its unified_tool_id.
Searches both manual configurations and IMS registrations.
Only returns registrations that are active and accessible from the
current account (owned by account, Site Admin, or has binding).

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
    api_instance = canvas_lms_python_client.RegistrationsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    utid = 'utid_example' # str | Scope response to utid

    try:
        # Get LTI Registration by Unified Tool ID
        api_response = await api_instance.registrations_show_by_utid(account_id, utid)
        print("The response of RegistrationsApi->registrations_show_by_utid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistrationsApi->registrations_show_by_utid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **utid** | **str**| Scope response to utid | 

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
**0** | Lti::Registration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registrations_show_registration_update_request**
> object registrations_show_registration_update_request(account_id, id, update_request_id)

Get LTI Registration Update Request

Retrieves details about a specific registration update request.

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
    api_instance = canvas_lms_python_client.RegistrationsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | The id of the registration.
    update_request_id = 'update_request_id_example' # str | The id of the registration update request to retrieve.

    try:
        # Get LTI Registration Update Request
        api_response = await api_instance.registrations_show_registration_update_request(account_id, id, update_request_id)
        print("The response of RegistrationsApi->registrations_show_registration_update_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistrationsApi->registrations_show_registration_update_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| The id of the registration. | 
 **update_request_id** | **str**| The id of the registration update request to retrieve. | 

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
**0** | Lti::RegistrationUpdateRequest |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registrations_unbind**
> object registrations_unbind(account_id, id)

Remove an Inherited LTI Registration

Deletes the account binding for this registration, effectively removing it from the account.

Only available when the lti_deactivate_registrations feature flag is enabled.
Only valid for inherited (Site Admin) registrations — use destroy for registrations owned by this account.

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
    api_instance = canvas_lms_python_client.RegistrationsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id

    try:
        # Remove an Inherited LTI Registration
        api_response = await api_instance.registrations_unbind(account_id, id)
        print("The response of RegistrationsApi->registrations_unbind:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistrationsApi->registrations_unbind: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 

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
**0** | Lti::RegistrationAccountBinding |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registrations_update**
> object registrations_update(account_id, id, registrations_update_request=registrations_update_request)

Update an LTI Registration

Update the specified LTI registration with the provided parameters. Note that updating the base tool configuration
of a registration that is associated with a Dynamic Registration will return a 422. All other fields can be updated
freely.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.registrations_update_request import RegistrationsUpdateRequest
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
    api_instance = canvas_lms_python_client.RegistrationsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id
    registrations_update_request = canvas_lms_python_client.RegistrationsUpdateRequest() # RegistrationsUpdateRequest | Request body parameters  **Example Request:** ``` This would update the specified LTI Registration, as well as its associated Developer Key and LTI Tool Configuration.  curl -X PUT 'https://<canvas>/api/v1/accounts/<account_id>/lti_registrations/<registration_id>' \\     -H \"Authorization: Bearer <token>\" \\     -H \"Content-Type: application/json\" \\     -d '{           \"vendor\": \"Example\",           \"name\": \"An Example Tool\",           \"admin_nickname\": \"A Great LTI Tool\",           \"configuration\": {             \"title\": \"Sample Tool\",             \"description\": \"A sample LTI tool\",             \"target_link_uri\": \"https://example.com/launch\",             \"oidc_initiation_url\": \"https://example.com/oidc\",             \"redirect_uris\": [\"https://example.com/redirect\"],             \"scopes\": [\"https://purl.imsglobal.org/spec/lti-ags/scope/lineitem\"],             \"placements\": [               {                 \"placement\": \"course_navigation\",                 \"enabled\": true               }             ],             \"launch_settings\": {}           }         }' ``` (optional)

    try:
        # Update an LTI Registration
        api_response = await api_instance.registrations_update(account_id, id, registrations_update_request=registrations_update_request)
        print("The response of RegistrationsApi->registrations_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistrationsApi->registrations_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 
 **registrations_update_request** | [**RegistrationsUpdateRequest**](RegistrationsUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; This would update the specified LTI Registration, as well as its associated Developer Key and LTI Tool Configuration.  curl -X PUT &#39;https://&lt;canvas&gt;/api/v1/accounts/&lt;account_id&gt;/lti_registrations/&lt;registration_id&gt;&#39; \\     -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; \\     -H \&quot;Content-Type: application/json\&quot; \\     -d &#39;{           \&quot;vendor\&quot;: \&quot;Example\&quot;,           \&quot;name\&quot;: \&quot;An Example Tool\&quot;,           \&quot;admin_nickname\&quot;: \&quot;A Great LTI Tool\&quot;,           \&quot;configuration\&quot;: {             \&quot;title\&quot;: \&quot;Sample Tool\&quot;,             \&quot;description\&quot;: \&quot;A sample LTI tool\&quot;,             \&quot;target_link_uri\&quot;: \&quot;https://example.com/launch\&quot;,             \&quot;oidc_initiation_url\&quot;: \&quot;https://example.com/oidc\&quot;,             \&quot;redirect_uris\&quot;: [\&quot;https://example.com/redirect\&quot;],             \&quot;scopes\&quot;: [\&quot;https://purl.imsglobal.org/spec/lti-ags/scope/lineitem\&quot;],             \&quot;placements\&quot;: [               {                 \&quot;placement\&quot;: \&quot;course_navigation\&quot;,                 \&quot;enabled\&quot;: true               }             ],             \&quot;launch_settings\&quot;: {}           }         }&#39; &#x60;&#x60;&#x60; | [optional] 

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
**0** | Lti::Registration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registrations_validate_lti_configuration**
> List[object] registrations_validate_lti_configuration(account_id, registrations_validate_lti_configuration_request=registrations_validate_lti_configuration_request)

Validate LtiConfiguration

Validates the provided LTI 1.3 JSON config against the LtiConfiguration schema,
and returns any errors found. Also transforms the JSON from LtiConfiguration
to InternalLtiConfiguration format before returning.
JSON config can be provided via url that points to an endpoint hosted by a tool,
or directly in the request body.
This is a utility endpoint for the LTI registration UI. Fetching tool config server-side
prevents CORS issues for the tool.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.registrations_validate_lti_configuration_request import RegistrationsValidateLtiConfigurationRequest
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
    api_instance = canvas_lms_python_client.RegistrationsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    registrations_validate_lti_configuration_request = canvas_lms_python_client.RegistrationsValidateLtiConfigurationRequest() # RegistrationsValidateLtiConfigurationRequest | Request body parameters  **Example Request:** ``` This would return the JSON in InternalLtiConfiguration format curl -X POST 'https://<canvas>/api/v1/accounts/<account_id>/lti_registrations/configuration/validate' \\      -d '{\"lti_configuration\": <LTI JSON config>}' \\      -H \"Content-Type: application/json\" \\      -H \"Authorization: Bearer <token>\" ``` (optional)

    try:
        # Validate LtiConfiguration
        api_response = await api_instance.registrations_validate_lti_configuration(account_id, registrations_validate_lti_configuration_request=registrations_validate_lti_configuration_request)
        print("The response of RegistrationsApi->registrations_validate_lti_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistrationsApi->registrations_validate_lti_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **registrations_validate_lti_configuration_request** | [**RegistrationsValidateLtiConfigurationRequest**](RegistrationsValidateLtiConfigurationRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; This would return the JSON in InternalLtiConfiguration format curl -X POST &#39;https://&lt;canvas&gt;/api/v1/accounts/&lt;account_id&gt;/lti_registrations/configuration/validate&#39; \\      -d &#39;{\&quot;lti_configuration\&quot;: &lt;LTI JSON config&gt;}&#39; \\      -H \&quot;Content-Type: application/json\&quot; \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; &#x60;&#x60;&#x60; | [optional] 

### Return type

**List[object]**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | | { errors: [String] } |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

