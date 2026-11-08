# canvas_lms_python_client.StudyAssistApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**study_assist_create**](StudyAssistApi.md#study_assist_create) | **POST** /api/v1/courses/{course_id}/study_assist | Request a study assist response


# **study_assist_create**
> AssistResponse study_assist_create(course_id, study_assist_create_request=study_assist_create_request)

Request a study assist response

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.assist_response import AssistResponse
from canvas_lms_python_client.models.study_assist_create_request import StudyAssistCreateRequest
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
    api_instance = canvas_lms_python_client.StudyAssistApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    study_assist_create_request = canvas_lms_python_client.StudyAssistCreateRequest() # StudyAssistCreateRequest | Request body parameters (optional)

    try:
        # Request a study assist response
        api_response = await api_instance.study_assist_create(course_id, study_assist_create_request=study_assist_create_request)
        print("The response of StudyAssistApi->study_assist_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StudyAssistApi->study_assist_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **study_assist_create_request** | [**StudyAssistCreateRequest**](StudyAssistCreateRequest.md)| Request body parameters | [optional] 

### Return type

[**AssistResponse**](AssistResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | AssistResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

