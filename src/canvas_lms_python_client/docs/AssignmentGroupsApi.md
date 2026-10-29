# canvas_lms_python_client.AssignmentGroupsApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assignment_groups_index**](AssignmentGroupsApi.md#assignment_groups_index) | **GET** /api/v1/courses/{course_id}/assignment_groups | List assignment groups


# **assignment_groups_index**
> List[AssignmentGroup] assignment_groups_index(course_id, include=include, assignment_ids=assignment_ids, exclude_assignment_submission_types=exclude_assignment_submission_types, override_assignment_dates=override_assignment_dates, grading_period_id=grading_period_id, scope_assignments_to_student=scope_assignments_to_student, page=page, per_page=per_page)

List assignment groups

Returns the paginated list of assignment groups for the current context.
The returned groups are sorted by their position field.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.assignment_group import AssignmentGroup
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
    api_instance = canvas_lms_python_client.AssignmentGroupsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    include = ['include_example'] # List[str] | Associations to include with the group. \"discussion_topic\", \"all_dates\", \"can_edit\", \"assignment_visibility\" & \"submission\" are only valid if \"assignments\" is also included. \"score_statistics\" requires that the \"assignments\" and \"submission\" options are included. The \"assignment_visibility\" option additionally requires that the Differentiated Assignments course feature be turned on. If \"observed_users\" is passed along with \"assignments\" and \"submission\", submissions for observed users will also be included as an array. The \"peer_review\" option requires that the Peer Review Grading course feature be turned on and that \"assignments\" is included. (optional)
    assignment_ids = ['assignment_ids_example'] # List[str] | If \"assignments\" are included, optionally return only assignments having their ID in this array. This argument may also be passed as a comma separated string. (optional)
    exclude_assignment_submission_types = ['exclude_assignment_submission_types_example'] # List[str] | If \"assignments\" are included, those with the specified submission types will be excluded from the assignment groups. (optional)
    override_assignment_dates = True # bool | Apply assignment overrides for each assignment, defaults to true. (optional)
    grading_period_id = 56 # int | The id of the grading period in which assignment groups are being requested (Requires grading periods to exist.) (optional)
    scope_assignments_to_student = True # bool | If true, all assignments returned will apply to the current user in the specified grading period. If assignments apply to other students in the specified grading period, but not the current user, they will not be returned. (Requires the grading_period_id argument and grading periods to exist. In addition, the current user must be a student.) (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List assignment groups
        api_response = await api_instance.assignment_groups_index(course_id, include=include, assignment_ids=assignment_ids, exclude_assignment_submission_types=exclude_assignment_submission_types, override_assignment_dates=override_assignment_dates, grading_period_id=grading_period_id, scope_assignments_to_student=scope_assignments_to_student, page=page, per_page=per_page)
        print("The response of AssignmentGroupsApi->assignment_groups_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssignmentGroupsApi->assignment_groups_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **include** | [**List[str]**](str.md)| Associations to include with the group. \&quot;discussion_topic\&quot;, \&quot;all_dates\&quot;, \&quot;can_edit\&quot;, \&quot;assignment_visibility\&quot; &amp; \&quot;submission\&quot; are only valid if \&quot;assignments\&quot; is also included. \&quot;score_statistics\&quot; requires that the \&quot;assignments\&quot; and \&quot;submission\&quot; options are included. The \&quot;assignment_visibility\&quot; option additionally requires that the Differentiated Assignments course feature be turned on. If \&quot;observed_users\&quot; is passed along with \&quot;assignments\&quot; and \&quot;submission\&quot;, submissions for observed users will also be included as an array. The \&quot;peer_review\&quot; option requires that the Peer Review Grading course feature be turned on and that \&quot;assignments\&quot; is included. | [optional] 
 **assignment_ids** | [**List[str]**](str.md)| If \&quot;assignments\&quot; are included, optionally return only assignments having their ID in this array. This argument may also be passed as a comma separated string. | [optional] 
 **exclude_assignment_submission_types** | [**List[str]**](str.md)| If \&quot;assignments\&quot; are included, those with the specified submission types will be excluded from the assignment groups. | [optional] 
 **override_assignment_dates** | **bool**| Apply assignment overrides for each assignment, defaults to true. | [optional] 
 **grading_period_id** | **int**| The id of the grading period in which assignment groups are being requested (Requires grading periods to exist.) | [optional] 
 **scope_assignments_to_student** | **bool**| If true, all assignments returned will apply to the current user in the specified grading period. If assignments apply to other students in the specified grading period, but not the current user, they will not be returned. (Requires the grading_period_id argument and grading periods to exist. In addition, the current user must be a student.) | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[AssignmentGroup]**](AssignmentGroup.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

