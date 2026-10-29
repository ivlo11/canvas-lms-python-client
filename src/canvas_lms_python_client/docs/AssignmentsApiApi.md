# canvas_lms_python_client.AssignmentsApiApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assignments_api_bulk_update**](AssignmentsApiApi.md#assignments_api_bulk_update) | **PUT** /api/v1/courses/{course_id}/assignments/bulk_update | Bulk update assignment dates
[**assignments_api_create**](AssignmentsApiApi.md#assignments_api_create) | **POST** /api/v1/courses/{course_id}/assignments | Create an assignment
[**assignments_api_duplicate**](AssignmentsApiApi.md#assignments_api_duplicate) | **POST** /api/v1/courses/{course_id}/assignments/{assignment_id}/duplicate | Duplicate assignment
[**assignments_api_index**](AssignmentsApiApi.md#assignments_api_index) | **GET** /api/v1/courses/{course_id}/assignments | List assignments
[**assignments_api_index_for_assignment_groups**](AssignmentsApiApi.md#assignments_api_index_for_assignment_groups) | **GET** /api/v1/courses/{course_id}/assignment_groups/{assignment_group_id}/assignments | List assignments
[**assignments_api_show**](AssignmentsApiApi.md#assignments_api_show) | **GET** /api/v1/courses/{course_id}/assignments/{id} | Get a single assignment
[**assignments_api_student_group_members**](AssignmentsApiApi.md#assignments_api_student_group_members) | **GET** /api/v1/courses/{course_id}/assignments/{assignment_id}/users/{user_id}/group_members | List group members for a student on an assignment
[**assignments_api_update**](AssignmentsApiApi.md#assignments_api_update) | **PUT** /api/v1/courses/{course_id}/assignments/{id} | Edit an assignment
[**assignments_api_user_index**](AssignmentsApiApi.md#assignments_api_user_index) | **GET** /api/v1/users/{user_id}/courses/{course_id}/assignments | List assignments for user


# **assignments_api_bulk_update**
> Progress assignments_api_bulk_update(course_id)

Bulk update assignment dates

Update due dates and availability dates for multiple assignments in a course.

Accepts a JSON array of objects containing two keys each: +id+, the assignment id,
and +all_dates+, an array of +AssignmentDate+ structures containing the base and/or override
dates for the assignment, as returned from the {api:AssignmentsApiController#index List assignments}
endpoint with +include[]=all_dates+.

This endpoint cannot create or destroy assignment overrides; any existing assignment overrides
that are not referenced in the arguments will be left alone. If an override is given, any dates
that are not supplied with it will be defaulted. To clear a date, specify null explicitly.

All referenced assignments will be validated before any are saved. A list of errors will
be returned if any provided dates are invalid, and no changes will be saved.

The bulk update is performed in a background job, use the {api:ProgressController#show Progress API}
to check its status.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
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
    api_instance = canvas_lms_python_client.AssignmentsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id

    try:
        # Bulk update assignment dates
        api_response = await api_instance.assignments_api_bulk_update(course_id)
        print("The response of AssignmentsApiApi->assignments_api_bulk_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssignmentsApiApi->assignments_api_bulk_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 

### Return type

[**Progress**](Progress.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Progress |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assignments_api_create**
> Assignment assignments_api_create(course_id, assignments_api_create_request=assignments_api_create_request)

Create an assignment

Create a new assignment for this course. The assignment is created in the
active state.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.assignment import Assignment
from canvas_lms_python_client.models.assignments_api_create_request import AssignmentsApiCreateRequest
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
    api_instance = canvas_lms_python_client.AssignmentsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    assignments_api_create_request = canvas_lms_python_client.AssignmentsApiCreateRequest() # AssignmentsApiCreateRequest | Request body parameters (optional)

    try:
        # Create an assignment
        api_response = await api_instance.assignments_api_create(course_id, assignments_api_create_request=assignments_api_create_request)
        print("The response of AssignmentsApiApi->assignments_api_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssignmentsApiApi->assignments_api_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **assignments_api_create_request** | [**AssignmentsApiCreateRequest**](AssignmentsApiCreateRequest.md)| Request body parameters | [optional] 

### Return type

[**Assignment**](Assignment.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Assignment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assignments_api_duplicate**
> Assignment assignments_api_duplicate(assignment_id, course_id, assignments_api_duplicate_request=assignments_api_duplicate_request)

Duplicate assignment

Duplicate an assignment and return a json based on result_type argument.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.assignment import Assignment
from canvas_lms_python_client.models.assignments_api_duplicate_request import AssignmentsApiDuplicateRequest
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
    api_instance = canvas_lms_python_client.AssignmentsApiApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    course_id = 'course_id_example' # str | Scope response to course_id
    assignments_api_duplicate_request = canvas_lms_python_client.AssignmentsApiDuplicateRequest() # AssignmentsApiDuplicateRequest | Request body parameters  **Example Request:** ``` curl -X POST -H 'Authorization: Bearer <token>' \\ https://<canvas>/api/v1/courses/123/assignments/123/duplicate ``` (optional)

    try:
        # Duplicate assignment
        api_response = await api_instance.assignments_api_duplicate(assignment_id, course_id, assignments_api_duplicate_request=assignments_api_duplicate_request)
        print("The response of AssignmentsApiApi->assignments_api_duplicate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssignmentsApiApi->assignments_api_duplicate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **course_id** | **str**| Scope response to course_id | 
 **assignments_api_duplicate_request** | [**AssignmentsApiDuplicateRequest**](AssignmentsApiDuplicateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl -X POST -H &#39;Authorization: Bearer &lt;token&gt;&#39; \\ https://&lt;canvas&gt;/api/v1/courses/123/assignments/123/duplicate &#x60;&#x60;&#x60; | [optional] 

### Return type

[**Assignment**](Assignment.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Assignment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assignments_api_index**
> List[Assignment] assignments_api_index(course_id, include=include, search_term=search_term, override_assignment_dates=override_assignment_dates, needs_grading_count_by_section=needs_grading_count_by_section, bucket=bucket, assignment_ids=assignment_ids, order_by=order_by, post_to_sis=post_to_sis, new_quizzes=new_quizzes, page=page, per_page=per_page)

List assignments

Returns the paginated list of assignments for the current course or assignment group.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.assignment import Assignment
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
    api_instance = canvas_lms_python_client.AssignmentsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    include = ['include_example'] # List[str] | Optional information to include with each assignment: submission:: The current user's current +Submission+ assignment_visibility:: An array of ids of students who can see the assignment all_dates:: An array of +AssignmentDate+ structures, one for each override, and also a +base+ if the assignment has an \"Everyone\" / \"Everyone Else\" date overrides:: An array of +AssignmentOverride+ structures observed_users:: An array of submissions for observed users can_edit:: an extra Boolean value will be included with each +Assignment+ (and +AssignmentDate+ if +all_dates+ is supplied) to indicate whether the caller can edit the assignment or date. Moderated grading and closed grading periods may restrict a user's ability to edit an assignment. score_statistics:: An object containing min, max, and mean score on this assignment. This will not be included for students if there are less than 5 graded assignments or if disabled by the instructor. Only valid if 'submission' is also included. ab_guid:: An array of guid strings for academic benchmarks (optional)
    search_term = 'search_term_example' # str | The partial title of the assignments to match and return. (optional)
    override_assignment_dates = True # bool | Apply assignment overrides for each assignment, defaults to true. (optional)
    needs_grading_count_by_section = True # bool | Split up \"needs_grading_count\" by sections into the \"needs_grading_count_by_section\" key, defaults to false (optional)
    bucket = 'bucket_example' # str | If included, only return certain assignments depending on due date and submission status. (optional)
    assignment_ids = ['assignment_ids_example'] # List[str] | if set, return only assignments specified (optional)
    order_by = 'order_by_example' # str | Determines the order of the assignments. Defaults to \"position\". (optional)
    post_to_sis = True # bool | Return only assignments that have post_to_sis set or not set. (optional)
    new_quizzes = True # bool | Return only New Quizzes assignments (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List assignments
        api_response = await api_instance.assignments_api_index(course_id, include=include, search_term=search_term, override_assignment_dates=override_assignment_dates, needs_grading_count_by_section=needs_grading_count_by_section, bucket=bucket, assignment_ids=assignment_ids, order_by=order_by, post_to_sis=post_to_sis, new_quizzes=new_quizzes, page=page, per_page=per_page)
        print("The response of AssignmentsApiApi->assignments_api_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssignmentsApiApi->assignments_api_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **include** | [**List[str]**](str.md)| Optional information to include with each assignment: submission:: The current user&#39;s current +Submission+ assignment_visibility:: An array of ids of students who can see the assignment all_dates:: An array of +AssignmentDate+ structures, one for each override, and also a +base+ if the assignment has an \&quot;Everyone\&quot; / \&quot;Everyone Else\&quot; date overrides:: An array of +AssignmentOverride+ structures observed_users:: An array of submissions for observed users can_edit:: an extra Boolean value will be included with each +Assignment+ (and +AssignmentDate+ if +all_dates+ is supplied) to indicate whether the caller can edit the assignment or date. Moderated grading and closed grading periods may restrict a user&#39;s ability to edit an assignment. score_statistics:: An object containing min, max, and mean score on this assignment. This will not be included for students if there are less than 5 graded assignments or if disabled by the instructor. Only valid if &#39;submission&#39; is also included. ab_guid:: An array of guid strings for academic benchmarks | [optional] 
 **search_term** | **str**| The partial title of the assignments to match and return. | [optional] 
 **override_assignment_dates** | **bool**| Apply assignment overrides for each assignment, defaults to true. | [optional] 
 **needs_grading_count_by_section** | **bool**| Split up \&quot;needs_grading_count\&quot; by sections into the \&quot;needs_grading_count_by_section\&quot; key, defaults to false | [optional] 
 **bucket** | **str**| If included, only return certain assignments depending on due date and submission status. | [optional] 
 **assignment_ids** | [**List[str]**](str.md)| if set, return only assignments specified | [optional] 
 **order_by** | **str**| Determines the order of the assignments. Defaults to \&quot;position\&quot;. | [optional] 
 **post_to_sis** | **bool**| Return only assignments that have post_to_sis set or not set. | [optional] 
 **new_quizzes** | **bool**| Return only New Quizzes assignments | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[Assignment]**](Assignment.md)

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

# **assignments_api_index_for_assignment_groups**
> List[Assignment] assignments_api_index_for_assignment_groups(assignment_group_id, course_id, include=include, search_term=search_term, override_assignment_dates=override_assignment_dates, needs_grading_count_by_section=needs_grading_count_by_section, bucket=bucket, assignment_ids=assignment_ids, order_by=order_by, post_to_sis=post_to_sis, new_quizzes=new_quizzes, page=page, per_page=per_page)

List assignments

Returns the paginated list of assignments for the current course or assignment group.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.assignment import Assignment
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
    api_instance = canvas_lms_python_client.AssignmentsApiApi(api_client)
    assignment_group_id = 'assignment_group_id_example' # str | Scope response to assignment_group_id
    course_id = 'course_id_example' # str | Scope response to course_id
    include = ['include_example'] # List[str] | Optional information to include with each assignment: submission:: The current user's current +Submission+ assignment_visibility:: An array of ids of students who can see the assignment all_dates:: An array of +AssignmentDate+ structures, one for each override, and also a +base+ if the assignment has an \"Everyone\" / \"Everyone Else\" date overrides:: An array of +AssignmentOverride+ structures observed_users:: An array of submissions for observed users can_edit:: an extra Boolean value will be included with each +Assignment+ (and +AssignmentDate+ if +all_dates+ is supplied) to indicate whether the caller can edit the assignment or date. Moderated grading and closed grading periods may restrict a user's ability to edit an assignment. score_statistics:: An object containing min, max, and mean score on this assignment. This will not be included for students if there are less than 5 graded assignments or if disabled by the instructor. Only valid if 'submission' is also included. ab_guid:: An array of guid strings for academic benchmarks (optional)
    search_term = 'search_term_example' # str | The partial title of the assignments to match and return. (optional)
    override_assignment_dates = True # bool | Apply assignment overrides for each assignment, defaults to true. (optional)
    needs_grading_count_by_section = True # bool | Split up \"needs_grading_count\" by sections into the \"needs_grading_count_by_section\" key, defaults to false (optional)
    bucket = 'bucket_example' # str | If included, only return certain assignments depending on due date and submission status. (optional)
    assignment_ids = ['assignment_ids_example'] # List[str] | if set, return only assignments specified (optional)
    order_by = 'order_by_example' # str | Determines the order of the assignments. Defaults to \"position\". (optional)
    post_to_sis = True # bool | Return only assignments that have post_to_sis set or not set. (optional)
    new_quizzes = True # bool | Return only New Quizzes assignments (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List assignments
        api_response = await api_instance.assignments_api_index_for_assignment_groups(assignment_group_id, course_id, include=include, search_term=search_term, override_assignment_dates=override_assignment_dates, needs_grading_count_by_section=needs_grading_count_by_section, bucket=bucket, assignment_ids=assignment_ids, order_by=order_by, post_to_sis=post_to_sis, new_quizzes=new_quizzes, page=page, per_page=per_page)
        print("The response of AssignmentsApiApi->assignments_api_index_for_assignment_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssignmentsApiApi->assignments_api_index_for_assignment_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_group_id** | **str**| Scope response to assignment_group_id | 
 **course_id** | **str**| Scope response to course_id | 
 **include** | [**List[str]**](str.md)| Optional information to include with each assignment: submission:: The current user&#39;s current +Submission+ assignment_visibility:: An array of ids of students who can see the assignment all_dates:: An array of +AssignmentDate+ structures, one for each override, and also a +base+ if the assignment has an \&quot;Everyone\&quot; / \&quot;Everyone Else\&quot; date overrides:: An array of +AssignmentOverride+ structures observed_users:: An array of submissions for observed users can_edit:: an extra Boolean value will be included with each +Assignment+ (and +AssignmentDate+ if +all_dates+ is supplied) to indicate whether the caller can edit the assignment or date. Moderated grading and closed grading periods may restrict a user&#39;s ability to edit an assignment. score_statistics:: An object containing min, max, and mean score on this assignment. This will not be included for students if there are less than 5 graded assignments or if disabled by the instructor. Only valid if &#39;submission&#39; is also included. ab_guid:: An array of guid strings for academic benchmarks | [optional] 
 **search_term** | **str**| The partial title of the assignments to match and return. | [optional] 
 **override_assignment_dates** | **bool**| Apply assignment overrides for each assignment, defaults to true. | [optional] 
 **needs_grading_count_by_section** | **bool**| Split up \&quot;needs_grading_count\&quot; by sections into the \&quot;needs_grading_count_by_section\&quot; key, defaults to false | [optional] 
 **bucket** | **str**| If included, only return certain assignments depending on due date and submission status. | [optional] 
 **assignment_ids** | [**List[str]**](str.md)| if set, return only assignments specified | [optional] 
 **order_by** | **str**| Determines the order of the assignments. Defaults to \&quot;position\&quot;. | [optional] 
 **post_to_sis** | **bool**| Return only assignments that have post_to_sis set or not set. | [optional] 
 **new_quizzes** | **bool**| Return only New Quizzes assignments | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[Assignment]**](Assignment.md)

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

# **assignments_api_show**
> Assignment assignments_api_show(course_id, id, include=include, override_assignment_dates=override_assignment_dates, needs_grading_count_by_section=needs_grading_count_by_section, all_dates=all_dates)

Get a single assignment

Returns the assignment with the given id.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.assignment import Assignment
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
    api_instance = canvas_lms_python_client.AssignmentsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    include = ['include_example'] # List[str] | Associations to include with the assignment. The \"assignment_visibility\" option requires that the Differentiated Assignments course feature be turned on. If \"observed_users\" is passed, submissions for observed users will also be included. For \"score_statistics\" to be included, the \"submission\" option must also be set. The \"peer_review\" option returns peer review sub assignment data if it exists, regardless of the Peer Review Allocation and Grading feature state. If no peer review sub assignment exists, the feature must be enabled to receive a null value; otherwise the key is omitted. (optional)
    override_assignment_dates = True # bool | Apply assignment overrides to the assignment, defaults to true. (optional)
    needs_grading_count_by_section = True # bool | Split up \"needs_grading_count\" by sections into the \"needs_grading_count_by_section\" key, defaults to false (optional)
    all_dates = True # bool | All dates associated with the assignment, if applicable (optional)

    try:
        # Get a single assignment
        api_response = await api_instance.assignments_api_show(course_id, id, include=include, override_assignment_dates=override_assignment_dates, needs_grading_count_by_section=needs_grading_count_by_section, all_dates=all_dates)
        print("The response of AssignmentsApiApi->assignments_api_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssignmentsApiApi->assignments_api_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **include** | [**List[str]**](str.md)| Associations to include with the assignment. The \&quot;assignment_visibility\&quot; option requires that the Differentiated Assignments course feature be turned on. If \&quot;observed_users\&quot; is passed, submissions for observed users will also be included. For \&quot;score_statistics\&quot; to be included, the \&quot;submission\&quot; option must also be set. The \&quot;peer_review\&quot; option returns peer review sub assignment data if it exists, regardless of the Peer Review Allocation and Grading feature state. If no peer review sub assignment exists, the feature must be enabled to receive a null value; otherwise the key is omitted. | [optional] 
 **override_assignment_dates** | **bool**| Apply assignment overrides to the assignment, defaults to true. | [optional] 
 **needs_grading_count_by_section** | **bool**| Split up \&quot;needs_grading_count\&quot; by sections into the \&quot;needs_grading_count_by_section\&quot; key, defaults to false | [optional] 
 **all_dates** | **bool**| All dates associated with the assignment, if applicable | [optional] 

### Return type

[**Assignment**](Assignment.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Assignment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assignments_api_student_group_members**
> List[BasicUser] assignments_api_student_group_members(assignment_id, course_id, user_id)

List group members for a student on an assignment

Returns student ids and names for the group.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.basic_user import BasicUser
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
    api_instance = canvas_lms_python_client.AssignmentsApiApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    course_id = 'course_id_example' # str | Scope response to course_id
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # List group members for a student on an assignment
        api_response = await api_instance.assignments_api_student_group_members(assignment_id, course_id, user_id)
        print("The response of AssignmentsApiApi->assignments_api_student_group_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssignmentsApiApi->assignments_api_student_group_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **course_id** | **str**| Scope response to course_id | 
 **user_id** | **str**| Scope response to user_id | 

### Return type

[**List[BasicUser]**](BasicUser.md)

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

# **assignments_api_update**
> Assignment assignments_api_update(course_id, id, assignments_api_update_request=assignments_api_update_request)

Edit an assignment

Modify an existing assignment.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.assignment import Assignment
from canvas_lms_python_client.models.assignments_api_update_request import AssignmentsApiUpdateRequest
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
    api_instance = canvas_lms_python_client.AssignmentsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    assignments_api_update_request = canvas_lms_python_client.AssignmentsApiUpdateRequest() # AssignmentsApiUpdateRequest | Request body parameters (optional)

    try:
        # Edit an assignment
        api_response = await api_instance.assignments_api_update(course_id, id, assignments_api_update_request=assignments_api_update_request)
        print("The response of AssignmentsApiApi->assignments_api_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssignmentsApiApi->assignments_api_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **assignments_api_update_request** | [**AssignmentsApiUpdateRequest**](AssignmentsApiUpdateRequest.md)| Request body parameters | [optional] 

### Return type

[**Assignment**](Assignment.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Assignment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assignments_api_user_index**
> assignments_api_user_index(course_id, user_id, page=page, per_page=per_page)

List assignments for user

Returns the paginated list of assignments for the specified user if the current user has rights to view.
See {api:AssignmentsApiController#index List assignments} for valid arguments.

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
    api_instance = canvas_lms_python_client.AssignmentsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    user_id = 'user_id_example' # str | Scope response to user_id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List assignments for user
        await api_instance.assignments_api_user_index(course_id, user_id, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling AssignmentsApiApi->assignments_api_user_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **user_id** | **str**| Scope response to user_id | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

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
**0** | List assignments for user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

