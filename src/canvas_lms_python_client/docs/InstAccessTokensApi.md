# canvas_lms_python_client.InstAccessTokensApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**inst_access_tokens_create**](InstAccessTokensApi.md#inst_access_tokens_create) | **POST** /api/v1/inst_access_tokens | Create InstAccess token


# **inst_access_tokens_create**
> InstAccessToken inst_access_tokens_create()

Create InstAccess token

Create a unique, encrypted InstAccess token.

Generates a different InstAccess token each time it's called, each one expires
after a short window (1 hour).

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.inst_access_token import InstAccessToken
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
    api_instance = canvas_lms_python_client.InstAccessTokensApi(api_client)

    try:
        # Create InstAccess token
        api_response = await api_instance.inst_access_tokens_create()
        print("The response of InstAccessTokensApi->inst_access_tokens_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstAccessTokensApi->inst_access_tokens_create: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InstAccessToken**](InstAccessToken.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | InstAccessToken |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

