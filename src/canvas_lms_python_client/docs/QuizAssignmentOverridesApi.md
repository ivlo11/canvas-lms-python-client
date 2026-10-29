# canvas_lms_python_client.QuizAssignmentOverridesApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quiz_assignment_overrides_index**](QuizAssignmentOverridesApi.md#quiz_assignment_overrides_index) | **GET** /api/v1/courses/{course_id}/quizzes/assignment_overrides | Retrieve assignment-overridden dates for Classic Quizzes
[**quiz_assignment_overrides_new_quizzes**](QuizAssignmentOverridesApi.md#quiz_assignment_overrides_new_quizzes) | **GET** /api/v1/courses/{course_id}/new_quizzes/assignment_overrides | Retrieve assignment-overridden dates for New Quizzes


# **quiz_assignment_overrides_index**
> QuizAssignmentOverrideSetContainer quiz_assignment_overrides_index(course_id, quiz_assignment_overrides_quiz_ids=quiz_assignment_overrides_quiz_ids, page=page, per_page=per_page)

Retrieve assignment-overridden dates for Classic Quizzes

Retrieve the actual due-at, unlock-at, and available-at dates for quizzes
based on the assignment overrides active for the current API user.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.quiz_assignment_override_set_container import QuizAssignmentOverrideSetContainer
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
    api_instance = canvas_lms_python_client.QuizAssignmentOverridesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    quiz_assignment_overrides_quiz_ids = ['quiz_assignment_overrides_quiz_ids_example'] # List[str] | An array of quiz IDs. If omitted, overrides for all quizzes available to the operating user will be returned. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # Retrieve assignment-overridden dates for Classic Quizzes
        api_response = await api_instance.quiz_assignment_overrides_index(course_id, quiz_assignment_overrides_quiz_ids=quiz_assignment_overrides_quiz_ids, page=page, per_page=per_page)
        print("The response of QuizAssignmentOverridesApi->quiz_assignment_overrides_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuizAssignmentOverridesApi->quiz_assignment_overrides_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **quiz_assignment_overrides_quiz_ids** | [**List[str]**](str.md)| An array of quiz IDs. If omitted, overrides for all quizzes available to the operating user will be returned. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**QuizAssignmentOverrideSetContainer**](QuizAssignmentOverrideSetContainer.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | QuizAssignmentOverrideSetContainer |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quiz_assignment_overrides_new_quizzes**
> QuizAssignmentOverrideSetContainer quiz_assignment_overrides_new_quizzes(course_id, quiz_assignment_overrides_quiz_ids=quiz_assignment_overrides_quiz_ids, page=page, per_page=per_page)

Retrieve assignment-overridden dates for New Quizzes

Retrieve the actual due-at, unlock-at, and available-at dates for quizzes
based on the assignment overrides active for the current API user.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.quiz_assignment_override_set_container import QuizAssignmentOverrideSetContainer
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
    api_instance = canvas_lms_python_client.QuizAssignmentOverridesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    quiz_assignment_overrides_quiz_ids = ['quiz_assignment_overrides_quiz_ids_example'] # List[str] | An array of quiz IDs. If omitted, overrides for all quizzes available to the operating user will be returned. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # Retrieve assignment-overridden dates for New Quizzes
        api_response = await api_instance.quiz_assignment_overrides_new_quizzes(course_id, quiz_assignment_overrides_quiz_ids=quiz_assignment_overrides_quiz_ids, page=page, per_page=per_page)
        print("The response of QuizAssignmentOverridesApi->quiz_assignment_overrides_new_quizzes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuizAssignmentOverridesApi->quiz_assignment_overrides_new_quizzes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **quiz_assignment_overrides_quiz_ids** | [**List[str]**](str.md)| An array of quiz IDs. If omitted, overrides for all quizzes available to the operating user will be returned. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**QuizAssignmentOverrideSetContainer**](QuizAssignmentOverrideSetContainer.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | QuizAssignmentOverrideSetContainer |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

