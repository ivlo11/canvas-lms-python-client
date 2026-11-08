# canvas_lms_python_client.ErrorsApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**errors_create**](ErrorsApi.md#errors_create) | **POST** /api/v1/error_reports | Create Error Report


# **errors_create**
> ErrorsCreateResponse errors_create(errors_create_request=errors_create_request)

Create Error Report

Create a new error report documenting an experienced problem

Performs the same action as when a user uses the "help -> report a problem"
dialog.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.errors_create_request import ErrorsCreateRequest
from canvas_lms_python_client.models.errors_create_response import ErrorsCreateResponse
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
    api_instance = canvas_lms_python_client.ErrorsApi(api_client)
    errors_create_request = canvas_lms_python_client.ErrorsCreateRequest() # ErrorsCreateRequest | Request body parameters  **Example Request:** ``` # Create error report curl 'https://<canvas>/api/v1/error_reports' \\       -X POST \\       -F 'error[subject]=\"things are broken\"' \\       -F 'error[url]=http://<canvas>/courses/1' \\       -F 'error[description]=\"All my thoughts on what I saw\"' \\       -H 'Authorization: Bearer <token>' ``` (optional)

    try:
        # Create Error Report
        api_response = await api_instance.errors_create(errors_create_request=errors_create_request)
        print("The response of ErrorsApi->errors_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ErrorsApi->errors_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **errors_create_request** | [**ErrorsCreateRequest**](ErrorsCreateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; # Create error report curl &#39;https://&lt;canvas&gt;/api/v1/error_reports&#39; \\       -X POST \\       -F &#39;error[subject]&#x3D;\&quot;things are broken\&quot;&#39; \\       -F &#39;error[url]&#x3D;http://&lt;canvas&gt;/courses/1&#39; \\       -F &#39;error[description]&#x3D;\&quot;All my thoughts on what I saw\&quot;&#39; \\       -H &#39;Authorization: Bearer &lt;token&gt;&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**ErrorsCreateResponse**](ErrorsCreateResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ErrorsCreateResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

