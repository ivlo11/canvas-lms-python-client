# canvas_lms_python_client.ServicesApiApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**services_api_show_kaltura_config**](ServicesApiApi.md#services_api_show_kaltura_config) | **GET** /api/v1/services/kaltura | Get Kaltura config
[**services_api_start_kaltura_session**](ServicesApiApi.md#services_api_start_kaltura_session) | **POST** /api/v1/services/kaltura_session | Start Kaltura session


# **services_api_show_kaltura_config**
> ServicesShowKalturaConfigResponse services_api_show_kaltura_config()

Get Kaltura config

Return the config information for the Kaltura plugin in json format.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.services_show_kaltura_config_response import ServicesShowKalturaConfigResponse
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
    api_instance = canvas_lms_python_client.ServicesApiApi(api_client)

    try:
        # Get Kaltura config
        api_response = await api_instance.services_api_show_kaltura_config()
        print("The response of ServicesApiApi->services_api_show_kaltura_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApiApi->services_api_show_kaltura_config: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ServicesShowKalturaConfigResponse**](ServicesShowKalturaConfigResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ServicesShowKalturaConfigResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **services_api_start_kaltura_session**
> ServicesStartKalturaSessionResponse services_api_start_kaltura_session()

Start Kaltura session

Start a new Kaltura session, so that new media can be recorded and uploaded
to this Canvas instance's Kaltura instance.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.services_start_kaltura_session_response import ServicesStartKalturaSessionResponse
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
    api_instance = canvas_lms_python_client.ServicesApiApi(api_client)

    try:
        # Start Kaltura session
        api_response = await api_instance.services_api_start_kaltura_session()
        print("The response of ServicesApiApi->services_api_start_kaltura_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApiApi->services_api_start_kaltura_session: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ServicesStartKalturaSessionResponse**](ServicesStartKalturaSessionResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ServicesStartKalturaSessionResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

