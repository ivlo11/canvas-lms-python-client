# canvas_lms_python_client.JwtsApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jwts_create**](JwtsApi.md#jwts_create) | **POST** /api/v1/jwts | Create JWT
[**jwts_refresh**](JwtsApi.md#jwts_refresh) | **POST** /api/v1/jwts/refresh | Refresh JWT


# **jwts_create**
> JWT jwts_create(jwts_create_request=jwts_create_request)

Create JWT

Create a unique JWT for use with other Canvas services

Generates a different JWT each time it's called. Each JWT expires
after a short window (1 hour)

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.jwt import JWT
from canvas_lms_python_client.models.jwts_create_request import JwtsCreateRequest
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
    api_instance = canvas_lms_python_client.JwtsApi(api_client)
    jwts_create_request = canvas_lms_python_client.JwtsCreateRequest() # JwtsCreateRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/jwts' \\       -X POST \\       -H \"Accept: application/json\" \\       -H 'Authorization: Bearer <token>' ``` (optional)

    try:
        # Create JWT
        api_response = await api_instance.jwts_create(jwts_create_request=jwts_create_request)
        print("The response of JwtsApi->jwts_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JwtsApi->jwts_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jwts_create_request** | [**JwtsCreateRequest**](JwtsCreateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/jwts&#39; \\       -X POST \\       -H \&quot;Accept: application/json\&quot; \\       -H &#39;Authorization: Bearer &lt;token&gt;&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**JWT**](JWT.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | JWT |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jwts_refresh**
> JWT jwts_refresh(jwts_refresh_request=jwts_refresh_request)

Refresh JWT

Refresh a JWT for use with other canvas services

Generates a different JWT each time it's called, each one expires
after a short window (1 hour).

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.jwt import JWT
from canvas_lms_python_client.models.jwts_refresh_request import JwtsRefreshRequest
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
    api_instance = canvas_lms_python_client.JwtsApi(api_client)
    jwts_refresh_request = canvas_lms_python_client.JwtsRefreshRequest() # JwtsRefreshRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/jwts/refresh' \\       -X POST \\       -H \"Accept: application/json\" \\       -H 'Authorization: Bearer <token>'       -d 'jwt=<jwt>' ``` (optional)

    try:
        # Refresh JWT
        api_response = await api_instance.jwts_refresh(jwts_refresh_request=jwts_refresh_request)
        print("The response of JwtsApi->jwts_refresh:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JwtsApi->jwts_refresh: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jwts_refresh_request** | [**JwtsRefreshRequest**](JwtsRefreshRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/jwts/refresh&#39; \\       -X POST \\       -H \&quot;Accept: application/json\&quot; \\       -H &#39;Authorization: Bearer &lt;token&gt;&#39;       -d &#39;jwt&#x3D;&lt;jwt&gt;&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**JWT**](JWT.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | JWT |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

