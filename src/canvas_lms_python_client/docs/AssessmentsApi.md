# canvas_lms_python_client.AssessmentsApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assessments_create**](AssessmentsApi.md#assessments_create) | **POST** /api/v1/courses/{course_id}/live_assessments | Create or find a live assessment
[**assessments_index**](AssessmentsApi.md#assessments_index) | **GET** /api/v1/courses/{course_id}/live_assessments | List live assessments


# **assessments_create**
> LiveAssessmentsAssessmentsCreateResponse assessments_create(course_id)

Create or find a live assessment

Creates or finds an existing live assessment with the given key and aligns it with
the linked outcome

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.live_assessments_assessments_create_response import LiveAssessmentsAssessmentsCreateResponse
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
    api_instance = canvas_lms_python_client.AssessmentsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id

    try:
        # Create or find a live assessment
        api_response = await api_instance.assessments_create(course_id)
        print("The response of AssessmentsApi->assessments_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssessmentsApi->assessments_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 

### Return type

[**LiveAssessmentsAssessmentsCreateResponse**](LiveAssessmentsAssessmentsCreateResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | LiveAssessmentsAssessmentsCreateResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assessments_index**
> LiveAssessmentsAssessmentsIndexResponse assessments_index(course_id, page=page, per_page=per_page)

List live assessments

Returns a paginated list of live assessments.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.live_assessments_assessments_index_response import LiveAssessmentsAssessmentsIndexResponse
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
    api_instance = canvas_lms_python_client.AssessmentsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List live assessments
        api_response = await api_instance.assessments_index(course_id, page=page, per_page=per_page)
        print("The response of AssessmentsApi->assessments_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssessmentsApi->assessments_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**LiveAssessmentsAssessmentsIndexResponse**](LiveAssessmentsAssessmentsIndexResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | LiveAssessmentsAssessmentsIndexResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

