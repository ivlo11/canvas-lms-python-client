# canvas_lms_python_client.DiscoveryPagesApiApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**discovery_pages_api_show**](DiscoveryPagesApiApi.md#discovery_pages_api_show) | **GET** /api/v1/discovery_pages | Get Discovery Page
[**discovery_pages_api_token**](DiscoveryPagesApiApi.md#discovery_pages_api_token) | **POST** /api/v1/discovery_pages/token | Generate Discovery Page Preview Token
[**discovery_pages_api_upsert**](DiscoveryPagesApiApi.md#discovery_pages_api_upsert) | **PUT** /api/v1/discovery_pages | Update Discovery Page


# **discovery_pages_api_show**
> DiscoveryPage discovery_pages_api_show()

Get Discovery Page

Get the discovery page configuration for the domain root account.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.discovery_page import DiscoveryPage
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
    api_instance = canvas_lms_python_client.DiscoveryPagesApiApi(api_client)

    try:
        # Get Discovery Page
        api_response = await api_instance.discovery_pages_api_show()
        print("The response of DiscoveryPagesApiApi->discovery_pages_api_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscoveryPagesApiApi->discovery_pages_api_show: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DiscoveryPage**](DiscoveryPage.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | DiscoveryPage |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discovery_pages_api_token**
> List[object] discovery_pages_api_token(discovery_pages_api_token_request=discovery_pages_api_token_request)

Generate Discovery Page Preview Token

Returns a short-lived RS256-signed JWT containing the discovery page
button link configuration, suitable for sending to the identity service
preview iframe via postMessage.

A discovery_page configuration must be provided in the request body.
Omitting it returns a 400 Bad Request.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.discovery_pages_api_token_request import DiscoveryPagesApiTokenRequest
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
    api_instance = canvas_lms_python_client.DiscoveryPagesApiApi(api_client)
    discovery_pages_api_token_request = canvas_lms_python_client.DiscoveryPagesApiTokenRequest() # DiscoveryPagesApiTokenRequest | Request body parameters  **Example Request:** ``` curl -X POST 'https://<canvas>/api/v1/discovery_pages/token' \\   -H 'Authorization: Bearer <token>' \\   -H 'Content-Type: application/json' \\   -d '{     \"discovery_page\": {       \"primary\": [         {           \"authentication_provider_id\": 1,           \"label\": \"Students\",           \"icon\": \"google\"         }       ],       \"secondary\": []     }   }' ``` (optional)

    try:
        # Generate Discovery Page Preview Token
        api_response = await api_instance.discovery_pages_api_token(discovery_pages_api_token_request=discovery_pages_api_token_request)
        print("The response of DiscoveryPagesApiApi->discovery_pages_api_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscoveryPagesApiApi->discovery_pages_api_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **discovery_pages_api_token_request** | [**DiscoveryPagesApiTokenRequest**](DiscoveryPagesApiTokenRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl -X POST &#39;https://&lt;canvas&gt;/api/v1/discovery_pages/token&#39; \\   -H &#39;Authorization: Bearer &lt;token&gt;&#39; \\   -H &#39;Content-Type: application/json&#39; \\   -d &#39;{     \&quot;discovery_page\&quot;: {       \&quot;primary\&quot;: [         {           \&quot;authentication_provider_id\&quot;: 1,           \&quot;label\&quot;: \&quot;Students\&quot;,           \&quot;icon\&quot;: \&quot;google\&quot;         }       ],       \&quot;secondary\&quot;: []     }   }&#39; &#x60;&#x60;&#x60; | [optional] 

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
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discovery_pages_api_upsert**
> DiscoveryPage discovery_pages_api_upsert(discovery_pages_api_upsert_request=discovery_pages_api_upsert_request)

Update Discovery Page

Update or create the discovery page configuration for the domain root account.
This is a full replacement - provide the complete configuration including
primary, secondary, and active fields. Any fields omitted will be removed.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.discovery_page import DiscoveryPage
from canvas_lms_python_client.models.discovery_pages_api_upsert_request import DiscoveryPagesApiUpsertRequest
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
    api_instance = canvas_lms_python_client.DiscoveryPagesApiApi(api_client)
    discovery_pages_api_upsert_request = canvas_lms_python_client.DiscoveryPagesApiUpsertRequest() # DiscoveryPagesApiUpsertRequest | Request body parameters  **Example Request:** ``` curl -X PUT 'https://<canvas>/api/v1/discovery_pages' \\   -H 'Authorization: Bearer <token>' \\   -H 'Content-Type: application/json' \\   -d '{     \"discovery_page\": {       \"primary\": [         {           \"authentication_provider_id\": 1,           \"label\": \"Students\",           \"icon\": \"google\"         },         {           \"authentication_provider_id\": 2,           \"label\": \"Faculty\",           \"icon\": \"okta\"         }       ],       \"secondary\": [         {           \"authentication_provider_id\": 3,           \"label\": \"Admins\"         }       ],       \"active\": true     }   }' ``` (optional)

    try:
        # Update Discovery Page
        api_response = await api_instance.discovery_pages_api_upsert(discovery_pages_api_upsert_request=discovery_pages_api_upsert_request)
        print("The response of DiscoveryPagesApiApi->discovery_pages_api_upsert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscoveryPagesApiApi->discovery_pages_api_upsert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **discovery_pages_api_upsert_request** | [**DiscoveryPagesApiUpsertRequest**](DiscoveryPagesApiUpsertRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl -X PUT &#39;https://&lt;canvas&gt;/api/v1/discovery_pages&#39; \\   -H &#39;Authorization: Bearer &lt;token&gt;&#39; \\   -H &#39;Content-Type: application/json&#39; \\   -d &#39;{     \&quot;discovery_page\&quot;: {       \&quot;primary\&quot;: [         {           \&quot;authentication_provider_id\&quot;: 1,           \&quot;label\&quot;: \&quot;Students\&quot;,           \&quot;icon\&quot;: \&quot;google\&quot;         },         {           \&quot;authentication_provider_id\&quot;: 2,           \&quot;label\&quot;: \&quot;Faculty\&quot;,           \&quot;icon\&quot;: \&quot;okta\&quot;         }       ],       \&quot;secondary\&quot;: [         {           \&quot;authentication_provider_id\&quot;: 3,           \&quot;label\&quot;: \&quot;Admins\&quot;         }       ],       \&quot;active\&quot;: true     }   }&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**DiscoveryPage**](DiscoveryPage.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | DiscoveryPage |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

