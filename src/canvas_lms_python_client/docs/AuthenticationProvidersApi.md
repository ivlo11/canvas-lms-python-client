# canvas_lms_python_client.AuthenticationProvidersApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authentication_providers_create**](AuthenticationProvidersApi.md#authentication_providers_create) | **POST** /api/v1/accounts/{account_id}/authentication_providers | Add authentication provider
[**authentication_providers_destroy**](AuthenticationProvidersApi.md#authentication_providers_destroy) | **DELETE** /api/v1/accounts/{account_id}/authentication_providers/{id} | Delete authentication provider
[**authentication_providers_index**](AuthenticationProvidersApi.md#authentication_providers_index) | **GET** /api/v1/accounts/{account_id}/authentication_providers | List authentication providers
[**authentication_providers_restore**](AuthenticationProvidersApi.md#authentication_providers_restore) | **PUT** /api/v1/accounts/{account_id}/authentication_providers/{id}/restore | Restore a deleted authentication provider
[**authentication_providers_show**](AuthenticationProvidersApi.md#authentication_providers_show) | **GET** /api/v1/accounts/{account_id}/authentication_providers/{id} | Get authentication provider
[**authentication_providers_show_sso_settings**](AuthenticationProvidersApi.md#authentication_providers_show_sso_settings) | **GET** /api/v1/accounts/{account_id}/sso_settings | Show account auth settings
[**authentication_providers_update**](AuthenticationProvidersApi.md#authentication_providers_update) | **PUT** /api/v1/accounts/{account_id}/authentication_providers/{id} | Update authentication provider
[**authentication_providers_update_sso_settings**](AuthenticationProvidersApi.md#authentication_providers_update_sso_settings) | **PUT** /api/v1/accounts/{account_id}/sso_settings | Update account auth settings


# **authentication_providers_create**
> AuthenticationProvider authentication_providers_create(account_id)

Add authentication provider

Add external authentication provider(s) for the account.
Services may be Apple, CAS, Facebook, GitHub, Google, LDAP, LinkedIn,
Microsoft, OpenID Connect, or SAML.

Each authentication provider is specified as a set of parameters as
described below. A provider specification must include an 'auth_type'
parameter with a value of 'apple', 'canvas', 'cas', 'clever', 'facebook',
'github', 'google', 'ldap', 'linkedin', 'microsoft', 'openid_connect',
or 'saml'. The other recognized parameters depend on this
auth_type; unrecognized parameters are discarded. Provider specifications
not specifying a valid auth_type are ignored.

You can set the 'position' for any provider. The config in the 1st position
is considered the default. You can set 'jit_provisioning' for any provider
besides Canvas. You can set 'mfa_required' for any provider.

For Apple, the additional recognized parameters are:

- client_id [Required]

  The developer’s client identifier, as provided by WWDR. Not available if
  configured globally for Canvas.

- login_attribute [Optional]

  The attribute to use to look up the user's login in Canvas. Either
  'sub' (the default), or 'email'

- federated_attributes [Optional]

  See FederatedAttributesConfig. Valid provider attributes are 'email',
  'firstName', 'lastName', and 'sub'.

For Canvas, the additional recognized parameter is:

- self_registration

  'all', 'none', or 'observer' - who is allowed to register as a new user

For CAS, the additional recognized parameters are:

- auth_base

  The CAS server's URL.

- log_in_url [Optional]

  An alternate SSO URL for logging into CAS. You probably should not set
  this.

For Clever, the additional recognized parameters are:

- client_id [Required]

  The Clever application's Client ID. Not available if configured globally
  for Canvas.

- client_secret [Required]

  The Clever application's Client Secret. Not available if configured
  globally for Canvas.

- district_id [Optional]

  A district's Clever ID. Leave this blank to let Clever handle the details
  with its District Picker. This is required for Clever Instant Login to
  work in a multi-tenant environment.

- login_attribute [Optional]

  The attribute to use to look up the user's login in Canvas. Either
  'id' (the default), 'sis_id', 'email', 'student_number', or
  'teacher_number'. Note that some fields may not be populated for
  all users at Clever.

- federated_attributes [Optional]

  See FederatedAttributesConfig. Valid provider attributes are 'id',
  'sis_id', 'email', 'student_number', and 'teacher_number'.

For Facebook, the additional recognized parameters are:

- app_id [Required]

  The Facebook App ID. Not available if configured globally for Canvas.

- app_secret [Required]

  The Facebook App Secret. Not available if configured globally for Canvas.

- login_attribute [Optional]

  The attribute to use to look up the user's login in Canvas. Either
  'id' (the default), or 'email'

- federated_attributes [Optional]

  See FederatedAttributesConfig. Valid provider attributes are 'email',
  'first_name', 'id', 'last_name', 'locale', and 'name'.

For GitHub, the additional recognized parameters are:

- domain [Optional]

  The domain of a GitHub Enterprise installation. I.e.
  github.mycompany.com. If not set, it will default to the public
  github.com.

- client_id [Required]

  The GitHub application's Client ID. Not available if configured globally
  for Canvas.

- client_secret [Required]

  The GitHub application's Client Secret. Not available if configured
  globally for Canvas.

- login_attribute [Optional]

  The attribute to use to look up the user's login in Canvas. Either
  'id' (the default), or 'login'

- federated_attributes [Optional]

  See FederatedAttributesConfig. Valid provider attributes are 'email',
  'id', 'login', and 'name'.

For Google, the additional recognized parameters are:

- client_id [Required]

  The Google application's Client ID. Not available if configured globally
  for Canvas.

- client_secret [Required]

  The Google application's Client Secret. Not available if configured
  globally for Canvas.

- hosted_domain [Optional]

  A Google Apps domain to restrict logins to. See
  https://developers.google.com/identity/protocols/OpenIDConnect?hl=en#hd-param

- login_attribute [Optional]

  The attribute to use to look up the user's login in Canvas. Either
  'sub' (the default), or 'email'

- federated_attributes [Optional]

  See FederatedAttributesConfig. Valid provider attributes are 'email',
  'family_name', 'given_name', 'locale', 'name', and 'sub'.

For LDAP, the additional recognized parameters are:

- auth_host

  The LDAP server's URL.

- auth_port [Optional, Integer]

  The LDAP server's TCP port. (default: 389)

- auth_over_tls [Optional]

  Whether to use TLS. Can be 'simple_tls', or 'start_tls'. For backwards
  compatibility, booleans are also accepted, with true meaning simple_tls.
  If not provided, it will default to start_tls.

- auth_base [Optional]

  A default treebase parameter for searches performed against the LDAP
  server.

- auth_filter

  LDAP search filter. Use !{{login}} as a placeholder for the username
  supplied by the user. For example: "(sAMAccountName=!{{login}})".

- identifier_format [Optional]

  The LDAP attribute to use to look up the Canvas login. Omit to use
  the username supplied by the user.

- auth_username

  Username

- auth_password

  Password

For LinkedIn, the additional recognized parameters are:

- client_id [Required]

  The LinkedIn application's Client ID. Not available if configured globally
  for Canvas.

- client_secret [Required]

  The LinkedIn application's Client Secret. Not available if configured
  globally for Canvas.

- login_attribute [Optional]

  The attribute to use to look up the user's login in Canvas. Either
  'id' (the default), or 'emailAddress'

- federated_attributes [Optional]

  See FederatedAttributesConfig. Valid provider attributes are 'emailAddress',
  'firstName', 'id', 'formattedName', and 'lastName'.

For Microsoft, the additional recognized parameters are:

- application_id [Required]

  The application's ID.

- application_secret [Required]

  The application's Client Secret (Password)

- tenant [Optional]

  See https://azure.microsoft.com/en-us/documentation/articles/active-directory-v2-protocols/
  Valid values are 'common', 'organizations', 'consumers', or an Azure Active Directory Tenant
  (as either a UUID or domain, such as contoso.onmicrosoft.com). Defaults to 'common'

- login_attribute [Optional]

  See https://azure.microsoft.com/en-us/documentation/articles/active-directory-v2-tokens/#idtokens
  Valid values are 'sub', 'email', 'oid', or 'preferred_username'. Note
  that email may not always be populated in the user's profile at
  Microsoft. Oid will not be populated for personal Microsoft accounts.
  Defaults to 'sub'

- federated_attributes [Optional]

  See FederatedAttributesConfig. Valid provider attributes are 'email',
  'name', 'preferred_username', 'oid', and 'sub'.

For OpenID Connect, the additional recognized parameters are:

- client_id [Required]

  The application's Client ID.

- client_secret [Required]

  The application's Client Secret.

- authorize_url [Required]

  The URL for getting starting the OAuth 2.0 web flow

- token_url [Required]

  The URL for exchanging the OAuth 2.0 authorization code for an Access
  Token and ID Token

- scope [Optional]

  Space separated additional scopes to request for the token. Note that
  you need not specify the 'openid' scope, or any scopes that can be
  automatically inferred by the rules defined at
  http://openid.net/specs/openid-connect-core-1_0.html#ScopeClaims

- end_session_endpoint [Optional]

  URL to send the end user to after logging out of Canvas. See
  https://openid.net/specs/openid-connect-session-1_0.html#RPLogout

- userinfo_endpoint [Optional]

  URL to request additional claims from. If the initial ID Token received
  from the provider cannot be used to satisfy the login_attribute and
  all federated_attributes, this endpoint will be queried for additional
  information.

- login_attribute [Optional]

  The attribute of the ID Token to look up the user's login in Canvas.
  Defaults to 'sub'.

- federated_attributes [Optional]

  See FederatedAttributesConfig. Any value is allowed for the provider
  attribute names, but standard claims are listed at
  http://openid.net/specs/openid-connect-core-1_0.html#StandardClaims

For SAML, the additional recognized parameters are:

- metadata [Optional]

  An XML document to parse as SAML metadata, and automatically populate idp_entity_id,
  log_in_url, log_out_url, certificate_fingerprint, and identifier_format

- metadata_uri [Optional]

  A URI to download the SAML metadata from, and automatically populate idp_entity_id,
  log_in_url, log_out_url, certificate_fingerprint, and identifier_format. This URI
  will also be saved, and the metadata periodically refreshed, automatically. If
  the metadata contains multiple entities, also supply idp_entity_id to distinguish
  which one you want (otherwise the only entity in the metadata will be inferred).
  If you provide the URI 'urn:mace:incommon' or 'http://ukfederation.org.uk',
  the InCommon or UK Access Management Federation metadata aggregate, respectively,
  will be used instead, and additional validation checks will happen (including
  validating that the metadata has been properly signed with the
  appropriate key).

- idp_entity_id

  The SAML IdP's entity ID

- log_in_url

  The SAML service's SSO target URL

- log_out_url [Optional]

  The SAML service's SLO target URL

- certificate_fingerprint

  The SAML service's certificate fingerprint.

- identifier_format

  The SAML service's identifier format. Must be one of:

  - urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress
  - urn:oasis:names:tc:SAML:2.0:nameid-format:entity
  - urn:oasis:names:tc:SAML:2.0:nameid-format:kerberos
  - urn:oasis:names:tc:SAML:2.0:nameid-format:persistent
  - urn:oasis:names:tc:SAML:2.0:nameid-format:transient
  - urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified
  - urn:oasis:names:tc:SAML:1.1:nameid-format:WindowsDomainQualifiedName
  - urn:oasis:names:tc:SAML:1.1:nameid-format:X509SubjectName

- requested_authn_context [Optional]

  The SAML AuthnContext

- sig_alg [Optional]

  If set, +AuthnRequest+, +LogoutRequest+, and +LogoutResponse+ messages
  are signed with the corresponding algorithm. Supported algorithms are:

  - {http://www.w3.org/2000/09/xmldsig#rsa-sha1}
  - {http://www.w3.org/2001/04/xmldsig-more#rsa-sha256}

  RSA-SHA1 and RSA-SHA256 are acceptable aliases.

- federated_attributes [Optional]

  See FederatedAttributesConfig. Any value is allowed for the provider attribute names.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.authentication_provider import AuthenticationProvider
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
    api_instance = canvas_lms_python_client.AuthenticationProvidersApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id

    try:
        # Add authentication provider
        api_response = await api_instance.authentication_providers_create(account_id)
        print("The response of AuthenticationProvidersApi->authentication_providers_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationProvidersApi->authentication_providers_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 

### Return type

[**AuthenticationProvider**](AuthenticationProvider.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | AuthenticationProvider |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authentication_providers_destroy**
> authentication_providers_destroy(account_id, id)

Delete authentication provider

Delete the config

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
    api_instance = canvas_lms_python_client.AuthenticationProvidersApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id

    try:
        # Delete authentication provider
        await api_instance.authentication_providers_destroy(account_id, id)
    except Exception as e:
        print("Exception when calling AuthenticationProvidersApi->authentication_providers_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Delete authentication provider |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authentication_providers_index**
> List[AuthenticationProvider] authentication_providers_index(account_id)

List authentication providers

Returns a paginated list of authentication providers

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.authentication_provider import AuthenticationProvider
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
    api_instance = canvas_lms_python_client.AuthenticationProvidersApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id

    try:
        # List authentication providers
        api_response = await api_instance.authentication_providers_index(account_id)
        print("The response of AuthenticationProvidersApi->authentication_providers_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationProvidersApi->authentication_providers_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 

### Return type

[**List[AuthenticationProvider]**](AuthenticationProvider.md)

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

# **authentication_providers_restore**
> AuthenticationProvider authentication_providers_restore(account_id, id)

Restore a deleted authentication provider

Restore an authentication provider back to active that was previously deleted. Only
available to admins who can manage_account_settings for given root account.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.authentication_provider import AuthenticationProvider
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
    api_instance = canvas_lms_python_client.AuthenticationProvidersApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id

    try:
        # Restore a deleted authentication provider
        api_response = await api_instance.authentication_providers_restore(account_id, id)
        print("The response of AuthenticationProvidersApi->authentication_providers_restore:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationProvidersApi->authentication_providers_restore: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**AuthenticationProvider**](AuthenticationProvider.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | AuthenticationProvider |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authentication_providers_show**
> AuthenticationProvider authentication_providers_show(account_id, id)

Get authentication provider

Get the specified authentication provider

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.authentication_provider import AuthenticationProvider
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
    api_instance = canvas_lms_python_client.AuthenticationProvidersApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id

    try:
        # Get authentication provider
        api_response = await api_instance.authentication_providers_show(account_id, id)
        print("The response of AuthenticationProvidersApi->authentication_providers_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationProvidersApi->authentication_providers_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**AuthenticationProvider**](AuthenticationProvider.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | AuthenticationProvider |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authentication_providers_show_sso_settings**
> SSOSettings authentication_providers_show_sso_settings(account_id)

Show account auth settings

The way to get the current state of each account level setting
that's relevant to Single Sign On configuration

You can list the current state of each setting with "update_sso_settings"

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.sso_settings import SSOSettings
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
    api_instance = canvas_lms_python_client.AuthenticationProvidersApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id

    try:
        # Show account auth settings
        api_response = await api_instance.authentication_providers_show_sso_settings(account_id)
        print("The response of AuthenticationProvidersApi->authentication_providers_show_sso_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationProvidersApi->authentication_providers_show_sso_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 

### Return type

[**SSOSettings**](SSOSettings.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | SSOSettings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authentication_providers_update**
> AuthenticationProvider authentication_providers_update(account_id, id)

Update authentication provider

Update an authentication provider using the same options as the
{api:AuthenticationProvidersController#create Add authentication provider} endpoint.
You cannot update an existing provider to a new authentication type.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.authentication_provider import AuthenticationProvider
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
    api_instance = canvas_lms_python_client.AuthenticationProvidersApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id

    try:
        # Update authentication provider
        api_response = await api_instance.authentication_providers_update(account_id, id)
        print("The response of AuthenticationProvidersApi->authentication_providers_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationProvidersApi->authentication_providers_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**AuthenticationProvider**](AuthenticationProvider.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | AuthenticationProvider |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authentication_providers_update_sso_settings**
> SSOSettings authentication_providers_update_sso_settings(account_id)

Update account auth settings

For various cases of mixed SSO configurations, you may need to set some
configuration at the account level to handle the particulars of your
setup.

This endpoint accepts a PUT request to set several possible account
settings. All setting are optional on each request, any that are not
provided at all are simply retained as is.  Any that provide the key but
a null-ish value (blank string, null, undefined) will be UN-set.

You can list the current state of each setting with "show_sso_settings"

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.sso_settings import SSOSettings
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
    api_instance = canvas_lms_python_client.AuthenticationProvidersApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id

    try:
        # Update account auth settings
        api_response = await api_instance.authentication_providers_update_sso_settings(account_id)
        print("The response of AuthenticationProvidersApi->authentication_providers_update_sso_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationProvidersApi->authentication_providers_update_sso_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 

### Return type

[**SSOSettings**](SSOSettings.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | SSOSettings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

