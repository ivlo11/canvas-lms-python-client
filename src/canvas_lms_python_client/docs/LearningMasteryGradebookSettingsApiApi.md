# canvas_lms_python_client.LearningMasteryGradebookSettingsApiApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**learning_mastery_gradebook_settings_api_show**](LearningMasteryGradebookSettingsApiApi.md#learning_mastery_gradebook_settings_api_show) | **GET** /api/v1/courses/{course_id}/learning_mastery_gradebook_settings | Get Learning Mastery Gradebook Settings
[**learning_mastery_gradebook_settings_api_update**](LearningMasteryGradebookSettingsApiApi.md#learning_mastery_gradebook_settings_api_update) | **PUT** /api/v1/courses/{course_id}/learning_mastery_gradebook_settings | Update Learning Mastery Gradebook Settings


# **learning_mastery_gradebook_settings_api_show**
> LearningMasteryGradebookSettingsApiShowResponse learning_mastery_gradebook_settings_api_show(course_id)

Get Learning Mastery Gradebook Settings

Get the current user's Learning Mastery Gradebook settings for the current context.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.learning_mastery_gradebook_settings_api_show_response import LearningMasteryGradebookSettingsApiShowResponse
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
    api_instance = canvas_lms_python_client.LearningMasteryGradebookSettingsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id

    try:
        # Get Learning Mastery Gradebook Settings
        api_response = await api_instance.learning_mastery_gradebook_settings_api_show(course_id)
        print("The response of LearningMasteryGradebookSettingsApiApi->learning_mastery_gradebook_settings_api_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LearningMasteryGradebookSettingsApiApi->learning_mastery_gradebook_settings_api_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 

### Return type

[**LearningMasteryGradebookSettingsApiShowResponse**](LearningMasteryGradebookSettingsApiShowResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | The Learning Mastery Gradebook settings. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **learning_mastery_gradebook_settings_api_update**
> LearningMasteryGradebookSettingsApiUpdateResponse learning_mastery_gradebook_settings_api_update(course_id)

Update Learning Mastery Gradebook Settings

Update the current user's Learning Mastery Gradebook settings for the current context.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.learning_mastery_gradebook_settings_api_update_response import LearningMasteryGradebookSettingsApiUpdateResponse
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
    api_instance = canvas_lms_python_client.LearningMasteryGradebookSettingsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id

    try:
        # Update Learning Mastery Gradebook Settings
        api_response = await api_instance.learning_mastery_gradebook_settings_api_update(course_id)
        print("The response of LearningMasteryGradebookSettingsApiApi->learning_mastery_gradebook_settings_api_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LearningMasteryGradebookSettingsApiApi->learning_mastery_gradebook_settings_api_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 

### Return type

[**LearningMasteryGradebookSettingsApiUpdateResponse**](LearningMasteryGradebookSettingsApiUpdateResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | The updated Learning Mastery Gradebook settings. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

