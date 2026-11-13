# canvas_lms_python_client.ResultsApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**results_create**](ResultsApi.md#results_create) | **POST** /api/v1/courses/{course_id}/live_assessments/{assessment_id}/results | Create live assessment results
[**results_index**](ResultsApi.md#results_index) | **GET** /api/v1/courses/{course_id}/live_assessments/{assessment_id}/results | List live assessment results


# **results_create**
> ResultsCreateResponse results_create(assessment_id, course_id)

Create live assessment results

Creates live assessment results and adds them to a live assessment

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.results_create_response import ResultsCreateResponse
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
    api_instance = canvas_lms_python_client.ResultsApi(api_client)
    assessment_id = 'assessment_id_example' # str | Scope response to assessment_id
    course_id = 'course_id_example' # str | Scope response to course_id

    try:
        # Create live assessment results
        api_response = await api_instance.results_create(assessment_id, course_id)
        print("The response of ResultsApi->results_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResultsApi->results_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assessment_id** | **str**| Scope response to assessment_id | 
 **course_id** | **str**| Scope response to course_id | 

### Return type

[**ResultsCreateResponse**](ResultsCreateResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Create live assessment results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **results_index**
> ResultsIndexResponse results_index(assessment_id, course_id, user_id=user_id)

List live assessment results

Returns a paginated list of live assessment results

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.results_index_response import ResultsIndexResponse
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
    api_instance = canvas_lms_python_client.ResultsApi(api_client)
    assessment_id = 'assessment_id_example' # str | Scope response to assessment_id
    course_id = 'course_id_example' # str | Scope response to course_id
    user_id = 56 # int | If set, restrict results to those for this user (optional)

    try:
        # List live assessment results
        api_response = await api_instance.results_index(assessment_id, course_id, user_id=user_id)
        print("The response of ResultsApi->results_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResultsApi->results_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assessment_id** | **str**| Scope response to assessment_id | 
 **course_id** | **str**| Scope response to course_id | 
 **user_id** | **int**| If set, restrict results to those for this user | [optional] 

### Return type

[**ResultsIndexResponse**](ResultsIndexResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | List live assessment results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

