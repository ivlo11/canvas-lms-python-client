# canvas_lms_python_client.EnrollmentsApiApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enrollments_api_accept**](EnrollmentsApiApi.md#enrollments_api_accept) | **POST** /api/v1/courses/{course_id}/enrollments/{id}/accept | Accept Course Invitation
[**enrollments_api_bulk_enrollment**](EnrollmentsApiApi.md#enrollments_api_bulk_enrollment) | **POST** /api/v1/accounts/{account_id}/bulk_enrollment | Enroll multiple users to one or more courses
[**enrollments_api_bulk_temporary_enrollment_status**](EnrollmentsApiApi.md#enrollments_api_bulk_temporary_enrollment_status) | **GET** /api/v1/temporary_enrollment_status | Bulk Temporary Enrollment Status
[**enrollments_api_create**](EnrollmentsApiApi.md#enrollments_api_create) | **POST** /api/v1/courses/{course_id}/enrollments | Enroll a user
[**enrollments_api_create_for_sections**](EnrollmentsApiApi.md#enrollments_api_create_for_sections) | **POST** /api/v1/sections/{section_id}/enrollments | Enroll a user
[**enrollments_api_destroy**](EnrollmentsApiApi.md#enrollments_api_destroy) | **DELETE** /api/v1/courses/{course_id}/enrollments/{id} | Conclude, deactivate, or delete an enrollment
[**enrollments_api_index**](EnrollmentsApiApi.md#enrollments_api_index) | **GET** /api/v1/courses/{course_id}/enrollments | List enrollments
[**enrollments_api_index_for_sections**](EnrollmentsApiApi.md#enrollments_api_index_for_sections) | **GET** /api/v1/sections/{section_id}/enrollments | List enrollments
[**enrollments_api_index_for_users**](EnrollmentsApiApi.md#enrollments_api_index_for_users) | **GET** /api/v1/users/{user_id}/enrollments | List enrollments
[**enrollments_api_last_attended**](EnrollmentsApiApi.md#enrollments_api_last_attended) | **PUT** /api/v1/courses/{course_id}/users/{user_id}/last_attended | Add last attended date
[**enrollments_api_reactivate**](EnrollmentsApiApi.md#enrollments_api_reactivate) | **PUT** /api/v1/courses/{course_id}/enrollments/{id}/reactivate | Re-activate an enrollment
[**enrollments_api_reject**](EnrollmentsApiApi.md#enrollments_api_reject) | **POST** /api/v1/courses/{course_id}/enrollments/{id}/reject | Reject Course Invitation
[**enrollments_api_show**](EnrollmentsApiApi.md#enrollments_api_show) | **GET** /api/v1/accounts/{account_id}/enrollments/{id} | Enrollment by ID
[**enrollments_api_show_temporary_enrollment_status**](EnrollmentsApiApi.md#enrollments_api_show_temporary_enrollment_status) | **GET** /api/v1/users/{user_id}/temporary_enrollment_status | Show Temporary Enrollment recipient and provider status


# **enrollments_api_accept**
> EnrollmentsAcceptResponse enrollments_api_accept(course_id, id)

Accept Course Invitation

accepts a pending course invitation for the current user

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.enrollments_accept_response import EnrollmentsAcceptResponse
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
    api_instance = canvas_lms_python_client.EnrollmentsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id

    try:
        # Accept Course Invitation
        api_response = await api_instance.enrollments_api_accept(course_id, id)
        print("The response of EnrollmentsApiApi->enrollments_api_accept:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmentsApiApi->enrollments_api_accept: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**EnrollmentsAcceptResponse**](EnrollmentsAcceptResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | EnrollmentsAcceptResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enrollments_api_bulk_enrollment**
> Progress enrollments_api_bulk_enrollment(account_id, enrollments_api_bulk_enrollment_request=enrollments_api_bulk_enrollment_request)

Enroll multiple users to one or more courses

Enrolls multiple users in one or more courses in a single operation.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.enrollments_api_bulk_enrollment_request import EnrollmentsApiBulkEnrollmentRequest
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
    api_instance = canvas_lms_python_client.EnrollmentsApiApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    enrollments_api_bulk_enrollment_request = canvas_lms_python_client.EnrollmentsApiBulkEnrollmentRequest() # EnrollmentsApiBulkEnrollmentRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/accounts/:account_id/bulk_enrollment \\   -X POST \\   -F 'user_ids[]=1' \\   -F 'user_ids[]=2' \\   -F 'course_ids[]=10' \\   -F 'course_ids[]=11' ``` (optional)

    try:
        # Enroll multiple users to one or more courses
        api_response = await api_instance.enrollments_api_bulk_enrollment(account_id, enrollments_api_bulk_enrollment_request=enrollments_api_bulk_enrollment_request)
        print("The response of EnrollmentsApiApi->enrollments_api_bulk_enrollment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmentsApiApi->enrollments_api_bulk_enrollment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **enrollments_api_bulk_enrollment_request** | [**EnrollmentsApiBulkEnrollmentRequest**](EnrollmentsApiBulkEnrollmentRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/accounts/:account_id/bulk_enrollment \\   -X POST \\   -F &#39;user_ids[]&#x3D;1&#39; \\   -F &#39;user_ids[]&#x3D;2&#39; \\   -F &#39;course_ids[]&#x3D;10&#39; \\   -F &#39;course_ids[]&#x3D;11&#39; &#x60;&#x60;&#x60; | [optional] 

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

# **enrollments_api_bulk_temporary_enrollment_status**
> enrollments_api_bulk_temporary_enrollment_status(user_ids, account_id=account_id, limit=limit)

Bulk Temporary Enrollment Status

Returns temporary enrollment statuses for multiple users at once.

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
    api_instance = canvas_lms_python_client.EnrollmentsApiApi(api_client)
    user_ids = ['user_ids_example'] # List[str] | The IDs of the users to check temporary enrollment status for.
    account_id = 'account_id_example' # str | The ID of the account to scope the check to. (optional)
    limit = 56 # int | The maximum number of user IDs to process. Defaults to 10, max 100. (optional)

    try:
        # Bulk Temporary Enrollment Status
        await api_instance.enrollments_api_bulk_temporary_enrollment_status(user_ids, account_id=account_id, limit=limit)
    except Exception as e:
        print("Exception when calling EnrollmentsApiApi->enrollments_api_bulk_temporary_enrollment_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_ids** | [**List[str]**](str.md)| The IDs of the users to check temporary enrollment status for. | 
 **account_id** | **str**| The ID of the account to scope the check to. | [optional] 
 **limit** | **int**| The maximum number of user IDs to process. Defaults to 10, max 100. | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Bulk Temporary Enrollment Status |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enrollments_api_create**
> Enrollment enrollments_api_create(course_id, enrollments_api_create_request=enrollments_api_create_request)

Enroll a user

Create a new user enrollment for a course or section.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.enrollment import Enrollment
from canvas_lms_python_client.models.enrollments_api_create_request import EnrollmentsApiCreateRequest
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
    api_instance = canvas_lms_python_client.EnrollmentsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    enrollments_api_create_request = canvas_lms_python_client.EnrollmentsApiCreateRequest() # EnrollmentsApiCreateRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/courses/:course_id/enrollments \\   -X POST \\   -F 'enrollment[user_id]=1' \\   -F 'enrollment[type]=StudentEnrollment' \\   -F 'enrollment[enrollment_state]=active' \\   -F 'enrollment[course_section_id]=1' \\   -F 'enrollment[limit_privileges_to_course_section]=true' \\   -F 'enrollment[notify]=false' ``` (optional)

    try:
        # Enroll a user
        api_response = await api_instance.enrollments_api_create(course_id, enrollments_api_create_request=enrollments_api_create_request)
        print("The response of EnrollmentsApiApi->enrollments_api_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmentsApiApi->enrollments_api_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **enrollments_api_create_request** | [**EnrollmentsApiCreateRequest**](EnrollmentsApiCreateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/courses/:course_id/enrollments \\   -X POST \\   -F &#39;enrollment[user_id]&#x3D;1&#39; \\   -F &#39;enrollment[type]&#x3D;StudentEnrollment&#39; \\   -F &#39;enrollment[enrollment_state]&#x3D;active&#39; \\   -F &#39;enrollment[course_section_id]&#x3D;1&#39; \\   -F &#39;enrollment[limit_privileges_to_course_section]&#x3D;true&#39; \\   -F &#39;enrollment[notify]&#x3D;false&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**Enrollment**](Enrollment.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Enrollment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enrollments_api_create_for_sections**
> Enrollment enrollments_api_create_for_sections(section_id, enrollments_api_create_request=enrollments_api_create_request)

Enroll a user

Create a new user enrollment for a course or section.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.enrollment import Enrollment
from canvas_lms_python_client.models.enrollments_api_create_request import EnrollmentsApiCreateRequest
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
    api_instance = canvas_lms_python_client.EnrollmentsApiApi(api_client)
    section_id = 'section_id_example' # str | Scope response to section_id
    enrollments_api_create_request = canvas_lms_python_client.EnrollmentsApiCreateRequest() # EnrollmentsApiCreateRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/courses/:course_id/enrollments \\   -X POST \\   -F 'enrollment[user_id]=1' \\   -F 'enrollment[type]=StudentEnrollment' \\   -F 'enrollment[enrollment_state]=active' \\   -F 'enrollment[course_section_id]=1' \\   -F 'enrollment[limit_privileges_to_course_section]=true' \\   -F 'enrollment[notify]=false' ``` (optional)

    try:
        # Enroll a user
        api_response = await api_instance.enrollments_api_create_for_sections(section_id, enrollments_api_create_request=enrollments_api_create_request)
        print("The response of EnrollmentsApiApi->enrollments_api_create_for_sections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmentsApiApi->enrollments_api_create_for_sections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **section_id** | **str**| Scope response to section_id | 
 **enrollments_api_create_request** | [**EnrollmentsApiCreateRequest**](EnrollmentsApiCreateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/courses/:course_id/enrollments \\   -X POST \\   -F &#39;enrollment[user_id]&#x3D;1&#39; \\   -F &#39;enrollment[type]&#x3D;StudentEnrollment&#39; \\   -F &#39;enrollment[enrollment_state]&#x3D;active&#39; \\   -F &#39;enrollment[course_section_id]&#x3D;1&#39; \\   -F &#39;enrollment[limit_privileges_to_course_section]&#x3D;true&#39; \\   -F &#39;enrollment[notify]&#x3D;false&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**Enrollment**](Enrollment.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Enrollment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enrollments_api_destroy**
> Enrollment enrollments_api_destroy(course_id, id, task=task)

Conclude, deactivate, or delete an enrollment

Conclude, deactivate, or delete an enrollment. If the +task+ argument isn't given, the enrollment
will be concluded.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.enrollment import Enrollment
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
    api_instance = canvas_lms_python_client.EnrollmentsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    task = 'task_example' # str | The action to take on the enrollment. When inactive, a user will still appear in the course roster to admins, but be unable to participate. (\"inactivate\" and \"deactivate\" are equivalent tasks) (optional)

    try:
        # Conclude, deactivate, or delete an enrollment
        api_response = await api_instance.enrollments_api_destroy(course_id, id, task=task)
        print("The response of EnrollmentsApiApi->enrollments_api_destroy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmentsApiApi->enrollments_api_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **task** | **str**| The action to take on the enrollment. When inactive, a user will still appear in the course roster to admins, but be unable to participate. (\&quot;inactivate\&quot; and \&quot;deactivate\&quot; are equivalent tasks) | [optional] 

### Return type

[**Enrollment**](Enrollment.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Enrollment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enrollments_api_index**
> List[Enrollment] enrollments_api_index(course_id, type=type, role=role, state=state, include=include, user_id=user_id, grading_period_id=grading_period_id, enrollment_term_id=enrollment_term_id, sis_account_id=sis_account_id, sis_course_id=sis_course_id, sis_section_id=sis_section_id, sis_user_id=sis_user_id, created_for_sis_id=created_for_sis_id, page=page, per_page=per_page)

List enrollments

Depending on the URL given, return a paginated list of either (1) all of
the enrollments in a course, (2) all of the enrollments in a section or (3)
all of a user's enrollments. This includes student, teacher, TA, and
observer enrollments.

If a user has multiple enrollments in a context (e.g. as a teacher
and a student or in multiple course sections), each enrollment will be
listed separately.

note: Currently, only a root level admin user can return other users' enrollments.
A user can, however, return his/her own enrollments.

Enrollments scoped to a course context will include inactive states by default
if the caller has account admin authorization and the state[] parameter is omitted.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.enrollment import Enrollment
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
    api_instance = canvas_lms_python_client.EnrollmentsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    type = ['type_example'] # List[str] | A list of enrollment types to return. Accepted values are 'StudentEnrollment', 'TeacherEnrollment', 'TaEnrollment', 'DesignerEnrollment', and 'ObserverEnrollment.' If omitted, all enrollment types are returned. This argument is ignored if `role` is given. (optional)
    role = ['role_example'] # List[str] | A list of enrollment roles to return. Accepted values include course-level roles created by the {api:RoleOverridesController#add_role Add Role API} as well as the base enrollment types accepted by the `type` argument above. (optional)
    state = ['state_example'] # List[str] | Filter by enrollment state. If omitted, 'active' and 'invited' enrollments are returned. The following synthetic states are supported only when querying a user's enrollments (either via user_id argument or via user enrollments endpoint): +current_and_invited+, +current_and_future+, +current_future_and_restricted+, +current_and_concluded+ (optional)
    include = ['include_example'] # List[str] | Array of additional information to include on the enrollment or user records. \"avatar_url\" and \"group_ids\" will be returned on the user record. If \"current_points\" is specified, the fields \"current_points\" and (if the caller has permissions to manage grades) \"unposted_current_points\" will be included in the \"grades\" hash for student enrollments. (optional)
    user_id = 'user_id_example' # str | Filter by user_id (only valid for course or section enrollment queries). If set to the current user's id, this is a way to determine if the user has any enrollments in the course or section, independent of whether the user has permission to view other people on the roster. (optional)
    grading_period_id = 56 # int | Return grades for the given grading_period.  If this parameter is not specified, the returned grades will be for the whole course. (optional)
    enrollment_term_id = 56 # int | Returns only enrollments for the specified enrollment term. This parameter only applies to the user enrollments path. May pass the ID from the enrollment terms api or the SIS id prepended with 'sis_term_id:'. (optional)
    sis_account_id = ['sis_account_id_example'] # List[str] | Returns only enrollments for the specified SIS account ID(s). Does not look into sub_accounts. May pass in array or string. (optional)
    sis_course_id = ['sis_course_id_example'] # List[str] | Returns only enrollments matching the specified SIS course ID(s). May pass in array or string. (optional)
    sis_section_id = ['sis_section_id_example'] # List[str] | Returns only section enrollments matching the specified SIS section ID(s). May pass in array or string. (optional)
    sis_user_id = ['sis_user_id_example'] # List[str] | Returns only enrollments for the specified SIS user ID(s). May pass in array or string. (optional)
    created_for_sis_id = [True] # List[bool] | If sis_user_id is present and created_for_sis_id is true, Returns only enrollments for the specified SIS ID(s). If a user has two sis_id's, one enrollment may be created using one of the two ids. This would limit the enrollments returned from the endpoint to enrollments that were created from a sis_import with that sis_user_id (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List enrollments
        api_response = await api_instance.enrollments_api_index(course_id, type=type, role=role, state=state, include=include, user_id=user_id, grading_period_id=grading_period_id, enrollment_term_id=enrollment_term_id, sis_account_id=sis_account_id, sis_course_id=sis_course_id, sis_section_id=sis_section_id, sis_user_id=sis_user_id, created_for_sis_id=created_for_sis_id, page=page, per_page=per_page)
        print("The response of EnrollmentsApiApi->enrollments_api_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmentsApiApi->enrollments_api_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **type** | [**List[str]**](str.md)| A list of enrollment types to return. Accepted values are &#39;StudentEnrollment&#39;, &#39;TeacherEnrollment&#39;, &#39;TaEnrollment&#39;, &#39;DesignerEnrollment&#39;, and &#39;ObserverEnrollment.&#39; If omitted, all enrollment types are returned. This argument is ignored if &#x60;role&#x60; is given. | [optional] 
 **role** | [**List[str]**](str.md)| A list of enrollment roles to return. Accepted values include course-level roles created by the {api:RoleOverridesController#add_role Add Role API} as well as the base enrollment types accepted by the &#x60;type&#x60; argument above. | [optional] 
 **state** | [**List[str]**](str.md)| Filter by enrollment state. If omitted, &#39;active&#39; and &#39;invited&#39; enrollments are returned. The following synthetic states are supported only when querying a user&#39;s enrollments (either via user_id argument or via user enrollments endpoint): +current_and_invited+, +current_and_future+, +current_future_and_restricted+, +current_and_concluded+ | [optional] 
 **include** | [**List[str]**](str.md)| Array of additional information to include on the enrollment or user records. \&quot;avatar_url\&quot; and \&quot;group_ids\&quot; will be returned on the user record. If \&quot;current_points\&quot; is specified, the fields \&quot;current_points\&quot; and (if the caller has permissions to manage grades) \&quot;unposted_current_points\&quot; will be included in the \&quot;grades\&quot; hash for student enrollments. | [optional] 
 **user_id** | **str**| Filter by user_id (only valid for course or section enrollment queries). If set to the current user&#39;s id, this is a way to determine if the user has any enrollments in the course or section, independent of whether the user has permission to view other people on the roster. | [optional] 
 **grading_period_id** | **int**| Return grades for the given grading_period.  If this parameter is not specified, the returned grades will be for the whole course. | [optional] 
 **enrollment_term_id** | **int**| Returns only enrollments for the specified enrollment term. This parameter only applies to the user enrollments path. May pass the ID from the enrollment terms api or the SIS id prepended with &#39;sis_term_id:&#39;. | [optional] 
 **sis_account_id** | [**List[str]**](str.md)| Returns only enrollments for the specified SIS account ID(s). Does not look into sub_accounts. May pass in array or string. | [optional] 
 **sis_course_id** | [**List[str]**](str.md)| Returns only enrollments matching the specified SIS course ID(s). May pass in array or string. | [optional] 
 **sis_section_id** | [**List[str]**](str.md)| Returns only section enrollments matching the specified SIS section ID(s). May pass in array or string. | [optional] 
 **sis_user_id** | [**List[str]**](str.md)| Returns only enrollments for the specified SIS user ID(s). May pass in array or string. | [optional] 
 **created_for_sis_id** | [**List[bool]**](bool.md)| If sis_user_id is present and created_for_sis_id is true, Returns only enrollments for the specified SIS ID(s). If a user has two sis_id&#39;s, one enrollment may be created using one of the two ids. This would limit the enrollments returned from the endpoint to enrollments that were created from a sis_import with that sis_user_id | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[Enrollment]**](Enrollment.md)

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

# **enrollments_api_index_for_sections**
> List[Enrollment] enrollments_api_index_for_sections(section_id, type=type, role=role, state=state, include=include, user_id=user_id, grading_period_id=grading_period_id, enrollment_term_id=enrollment_term_id, sis_account_id=sis_account_id, sis_course_id=sis_course_id, sis_section_id=sis_section_id, sis_user_id=sis_user_id, created_for_sis_id=created_for_sis_id, page=page, per_page=per_page)

List enrollments

Depending on the URL given, return a paginated list of either (1) all of
the enrollments in a course, (2) all of the enrollments in a section or (3)
all of a user's enrollments. This includes student, teacher, TA, and
observer enrollments.

If a user has multiple enrollments in a context (e.g. as a teacher
and a student or in multiple course sections), each enrollment will be
listed separately.

note: Currently, only a root level admin user can return other users' enrollments.
A user can, however, return his/her own enrollments.

Enrollments scoped to a course context will include inactive states by default
if the caller has account admin authorization and the state[] parameter is omitted.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.enrollment import Enrollment
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
    api_instance = canvas_lms_python_client.EnrollmentsApiApi(api_client)
    section_id = 'section_id_example' # str | Scope response to section_id
    type = ['type_example'] # List[str] | A list of enrollment types to return. Accepted values are 'StudentEnrollment', 'TeacherEnrollment', 'TaEnrollment', 'DesignerEnrollment', and 'ObserverEnrollment.' If omitted, all enrollment types are returned. This argument is ignored if `role` is given. (optional)
    role = ['role_example'] # List[str] | A list of enrollment roles to return. Accepted values include course-level roles created by the {api:RoleOverridesController#add_role Add Role API} as well as the base enrollment types accepted by the `type` argument above. (optional)
    state = ['state_example'] # List[str] | Filter by enrollment state. If omitted, 'active' and 'invited' enrollments are returned. The following synthetic states are supported only when querying a user's enrollments (either via user_id argument or via user enrollments endpoint): +current_and_invited+, +current_and_future+, +current_future_and_restricted+, +current_and_concluded+ (optional)
    include = ['include_example'] # List[str] | Array of additional information to include on the enrollment or user records. \"avatar_url\" and \"group_ids\" will be returned on the user record. If \"current_points\" is specified, the fields \"current_points\" and (if the caller has permissions to manage grades) \"unposted_current_points\" will be included in the \"grades\" hash for student enrollments. (optional)
    user_id = 'user_id_example' # str | Filter by user_id (only valid for course or section enrollment queries). If set to the current user's id, this is a way to determine if the user has any enrollments in the course or section, independent of whether the user has permission to view other people on the roster. (optional)
    grading_period_id = 56 # int | Return grades for the given grading_period.  If this parameter is not specified, the returned grades will be for the whole course. (optional)
    enrollment_term_id = 56 # int | Returns only enrollments for the specified enrollment term. This parameter only applies to the user enrollments path. May pass the ID from the enrollment terms api or the SIS id prepended with 'sis_term_id:'. (optional)
    sis_account_id = ['sis_account_id_example'] # List[str] | Returns only enrollments for the specified SIS account ID(s). Does not look into sub_accounts. May pass in array or string. (optional)
    sis_course_id = ['sis_course_id_example'] # List[str] | Returns only enrollments matching the specified SIS course ID(s). May pass in array or string. (optional)
    sis_section_id = ['sis_section_id_example'] # List[str] | Returns only section enrollments matching the specified SIS section ID(s). May pass in array or string. (optional)
    sis_user_id = ['sis_user_id_example'] # List[str] | Returns only enrollments for the specified SIS user ID(s). May pass in array or string. (optional)
    created_for_sis_id = [True] # List[bool] | If sis_user_id is present and created_for_sis_id is true, Returns only enrollments for the specified SIS ID(s). If a user has two sis_id's, one enrollment may be created using one of the two ids. This would limit the enrollments returned from the endpoint to enrollments that were created from a sis_import with that sis_user_id (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List enrollments
        api_response = await api_instance.enrollments_api_index_for_sections(section_id, type=type, role=role, state=state, include=include, user_id=user_id, grading_period_id=grading_period_id, enrollment_term_id=enrollment_term_id, sis_account_id=sis_account_id, sis_course_id=sis_course_id, sis_section_id=sis_section_id, sis_user_id=sis_user_id, created_for_sis_id=created_for_sis_id, page=page, per_page=per_page)
        print("The response of EnrollmentsApiApi->enrollments_api_index_for_sections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmentsApiApi->enrollments_api_index_for_sections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **section_id** | **str**| Scope response to section_id | 
 **type** | [**List[str]**](str.md)| A list of enrollment types to return. Accepted values are &#39;StudentEnrollment&#39;, &#39;TeacherEnrollment&#39;, &#39;TaEnrollment&#39;, &#39;DesignerEnrollment&#39;, and &#39;ObserverEnrollment.&#39; If omitted, all enrollment types are returned. This argument is ignored if &#x60;role&#x60; is given. | [optional] 
 **role** | [**List[str]**](str.md)| A list of enrollment roles to return. Accepted values include course-level roles created by the {api:RoleOverridesController#add_role Add Role API} as well as the base enrollment types accepted by the &#x60;type&#x60; argument above. | [optional] 
 **state** | [**List[str]**](str.md)| Filter by enrollment state. If omitted, &#39;active&#39; and &#39;invited&#39; enrollments are returned. The following synthetic states are supported only when querying a user&#39;s enrollments (either via user_id argument or via user enrollments endpoint): +current_and_invited+, +current_and_future+, +current_future_and_restricted+, +current_and_concluded+ | [optional] 
 **include** | [**List[str]**](str.md)| Array of additional information to include on the enrollment or user records. \&quot;avatar_url\&quot; and \&quot;group_ids\&quot; will be returned on the user record. If \&quot;current_points\&quot; is specified, the fields \&quot;current_points\&quot; and (if the caller has permissions to manage grades) \&quot;unposted_current_points\&quot; will be included in the \&quot;grades\&quot; hash for student enrollments. | [optional] 
 **user_id** | **str**| Filter by user_id (only valid for course or section enrollment queries). If set to the current user&#39;s id, this is a way to determine if the user has any enrollments in the course or section, independent of whether the user has permission to view other people on the roster. | [optional] 
 **grading_period_id** | **int**| Return grades for the given grading_period.  If this parameter is not specified, the returned grades will be for the whole course. | [optional] 
 **enrollment_term_id** | **int**| Returns only enrollments for the specified enrollment term. This parameter only applies to the user enrollments path. May pass the ID from the enrollment terms api or the SIS id prepended with &#39;sis_term_id:&#39;. | [optional] 
 **sis_account_id** | [**List[str]**](str.md)| Returns only enrollments for the specified SIS account ID(s). Does not look into sub_accounts. May pass in array or string. | [optional] 
 **sis_course_id** | [**List[str]**](str.md)| Returns only enrollments matching the specified SIS course ID(s). May pass in array or string. | [optional] 
 **sis_section_id** | [**List[str]**](str.md)| Returns only section enrollments matching the specified SIS section ID(s). May pass in array or string. | [optional] 
 **sis_user_id** | [**List[str]**](str.md)| Returns only enrollments for the specified SIS user ID(s). May pass in array or string. | [optional] 
 **created_for_sis_id** | [**List[bool]**](bool.md)| If sis_user_id is present and created_for_sis_id is true, Returns only enrollments for the specified SIS ID(s). If a user has two sis_id&#39;s, one enrollment may be created using one of the two ids. This would limit the enrollments returned from the endpoint to enrollments that were created from a sis_import with that sis_user_id | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[Enrollment]**](Enrollment.md)

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

# **enrollments_api_index_for_users**
> List[Enrollment] enrollments_api_index_for_users(user_id, type=type, role=role, state=state, include=include, grading_period_id=grading_period_id, enrollment_term_id=enrollment_term_id, sis_account_id=sis_account_id, sis_course_id=sis_course_id, sis_section_id=sis_section_id, sis_user_id=sis_user_id, created_for_sis_id=created_for_sis_id, page=page, per_page=per_page)

List enrollments

Depending on the URL given, return a paginated list of either (1) all of
the enrollments in a course, (2) all of the enrollments in a section or (3)
all of a user's enrollments. This includes student, teacher, TA, and
observer enrollments.

If a user has multiple enrollments in a context (e.g. as a teacher
and a student or in multiple course sections), each enrollment will be
listed separately.

note: Currently, only a root level admin user can return other users' enrollments.
A user can, however, return his/her own enrollments.

Enrollments scoped to a course context will include inactive states by default
if the caller has account admin authorization and the state[] parameter is omitted.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.enrollment import Enrollment
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
    api_instance = canvas_lms_python_client.EnrollmentsApiApi(api_client)
    user_id = 'user_id_example' # str | Filter by user_id (only valid for course or section enrollment queries). If set to the current user's id, this is a way to determine if the user has any enrollments in the course or section, independent of whether the user has permission to view other people on the roster.
    type = ['type_example'] # List[str] | A list of enrollment types to return. Accepted values are 'StudentEnrollment', 'TeacherEnrollment', 'TaEnrollment', 'DesignerEnrollment', and 'ObserverEnrollment.' If omitted, all enrollment types are returned. This argument is ignored if `role` is given. (optional)
    role = ['role_example'] # List[str] | A list of enrollment roles to return. Accepted values include course-level roles created by the {api:RoleOverridesController#add_role Add Role API} as well as the base enrollment types accepted by the `type` argument above. (optional)
    state = ['state_example'] # List[str] | Filter by enrollment state. If omitted, 'active' and 'invited' enrollments are returned. The following synthetic states are supported only when querying a user's enrollments (either via user_id argument or via user enrollments endpoint): +current_and_invited+, +current_and_future+, +current_future_and_restricted+, +current_and_concluded+ (optional)
    include = ['include_example'] # List[str] | Array of additional information to include on the enrollment or user records. \"avatar_url\" and \"group_ids\" will be returned on the user record. If \"current_points\" is specified, the fields \"current_points\" and (if the caller has permissions to manage grades) \"unposted_current_points\" will be included in the \"grades\" hash for student enrollments. (optional)
    grading_period_id = 56 # int | Return grades for the given grading_period.  If this parameter is not specified, the returned grades will be for the whole course. (optional)
    enrollment_term_id = 56 # int | Returns only enrollments for the specified enrollment term. This parameter only applies to the user enrollments path. May pass the ID from the enrollment terms api or the SIS id prepended with 'sis_term_id:'. (optional)
    sis_account_id = ['sis_account_id_example'] # List[str] | Returns only enrollments for the specified SIS account ID(s). Does not look into sub_accounts. May pass in array or string. (optional)
    sis_course_id = ['sis_course_id_example'] # List[str] | Returns only enrollments matching the specified SIS course ID(s). May pass in array or string. (optional)
    sis_section_id = ['sis_section_id_example'] # List[str] | Returns only section enrollments matching the specified SIS section ID(s). May pass in array or string. (optional)
    sis_user_id = ['sis_user_id_example'] # List[str] | Returns only enrollments for the specified SIS user ID(s). May pass in array or string. (optional)
    created_for_sis_id = [True] # List[bool] | If sis_user_id is present and created_for_sis_id is true, Returns only enrollments for the specified SIS ID(s). If a user has two sis_id's, one enrollment may be created using one of the two ids. This would limit the enrollments returned from the endpoint to enrollments that were created from a sis_import with that sis_user_id (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List enrollments
        api_response = await api_instance.enrollments_api_index_for_users(user_id, type=type, role=role, state=state, include=include, grading_period_id=grading_period_id, enrollment_term_id=enrollment_term_id, sis_account_id=sis_account_id, sis_course_id=sis_course_id, sis_section_id=sis_section_id, sis_user_id=sis_user_id, created_for_sis_id=created_for_sis_id, page=page, per_page=per_page)
        print("The response of EnrollmentsApiApi->enrollments_api_index_for_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmentsApiApi->enrollments_api_index_for_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Filter by user_id (only valid for course or section enrollment queries). If set to the current user&#39;s id, this is a way to determine if the user has any enrollments in the course or section, independent of whether the user has permission to view other people on the roster. | 
 **type** | [**List[str]**](str.md)| A list of enrollment types to return. Accepted values are &#39;StudentEnrollment&#39;, &#39;TeacherEnrollment&#39;, &#39;TaEnrollment&#39;, &#39;DesignerEnrollment&#39;, and &#39;ObserverEnrollment.&#39; If omitted, all enrollment types are returned. This argument is ignored if &#x60;role&#x60; is given. | [optional] 
 **role** | [**List[str]**](str.md)| A list of enrollment roles to return. Accepted values include course-level roles created by the {api:RoleOverridesController#add_role Add Role API} as well as the base enrollment types accepted by the &#x60;type&#x60; argument above. | [optional] 
 **state** | [**List[str]**](str.md)| Filter by enrollment state. If omitted, &#39;active&#39; and &#39;invited&#39; enrollments are returned. The following synthetic states are supported only when querying a user&#39;s enrollments (either via user_id argument or via user enrollments endpoint): +current_and_invited+, +current_and_future+, +current_future_and_restricted+, +current_and_concluded+ | [optional] 
 **include** | [**List[str]**](str.md)| Array of additional information to include on the enrollment or user records. \&quot;avatar_url\&quot; and \&quot;group_ids\&quot; will be returned on the user record. If \&quot;current_points\&quot; is specified, the fields \&quot;current_points\&quot; and (if the caller has permissions to manage grades) \&quot;unposted_current_points\&quot; will be included in the \&quot;grades\&quot; hash for student enrollments. | [optional] 
 **grading_period_id** | **int**| Return grades for the given grading_period.  If this parameter is not specified, the returned grades will be for the whole course. | [optional] 
 **enrollment_term_id** | **int**| Returns only enrollments for the specified enrollment term. This parameter only applies to the user enrollments path. May pass the ID from the enrollment terms api or the SIS id prepended with &#39;sis_term_id:&#39;. | [optional] 
 **sis_account_id** | [**List[str]**](str.md)| Returns only enrollments for the specified SIS account ID(s). Does not look into sub_accounts. May pass in array or string. | [optional] 
 **sis_course_id** | [**List[str]**](str.md)| Returns only enrollments matching the specified SIS course ID(s). May pass in array or string. | [optional] 
 **sis_section_id** | [**List[str]**](str.md)| Returns only section enrollments matching the specified SIS section ID(s). May pass in array or string. | [optional] 
 **sis_user_id** | [**List[str]**](str.md)| Returns only enrollments for the specified SIS user ID(s). May pass in array or string. | [optional] 
 **created_for_sis_id** | [**List[bool]**](bool.md)| If sis_user_id is present and created_for_sis_id is true, Returns only enrollments for the specified SIS ID(s). If a user has two sis_id&#39;s, one enrollment may be created using one of the two ids. This would limit the enrollments returned from the endpoint to enrollments that were created from a sis_import with that sis_user_id | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[Enrollment]**](Enrollment.md)

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

# **enrollments_api_last_attended**
> Enrollment enrollments_api_last_attended(course_id, user_id, enrollments_api_last_attended_request=enrollments_api_last_attended_request)

Add last attended date

Add last attended date to student enrollment in course

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.enrollment import Enrollment
from canvas_lms_python_client.models.enrollments_api_last_attended_request import EnrollmentsApiLastAttendedRequest
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
    api_instance = canvas_lms_python_client.EnrollmentsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    user_id = 'user_id_example' # str | Scope response to user_id
    enrollments_api_last_attended_request = canvas_lms_python_client.EnrollmentsApiLastAttendedRequest() # EnrollmentsApiLastAttendedRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/courses/:course_id/user/:user_id/last_attended\"   -X PUT => date=\"Thu%20Dec%2021%202017%2000:00:00%20GMT-0700%20(MST) ``` (optional)

    try:
        # Add last attended date
        api_response = await api_instance.enrollments_api_last_attended(course_id, user_id, enrollments_api_last_attended_request=enrollments_api_last_attended_request)
        print("The response of EnrollmentsApiApi->enrollments_api_last_attended:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmentsApiApi->enrollments_api_last_attended: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **user_id** | **str**| Scope response to user_id | 
 **enrollments_api_last_attended_request** | [**EnrollmentsApiLastAttendedRequest**](EnrollmentsApiLastAttendedRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/courses/:course_id/user/:user_id/last_attended\&quot;   -X PUT &#x3D;&gt; date&#x3D;\&quot;Thu%20Dec%2021%202017%2000:00:00%20GMT-0700%20(MST) &#x60;&#x60;&#x60; | [optional] 

### Return type

[**Enrollment**](Enrollment.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Enrollment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enrollments_api_reactivate**
> Enrollment enrollments_api_reactivate(course_id, id)

Re-activate an enrollment

Activates an inactive enrollment

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.enrollment import Enrollment
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
    api_instance = canvas_lms_python_client.EnrollmentsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id

    try:
        # Re-activate an enrollment
        api_response = await api_instance.enrollments_api_reactivate(course_id, id)
        print("The response of EnrollmentsApiApi->enrollments_api_reactivate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmentsApiApi->enrollments_api_reactivate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**Enrollment**](Enrollment.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Enrollment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enrollments_api_reject**
> EnrollmentsAcceptResponse enrollments_api_reject(course_id, id)

Reject Course Invitation

rejects a pending course invitation for the current user

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.enrollments_accept_response import EnrollmentsAcceptResponse
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
    api_instance = canvas_lms_python_client.EnrollmentsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id

    try:
        # Reject Course Invitation
        api_response = await api_instance.enrollments_api_reject(course_id, id)
        print("The response of EnrollmentsApiApi->enrollments_api_reject:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmentsApiApi->enrollments_api_reject: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**EnrollmentsAcceptResponse**](EnrollmentsAcceptResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | EnrollmentsAcceptResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enrollments_api_show**
> Enrollment enrollments_api_show(account_id, id)

Enrollment by ID

Get an Enrollment object by Enrollment ID

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.enrollment import Enrollment
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
    api_instance = canvas_lms_python_client.EnrollmentsApiApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | The ID of the enrollment object

    try:
        # Enrollment by ID
        api_response = await api_instance.enrollments_api_show(account_id, id)
        print("The response of EnrollmentsApiApi->enrollments_api_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmentsApiApi->enrollments_api_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| The ID of the enrollment object | 

### Return type

[**Enrollment**](Enrollment.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Enrollment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enrollments_api_show_temporary_enrollment_status**
> EnrollmentsShowTemporaryEnrollmentStatusResponse enrollments_api_show_temporary_enrollment_status(user_id, account_id=account_id)

Show Temporary Enrollment recipient and provider status

Returns a JSON Object containing the temporary enrollment status for a user.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.enrollments_show_temporary_enrollment_status_response import EnrollmentsShowTemporaryEnrollmentStatusResponse
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
    api_instance = canvas_lms_python_client.EnrollmentsApiApi(api_client)
    user_id = 'user_id_example' # str | Scope response to user_id
    account_id = 'account_id_example' # str | The ID of the account to check for temporary enrollment status. Defaults to the domain root account if not provided. (optional)

    try:
        # Show Temporary Enrollment recipient and provider status
        api_response = await api_instance.enrollments_api_show_temporary_enrollment_status(user_id, account_id=account_id)
        print("The response of EnrollmentsApiApi->enrollments_api_show_temporary_enrollment_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmentsApiApi->enrollments_api_show_temporary_enrollment_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Scope response to user_id | 
 **account_id** | **str**| The ID of the account to check for temporary enrollment status. Defaults to the domain root account if not provided. | [optional] 

### Return type

[**EnrollmentsShowTemporaryEnrollmentStatusResponse**](EnrollmentsShowTemporaryEnrollmentStatusResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | EnrollmentsShowTemporaryEnrollmentStatusResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

