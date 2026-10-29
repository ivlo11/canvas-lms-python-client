# canvas_lms_python_client.ObserverPairingCodesApiApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**observer_pairing_codes_api_create**](ObserverPairingCodesApiApi.md#observer_pairing_codes_api_create) | **POST** /api/v1/users/{user_id}/observer_pairing_codes | Create observer pairing code


# **observer_pairing_codes_api_create**
> PairingCode observer_pairing_codes_api_create(user_id)

Create observer pairing code

If the user is a student, will generate a code to be used with self registration
or observees APIs to link another user to this student.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.pairing_code import PairingCode
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
    api_instance = canvas_lms_python_client.ObserverPairingCodesApiApi(api_client)
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # Create observer pairing code
        api_response = await api_instance.observer_pairing_codes_api_create(user_id)
        print("The response of ObserverPairingCodesApiApi->observer_pairing_codes_api_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObserverPairingCodesApiApi->observer_pairing_codes_api_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Scope response to user_id | 

### Return type

[**PairingCode**](PairingCode.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | PairingCode |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

