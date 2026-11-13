# canvas_lms_python_client.CoursesApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**courses_activity_stream**](CoursesApi.md#courses_activity_stream) | **GET** /api/v1/courses/{course_id}/activity_stream | Course activity stream
[**courses_activity_stream_summary**](CoursesApi.md#courses_activity_stream_summary) | **GET** /api/v1/courses/{course_id}/activity_stream/summary | Course activity stream summary
[**courses_api_settings**](CoursesApi.md#courses_api_settings) | **GET** /api/v1/courses/{course_id}/settings | Get course settings
[**courses_batch_update**](CoursesApi.md#courses_batch_update) | **PUT** /api/v1/accounts/{account_id}/courses | Update courses
[**courses_bulk_user_progress**](CoursesApi.md#courses_bulk_user_progress) | **GET** /api/v1/courses/{course_id}/bulk_user_progress | Get bulk user progress
[**courses_content_share_users**](CoursesApi.md#courses_content_share_users) | **GET** /api/v1/courses/{course_id}/content_share_users | Search for content share users
[**courses_create**](CoursesApi.md#courses_create) | **POST** /api/v1/accounts/{account_id}/courses | Create a new course
[**courses_create_file**](CoursesApi.md#courses_create_file) | **POST** /api/v1/courses/{course_id}/files | Upload a file
[**courses_destroy**](CoursesApi.md#courses_destroy) | **DELETE** /api/v1/courses/{id} | Delete/Conclude a course
[**courses_dismiss_migration_limitation_msg**](CoursesApi.md#courses_dismiss_migration_limitation_msg) | **POST** /api/v1/courses/{id}/dismiss_migration_limitation_message | Remove quiz migration alert
[**courses_effective_due_dates**](CoursesApi.md#courses_effective_due_dates) | **GET** /api/v1/courses/{course_id}/effective_due_dates | Get effective due dates
[**courses_index**](CoursesApi.md#courses_index) | **GET** /api/v1/courses | List your courses
[**courses_permissions**](CoursesApi.md#courses_permissions) | **GET** /api/v1/courses/{course_id}/permissions | Permissions
[**courses_preview_html**](CoursesApi.md#courses_preview_html) | **POST** /api/v1/courses/{course_id}/preview_html | Preview processed html
[**courses_recent_students**](CoursesApi.md#courses_recent_students) | **GET** /api/v1/courses/{course_id}/recent_students | List recently logged in students
[**courses_reset_content**](CoursesApi.md#courses_reset_content) | **POST** /api/v1/courses/{course_id}/reset_content | Reset a course
[**courses_restore_version**](CoursesApi.md#courses_restore_version) | **POST** /api/v1/courses/{course_id}/restore/{version_id} | Restore course version
[**courses_show**](CoursesApi.md#courses_show) | **GET** /api/v1/courses/{id} | Get a single course
[**courses_show_for_accounts**](CoursesApi.md#courses_show_for_accounts) | **GET** /api/v1/accounts/{account_id}/courses/{id} | Get a single course
[**courses_student_view_student**](CoursesApi.md#courses_student_view_student) | **GET** /api/v1/courses/{course_id}/student_view_student | Return test student for course
[**courses_students**](CoursesApi.md#courses_students) | **GET** /api/v1/courses/{course_id}/students | List students
[**courses_todo_items**](CoursesApi.md#courses_todo_items) | **GET** /api/v1/courses/{course_id}/todo | Course TODO items
[**courses_update**](CoursesApi.md#courses_update) | **PUT** /api/v1/courses/{id} | Update a course
[**courses_update_settings**](CoursesApi.md#courses_update_settings) | **PUT** /api/v1/courses/{course_id}/settings | Update course settings
[**courses_user**](CoursesApi.md#courses_user) | **GET** /api/v1/courses/{course_id}/users/{id} | Get single user
[**courses_user_index**](CoursesApi.md#courses_user_index) | **GET** /api/v1/users/{user_id}/courses | List courses for a user
[**courses_user_progress**](CoursesApi.md#courses_user_progress) | **GET** /api/v1/courses/{course_id}/users/{user_id}/progress | Get user progress
[**courses_users**](CoursesApi.md#courses_users) | **GET** /api/v1/courses/{course_id}/users | List users in course
[**courses_users_for_courses**](CoursesApi.md#courses_users_for_courses) | **GET** /api/v1/courses/{course_id}/search_users | List users in course


# **courses_activity_stream**
> courses_activity_stream(course_id)

Course activity stream

Returns the current user's course-specific activity stream, paginated.

For full documentation, see the API documentation for the user activity
stream, in the user api.

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
    api_instance = canvas_lms_python_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id

    try:
        # Course activity stream
        await api_instance.courses_activity_stream(course_id)
    except Exception as e:
        print("Exception when calling CoursesApi->courses_activity_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 

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
**0** | Course activity stream |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **courses_activity_stream_summary**
> courses_activity_stream_summary(course_id)

Course activity stream summary

Returns a summary of the current user's course-specific activity stream.

For full documentation, see the API documentation for the user activity
stream summary, in the user api.

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
    api_instance = canvas_lms_python_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id

    try:
        # Course activity stream summary
        await api_instance.courses_activity_stream_summary(course_id)
    except Exception as e:
        print("Exception when calling CoursesApi->courses_activity_stream_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 

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
**0** | Course activity stream summary |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **courses_api_settings**
> courses_api_settings(course_id)

Get course settings

Returns some of a course's settings.

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
    api_instance = canvas_lms_python_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id

    try:
        # Get course settings
        await api_instance.courses_api_settings(course_id)
    except Exception as e:
        print("Exception when calling CoursesApi->courses_api_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 

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
**0** | Get course settings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **courses_batch_update**
> Progress courses_batch_update(account_id, courses_batch_update_request=courses_batch_update_request)

Update courses

Update multiple courses in an account.  Operates asynchronously; use the {api:ProgressController#show progress endpoint}
to query the status of an operation.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.courses_batch_update_request import CoursesBatchUpdateRequest
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
    api_instance = canvas_lms_python_client.CoursesApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    courses_batch_update_request = canvas_lms_python_client.CoursesBatchUpdateRequest() # CoursesBatchUpdateRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/accounts/<account_id>/courses \\   -X PUT \\   -H 'Authorization: Bearer <token>' \\   -d 'event=offer' \\   -d 'course_ids[]=1' \\   -d 'course_ids[]=2' ``` (optional)

    try:
        # Update courses
        api_response = await api_instance.courses_batch_update(account_id, courses_batch_update_request=courses_batch_update_request)
        print("The response of CoursesApi->courses_batch_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->courses_batch_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **courses_batch_update_request** | [**CoursesBatchUpdateRequest**](CoursesBatchUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/accounts/&lt;account_id&gt;/courses \\   -X PUT \\   -H &#39;Authorization: Bearer &lt;token&gt;&#39; \\   -d &#39;event&#x3D;offer&#39; \\   -d &#39;course_ids[]&#x3D;1&#39; \\   -d &#39;course_ids[]&#x3D;2&#39; &#x60;&#x60;&#x60; | [optional] 

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

# **courses_bulk_user_progress**
> List[UserProgress] courses_bulk_user_progress(course_id, page=page, per_page=per_page)

Get bulk user progress

Returns progress information for all users enrolled in the given course.

You must be a user who has permission to view all grades in the course (such as a teacher or administrator).

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.user_progress import UserProgress
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
    api_instance = canvas_lms_python_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # Get bulk user progress
        api_response = await api_instance.courses_bulk_user_progress(course_id, page=page, per_page=per_page)
        print("The response of CoursesApi->courses_bulk_user_progress:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->courses_bulk_user_progress: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[UserProgress]**](UserProgress.md)

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

# **courses_content_share_users**
> List[User] courses_content_share_users(course_id, search_term, page=page, per_page=per_page)

Search for content share users

Returns a paginated list of users you can share content with.  Requires the content share
feature and the user must have the manage content permission for the course.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.user import User
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
    api_instance = canvas_lms_python_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    search_term = 'search_term_example' # str | Term used to find users.  Will search available share users with the search term in their name.
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # Search for content share users
        api_response = await api_instance.courses_content_share_users(course_id, search_term, page=page, per_page=per_page)
        print("The response of CoursesApi->courses_content_share_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->courses_content_share_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **search_term** | **str**| Term used to find users.  Will search available share users with the search term in their name. | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[User]**](User.md)

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

# **courses_create**
> Course courses_create(account_id, courses_create_request=courses_create_request)

Create a new course

Create a new course

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.course import Course
from canvas_lms_python_client.models.courses_create_request import CoursesCreateRequest
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
    api_instance = canvas_lms_python_client.CoursesApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    courses_create_request = canvas_lms_python_client.CoursesCreateRequest() # CoursesCreateRequest | Request body parameters (optional)

    try:
        # Create a new course
        api_response = await api_instance.courses_create(account_id, courses_create_request=courses_create_request)
        print("The response of CoursesApi->courses_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->courses_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **courses_create_request** | [**CoursesCreateRequest**](CoursesCreateRequest.md)| Request body parameters | [optional] 

### Return type

[**Course**](Course.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Course |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **courses_create_file**
> courses_create_file(course_id)

Upload a file

Upload a file to the course.

This API endpoint is the first step in uploading a file to a course.
See the {file:file.file_uploads.html File Upload Documentation} for details on
the file upload workflow.

Only those with the "Manage Files" permission on a course can upload files
to the course. By default, this is Teachers, TAs and Designers.

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
    api_instance = canvas_lms_python_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id

    try:
        # Upload a file
        await api_instance.courses_create_file(course_id)
    except Exception as e:
        print("Exception when calling CoursesApi->courses_create_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 

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
**0** | Upload a file |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **courses_destroy**
> courses_destroy(id, event)

Delete/Conclude a course

Delete or conclude an existing course

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
    api_instance = canvas_lms_python_client.CoursesApi(api_client)
    id = 'id_example' # str | Scope response to id
    event = 'event_example' # str | The action to take on the course.

    try:
        # Delete/Conclude a course
        await api_instance.courses_destroy(id, event)
    except Exception as e:
        print("Exception when calling CoursesApi->courses_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **event** | **str**| The action to take on the course. | 

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
**0** | Delete/Conclude a course |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **courses_dismiss_migration_limitation_msg**
> courses_dismiss_migration_limitation_msg(id)

Remove quiz migration alert

Remove alert about the limitations of quiz migrations that is displayed
to a user in a course

you must be logged in to use this endpoint

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
    api_instance = canvas_lms_python_client.CoursesApi(api_client)
    id = 'id_example' # str | Scope response to id

    try:
        # Remove quiz migration alert
        await api_instance.courses_dismiss_migration_limitation_msg(id)
    except Exception as e:
        print("Exception when calling CoursesApi->courses_dismiss_migration_limitation_msg: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 

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
**0** | Remove quiz migration alert |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **courses_effective_due_dates**
> courses_effective_due_dates(course_id, assignment_ids=assignment_ids)

Get effective due dates

For each assignment in the course, returns each assigned student's ID
and their corresponding due date along with some grading period data.
Returns a collection with keys representing assignment IDs and values as a
collection containing keys representing student IDs and values representing
the student's effective due_at, the grading_period_id of which the due_at falls
in, and whether or not the grading period is closed (in_closed_grading_period)

The list of assignment IDs for which effective student due dates are
requested. If not provided, all assignments in the course will be used.

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
    api_instance = canvas_lms_python_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    assignment_ids = ['assignment_ids_example'] # List[str] |  (optional)

    try:
        # Get effective due dates
        await api_instance.courses_effective_due_dates(course_id, assignment_ids=assignment_ids)
    except Exception as e:
        print("Exception when calling CoursesApi->courses_effective_due_dates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **assignment_ids** | [**List[str]**](str.md)|  | [optional] 

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
**0** | Get effective due dates |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **courses_index**
> List[Course] courses_index(enrollment_type=enrollment_type, enrollment_role=enrollment_role, enrollment_role_id=enrollment_role_id, enrollment_state=enrollment_state, exclude_blueprint_courses=exclude_blueprint_courses, include=include, state=state, page=page, per_page=per_page)

List your courses

Returns the paginated list of active courses for the current user.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.course import Course
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
    api_instance = canvas_lms_python_client.CoursesApi(api_client)
    enrollment_type = 'enrollment_type_example' # str | When set, only return courses where the user is enrolled as this type. For example, set to \"teacher\" to return only courses where the user is enrolled as a Teacher.  This argument is ignored if enrollment_role is given. (optional)
    enrollment_role = 'enrollment_role_example' # str | Deprecated When set, only return courses where the user is enrolled with the specified course-level role.  This can be a role created with the {api:RoleOverridesController#add_role Add Role API} or a base role type of 'StudentEnrollment', 'TeacherEnrollment', 'TaEnrollment', 'ObserverEnrollment', or 'DesignerEnrollment'. (optional)
    enrollment_role_id = 56 # int | When set, only return courses where the user is enrolled with the specified course-level role.  This can be a role created with the {api:RoleOverridesController#add_role Add Role API} or a built_in role type of 'StudentEnrollment', 'TeacherEnrollment', 'TaEnrollment', 'ObserverEnrollment', or 'DesignerEnrollment'. (optional)
    enrollment_state = 'enrollment_state_example' # str | When set, only return courses where the user has an enrollment with the given state. This will respect section/course/term date overrides. (optional)
    exclude_blueprint_courses = True # bool | When set, only return courses that are not configured as blueprint courses. (optional)
    include = ['include_example'] # List[str] | - \"needs_grading_count\": Optional information to include with each Course.   When needs_grading_count is given, and the current user has grading   rights, the total number of submissions needing grading for all   assignments is returned. - \"syllabus_body\": Optional information to include with each Course.   When syllabus_body is given the user-generated html for the course   syllabus is returned. - \"public_description\": Optional information to include with each Course.   When public_description is given the user-generated text for the course   public description is returned. - \"total_scores\": Optional information to include with each Course.   When total_scores is given, any student enrollments will also   include the fields 'computed_current_score', 'computed_final_score',   'computed_current_grade', and 'computed_final_grade', as well as (if   the user has permission) 'unposted_current_score',   'unposted_final_score', 'unposted_current_grade', and   'unposted_final_grade' (see Enrollment documentation for more   information on these fields). This argument is ignored if the course is   configured to hide final grades. - \"current_grading_period_scores\": Optional information to include with   each Course. When current_grading_period_scores is given and total_scores   is given, any student enrollments will also include the fields   'has_grading_periods',   'totals_for_all_grading_periods_option', 'current_grading_period_title',   'current_grading_period_id', current_period_computed_current_score',   'current_period_computed_final_score',   'current_period_computed_current_grade', and   'current_period_computed_final_grade', as well as (if the user has permission)   'current_period_unposted_current_score',   'current_period_unposted_final_score',   'current_period_unposted_current_grade', and   'current_period_unposted_final_grade' (see Enrollment documentation for   more information on these fields). In addition, when this argument is   passed, the course will have a 'has_grading_periods' attribute   on it. This argument is ignored if the total_scores argument is not   included. If the course is configured to hide final grades, the   following fields are not returned:   'totals_for_all_grading_periods_option',   'current_period_computed_current_score',   'current_period_computed_final_score',   'current_period_computed_current_grade',   'current_period_computed_final_grade',   'current_period_unposted_current_score',   'current_period_unposted_final_score',   'current_period_unposted_current_grade', and   'current_period_unposted_final_grade' - \"grading_periods\": Optional information to include with each Course. When   grading_periods is given, a list of the grading periods associated with   each course is returned. - \"term\": Optional information to include with each Course. When   term is given, the information for the enrollment term for each course   is returned. - \"account\": Optional information to include with each Course. When   account is given, the account json for each course is returned. - \"course_progress\": Optional information to include with each Course.   When course_progress is given, each course will include a   'course_progress' object with the fields: 'requirement_count', an integer   specifying the total number of requirements in the course,   'requirement_completed_count', an integer specifying the total number of   requirements in this course that have been completed, and   'next_requirement_url', a string url to the next requirement item, and   'completed_at', the date the course was completed (null if incomplete).   'next_requirement_url' will be null if all requirements have been   completed or the current module does not require sequential progress.   \"course_progress\" will return an error message if the course is not   module based or the user is not enrolled as a student in the course. - \"sections\": Section enrollment information to include with each Course.   Returns an array of hashes containing the section ID (id), section name   (name), start and end dates (start_at, end_at), as well as the enrollment   type (enrollment_role, e.g. 'StudentEnrollment'). - \"storage_quota_used_mb\": The amount of storage space used by the files in this course - \"total_students\": Optional information to include with each Course.   Returns an integer for the total amount of active and invited students. - \"passback_status\": Include the grade passback_status - \"favorites\": Optional information to include with each Course.   Indicates if the user has marked the course as a favorite course. - \"teachers\": Teacher information to include with each Course.   Returns an array of hashes containing the {api:Users:UserDisplay UserDisplay} information   for each teacher in the course. - \"observed_users\": Optional information to include with each Course.   Will include data for observed users if the current user has an   observer enrollment. - \"tabs\": Optional information to include with each Course.   Will include the list of tabs configured for each course.  See the   {api:TabsController#index List available tabs API} for more information. - \"course_image\": Optional information to include with each Course. Returns course   image url if a course image has been set. - \"banner_image\": Optional information to include with each Course. Returns course   banner image url if the course is a Canvas for Elementary subject and a banner   image has been set. - \"concluded\": Optional information to include with each Course. Indicates whether   the course has been concluded, taking course and term dates into account. - \"post_manually\": Optional information to include with each Course. Returns true if   the course post policy is set to Manually post grades. Returns false if the the course   post policy is set to Automatically post grades. (optional)
    state = ['state_example'] # List[str] | If set, only return courses that are in the given state(s). By default, \"available\" is returned for students and observers, and anything except \"deleted\", for all other enrollment types (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List your courses
        api_response = await api_instance.courses_index(enrollment_type=enrollment_type, enrollment_role=enrollment_role, enrollment_role_id=enrollment_role_id, enrollment_state=enrollment_state, exclude_blueprint_courses=exclude_blueprint_courses, include=include, state=state, page=page, per_page=per_page)
        print("The response of CoursesApi->courses_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->courses_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enrollment_type** | **str**| When set, only return courses where the user is enrolled as this type. For example, set to \&quot;teacher\&quot; to return only courses where the user is enrolled as a Teacher.  This argument is ignored if enrollment_role is given. | [optional] 
 **enrollment_role** | **str**| Deprecated When set, only return courses where the user is enrolled with the specified course-level role.  This can be a role created with the {api:RoleOverridesController#add_role Add Role API} or a base role type of &#39;StudentEnrollment&#39;, &#39;TeacherEnrollment&#39;, &#39;TaEnrollment&#39;, &#39;ObserverEnrollment&#39;, or &#39;DesignerEnrollment&#39;. | [optional] 
 **enrollment_role_id** | **int**| When set, only return courses where the user is enrolled with the specified course-level role.  This can be a role created with the {api:RoleOverridesController#add_role Add Role API} or a built_in role type of &#39;StudentEnrollment&#39;, &#39;TeacherEnrollment&#39;, &#39;TaEnrollment&#39;, &#39;ObserverEnrollment&#39;, or &#39;DesignerEnrollment&#39;. | [optional] 
 **enrollment_state** | **str**| When set, only return courses where the user has an enrollment with the given state. This will respect section/course/term date overrides. | [optional] 
 **exclude_blueprint_courses** | **bool**| When set, only return courses that are not configured as blueprint courses. | [optional] 
 **include** | [**List[str]**](str.md)| - \&quot;needs_grading_count\&quot;: Optional information to include with each Course.   When needs_grading_count is given, and the current user has grading   rights, the total number of submissions needing grading for all   assignments is returned. - \&quot;syllabus_body\&quot;: Optional information to include with each Course.   When syllabus_body is given the user-generated html for the course   syllabus is returned. - \&quot;public_description\&quot;: Optional information to include with each Course.   When public_description is given the user-generated text for the course   public description is returned. - \&quot;total_scores\&quot;: Optional information to include with each Course.   When total_scores is given, any student enrollments will also   include the fields &#39;computed_current_score&#39;, &#39;computed_final_score&#39;,   &#39;computed_current_grade&#39;, and &#39;computed_final_grade&#39;, as well as (if   the user has permission) &#39;unposted_current_score&#39;,   &#39;unposted_final_score&#39;, &#39;unposted_current_grade&#39;, and   &#39;unposted_final_grade&#39; (see Enrollment documentation for more   information on these fields). This argument is ignored if the course is   configured to hide final grades. - \&quot;current_grading_period_scores\&quot;: Optional information to include with   each Course. When current_grading_period_scores is given and total_scores   is given, any student enrollments will also include the fields   &#39;has_grading_periods&#39;,   &#39;totals_for_all_grading_periods_option&#39;, &#39;current_grading_period_title&#39;,   &#39;current_grading_period_id&#39;, current_period_computed_current_score&#39;,   &#39;current_period_computed_final_score&#39;,   &#39;current_period_computed_current_grade&#39;, and   &#39;current_period_computed_final_grade&#39;, as well as (if the user has permission)   &#39;current_period_unposted_current_score&#39;,   &#39;current_period_unposted_final_score&#39;,   &#39;current_period_unposted_current_grade&#39;, and   &#39;current_period_unposted_final_grade&#39; (see Enrollment documentation for   more information on these fields). In addition, when this argument is   passed, the course will have a &#39;has_grading_periods&#39; attribute   on it. This argument is ignored if the total_scores argument is not   included. If the course is configured to hide final grades, the   following fields are not returned:   &#39;totals_for_all_grading_periods_option&#39;,   &#39;current_period_computed_current_score&#39;,   &#39;current_period_computed_final_score&#39;,   &#39;current_period_computed_current_grade&#39;,   &#39;current_period_computed_final_grade&#39;,   &#39;current_period_unposted_current_score&#39;,   &#39;current_period_unposted_final_score&#39;,   &#39;current_period_unposted_current_grade&#39;, and   &#39;current_period_unposted_final_grade&#39; - \&quot;grading_periods\&quot;: Optional information to include with each Course. When   grading_periods is given, a list of the grading periods associated with   each course is returned. - \&quot;term\&quot;: Optional information to include with each Course. When   term is given, the information for the enrollment term for each course   is returned. - \&quot;account\&quot;: Optional information to include with each Course. When   account is given, the account json for each course is returned. - \&quot;course_progress\&quot;: Optional information to include with each Course.   When course_progress is given, each course will include a   &#39;course_progress&#39; object with the fields: &#39;requirement_count&#39;, an integer   specifying the total number of requirements in the course,   &#39;requirement_completed_count&#39;, an integer specifying the total number of   requirements in this course that have been completed, and   &#39;next_requirement_url&#39;, a string url to the next requirement item, and   &#39;completed_at&#39;, the date the course was completed (null if incomplete).   &#39;next_requirement_url&#39; will be null if all requirements have been   completed or the current module does not require sequential progress.   \&quot;course_progress\&quot; will return an error message if the course is not   module based or the user is not enrolled as a student in the course. - \&quot;sections\&quot;: Section enrollment information to include with each Course.   Returns an array of hashes containing the section ID (id), section name   (name), start and end dates (start_at, end_at), as well as the enrollment   type (enrollment_role, e.g. &#39;StudentEnrollment&#39;). - \&quot;storage_quota_used_mb\&quot;: The amount of storage space used by the files in this course - \&quot;total_students\&quot;: Optional information to include with each Course.   Returns an integer for the total amount of active and invited students. - \&quot;passback_status\&quot;: Include the grade passback_status - \&quot;favorites\&quot;: Optional information to include with each Course.   Indicates if the user has marked the course as a favorite course. - \&quot;teachers\&quot;: Teacher information to include with each Course.   Returns an array of hashes containing the {api:Users:UserDisplay UserDisplay} information   for each teacher in the course. - \&quot;observed_users\&quot;: Optional information to include with each Course.   Will include data for observed users if the current user has an   observer enrollment. - \&quot;tabs\&quot;: Optional information to include with each Course.   Will include the list of tabs configured for each course.  See the   {api:TabsController#index List available tabs API} for more information. - \&quot;course_image\&quot;: Optional information to include with each Course. Returns course   image url if a course image has been set. - \&quot;banner_image\&quot;: Optional information to include with each Course. Returns course   banner image url if the course is a Canvas for Elementary subject and a banner   image has been set. - \&quot;concluded\&quot;: Optional information to include with each Course. Indicates whether   the course has been concluded, taking course and term dates into account. - \&quot;post_manually\&quot;: Optional information to include with each Course. Returns true if   the course post policy is set to Manually post grades. Returns false if the the course   post policy is set to Automatically post grades. | [optional] 
 **state** | [**List[str]**](str.md)| If set, only return courses that are in the given state(s). By default, \&quot;available\&quot; is returned for students and observers, and anything except \&quot;deleted\&quot;, for all other enrollment types | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[Course]**](Course.md)

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

# **courses_permissions**
> courses_permissions(course_id, permissions=permissions)

Permissions

Returns permission information for the calling user in the given course.
See also the {api:AccountsController#permissions Account} and
{api:GroupsController#permissions Group} counterparts.

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
    api_instance = canvas_lms_python_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    permissions = ['permissions_example'] # List[str] | List of permissions to check against the authenticated user. Permission names are documented in the {api:RoleOverridesController#manageable_permissions List assignable permissions} endpoint. (optional)

    try:
        # Permissions
        await api_instance.courses_permissions(course_id, permissions=permissions)
    except Exception as e:
        print("Exception when calling CoursesApi->courses_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **permissions** | [**List[str]**](str.md)| List of permissions to check against the authenticated user. Permission names are documented in the {api:RoleOverridesController#manageable_permissions List assignable permissions} endpoint. | [optional] 

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
**0** | Permissions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **courses_preview_html**
> courses_preview_html(course_id, courses_preview_html_request=courses_preview_html_request)

Preview processed html

Preview html content processed for this course

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.courses_preview_html_request import CoursesPreviewHtmlRequest
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
    api_instance = canvas_lms_python_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    courses_preview_html_request = canvas_lms_python_client.CoursesPreviewHtmlRequest() # CoursesPreviewHtmlRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/courses/<course_id>/preview_html \\      -F 'html=<p><badhtml></badhtml>processed html</p>' \\      -H 'Authorization: Bearer <token>' ``` (optional)

    try:
        # Preview processed html
        await api_instance.courses_preview_html(course_id, courses_preview_html_request=courses_preview_html_request)
    except Exception as e:
        print("Exception when calling CoursesApi->courses_preview_html: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **courses_preview_html_request** | [**CoursesPreviewHtmlRequest**](CoursesPreviewHtmlRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/courses/&lt;course_id&gt;/preview_html \\      -F &#39;html&#x3D;&lt;p&gt;&lt;badhtml&gt;&lt;/badhtml&gt;processed html&lt;/p&gt;&#39; \\      -H &#39;Authorization: Bearer &lt;token&gt;&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Preview processed html |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **courses_recent_students**
> List[User] courses_recent_students(course_id, page=page, per_page=per_page)

List recently logged in students

Returns the paginated list of users in this course, ordered by how recently they have
logged in. The records include the 'last_login' field which contains
a timestamp of the last time that user logged into canvas.  The querying
user must have the 'View usage reports' permission.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.user import User
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
    api_instance = canvas_lms_python_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List recently logged in students
        api_response = await api_instance.courses_recent_students(course_id, page=page, per_page=per_page)
        print("The response of CoursesApi->courses_recent_students:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->courses_recent_students: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[User]**](User.md)

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

# **courses_reset_content**
> Course courses_reset_content(course_id)

Reset a course

Deletes the current course, and creates a new equivalent course with
no content, but all sections and users moved over.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.course import Course
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
    api_instance = canvas_lms_python_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id

    try:
        # Reset a course
        api_response = await api_instance.courses_reset_content(course_id)
        print("The response of CoursesApi->courses_reset_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->courses_reset_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 

### Return type

[**Course**](Course.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Course |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **courses_restore_version**
> Course courses_restore_version(course_id, version_id)

Restore course version

Restore a course to a prior version.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.course import Course
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
    api_instance = canvas_lms_python_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    version_id = 'version_id_example' # str | The version to restore to (use the syllabus_versions include parameter in the course show API to see available versions)

    try:
        # Restore course version
        api_response = await api_instance.courses_restore_version(course_id, version_id)
        print("The response of CoursesApi->courses_restore_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->courses_restore_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **version_id** | **str**| The version to restore to (use the syllabus_versions include parameter in the course show API to see available versions) | 

### Return type

[**Course**](Course.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Course |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **courses_show**
> Course courses_show(id, include=include, teacher_limit=teacher_limit)

Get a single course

Return information on a single course.

Accepts the same include[] parameters as the list action plus:

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.course import Course
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
    api_instance = canvas_lms_python_client.CoursesApi(api_client)
    id = 'id_example' # str | Scope response to id
    include = ['include_example'] # List[str] | - \"all_courses\": Also search recently deleted courses. - \"permissions\": Include permissions the current user has   for the course. - \"observed_users\": Include observed users in the enrollments - \"course_image\": Include course image url if a course image has been set - \"banner_image\": Include course banner image url if the course is a Canvas for   Elementary subject and a banner image has been set - \"concluded\": Optional information to include with Course. Indicates whether   the course has been concluded, taking course and term dates into account. - \"lti_context_id\": Include course LTI tool id. - \"post_manually\": Include course post policy. If the post policy is manually post grades,   the value will be true. If the post policy is automatically post grades, the value will be false. (optional)
    teacher_limit = 56 # int | The maximum number of teacher enrollments to show. If the course contains more teachers than this, instead of giving the teacher enrollments, the count of teachers will be given under a _teacher_count_ key. (optional)

    try:
        # Get a single course
        api_response = await api_instance.courses_show(id, include=include, teacher_limit=teacher_limit)
        print("The response of CoursesApi->courses_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->courses_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **include** | [**List[str]**](str.md)| - \&quot;all_courses\&quot;: Also search recently deleted courses. - \&quot;permissions\&quot;: Include permissions the current user has   for the course. - \&quot;observed_users\&quot;: Include observed users in the enrollments - \&quot;course_image\&quot;: Include course image url if a course image has been set - \&quot;banner_image\&quot;: Include course banner image url if the course is a Canvas for   Elementary subject and a banner image has been set - \&quot;concluded\&quot;: Optional information to include with Course. Indicates whether   the course has been concluded, taking course and term dates into account. - \&quot;lti_context_id\&quot;: Include course LTI tool id. - \&quot;post_manually\&quot;: Include course post policy. If the post policy is manually post grades,   the value will be true. If the post policy is automatically post grades, the value will be false. | [optional] 
 **teacher_limit** | **int**| The maximum number of teacher enrollments to show. If the course contains more teachers than this, instead of giving the teacher enrollments, the count of teachers will be given under a _teacher_count_ key. | [optional] 

### Return type

[**Course**](Course.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Course |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **courses_show_for_accounts**
> Course courses_show_for_accounts(account_id, id, include=include, teacher_limit=teacher_limit)

Get a single course

Return information on a single course.

Accepts the same include[] parameters as the list action plus:

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.course import Course
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
    api_instance = canvas_lms_python_client.CoursesApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id
    include = ['include_example'] # List[str] | - \"all_courses\": Also search recently deleted courses. - \"permissions\": Include permissions the current user has   for the course. - \"observed_users\": Include observed users in the enrollments - \"course_image\": Include course image url if a course image has been set - \"banner_image\": Include course banner image url if the course is a Canvas for   Elementary subject and a banner image has been set - \"concluded\": Optional information to include with Course. Indicates whether   the course has been concluded, taking course and term dates into account. - \"lti_context_id\": Include course LTI tool id. - \"post_manually\": Include course post policy. If the post policy is manually post grades,   the value will be true. If the post policy is automatically post grades, the value will be false. (optional)
    teacher_limit = 56 # int | The maximum number of teacher enrollments to show. If the course contains more teachers than this, instead of giving the teacher enrollments, the count of teachers will be given under a _teacher_count_ key. (optional)

    try:
        # Get a single course
        api_response = await api_instance.courses_show_for_accounts(account_id, id, include=include, teacher_limit=teacher_limit)
        print("The response of CoursesApi->courses_show_for_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->courses_show_for_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 
 **include** | [**List[str]**](str.md)| - \&quot;all_courses\&quot;: Also search recently deleted courses. - \&quot;permissions\&quot;: Include permissions the current user has   for the course. - \&quot;observed_users\&quot;: Include observed users in the enrollments - \&quot;course_image\&quot;: Include course image url if a course image has been set - \&quot;banner_image\&quot;: Include course banner image url if the course is a Canvas for   Elementary subject and a banner image has been set - \&quot;concluded\&quot;: Optional information to include with Course. Indicates whether   the course has been concluded, taking course and term dates into account. - \&quot;lti_context_id\&quot;: Include course LTI tool id. - \&quot;post_manually\&quot;: Include course post policy. If the post policy is manually post grades,   the value will be true. If the post policy is automatically post grades, the value will be false. | [optional] 
 **teacher_limit** | **int**| The maximum number of teacher enrollments to show. If the course contains more teachers than this, instead of giving the teacher enrollments, the count of teachers will be given under a _teacher_count_ key. | [optional] 

### Return type

[**Course**](Course.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Course |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **courses_student_view_student**
> User courses_student_view_student(course_id)

Return test student for course

Returns information for a test student in this course. Creates a test
student if one does not already exist for the course. The caller must have
permission to access the course's student view.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.user import User
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
    api_instance = canvas_lms_python_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id

    try:
        # Return test student for course
        api_response = await api_instance.courses_student_view_student(course_id)
        print("The response of CoursesApi->courses_student_view_student:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->courses_student_view_student: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 

### Return type

[**User**](User.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | User |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **courses_students**
> List[User] courses_students(course_id)

List students

Returns the paginated list of students enrolled in this course.

DEPRECATED: Please use the {api:CoursesController#users course users} endpoint
and pass "student" as the enrollment_type.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.user import User
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
    api_instance = canvas_lms_python_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id

    try:
        # List students
        api_response = await api_instance.courses_students(course_id)
        print("The response of CoursesApi->courses_students:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->courses_students: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 

### Return type

[**List[User]**](User.md)

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

# **courses_todo_items**
> List[TodoItem] courses_todo_items(course_id, page=page, per_page=per_page)

Course TODO items

Returns the current user's course-specific todo items.

For full documentation, see the API documentation for the user todo items, in the user api.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.todo_item import TodoItem
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
    api_instance = canvas_lms_python_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # Course TODO items
        api_response = await api_instance.courses_todo_items(course_id, page=page, per_page=per_page)
        print("The response of CoursesApi->courses_todo_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->courses_todo_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[TodoItem]**](TodoItem.md)

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

# **courses_update**
> courses_update(id, courses_update_request=courses_update_request)

Update a course

Update an existing course.

Arguments are the same as Courses#create, with a few exceptions (enroll_me).

If a user has content management rights, but not full course editing rights, the only attribute
editable through this endpoint will be "syllabus_body"

If an account has set prevent_course_availability_editing_by_teachers, a teacher cannot change
+course[start_at]+, +course[conclude_at]+, or +course[restrict_enrollments_to_course_dates]+ here.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.courses_update_request import CoursesUpdateRequest
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
    api_instance = canvas_lms_python_client.CoursesApi(api_client)
    id = 'id_example' # str | Scope response to id
    courses_update_request = canvas_lms_python_client.CoursesUpdateRequest() # CoursesUpdateRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/courses/<course_id> \\   -X PUT \\   -H 'Authorization: Bearer <token>' \\   -d 'course[name]=New course name' \\   -d 'course[start_at]=2012-05-05T00:00:00Z' ``` (optional)

    try:
        # Update a course
        await api_instance.courses_update(id, courses_update_request=courses_update_request)
    except Exception as e:
        print("Exception when calling CoursesApi->courses_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **courses_update_request** | [**CoursesUpdateRequest**](CoursesUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/courses/&lt;course_id&gt; \\   -X PUT \\   -H &#39;Authorization: Bearer &lt;token&gt;&#39; \\   -d &#39;course[name]&#x3D;New course name&#39; \\   -d &#39;course[start_at]&#x3D;2012-05-05T00:00:00Z&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Update a course |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **courses_update_settings**
> courses_update_settings(course_id, courses_update_settings_request=courses_update_settings_request)

Update course settings

Can update the following course settings:

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.courses_update_settings_request import CoursesUpdateSettingsRequest
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
    api_instance = canvas_lms_python_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    courses_update_settings_request = canvas_lms_python_client.CoursesUpdateSettingsRequest() # CoursesUpdateSettingsRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/courses/<course_id>/settings \\   -X PUT \\   -H 'Authorization: Bearer <token>' \\   -d 'allow_student_discussion_topics=false' ``` (optional)

    try:
        # Update course settings
        await api_instance.courses_update_settings(course_id, courses_update_settings_request=courses_update_settings_request)
    except Exception as e:
        print("Exception when calling CoursesApi->courses_update_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **courses_update_settings_request** | [**CoursesUpdateSettingsRequest**](CoursesUpdateSettingsRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/courses/&lt;course_id&gt;/settings \\   -X PUT \\   -H &#39;Authorization: Bearer &lt;token&gt;&#39; \\   -d &#39;allow_student_discussion_topics&#x3D;false&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Update course settings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **courses_user**
> User courses_user(course_id, id)

Get single user

Return information on a single user.

Accepts the same include[] parameters as the :users: action, and returns a
single user with the same fields as that action.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.user import User
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
    api_instance = canvas_lms_python_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id

    try:
        # Get single user
        api_response = await api_instance.courses_user(course_id, id)
        print("The response of CoursesApi->courses_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->courses_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**User**](User.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | User |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **courses_user_index**
> List[Course] courses_user_index(user_id, include=include, state=state, enrollment_state=enrollment_state, homeroom=homeroom, account_id=account_id, page=page, per_page=per_page)

List courses for a user

Returns a paginated list of active courses for this user. To view the course list for a user other than yourself, you must be either an observer of that user or an administrator.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.course import Course
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
    api_instance = canvas_lms_python_client.CoursesApi(api_client)
    user_id = 'user_id_example' # str | Scope response to user_id
    include = ['include_example'] # List[str] | - \"needs_grading_count\": Optional information to include with each Course.   When needs_grading_count is given, and the current user has grading   rights, the total number of submissions needing grading for all   assignments is returned. - \"syllabus_body\": Optional information to include with each Course.   When syllabus_body is given the user-generated html for the course   syllabus is returned. - \"public_description\": Optional information to include with each Course.   When public_description is given the user-generated text for the course   public description is returned. - \"total_scores\": Optional information to include with each Course.   When total_scores is given, any student enrollments will also   include the fields 'computed_current_score', 'computed_final_score',   'computed_current_grade', and 'computed_final_grade' (see Enrollment   documentation for more information on these fields). This argument   is ignored if the course is configured to hide final grades. - \"current_grading_period_scores\": Optional information to include with   each Course. When current_grading_period_scores is given and total_scores   is given, any student enrollments will also include the fields   'has_grading_periods',   'totals_for_all_grading_periods_option', 'current_grading_period_title',   'current_grading_period_id', current_period_computed_current_score',   'current_period_computed_final_score',   'current_period_computed_current_grade', and   'current_period_computed_final_grade', as well as (if the user has permission)   'current_period_unposted_current_score',   'current_period_unposted_final_score',   'current_period_unposted_current_grade', and   'current_period_unposted_final_grade' (see Enrollment documentation for   more information on these fields). In addition, when this argument is   passed, the course will have a 'has_grading_periods' attribute   on it. This argument is ignored if the course is configured to hide final   grades or if the total_scores argument is not included. - \"grading_periods\": Optional information to include with each Course. When   grading_periods is given, a list of the grading periods associated with   each course is returned. - \"term\": Optional information to include with each Course. When   term is given, the information for the enrollment term for each course   is returned. - \"account\": Optional information to include with each Course. When   account is given, the account json for each course is returned. - \"course_progress\": Optional information to include with each Course.   When course_progress is given, each course will include a   'course_progress' object with the fields: 'requirement_count', an integer   specifying the total number of requirements in the course,   'requirement_completed_count', an integer specifying the total number of   requirements in this course that have been completed, and   'next_requirement_url', a string url to the next requirement item, and   'completed_at', the date the course was completed (null if incomplete).   'next_requirement_url' will be null if all requirements have been   completed or the current module does not require sequential progress.   \"course_progress\" will return an error message if the course is not   module based or the user is not enrolled as a student in the course. - \"sections\": Section enrollment information to include with each Course.   Returns an array of hashes containing the section ID (id), section name   (name), start and end dates (start_at, end_at), as well as the enrollment   type (enrollment_role, e.g. 'StudentEnrollment'). - \"storage_quota_used_mb\": The amount of storage space used by the files in this course - \"total_students\": Optional information to include with each Course.   Returns an integer for the total amount of active and invited students. - \"passback_status\": Include the grade passback_status - \"favorites\": Optional information to include with each Course.   Indicates if the user has marked the course as a favorite course. - \"teachers\": Teacher information to include with each Course.   Returns an array of hashes containing the {api:Users:UserDisplay UserDisplay} information   for each teacher in the course. - \"observed_users\": Optional information to include with each Course.   Will include data for observed users if the current user has an   observer enrollment. - \"tabs\": Optional information to include with each Course.   Will include the list of tabs configured for each course.  See the   {api:TabsController#index List available tabs API} for more information. - \"course_image\": Optional information to include with each Course. Returns course   image url if a course image has been set. - \"banner_image\": Optional information to include with each Course. Returns course   banner image url if the course is a Canvas for Elementary subject and a banner   image has been set. - \"concluded\": Optional information to include with each Course. Indicates whether   the course has been concluded, taking course and term dates into account. - \"post_manually\": Optional information to include with each Course. Returns true if   the course post policy is set to \"Manually\". Returns false if the the course post   policy is set to \"Automatically\". (optional)
    state = ['state_example'] # List[str] | If set, only return courses that are in the given state(s). By default, \"available\" is returned for students and observers, and anything except \"deleted\", for all other enrollment types (optional)
    enrollment_state = 'enrollment_state_example' # str | When set, only return courses where the user has an enrollment with the given state. This will respect section/course/term date overrides. (optional)
    homeroom = True # bool | If set, only return homeroom courses. (optional)
    account_id = 'account_id_example' # str | If set, only include courses associated with this account (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List courses for a user
        api_response = await api_instance.courses_user_index(user_id, include=include, state=state, enrollment_state=enrollment_state, homeroom=homeroom, account_id=account_id, page=page, per_page=per_page)
        print("The response of CoursesApi->courses_user_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->courses_user_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Scope response to user_id | 
 **include** | [**List[str]**](str.md)| - \&quot;needs_grading_count\&quot;: Optional information to include with each Course.   When needs_grading_count is given, and the current user has grading   rights, the total number of submissions needing grading for all   assignments is returned. - \&quot;syllabus_body\&quot;: Optional information to include with each Course.   When syllabus_body is given the user-generated html for the course   syllabus is returned. - \&quot;public_description\&quot;: Optional information to include with each Course.   When public_description is given the user-generated text for the course   public description is returned. - \&quot;total_scores\&quot;: Optional information to include with each Course.   When total_scores is given, any student enrollments will also   include the fields &#39;computed_current_score&#39;, &#39;computed_final_score&#39;,   &#39;computed_current_grade&#39;, and &#39;computed_final_grade&#39; (see Enrollment   documentation for more information on these fields). This argument   is ignored if the course is configured to hide final grades. - \&quot;current_grading_period_scores\&quot;: Optional information to include with   each Course. When current_grading_period_scores is given and total_scores   is given, any student enrollments will also include the fields   &#39;has_grading_periods&#39;,   &#39;totals_for_all_grading_periods_option&#39;, &#39;current_grading_period_title&#39;,   &#39;current_grading_period_id&#39;, current_period_computed_current_score&#39;,   &#39;current_period_computed_final_score&#39;,   &#39;current_period_computed_current_grade&#39;, and   &#39;current_period_computed_final_grade&#39;, as well as (if the user has permission)   &#39;current_period_unposted_current_score&#39;,   &#39;current_period_unposted_final_score&#39;,   &#39;current_period_unposted_current_grade&#39;, and   &#39;current_period_unposted_final_grade&#39; (see Enrollment documentation for   more information on these fields). In addition, when this argument is   passed, the course will have a &#39;has_grading_periods&#39; attribute   on it. This argument is ignored if the course is configured to hide final   grades or if the total_scores argument is not included. - \&quot;grading_periods\&quot;: Optional information to include with each Course. When   grading_periods is given, a list of the grading periods associated with   each course is returned. - \&quot;term\&quot;: Optional information to include with each Course. When   term is given, the information for the enrollment term for each course   is returned. - \&quot;account\&quot;: Optional information to include with each Course. When   account is given, the account json for each course is returned. - \&quot;course_progress\&quot;: Optional information to include with each Course.   When course_progress is given, each course will include a   &#39;course_progress&#39; object with the fields: &#39;requirement_count&#39;, an integer   specifying the total number of requirements in the course,   &#39;requirement_completed_count&#39;, an integer specifying the total number of   requirements in this course that have been completed, and   &#39;next_requirement_url&#39;, a string url to the next requirement item, and   &#39;completed_at&#39;, the date the course was completed (null if incomplete).   &#39;next_requirement_url&#39; will be null if all requirements have been   completed or the current module does not require sequential progress.   \&quot;course_progress\&quot; will return an error message if the course is not   module based or the user is not enrolled as a student in the course. - \&quot;sections\&quot;: Section enrollment information to include with each Course.   Returns an array of hashes containing the section ID (id), section name   (name), start and end dates (start_at, end_at), as well as the enrollment   type (enrollment_role, e.g. &#39;StudentEnrollment&#39;). - \&quot;storage_quota_used_mb\&quot;: The amount of storage space used by the files in this course - \&quot;total_students\&quot;: Optional information to include with each Course.   Returns an integer for the total amount of active and invited students. - \&quot;passback_status\&quot;: Include the grade passback_status - \&quot;favorites\&quot;: Optional information to include with each Course.   Indicates if the user has marked the course as a favorite course. - \&quot;teachers\&quot;: Teacher information to include with each Course.   Returns an array of hashes containing the {api:Users:UserDisplay UserDisplay} information   for each teacher in the course. - \&quot;observed_users\&quot;: Optional information to include with each Course.   Will include data for observed users if the current user has an   observer enrollment. - \&quot;tabs\&quot;: Optional information to include with each Course.   Will include the list of tabs configured for each course.  See the   {api:TabsController#index List available tabs API} for more information. - \&quot;course_image\&quot;: Optional information to include with each Course. Returns course   image url if a course image has been set. - \&quot;banner_image\&quot;: Optional information to include with each Course. Returns course   banner image url if the course is a Canvas for Elementary subject and a banner   image has been set. - \&quot;concluded\&quot;: Optional information to include with each Course. Indicates whether   the course has been concluded, taking course and term dates into account. - \&quot;post_manually\&quot;: Optional information to include with each Course. Returns true if   the course post policy is set to \&quot;Manually\&quot;. Returns false if the the course post   policy is set to \&quot;Automatically\&quot;. | [optional] 
 **state** | [**List[str]**](str.md)| If set, only return courses that are in the given state(s). By default, \&quot;available\&quot; is returned for students and observers, and anything except \&quot;deleted\&quot;, for all other enrollment types | [optional] 
 **enrollment_state** | **str**| When set, only return courses where the user has an enrollment with the given state. This will respect section/course/term date overrides. | [optional] 
 **homeroom** | **bool**| If set, only return homeroom courses. | [optional] 
 **account_id** | **str**| If set, only include courses associated with this account | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[Course]**](Course.md)

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

# **courses_user_progress**
> CourseProgress courses_user_progress(course_id, user_id)

Get user progress

Return progress information for the user and course

You can supply +self+ as the user_id to query your own progress in a course. To query another user's progress,
you must be a teacher in the course, an administrator, or a linked observer of the user.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.course_progress import CourseProgress
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
    api_instance = canvas_lms_python_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # Get user progress
        api_response = await api_instance.courses_user_progress(course_id, user_id)
        print("The response of CoursesApi->courses_user_progress:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->courses_user_progress: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **user_id** | **str**| Scope response to user_id | 

### Return type

[**CourseProgress**](CourseProgress.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | CourseProgress |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **courses_users**
> List[User] courses_users(course_id, search_term=search_term, sort=sort, enrollment_type=enrollment_type, enrollment_role=enrollment_role, enrollment_role_id=enrollment_role_id, section_ids=section_ids, include=include, user_id=user_id, user_ids=user_ids, enrollment_state=enrollment_state, page=page, per_page=per_page)

List users in course

Returns the paginated list of users in this course. And optionally the user's enrollments in the course.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.user import User
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
    api_instance = canvas_lms_python_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    search_term = 'search_term_example' # str | The partial name or full ID of the users to match and return in the results list. (optional)
    sort = 'sort_example' # str | When set, sort the results of the search based on the given field. (optional)
    enrollment_type = ['enrollment_type_example'] # List[str] | When set, only return users where the user is enrolled as this type. \"student_view\" implies include[]=test_student. This argument is ignored if enrollment_role is given. (optional)
    enrollment_role = 'enrollment_role_example' # str | Deprecated When set, only return users enrolled with the specified course-level role.  This can be a role created with the {api:RoleOverridesController#add_role Add Role API} or a base role type of 'StudentEnrollment', 'TeacherEnrollment', 'TaEnrollment', 'ObserverEnrollment', or 'DesignerEnrollment'. (optional)
    enrollment_role_id = 56 # int | When set, only return courses where the user is enrolled with the specified course-level role.  This can be a role created with the {api:RoleOverridesController#add_role Add Role API} or a built_in role id with type 'StudentEnrollment', 'TeacherEnrollment', 'TaEnrollment', 'ObserverEnrollment', or 'DesignerEnrollment'. (optional)
    section_ids = [56] # List[int] | When set, only return users who are enrolled in the given section(s). (optional)
    include = ['include_example'] # List[str] | - \"enrollments\": Optionally include with each Course the user's current and invited enrollments. If the user is enrolled as a student, and the account has permission to manage or view all grades, each enrollment will include a 'grades' key with 'current_score', 'final_score', 'current_grade' and 'final_grade' values. - \"locked\": Optionally include whether an enrollment is locked. - \"avatar_url\": Optionally include avatar_url. - \"bio\": Optionally include each user's bio. - \"test_student\": Optionally include the course's Test Student, if present. Default is to not include Test Student. - \"custom_links\": Optionally include plugin-supplied custom links for each student, such as analytics information - \"current_grading_period_scores\": if enrollments is included as well as this directive, the scores returned in the enrollment will be for the current grading period if there is one. A 'grading_period_id' value will also be included with the scores. if grading_period_id is nil there is no current grading period and the score is a total score. - \"uuid\": Optionally include the users uuid (optional)
    user_id = 'user_id_example' # str | If this parameter is given and it corresponds to a user in the course, the +page+ parameter will be ignored and the page containing the specified user will be returned instead. (optional)
    user_ids = [56] # List[int] | If included, the course users set will only include users with IDs specified by the param. Note: this will not work in conjunction with the \"user_id\" argument but multiple user_ids can be included. (optional)
    enrollment_state = ['enrollment_state_example'] # List[str] | When set, only return users where the enrollment workflow state is of one of the given types. \"active\" and \"invited\" enrollments are returned by default. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List users in course
        api_response = await api_instance.courses_users(course_id, search_term=search_term, sort=sort, enrollment_type=enrollment_type, enrollment_role=enrollment_role, enrollment_role_id=enrollment_role_id, section_ids=section_ids, include=include, user_id=user_id, user_ids=user_ids, enrollment_state=enrollment_state, page=page, per_page=per_page)
        print("The response of CoursesApi->courses_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->courses_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **search_term** | **str**| The partial name or full ID of the users to match and return in the results list. | [optional] 
 **sort** | **str**| When set, sort the results of the search based on the given field. | [optional] 
 **enrollment_type** | [**List[str]**](str.md)| When set, only return users where the user is enrolled as this type. \&quot;student_view\&quot; implies include[]&#x3D;test_student. This argument is ignored if enrollment_role is given. | [optional] 
 **enrollment_role** | **str**| Deprecated When set, only return users enrolled with the specified course-level role.  This can be a role created with the {api:RoleOverridesController#add_role Add Role API} or a base role type of &#39;StudentEnrollment&#39;, &#39;TeacherEnrollment&#39;, &#39;TaEnrollment&#39;, &#39;ObserverEnrollment&#39;, or &#39;DesignerEnrollment&#39;. | [optional] 
 **enrollment_role_id** | **int**| When set, only return courses where the user is enrolled with the specified course-level role.  This can be a role created with the {api:RoleOverridesController#add_role Add Role API} or a built_in role id with type &#39;StudentEnrollment&#39;, &#39;TeacherEnrollment&#39;, &#39;TaEnrollment&#39;, &#39;ObserverEnrollment&#39;, or &#39;DesignerEnrollment&#39;. | [optional] 
 **section_ids** | [**List[int]**](int.md)| When set, only return users who are enrolled in the given section(s). | [optional] 
 **include** | [**List[str]**](str.md)| - \&quot;enrollments\&quot;: Optionally include with each Course the user&#39;s current and invited enrollments. If the user is enrolled as a student, and the account has permission to manage or view all grades, each enrollment will include a &#39;grades&#39; key with &#39;current_score&#39;, &#39;final_score&#39;, &#39;current_grade&#39; and &#39;final_grade&#39; values. - \&quot;locked\&quot;: Optionally include whether an enrollment is locked. - \&quot;avatar_url\&quot;: Optionally include avatar_url. - \&quot;bio\&quot;: Optionally include each user&#39;s bio. - \&quot;test_student\&quot;: Optionally include the course&#39;s Test Student, if present. Default is to not include Test Student. - \&quot;custom_links\&quot;: Optionally include plugin-supplied custom links for each student, such as analytics information - \&quot;current_grading_period_scores\&quot;: if enrollments is included as well as this directive, the scores returned in the enrollment will be for the current grading period if there is one. A &#39;grading_period_id&#39; value will also be included with the scores. if grading_period_id is nil there is no current grading period and the score is a total score. - \&quot;uuid\&quot;: Optionally include the users uuid | [optional] 
 **user_id** | **str**| If this parameter is given and it corresponds to a user in the course, the +page+ parameter will be ignored and the page containing the specified user will be returned instead. | [optional] 
 **user_ids** | [**List[int]**](int.md)| If included, the course users set will only include users with IDs specified by the param. Note: this will not work in conjunction with the \&quot;user_id\&quot; argument but multiple user_ids can be included. | [optional] 
 **enrollment_state** | [**List[str]**](str.md)| When set, only return users where the enrollment workflow state is of one of the given types. \&quot;active\&quot; and \&quot;invited\&quot; enrollments are returned by default. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[User]**](User.md)

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

# **courses_users_for_courses**
> List[User] courses_users_for_courses(course_id, search_term=search_term, sort=sort, enrollment_type=enrollment_type, enrollment_role=enrollment_role, enrollment_role_id=enrollment_role_id, section_ids=section_ids, include=include, user_id=user_id, user_ids=user_ids, enrollment_state=enrollment_state, page=page, per_page=per_page)

List users in course

Returns the paginated list of users in this course. And optionally the user's enrollments in the course.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.user import User
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
    api_instance = canvas_lms_python_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    search_term = 'search_term_example' # str | The partial name or full ID of the users to match and return in the results list. (optional)
    sort = 'sort_example' # str | When set, sort the results of the search based on the given field. (optional)
    enrollment_type = ['enrollment_type_example'] # List[str] | When set, only return users where the user is enrolled as this type. \"student_view\" implies include[]=test_student. This argument is ignored if enrollment_role is given. (optional)
    enrollment_role = 'enrollment_role_example' # str | Deprecated When set, only return users enrolled with the specified course-level role.  This can be a role created with the {api:RoleOverridesController#add_role Add Role API} or a base role type of 'StudentEnrollment', 'TeacherEnrollment', 'TaEnrollment', 'ObserverEnrollment', or 'DesignerEnrollment'. (optional)
    enrollment_role_id = 56 # int | When set, only return courses where the user is enrolled with the specified course-level role.  This can be a role created with the {api:RoleOverridesController#add_role Add Role API} or a built_in role id with type 'StudentEnrollment', 'TeacherEnrollment', 'TaEnrollment', 'ObserverEnrollment', or 'DesignerEnrollment'. (optional)
    section_ids = [56] # List[int] | When set, only return users who are enrolled in the given section(s). (optional)
    include = ['include_example'] # List[str] | - \"enrollments\": Optionally include with each Course the user's current and invited enrollments. If the user is enrolled as a student, and the account has permission to manage or view all grades, each enrollment will include a 'grades' key with 'current_score', 'final_score', 'current_grade' and 'final_grade' values. - \"locked\": Optionally include whether an enrollment is locked. - \"avatar_url\": Optionally include avatar_url. - \"bio\": Optionally include each user's bio. - \"test_student\": Optionally include the course's Test Student, if present. Default is to not include Test Student. - \"custom_links\": Optionally include plugin-supplied custom links for each student, such as analytics information - \"current_grading_period_scores\": if enrollments is included as well as this directive, the scores returned in the enrollment will be for the current grading period if there is one. A 'grading_period_id' value will also be included with the scores. if grading_period_id is nil there is no current grading period and the score is a total score. - \"uuid\": Optionally include the users uuid (optional)
    user_id = 'user_id_example' # str | If this parameter is given and it corresponds to a user in the course, the +page+ parameter will be ignored and the page containing the specified user will be returned instead. (optional)
    user_ids = [56] # List[int] | If included, the course users set will only include users with IDs specified by the param. Note: this will not work in conjunction with the \"user_id\" argument but multiple user_ids can be included. (optional)
    enrollment_state = ['enrollment_state_example'] # List[str] | When set, only return users where the enrollment workflow state is of one of the given types. \"active\" and \"invited\" enrollments are returned by default. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List users in course
        api_response = await api_instance.courses_users_for_courses(course_id, search_term=search_term, sort=sort, enrollment_type=enrollment_type, enrollment_role=enrollment_role, enrollment_role_id=enrollment_role_id, section_ids=section_ids, include=include, user_id=user_id, user_ids=user_ids, enrollment_state=enrollment_state, page=page, per_page=per_page)
        print("The response of CoursesApi->courses_users_for_courses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->courses_users_for_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **search_term** | **str**| The partial name or full ID of the users to match and return in the results list. | [optional] 
 **sort** | **str**| When set, sort the results of the search based on the given field. | [optional] 
 **enrollment_type** | [**List[str]**](str.md)| When set, only return users where the user is enrolled as this type. \&quot;student_view\&quot; implies include[]&#x3D;test_student. This argument is ignored if enrollment_role is given. | [optional] 
 **enrollment_role** | **str**| Deprecated When set, only return users enrolled with the specified course-level role.  This can be a role created with the {api:RoleOverridesController#add_role Add Role API} or a base role type of &#39;StudentEnrollment&#39;, &#39;TeacherEnrollment&#39;, &#39;TaEnrollment&#39;, &#39;ObserverEnrollment&#39;, or &#39;DesignerEnrollment&#39;. | [optional] 
 **enrollment_role_id** | **int**| When set, only return courses where the user is enrolled with the specified course-level role.  This can be a role created with the {api:RoleOverridesController#add_role Add Role API} or a built_in role id with type &#39;StudentEnrollment&#39;, &#39;TeacherEnrollment&#39;, &#39;TaEnrollment&#39;, &#39;ObserverEnrollment&#39;, or &#39;DesignerEnrollment&#39;. | [optional] 
 **section_ids** | [**List[int]**](int.md)| When set, only return users who are enrolled in the given section(s). | [optional] 
 **include** | [**List[str]**](str.md)| - \&quot;enrollments\&quot;: Optionally include with each Course the user&#39;s current and invited enrollments. If the user is enrolled as a student, and the account has permission to manage or view all grades, each enrollment will include a &#39;grades&#39; key with &#39;current_score&#39;, &#39;final_score&#39;, &#39;current_grade&#39; and &#39;final_grade&#39; values. - \&quot;locked\&quot;: Optionally include whether an enrollment is locked. - \&quot;avatar_url\&quot;: Optionally include avatar_url. - \&quot;bio\&quot;: Optionally include each user&#39;s bio. - \&quot;test_student\&quot;: Optionally include the course&#39;s Test Student, if present. Default is to not include Test Student. - \&quot;custom_links\&quot;: Optionally include plugin-supplied custom links for each student, such as analytics information - \&quot;current_grading_period_scores\&quot;: if enrollments is included as well as this directive, the scores returned in the enrollment will be for the current grading period if there is one. A &#39;grading_period_id&#39; value will also be included with the scores. if grading_period_id is nil there is no current grading period and the score is a total score. - \&quot;uuid\&quot;: Optionally include the users uuid | [optional] 
 **user_id** | **str**| If this parameter is given and it corresponds to a user in the course, the +page+ parameter will be ignored and the page containing the specified user will be returned instead. | [optional] 
 **user_ids** | [**List[int]**](int.md)| If included, the course users set will only include users with IDs specified by the param. Note: this will not work in conjunction with the \&quot;user_id\&quot; argument but multiple user_ids can be included. | [optional] 
 **enrollment_state** | [**List[str]**](str.md)| When set, only return users where the enrollment workflow state is of one of the given types. \&quot;active\&quot; and \&quot;invited\&quot; enrollments are returned by default. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[User]**](User.md)

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

