# canvas_lms_python_client.PlagiarismPlatformApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**plagiarism_platform_add_service**](PlagiarismPlatformApi.md#plagiarism_platform_add_service) | **GET** /api/v1/support_helpers/plagiarism_platform/add_service | Add Tool Service
[**plagiarism_platform_resubmit_for_assignment**](PlagiarismPlatformApi.md#plagiarism_platform_resubmit_for_assignment) | **GET** /api/v1/support_helpers/plagiarism_platform/resubmit_for_assignment/{assignment_id} | Resubmit All Submissions to Tool


# **plagiarism_platform_add_service**
> plagiarism_platform_add_service(product_code=product_code, vendor_code=vendor_code, service=service, actions=actions)

Add Tool Service

Add a service to the security contracts of all tool proxies
with the provided vendor/product codes.

Example Request:
http://canvas.docker/api/v1/support_helpers/plagiarism_platform/add_service?
  product_code=similarity%20detection%20reference%20tool
  &vendor_code=Instructure.com
  &service=vnd.Canvas.webhooksSubscription
  &actions[]=POST&actions[]=GET

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
    api_instance = canvas_lms_python_client.PlagiarismPlatformApi(api_client)
    product_code = 'product_code_example' # str | The product code of the tool proxies to modify (optional)
    vendor_code = 'vendor_code_example' # str | The vendor code of the tool proxies to modify (optional)
    service = 'service_example' # str | The case-sensitive service name (optional)
    actions = ['actions_example'] # List[str] | The actions ('GET', 'POST', 'GET', 'PUT', or 'Delete') the tool should be authorized to use with the service (optional)

    try:
        # Add Tool Service
        await api_instance.plagiarism_platform_add_service(product_code=product_code, vendor_code=vendor_code, service=service, actions=actions)
    except Exception as e:
        print("Exception when calling PlagiarismPlatformApi->plagiarism_platform_add_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_code** | **str**| The product code of the tool proxies to modify | [optional] 
 **vendor_code** | **str**| The vendor code of the tool proxies to modify | [optional] 
 **service** | **str**| The case-sensitive service name | [optional] 
 **actions** | [**List[str]**](str.md)| The actions (&#39;GET&#39;, &#39;POST&#39;, &#39;GET&#39;, &#39;PUT&#39;, or &#39;Delete&#39;) the tool should be authorized to use with the service | [optional] 

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
**0** | Add Tool Service |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plagiarism_platform_resubmit_for_assignment**
> plagiarism_platform_resubmit_for_assignment(assignment_id)

Resubmit All Submissions to Tool

Resends a 'plagiarism_resubmit' webhook for each submission
in the specified assignment

Example Request:
http://canvas.docker/api/v1/support_helpers/plagiarism_platform/
  resubmit_for_assignment/85

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
    api_instance = canvas_lms_python_client.PlagiarismPlatformApi(api_client)
    assignment_id = 'assignment_id_example' # str | The assignment ID

    try:
        # Resubmit All Submissions to Tool
        await api_instance.plagiarism_platform_resubmit_for_assignment(assignment_id)
    except Exception as e:
        print("Exception when calling PlagiarismPlatformApi->plagiarism_platform_resubmit_for_assignment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| The assignment ID | 

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
**0** | Resubmit All Submissions to Tool |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

