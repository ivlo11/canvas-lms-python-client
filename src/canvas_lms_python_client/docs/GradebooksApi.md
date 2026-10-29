# canvas_lms_python_client.GradebooksApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gradebooks_apply_score_to_ungraded_submissions**](GradebooksApi.md#gradebooks_apply_score_to_ungraded_submissions) | **PUT** /api/v1/courses/{course_id}/apply_score_to_ungraded_submissions | Apply score to ungraded submissions
[**gradebooks_update_final_grade_overrides**](GradebooksApi.md#gradebooks_update_final_grade_overrides) | **PUT** /api/v1/courses/{course_id}/update_final_grade_overrides | Bulk update final grade overrides


# **gradebooks_apply_score_to_ungraded_submissions**
> Progress gradebooks_apply_score_to_ungraded_submissions(course_id, gradebooks_apply_score_to_ungraded_submissions_request=gradebooks_apply_score_to_ungraded_submissions_request)

Apply score to ungraded submissions

Perform a bulk scoring of ungraded submissions for a course, or mark
ungraded submissions as excused. The course's account must have the "Apply
Score to Ungraded" feature enabled, and the caller must have permission to
manage grades. By default, will apply scores to all ungraded submissions in
the course, but the scope may be restricted using the parameters below.

{
  "percent": "50.0",
  "mark_as_missing": true,
  "only_past_due": true,
  "assignment_ids": ["1", "2", "3"],
  "student_ids": ["11", "22"]
}

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.gradebooks_apply_score_to_ungraded_submissions_request import GradebooksApplyScoreToUngradedSubmissionsRequest
from canvas_lms_python_client.models.progress import Progress
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
    api_instance = canvas_lms_python_client.GradebooksApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    gradebooks_apply_score_to_ungraded_submissions_request = canvas_lms_python_client.GradebooksApplyScoreToUngradedSubmissionsRequest() # GradebooksApplyScoreToUngradedSubmissionsRequest | Request body parameters (optional)

    try:
        # Apply score to ungraded submissions
        api_response = await api_instance.gradebooks_apply_score_to_ungraded_submissions(course_id, gradebooks_apply_score_to_ungraded_submissions_request=gradebooks_apply_score_to_ungraded_submissions_request)
        print("The response of GradebooksApi->gradebooks_apply_score_to_ungraded_submissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GradebooksApi->gradebooks_apply_score_to_ungraded_submissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **gradebooks_apply_score_to_ungraded_submissions_request** | [**GradebooksApplyScoreToUngradedSubmissionsRequest**](GradebooksApplyScoreToUngradedSubmissionsRequest.md)| Request body parameters | [optional] 

### Return type

[**Progress**](Progress.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Progress |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gradebooks_update_final_grade_overrides**
> Progress gradebooks_update_final_grade_overrides(course_id, gradebooks_update_final_grade_overrides_request=gradebooks_update_final_grade_overrides_request)

Bulk update final grade overrides

Set multiple final grade override scores for a course. The course must have
final grade override enabled, and the caller must have permission to
manage grades. Additionally, the "Import Override Scores in Gradebook" feature
flag must be enabled.

{
  "grading_period_id": "10",
  "override_scores": [
    {
      "student_id": "124",
      "override_score": "80.0"
    },
    {
      "student_id": "126",
      "override_score": "70.0"
    }
  ]
}

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.gradebooks_update_final_grade_overrides_request import GradebooksUpdateFinalGradeOverridesRequest
from canvas_lms_python_client.models.progress import Progress
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
    api_instance = canvas_lms_python_client.GradebooksApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    gradebooks_update_final_grade_overrides_request = canvas_lms_python_client.GradebooksUpdateFinalGradeOverridesRequest() # GradebooksUpdateFinalGradeOverridesRequest | Request body parameters (optional)

    try:
        # Bulk update final grade overrides
        api_response = await api_instance.gradebooks_update_final_grade_overrides(course_id, gradebooks_update_final_grade_overrides_request=gradebooks_update_final_grade_overrides_request)
        print("The response of GradebooksApi->gradebooks_update_final_grade_overrides:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GradebooksApi->gradebooks_update_final_grade_overrides: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **gradebooks_update_final_grade_overrides_request** | [**GradebooksUpdateFinalGradeOverridesRequest**](GradebooksUpdateFinalGradeOverridesRequest.md)| Request body parameters | [optional] 

### Return type

[**Progress**](Progress.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Progress |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

