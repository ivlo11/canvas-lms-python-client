# canvas_lms_python_client.BrandConfigsApiApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**brand_configs_api_show**](BrandConfigsApiApi.md#brand_configs_api_show) | **GET** /api/v1/brand_variables | Get the brand config variables that should be used for this domain
[**brand_configs_api_show_context**](BrandConfigsApiApi.md#brand_configs_api_show_context) | **GET** /api/v1/accounts/{account_id}/brand_variables | Get the brand config variables for a sub-account or course
[**brand_configs_api_show_context_for_courses**](BrandConfigsApiApi.md#brand_configs_api_show_context_for_courses) | **GET** /api/v1/courses/{course_id}/brand_variables | Get the brand config variables for a sub-account or course


# **brand_configs_api_show**
> BrandConfigsShowResponse brand_configs_api_show()

Get the brand config variables that should be used for this domain

Will redirect to a static json file that has all of the brand
variables used by this account. Even though this is a redirect,
do not store the redirected url since if the account makes any changes
it will redirect to a new url. Needs no authentication.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.brand_configs_show_response import BrandConfigsShowResponse
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
    api_instance = canvas_lms_python_client.BrandConfigsApiApi(api_client)

    try:
        # Get the brand config variables that should be used for this domain
        api_response = await api_instance.brand_configs_api_show()
        print("The response of BrandConfigsApiApi->brand_configs_api_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrandConfigsApiApi->brand_configs_api_show: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BrandConfigsShowResponse**](BrandConfigsShowResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | BrandConfigsShowResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **brand_configs_api_show_context**
> BrandConfigsShowResponse brand_configs_api_show_context(account_id)

Get the brand config variables for a sub-account or course

Will redirect to a static json file that has all of the brand
variables used by the provided context. Even though this is a redirect,
do not store the redirected url since if the sub-account makes any changes
it will redirect to a new url.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.brand_configs_show_response import BrandConfigsShowResponse
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
    api_instance = canvas_lms_python_client.BrandConfigsApiApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id

    try:
        # Get the brand config variables for a sub-account or course
        api_response = await api_instance.brand_configs_api_show_context(account_id)
        print("The response of BrandConfigsApiApi->brand_configs_api_show_context:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrandConfigsApiApi->brand_configs_api_show_context: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 

### Return type

[**BrandConfigsShowResponse**](BrandConfigsShowResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | BrandConfigsShowResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **brand_configs_api_show_context_for_courses**
> BrandConfigsShowResponse brand_configs_api_show_context_for_courses(course_id)

Get the brand config variables for a sub-account or course

Will redirect to a static json file that has all of the brand
variables used by the provided context. Even though this is a redirect,
do not store the redirected url since if the sub-account makes any changes
it will redirect to a new url.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.brand_configs_show_response import BrandConfigsShowResponse
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
    api_instance = canvas_lms_python_client.BrandConfigsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id

    try:
        # Get the brand config variables for a sub-account or course
        api_response = await api_instance.brand_configs_api_show_context_for_courses(course_id)
        print("The response of BrandConfigsApiApi->brand_configs_api_show_context_for_courses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrandConfigsApiApi->brand_configs_api_show_context_for_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 

### Return type

[**BrandConfigsShowResponse**](BrandConfigsShowResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | BrandConfigsShowResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

