# canvas_lms_python_client.FeatureFlagsApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**feature_flags_delete**](FeatureFlagsApi.md#feature_flags_delete) | **DELETE** /api/v1/courses/{course_id}/features/flags/{feature} | Remove feature flag
[**feature_flags_delete_for_accounts**](FeatureFlagsApi.md#feature_flags_delete_for_accounts) | **DELETE** /api/v1/accounts/{account_id}/features/flags/{feature} | Remove feature flag
[**feature_flags_delete_for_users**](FeatureFlagsApi.md#feature_flags_delete_for_users) | **DELETE** /api/v1/users/{user_id}/features/flags/{feature} | Remove feature flag
[**feature_flags_enabled_features**](FeatureFlagsApi.md#feature_flags_enabled_features) | **GET** /api/v1/courses/{course_id}/features/enabled | List enabled features
[**feature_flags_enabled_features_for_accounts**](FeatureFlagsApi.md#feature_flags_enabled_features_for_accounts) | **GET** /api/v1/accounts/{account_id}/features/enabled | List enabled features
[**feature_flags_enabled_features_for_users**](FeatureFlagsApi.md#feature_flags_enabled_features_for_users) | **GET** /api/v1/users/{user_id}/features/enabled | List enabled features
[**feature_flags_environment**](FeatureFlagsApi.md#feature_flags_environment) | **GET** /api/v1/features/environment | List environment features
[**feature_flags_index**](FeatureFlagsApi.md#feature_flags_index) | **GET** /api/v1/courses/{course_id}/features | List features
[**feature_flags_index_for_accounts**](FeatureFlagsApi.md#feature_flags_index_for_accounts) | **GET** /api/v1/accounts/{account_id}/features | List features
[**feature_flags_index_for_users**](FeatureFlagsApi.md#feature_flags_index_for_users) | **GET** /api/v1/users/{user_id}/features | List features
[**feature_flags_show**](FeatureFlagsApi.md#feature_flags_show) | **GET** /api/v1/courses/{course_id}/features/flags/{feature} | Get feature flag
[**feature_flags_show_for_accounts**](FeatureFlagsApi.md#feature_flags_show_for_accounts) | **GET** /api/v1/accounts/{account_id}/features/flags/{feature} | Get feature flag
[**feature_flags_show_for_users**](FeatureFlagsApi.md#feature_flags_show_for_users) | **GET** /api/v1/users/{user_id}/features/flags/{feature} | Get feature flag
[**feature_flags_update**](FeatureFlagsApi.md#feature_flags_update) | **PUT** /api/v1/courses/{course_id}/features/flags/{feature} | Set feature flag
[**feature_flags_update_for_accounts**](FeatureFlagsApi.md#feature_flags_update_for_accounts) | **PUT** /api/v1/accounts/{account_id}/features/flags/{feature} | Set feature flag
[**feature_flags_update_for_users**](FeatureFlagsApi.md#feature_flags_update_for_users) | **PUT** /api/v1/users/{user_id}/features/flags/{feature} | Set feature flag


# **feature_flags_delete**
> FeatureFlag feature_flags_delete(course_id, feature)

Remove feature flag

Remove feature flag for a given Account, Course, or User.  (Note that the flag must
be defined on the Account, Course, or User directly.)  The object will then inherit
the feature flags from a higher account, if any exist.  If this flag was 'on' or 'off',
then lower-level account flags that were masked by this one will apply again.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.feature_flag import FeatureFlag
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
    api_instance = canvas_lms_python_client.FeatureFlagsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    feature = 'feature_example' # str | Scope response to feature

    try:
        # Remove feature flag
        api_response = await api_instance.feature_flags_delete(course_id, feature)
        print("The response of FeatureFlagsApi->feature_flags_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeatureFlagsApi->feature_flags_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **feature** | **str**| Scope response to feature | 

### Return type

[**FeatureFlag**](FeatureFlag.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | FeatureFlag |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **feature_flags_delete_for_accounts**
> FeatureFlag feature_flags_delete_for_accounts(account_id, feature)

Remove feature flag

Remove feature flag for a given Account, Course, or User.  (Note that the flag must
be defined on the Account, Course, or User directly.)  The object will then inherit
the feature flags from a higher account, if any exist.  If this flag was 'on' or 'off',
then lower-level account flags that were masked by this one will apply again.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.feature_flag import FeatureFlag
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
    api_instance = canvas_lms_python_client.FeatureFlagsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    feature = 'feature_example' # str | Scope response to feature

    try:
        # Remove feature flag
        api_response = await api_instance.feature_flags_delete_for_accounts(account_id, feature)
        print("The response of FeatureFlagsApi->feature_flags_delete_for_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeatureFlagsApi->feature_flags_delete_for_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **feature** | **str**| Scope response to feature | 

### Return type

[**FeatureFlag**](FeatureFlag.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | FeatureFlag |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **feature_flags_delete_for_users**
> FeatureFlag feature_flags_delete_for_users(feature, user_id)

Remove feature flag

Remove feature flag for a given Account, Course, or User.  (Note that the flag must
be defined on the Account, Course, or User directly.)  The object will then inherit
the feature flags from a higher account, if any exist.  If this flag was 'on' or 'off',
then lower-level account flags that were masked by this one will apply again.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.feature_flag import FeatureFlag
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
    api_instance = canvas_lms_python_client.FeatureFlagsApi(api_client)
    feature = 'feature_example' # str | Scope response to feature
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # Remove feature flag
        api_response = await api_instance.feature_flags_delete_for_users(feature, user_id)
        print("The response of FeatureFlagsApi->feature_flags_delete_for_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeatureFlagsApi->feature_flags_delete_for_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature** | **str**| Scope response to feature | 
 **user_id** | **str**| Scope response to user_id | 

### Return type

[**FeatureFlag**](FeatureFlag.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | FeatureFlag |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **feature_flags_enabled_features**
> feature_flags_enabled_features(course_id)

List enabled features

A paginated list of all features that are enabled on a given Account, Course, or User.
Only the feature names are returned.

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
    api_instance = canvas_lms_python_client.FeatureFlagsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id

    try:
        # List enabled features
        await api_instance.feature_flags_enabled_features(course_id)
    except Exception as e:
        print("Exception when calling FeatureFlagsApi->feature_flags_enabled_features: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | List enabled features |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **feature_flags_enabled_features_for_accounts**
> feature_flags_enabled_features_for_accounts(account_id)

List enabled features

A paginated list of all features that are enabled on a given Account, Course, or User.
Only the feature names are returned.

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
    api_instance = canvas_lms_python_client.FeatureFlagsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id

    try:
        # List enabled features
        await api_instance.feature_flags_enabled_features_for_accounts(account_id)
    except Exception as e:
        print("Exception when calling FeatureFlagsApi->feature_flags_enabled_features_for_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | List enabled features |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **feature_flags_enabled_features_for_users**
> feature_flags_enabled_features_for_users(user_id)

List enabled features

A paginated list of all features that are enabled on a given Account, Course, or User.
Only the feature names are returned.

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
    api_instance = canvas_lms_python_client.FeatureFlagsApi(api_client)
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # List enabled features
        await api_instance.feature_flags_enabled_features_for_users(user_id)
    except Exception as e:
        print("Exception when calling FeatureFlagsApi->feature_flags_enabled_features_for_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Scope response to user_id | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | List enabled features |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **feature_flags_environment**
> feature_flags_environment()

List environment features

Return a hash of global feature options that pertain to the
Canvas user interface. This is the same information supplied to the
web interface as +ENV.FEATURES+.

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
    api_instance = canvas_lms_python_client.FeatureFlagsApi(api_client)

    try:
        # List environment features
        await api_instance.feature_flags_environment()
    except Exception as e:
        print("Exception when calling FeatureFlagsApi->feature_flags_environment: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | List environment features |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **feature_flags_index**
> List[Feature] feature_flags_index(course_id, hide_inherited_enabled=hide_inherited_enabled, page=page, per_page=per_page)

List features

A paginated list of all features that apply to a given Account, Course, or User.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.feature import Feature
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
    api_instance = canvas_lms_python_client.FeatureFlagsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    hide_inherited_enabled = True # bool | When true, feature flags that are enabled in a higher context and cannot be overridden will be omitted. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List features
        api_response = await api_instance.feature_flags_index(course_id, hide_inherited_enabled=hide_inherited_enabled, page=page, per_page=per_page)
        print("The response of FeatureFlagsApi->feature_flags_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeatureFlagsApi->feature_flags_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **hide_inherited_enabled** | **bool**| When true, feature flags that are enabled in a higher context and cannot be overridden will be omitted. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[Feature]**](Feature.md)

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

# **feature_flags_index_for_accounts**
> List[Feature] feature_flags_index_for_accounts(account_id, hide_inherited_enabled=hide_inherited_enabled, page=page, per_page=per_page)

List features

A paginated list of all features that apply to a given Account, Course, or User.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.feature import Feature
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
    api_instance = canvas_lms_python_client.FeatureFlagsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    hide_inherited_enabled = True # bool | When true, feature flags that are enabled in a higher context and cannot be overridden will be omitted. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List features
        api_response = await api_instance.feature_flags_index_for_accounts(account_id, hide_inherited_enabled=hide_inherited_enabled, page=page, per_page=per_page)
        print("The response of FeatureFlagsApi->feature_flags_index_for_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeatureFlagsApi->feature_flags_index_for_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **hide_inherited_enabled** | **bool**| When true, feature flags that are enabled in a higher context and cannot be overridden will be omitted. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[Feature]**](Feature.md)

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

# **feature_flags_index_for_users**
> List[Feature] feature_flags_index_for_users(user_id, hide_inherited_enabled=hide_inherited_enabled, page=page, per_page=per_page)

List features

A paginated list of all features that apply to a given Account, Course, or User.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.feature import Feature
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
    api_instance = canvas_lms_python_client.FeatureFlagsApi(api_client)
    user_id = 'user_id_example' # str | Scope response to user_id
    hide_inherited_enabled = True # bool | When true, feature flags that are enabled in a higher context and cannot be overridden will be omitted. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List features
        api_response = await api_instance.feature_flags_index_for_users(user_id, hide_inherited_enabled=hide_inherited_enabled, page=page, per_page=per_page)
        print("The response of FeatureFlagsApi->feature_flags_index_for_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeatureFlagsApi->feature_flags_index_for_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Scope response to user_id | 
 **hide_inherited_enabled** | **bool**| When true, feature flags that are enabled in a higher context and cannot be overridden will be omitted. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[Feature]**](Feature.md)

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

# **feature_flags_show**
> FeatureFlag feature_flags_show(course_id, feature)

Get feature flag

Get the feature flag that applies to a given Account, Course, or User.
The flag may be defined on the object, or it may be inherited from a parent
account. You can look at the context_id and context_type of the returned object
to determine which is the case. If these fields are missing, then the object
is the global Canvas default.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.feature_flag import FeatureFlag
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
    api_instance = canvas_lms_python_client.FeatureFlagsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    feature = 'feature_example' # str | Scope response to feature

    try:
        # Get feature flag
        api_response = await api_instance.feature_flags_show(course_id, feature)
        print("The response of FeatureFlagsApi->feature_flags_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeatureFlagsApi->feature_flags_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **feature** | **str**| Scope response to feature | 

### Return type

[**FeatureFlag**](FeatureFlag.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | FeatureFlag |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **feature_flags_show_for_accounts**
> FeatureFlag feature_flags_show_for_accounts(account_id, feature)

Get feature flag

Get the feature flag that applies to a given Account, Course, or User.
The flag may be defined on the object, or it may be inherited from a parent
account. You can look at the context_id and context_type of the returned object
to determine which is the case. If these fields are missing, then the object
is the global Canvas default.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.feature_flag import FeatureFlag
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
    api_instance = canvas_lms_python_client.FeatureFlagsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    feature = 'feature_example' # str | Scope response to feature

    try:
        # Get feature flag
        api_response = await api_instance.feature_flags_show_for_accounts(account_id, feature)
        print("The response of FeatureFlagsApi->feature_flags_show_for_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeatureFlagsApi->feature_flags_show_for_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **feature** | **str**| Scope response to feature | 

### Return type

[**FeatureFlag**](FeatureFlag.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | FeatureFlag |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **feature_flags_show_for_users**
> FeatureFlag feature_flags_show_for_users(feature, user_id)

Get feature flag

Get the feature flag that applies to a given Account, Course, or User.
The flag may be defined on the object, or it may be inherited from a parent
account. You can look at the context_id and context_type of the returned object
to determine which is the case. If these fields are missing, then the object
is the global Canvas default.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.feature_flag import FeatureFlag
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
    api_instance = canvas_lms_python_client.FeatureFlagsApi(api_client)
    feature = 'feature_example' # str | Scope response to feature
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # Get feature flag
        api_response = await api_instance.feature_flags_show_for_users(feature, user_id)
        print("The response of FeatureFlagsApi->feature_flags_show_for_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeatureFlagsApi->feature_flags_show_for_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature** | **str**| Scope response to feature | 
 **user_id** | **str**| Scope response to user_id | 

### Return type

[**FeatureFlag**](FeatureFlag.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | FeatureFlag |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **feature_flags_update**
> FeatureFlag feature_flags_update(course_id, feature, feature_flags_update_request=feature_flags_update_request)

Set feature flag

Set a feature flag for a given Account, Course, or User. This call will fail if a parent account sets
a feature flag for the same feature in any state other than "allowed".

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.feature_flag import FeatureFlag
from canvas_lms_python_client.models.feature_flags_update_request import FeatureFlagsUpdateRequest
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
    api_instance = canvas_lms_python_client.FeatureFlagsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    feature = 'feature_example' # str | Scope response to feature
    feature_flags_update_request = canvas_lms_python_client.FeatureFlagsUpdateRequest() # FeatureFlagsUpdateRequest | Request body parameters  **Example Request:** ``` curl -X PUT 'http://<canvas>/api/v1/courses/1/features/flags/fancy_wickets' \\   -H \"Authorization: Bearer \" \\   -F \"state=on\" ``` (optional)

    try:
        # Set feature flag
        api_response = await api_instance.feature_flags_update(course_id, feature, feature_flags_update_request=feature_flags_update_request)
        print("The response of FeatureFlagsApi->feature_flags_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeatureFlagsApi->feature_flags_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **feature** | **str**| Scope response to feature | 
 **feature_flags_update_request** | [**FeatureFlagsUpdateRequest**](FeatureFlagsUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl -X PUT &#39;http://&lt;canvas&gt;/api/v1/courses/1/features/flags/fancy_wickets&#39; \\   -H \&quot;Authorization: Bearer \&quot; \\   -F \&quot;state&#x3D;on\&quot; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**FeatureFlag**](FeatureFlag.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | FeatureFlag |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **feature_flags_update_for_accounts**
> FeatureFlag feature_flags_update_for_accounts(account_id, feature, feature_flags_update_request=feature_flags_update_request)

Set feature flag

Set a feature flag for a given Account, Course, or User. This call will fail if a parent account sets
a feature flag for the same feature in any state other than "allowed".

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.feature_flag import FeatureFlag
from canvas_lms_python_client.models.feature_flags_update_request import FeatureFlagsUpdateRequest
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
    api_instance = canvas_lms_python_client.FeatureFlagsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    feature = 'feature_example' # str | Scope response to feature
    feature_flags_update_request = canvas_lms_python_client.FeatureFlagsUpdateRequest() # FeatureFlagsUpdateRequest | Request body parameters  **Example Request:** ``` curl -X PUT 'http://<canvas>/api/v1/courses/1/features/flags/fancy_wickets' \\   -H \"Authorization: Bearer \" \\   -F \"state=on\" ``` (optional)

    try:
        # Set feature flag
        api_response = await api_instance.feature_flags_update_for_accounts(account_id, feature, feature_flags_update_request=feature_flags_update_request)
        print("The response of FeatureFlagsApi->feature_flags_update_for_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeatureFlagsApi->feature_flags_update_for_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **feature** | **str**| Scope response to feature | 
 **feature_flags_update_request** | [**FeatureFlagsUpdateRequest**](FeatureFlagsUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl -X PUT &#39;http://&lt;canvas&gt;/api/v1/courses/1/features/flags/fancy_wickets&#39; \\   -H \&quot;Authorization: Bearer \&quot; \\   -F \&quot;state&#x3D;on\&quot; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**FeatureFlag**](FeatureFlag.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | FeatureFlag |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **feature_flags_update_for_users**
> FeatureFlag feature_flags_update_for_users(feature, user_id, feature_flags_update_request=feature_flags_update_request)

Set feature flag

Set a feature flag for a given Account, Course, or User. This call will fail if a parent account sets
a feature flag for the same feature in any state other than "allowed".

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.feature_flag import FeatureFlag
from canvas_lms_python_client.models.feature_flags_update_request import FeatureFlagsUpdateRequest
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
    api_instance = canvas_lms_python_client.FeatureFlagsApi(api_client)
    feature = 'feature_example' # str | Scope response to feature
    user_id = 'user_id_example' # str | Scope response to user_id
    feature_flags_update_request = canvas_lms_python_client.FeatureFlagsUpdateRequest() # FeatureFlagsUpdateRequest | Request body parameters  **Example Request:** ``` curl -X PUT 'http://<canvas>/api/v1/courses/1/features/flags/fancy_wickets' \\   -H \"Authorization: Bearer \" \\   -F \"state=on\" ``` (optional)

    try:
        # Set feature flag
        api_response = await api_instance.feature_flags_update_for_users(feature, user_id, feature_flags_update_request=feature_flags_update_request)
        print("The response of FeatureFlagsApi->feature_flags_update_for_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeatureFlagsApi->feature_flags_update_for_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature** | **str**| Scope response to feature | 
 **user_id** | **str**| Scope response to user_id | 
 **feature_flags_update_request** | [**FeatureFlagsUpdateRequest**](FeatureFlagsUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl -X PUT &#39;http://&lt;canvas&gt;/api/v1/courses/1/features/flags/fancy_wickets&#39; \\   -H \&quot;Authorization: Bearer \&quot; \\   -F \&quot;state&#x3D;on\&quot; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**FeatureFlag**](FeatureFlag.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | FeatureFlag |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

