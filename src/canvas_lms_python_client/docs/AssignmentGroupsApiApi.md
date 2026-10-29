# canvas_lms_python_client.AssignmentGroupsApiApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assignment_groups_api_create**](AssignmentGroupsApiApi.md#assignment_groups_api_create) | **POST** /api/v1/courses/{course_id}/assignment_groups | Create an Assignment Group
[**assignment_groups_api_destroy**](AssignmentGroupsApiApi.md#assignment_groups_api_destroy) | **DELETE** /api/v1/courses/{course_id}/assignment_groups/{assignment_group_id} | Destroy an Assignment Group
[**assignment_groups_api_show**](AssignmentGroupsApiApi.md#assignment_groups_api_show) | **GET** /api/v1/courses/{course_id}/assignment_groups/{assignment_group_id} | Get an Assignment Group
[**assignment_groups_api_update**](AssignmentGroupsApiApi.md#assignment_groups_api_update) | **PUT** /api/v1/courses/{course_id}/assignment_groups/{assignment_group_id} | Edit an Assignment Group


# **assignment_groups_api_create**
> AssignmentGroup assignment_groups_api_create(course_id, assignment_groups_api_create_request=assignment_groups_api_create_request)

Create an Assignment Group

Create a new assignment group for this course.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.assignment_group import AssignmentGroup
from canvas_lms_python_client.models.assignment_groups_api_create_request import AssignmentGroupsApiCreateRequest
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
    api_instance = canvas_lms_python_client.AssignmentGroupsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    assignment_groups_api_create_request = canvas_lms_python_client.AssignmentGroupsApiCreateRequest() # AssignmentGroupsApiCreateRequest | Request body parameters (optional)

    try:
        # Create an Assignment Group
        api_response = await api_instance.assignment_groups_api_create(course_id, assignment_groups_api_create_request=assignment_groups_api_create_request)
        print("The response of AssignmentGroupsApiApi->assignment_groups_api_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssignmentGroupsApiApi->assignment_groups_api_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **assignment_groups_api_create_request** | [**AssignmentGroupsApiCreateRequest**](AssignmentGroupsApiCreateRequest.md)| Request body parameters | [optional] 

### Return type

[**AssignmentGroup**](AssignmentGroup.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | AssignmentGroup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assignment_groups_api_destroy**
> AssignmentGroup assignment_groups_api_destroy(assignment_group_id, course_id, move_assignments_to=move_assignments_to)

Destroy an Assignment Group

Deletes the assignment group with the given id.

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
    api_instance = canvas_lms_python_client.AssignmentGroupsApiApi(api_client)
    assignment_group_id = 'assignment_group_id_example' # str | Scope response to assignment_group_id
    course_id = 'course_id_example' # str | Scope response to course_id
    move_assignments_to = 56 # int | The ID of an active Assignment Group to which the assignments that are currently assigned to the destroyed Assignment Group will be assigned. NOTE: If this argument is not provided, any assignments in this Assignment Group will be deleted. (optional)

    try:
        # Destroy an Assignment Group
        api_response = await api_instance.assignment_groups_api_destroy(assignment_group_id, course_id, move_assignments_to=move_assignments_to)
        print("The response of AssignmentGroupsApiApi->assignment_groups_api_destroy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssignmentGroupsApiApi->assignment_groups_api_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_group_id** | **str**| Scope response to assignment_group_id | 
 **course_id** | **str**| Scope response to course_id | 
 **move_assignments_to** | **int**| The ID of an active Assignment Group to which the assignments that are currently assigned to the destroyed Assignment Group will be assigned. NOTE: If this argument is not provided, any assignments in this Assignment Group will be deleted. | [optional] 

### Return type

[**AssignmentGroup**](AssignmentGroup.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | AssignmentGroup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assignment_groups_api_show**
> AssignmentGroup assignment_groups_api_show(assignment_group_id, course_id, include_assignments_discussion_topic_assignment_visibility_submission_score_statistics=include_assignments_discussion_topic_assignment_visibility_submission_score_statistics, override_assignment_dates=override_assignment_dates, grading_period_id=grading_period_id)

Get an Assignment Group

Returns the assignment group with the given id.

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
    api_instance = canvas_lms_python_client.AssignmentGroupsApiApi(api_client)
    assignment_group_id = 'assignment_group_id_example' # str | Scope response to assignment_group_id
    course_id = 'course_id_example' # str | Scope response to course_id
    include_assignments_discussion_topic_assignment_visibility_submission_score_statistics = 'include_assignments_discussion_topic_assignment_visibility_submission_score_statistics_example' # str | Associations to include with the group. \"discussion_topic\" and \"assignment_visibility\" and \"submission\" are only valid if \"assignments\" is also included. \"score_statistics\" is only valid if \"submission\" and \"assignments\" are also included. The \"assignment_visibility\" option additionally requires that the Differentiated Assignments course feature be turned on. (optional)
    override_assignment_dates = True # bool | Apply assignment overrides for each assignment, defaults to true. (optional)
    grading_period_id = 56 # int | The id of the grading period in which assignment groups are being requested (Requires grading periods to exist on the account) (optional)

    try:
        # Get an Assignment Group
        api_response = await api_instance.assignment_groups_api_show(assignment_group_id, course_id, include_assignments_discussion_topic_assignment_visibility_submission_score_statistics=include_assignments_discussion_topic_assignment_visibility_submission_score_statistics, override_assignment_dates=override_assignment_dates, grading_period_id=grading_period_id)
        print("The response of AssignmentGroupsApiApi->assignment_groups_api_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssignmentGroupsApiApi->assignment_groups_api_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_group_id** | **str**| Scope response to assignment_group_id | 
 **course_id** | **str**| Scope response to course_id | 
 **include_assignments_discussion_topic_assignment_visibility_submission_score_statistics** | **str**| Associations to include with the group. \&quot;discussion_topic\&quot; and \&quot;assignment_visibility\&quot; and \&quot;submission\&quot; are only valid if \&quot;assignments\&quot; is also included. \&quot;score_statistics\&quot; is only valid if \&quot;submission\&quot; and \&quot;assignments\&quot; are also included. The \&quot;assignment_visibility\&quot; option additionally requires that the Differentiated Assignments course feature be turned on. | [optional] 
 **override_assignment_dates** | **bool**| Apply assignment overrides for each assignment, defaults to true. | [optional] 
 **grading_period_id** | **int**| The id of the grading period in which assignment groups are being requested (Requires grading periods to exist on the account) | [optional] 

### Return type

[**AssignmentGroup**](AssignmentGroup.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | AssignmentGroup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assignment_groups_api_update**
> AssignmentGroup assignment_groups_api_update(assignment_group_id, course_id, assignment_groups_api_update_request=assignment_groups_api_update_request)

Edit an Assignment Group

Modify an existing Assignment Group.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.assignment_group import AssignmentGroup
from canvas_lms_python_client.models.assignment_groups_api_update_request import AssignmentGroupsApiUpdateRequest
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
    api_instance = canvas_lms_python_client.AssignmentGroupsApiApi(api_client)
    assignment_group_id = 'assignment_group_id_example' # str | Scope response to assignment_group_id
    course_id = 'course_id_example' # str | Scope response to course_id
    assignment_groups_api_update_request = canvas_lms_python_client.AssignmentGroupsApiUpdateRequest() # AssignmentGroupsApiUpdateRequest | Request body parameters (optional)

    try:
        # Edit an Assignment Group
        api_response = await api_instance.assignment_groups_api_update(assignment_group_id, course_id, assignment_groups_api_update_request=assignment_groups_api_update_request)
        print("The response of AssignmentGroupsApiApi->assignment_groups_api_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssignmentGroupsApiApi->assignment_groups_api_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_group_id** | **str**| Scope response to assignment_group_id | 
 **course_id** | **str**| Scope response to course_id | 
 **assignment_groups_api_update_request** | [**AssignmentGroupsApiUpdateRequest**](AssignmentGroupsApiUpdateRequest.md)| Request body parameters | [optional] 

### Return type

[**AssignmentGroup**](AssignmentGroup.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | AssignmentGroup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

