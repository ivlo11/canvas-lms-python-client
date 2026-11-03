# canvas_lms_python_client.SubmissionsApiApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**submissions_api_bulk_update**](SubmissionsApiApi.md#submissions_api_bulk_update) | **POST** /api/v1/courses/{course_id}/submissions/update_grades | Grade or comment on multiple submissions
[**submissions_api_bulk_update_by_assignment_id_for_sections**](SubmissionsApiApi.md#submissions_api_bulk_update_by_assignment_id_for_sections) | **POST** /api/v1/sections/{section_id}/assignments/{assignment_id}/submissions/update_grades | Grade or comment on multiple submissions
[**submissions_api_bulk_update_for_courses**](SubmissionsApiApi.md#submissions_api_bulk_update_for_courses) | **POST** /api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/update_grades | Grade or comment on multiple submissions
[**submissions_api_bulk_update_for_sections**](SubmissionsApiApi.md#submissions_api_bulk_update_for_sections) | **POST** /api/v1/sections/{section_id}/submissions/update_grades | Grade or comment on multiple submissions
[**submissions_api_create_file**](SubmissionsApiApi.md#submissions_api_create_file) | **POST** /api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/files | Upload a file
[**submissions_api_create_file_for_sections**](SubmissionsApiApi.md#submissions_api_create_file_for_sections) | **POST** /api/v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id}/files | Upload a file
[**submissions_api_document_annotations_read_state**](SubmissionsApiApi.md#submissions_api_document_annotations_read_state) | **GET** /api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/document_annotations/read | Get document annotations read state
[**submissions_api_document_annotations_read_state_for_sections**](SubmissionsApiApi.md#submissions_api_document_annotations_read_state_for_sections) | **GET** /api/v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id}/document_annotations/read | Get document annotations read state
[**submissions_api_for_students**](SubmissionsApiApi.md#submissions_api_for_students) | **GET** /api/v1/courses/{course_id}/students/submissions | List submissions for multiple assignments
[**submissions_api_for_students_for_sections**](SubmissionsApiApi.md#submissions_api_for_students_for_sections) | **GET** /api/v1/sections/{section_id}/students/submissions | List submissions for multiple assignments
[**submissions_api_gradeable_students**](SubmissionsApiApi.md#submissions_api_gradeable_students) | **GET** /api/v1/courses/{course_id}/assignments/{assignment_id}/gradeable_students | List gradeable students
[**submissions_api_index**](SubmissionsApiApi.md#submissions_api_index) | **GET** /api/v1/courses/{course_id}/assignments/{assignment_id}/submissions | List assignment submissions
[**submissions_api_index_for_sections**](SubmissionsApiApi.md#submissions_api_index_for_sections) | **GET** /api/v1/sections/{section_id}/assignments/{assignment_id}/submissions | List assignment submissions
[**submissions_api_mark_bulk_submissions_as_read**](SubmissionsApiApi.md#submissions_api_mark_bulk_submissions_as_read) | **PUT** /api/v1/courses/{course_id}/submissions/bulk_mark_read | Mark bulk submissions as read
[**submissions_api_mark_bulk_submissions_as_read_for_sections**](SubmissionsApiApi.md#submissions_api_mark_bulk_submissions_as_read_for_sections) | **PUT** /api/v1/sections/{section_id}/submissions/bulk_mark_read | Mark bulk submissions as read
[**submissions_api_mark_document_annotations_read**](SubmissionsApiApi.md#submissions_api_mark_document_annotations_read) | **PUT** /api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/document_annotations/read | Mark document annotations as read
[**submissions_api_mark_document_annotations_read_for_sections**](SubmissionsApiApi.md#submissions_api_mark_document_annotations_read_for_sections) | **PUT** /api/v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id}/document_annotations/read | Mark document annotations as read
[**submissions_api_mark_rubric_assessments_read**](SubmissionsApiApi.md#submissions_api_mark_rubric_assessments_read) | **PUT** /api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/rubric_comments/read | Mark rubric assessments as read
[**submissions_api_mark_rubric_assessments_read_by_user_id_for_sections**](SubmissionsApiApi.md#submissions_api_mark_rubric_assessments_read_by_user_id_for_sections) | **PUT** /api/v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id}/rubric_assessments/read | Mark rubric assessments as read
[**submissions_api_mark_rubric_assessments_read_for_courses**](SubmissionsApiApi.md#submissions_api_mark_rubric_assessments_read_for_courses) | **PUT** /api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/rubric_assessments/read | Mark rubric assessments as read
[**submissions_api_mark_rubric_assessments_read_for_sections**](SubmissionsApiApi.md#submissions_api_mark_rubric_assessments_read_for_sections) | **PUT** /api/v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id}/rubric_comments/read | Mark rubric assessments as read
[**submissions_api_mark_submission_item_read**](SubmissionsApiApi.md#submissions_api_mark_submission_item_read) | **PUT** /api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/read/{item} | Mark submission item as read
[**submissions_api_mark_submission_item_read_for_sections**](SubmissionsApiApi.md#submissions_api_mark_submission_item_read_for_sections) | **PUT** /api/v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id}/read/{item} | Mark submission item as read
[**submissions_api_mark_submission_read**](SubmissionsApiApi.md#submissions_api_mark_submission_read) | **PUT** /api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/read | Mark submission as read
[**submissions_api_mark_submission_read_for_sections**](SubmissionsApiApi.md#submissions_api_mark_submission_read_for_sections) | **PUT** /api/v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id}/read | Mark submission as read
[**submissions_api_mark_submission_unread**](SubmissionsApiApi.md#submissions_api_mark_submission_unread) | **DELETE** /api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/read | Mark submission as unread
[**submissions_api_mark_submission_unread_for_sections**](SubmissionsApiApi.md#submissions_api_mark_submission_unread_for_sections) | **DELETE** /api/v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id}/read | Mark submission as unread
[**submissions_api_multiple_gradeable_students**](SubmissionsApiApi.md#submissions_api_multiple_gradeable_students) | **GET** /api/v1/courses/{course_id}/assignments/gradeable_students | List multiple assignments gradeable students
[**submissions_api_rubric_assessments_read_state**](SubmissionsApiApi.md#submissions_api_rubric_assessments_read_state) | **GET** /api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/rubric_comments/read | Get rubric assessments read state
[**submissions_api_rubric_assessments_read_state_by_user_id_for_sections**](SubmissionsApiApi.md#submissions_api_rubric_assessments_read_state_by_user_id_for_sections) | **GET** /api/v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id}/rubric_assessments/read | Get rubric assessments read state
[**submissions_api_rubric_assessments_read_state_for_courses**](SubmissionsApiApi.md#submissions_api_rubric_assessments_read_state_for_courses) | **GET** /api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/rubric_assessments/read | Get rubric assessments read state
[**submissions_api_rubric_assessments_read_state_for_sections**](SubmissionsApiApi.md#submissions_api_rubric_assessments_read_state_for_sections) | **GET** /api/v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id}/rubric_comments/read | Get rubric assessments read state
[**submissions_api_show**](SubmissionsApiApi.md#submissions_api_show) | **GET** /api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id} | Get a single submission
[**submissions_api_show_anonymous**](SubmissionsApiApi.md#submissions_api_show_anonymous) | **GET** /api/v1/courses/{course_id}/assignments/{assignment_id}/anonymous_submissions/{anonymous_id} | Get a single submission by anonymous id
[**submissions_api_show_anonymous_for_sections**](SubmissionsApiApi.md#submissions_api_show_anonymous_for_sections) | **GET** /api/v1/sections/{section_id}/assignments/{assignment_id}/anonymous_submissions/{anonymous_id} | Get a single submission by anonymous id
[**submissions_api_show_for_sections**](SubmissionsApiApi.md#submissions_api_show_for_sections) | **GET** /api/v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id} | Get a single submission
[**submissions_api_submission_summary**](SubmissionsApiApi.md#submissions_api_submission_summary) | **GET** /api/v1/courses/{course_id}/assignments/{assignment_id}/submission_summary | Submission Summary
[**submissions_api_submission_summary_for_sections**](SubmissionsApiApi.md#submissions_api_submission_summary_for_sections) | **GET** /api/v1/sections/{section_id}/assignments/{assignment_id}/submission_summary | Submission Summary
[**submissions_api_submissions_clear_unread**](SubmissionsApiApi.md#submissions_api_submissions_clear_unread) | **PUT** /api/v1/courses/{course_id}/submissions/{user_id}/clear_unread | Clear unread status for all submissions.
[**submissions_api_submissions_clear_unread_for_sections**](SubmissionsApiApi.md#submissions_api_submissions_clear_unread_for_sections) | **PUT** /api/v1/sections/{section_id}/submissions/{user_id}/clear_unread | Clear unread status for all submissions.
[**submissions_api_update**](SubmissionsApiApi.md#submissions_api_update) | **PUT** /api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id} | Grade or comment on a submission
[**submissions_api_update_anonymous**](SubmissionsApiApi.md#submissions_api_update_anonymous) | **PUT** /api/v1/courses/{course_id}/assignments/{assignment_id}/anonymous_submissions/{anonymous_id} | Grade or comment on a submission by anonymous id
[**submissions_api_update_anonymous_for_sections**](SubmissionsApiApi.md#submissions_api_update_anonymous_for_sections) | **PUT** /api/v1/sections/{section_id}/assignments/{assignment_id}/anonymous_submissions/{anonymous_id} | Grade or comment on a submission by anonymous id
[**submissions_api_update_for_sections**](SubmissionsApiApi.md#submissions_api_update_for_sections) | **PUT** /api/v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id} | Grade or comment on a submission


# **submissions_api_bulk_update**
> Progress submissions_api_bulk_update(course_id, submissions_api_bulk_update_request=submissions_api_bulk_update_request)

Grade or comment on multiple submissions

Update the grading and comments on multiple student's assignment
submissions in an asynchronous job.

The user must have permission to manage grades in the appropriate context
(course or section).

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.progress import Progress
from canvas_lms_python_client.models.submissions_api_bulk_update_request import SubmissionsApiBulkUpdateRequest
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
    api_instance = canvas_lms_python_client.SubmissionsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    submissions_api_bulk_update_request = canvas_lms_python_client.SubmissionsApiBulkUpdateRequest() # SubmissionsApiBulkUpdateRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/courses/1/assignments/2/submissions/update_grades' \\      -X POST \\      -F 'grade_data[3][posted_grade]=88' \\      -F 'grade_data[4][posted_grade]=95' \\      -H \"Authorization: Bearer <token>\" ``` (optional)

    try:
        # Grade or comment on multiple submissions
        api_response = await api_instance.submissions_api_bulk_update(course_id, submissions_api_bulk_update_request=submissions_api_bulk_update_request)
        print("The response of SubmissionsApiApi->submissions_api_bulk_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubmissionsApiApi->submissions_api_bulk_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **submissions_api_bulk_update_request** | [**SubmissionsApiBulkUpdateRequest**](SubmissionsApiBulkUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/courses/1/assignments/2/submissions/update_grades&#39; \\      -X POST \\      -F &#39;grade_data[3][posted_grade]&#x3D;88&#39; \\      -F &#39;grade_data[4][posted_grade]&#x3D;95&#39; \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; &#x60;&#x60;&#x60; | [optional] 

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

# **submissions_api_bulk_update_by_assignment_id_for_sections**
> Progress submissions_api_bulk_update_by_assignment_id_for_sections(assignment_id, section_id, submissions_api_bulk_update_request=submissions_api_bulk_update_request)

Grade or comment on multiple submissions

Update the grading and comments on multiple student's assignment
submissions in an asynchronous job.

The user must have permission to manage grades in the appropriate context
(course or section).

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.progress import Progress
from canvas_lms_python_client.models.submissions_api_bulk_update_request import SubmissionsApiBulkUpdateRequest
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
    api_instance = canvas_lms_python_client.SubmissionsApiApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    section_id = 'section_id_example' # str | Scope response to section_id
    submissions_api_bulk_update_request = canvas_lms_python_client.SubmissionsApiBulkUpdateRequest() # SubmissionsApiBulkUpdateRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/courses/1/assignments/2/submissions/update_grades' \\      -X POST \\      -F 'grade_data[3][posted_grade]=88' \\      -F 'grade_data[4][posted_grade]=95' \\      -H \"Authorization: Bearer <token>\" ``` (optional)

    try:
        # Grade or comment on multiple submissions
        api_response = await api_instance.submissions_api_bulk_update_by_assignment_id_for_sections(assignment_id, section_id, submissions_api_bulk_update_request=submissions_api_bulk_update_request)
        print("The response of SubmissionsApiApi->submissions_api_bulk_update_by_assignment_id_for_sections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubmissionsApiApi->submissions_api_bulk_update_by_assignment_id_for_sections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **section_id** | **str**| Scope response to section_id | 
 **submissions_api_bulk_update_request** | [**SubmissionsApiBulkUpdateRequest**](SubmissionsApiBulkUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/courses/1/assignments/2/submissions/update_grades&#39; \\      -X POST \\      -F &#39;grade_data[3][posted_grade]&#x3D;88&#39; \\      -F &#39;grade_data[4][posted_grade]&#x3D;95&#39; \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; &#x60;&#x60;&#x60; | [optional] 

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

# **submissions_api_bulk_update_for_courses**
> Progress submissions_api_bulk_update_for_courses(assignment_id, course_id, submissions_api_bulk_update_request=submissions_api_bulk_update_request)

Grade or comment on multiple submissions

Update the grading and comments on multiple student's assignment
submissions in an asynchronous job.

The user must have permission to manage grades in the appropriate context
(course or section).

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.progress import Progress
from canvas_lms_python_client.models.submissions_api_bulk_update_request import SubmissionsApiBulkUpdateRequest
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
    api_instance = canvas_lms_python_client.SubmissionsApiApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    course_id = 'course_id_example' # str | Scope response to course_id
    submissions_api_bulk_update_request = canvas_lms_python_client.SubmissionsApiBulkUpdateRequest() # SubmissionsApiBulkUpdateRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/courses/1/assignments/2/submissions/update_grades' \\      -X POST \\      -F 'grade_data[3][posted_grade]=88' \\      -F 'grade_data[4][posted_grade]=95' \\      -H \"Authorization: Bearer <token>\" ``` (optional)

    try:
        # Grade or comment on multiple submissions
        api_response = await api_instance.submissions_api_bulk_update_for_courses(assignment_id, course_id, submissions_api_bulk_update_request=submissions_api_bulk_update_request)
        print("The response of SubmissionsApiApi->submissions_api_bulk_update_for_courses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubmissionsApiApi->submissions_api_bulk_update_for_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **course_id** | **str**| Scope response to course_id | 
 **submissions_api_bulk_update_request** | [**SubmissionsApiBulkUpdateRequest**](SubmissionsApiBulkUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/courses/1/assignments/2/submissions/update_grades&#39; \\      -X POST \\      -F &#39;grade_data[3][posted_grade]&#x3D;88&#39; \\      -F &#39;grade_data[4][posted_grade]&#x3D;95&#39; \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; &#x60;&#x60;&#x60; | [optional] 

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

# **submissions_api_bulk_update_for_sections**
> Progress submissions_api_bulk_update_for_sections(section_id, submissions_api_bulk_update_request=submissions_api_bulk_update_request)

Grade or comment on multiple submissions

Update the grading and comments on multiple student's assignment
submissions in an asynchronous job.

The user must have permission to manage grades in the appropriate context
(course or section).

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.progress import Progress
from canvas_lms_python_client.models.submissions_api_bulk_update_request import SubmissionsApiBulkUpdateRequest
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
    api_instance = canvas_lms_python_client.SubmissionsApiApi(api_client)
    section_id = 'section_id_example' # str | Scope response to section_id
    submissions_api_bulk_update_request = canvas_lms_python_client.SubmissionsApiBulkUpdateRequest() # SubmissionsApiBulkUpdateRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/courses/1/assignments/2/submissions/update_grades' \\      -X POST \\      -F 'grade_data[3][posted_grade]=88' \\      -F 'grade_data[4][posted_grade]=95' \\      -H \"Authorization: Bearer <token>\" ``` (optional)

    try:
        # Grade or comment on multiple submissions
        api_response = await api_instance.submissions_api_bulk_update_for_sections(section_id, submissions_api_bulk_update_request=submissions_api_bulk_update_request)
        print("The response of SubmissionsApiApi->submissions_api_bulk_update_for_sections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubmissionsApiApi->submissions_api_bulk_update_for_sections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **section_id** | **str**| Scope response to section_id | 
 **submissions_api_bulk_update_request** | [**SubmissionsApiBulkUpdateRequest**](SubmissionsApiBulkUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/courses/1/assignments/2/submissions/update_grades&#39; \\      -X POST \\      -F &#39;grade_data[3][posted_grade]&#x3D;88&#39; \\      -F &#39;grade_data[4][posted_grade]&#x3D;95&#39; \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; &#x60;&#x60;&#x60; | [optional] 

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

# **submissions_api_create_file**
> submissions_api_create_file(assignment_id, course_id, user_id)

Upload a file

Upload a file to a submission.

This API endpoint is the first step in uploading a file to a submission as a student.
See the {file:file.file_uploads.html File Upload Documentation} for details on the file upload workflow.

The final step of the file upload workflow will return the attachment data,
including the new file id. The caller can then POST to submit the
+online_upload+ assignment with these file ids.

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
    api_instance = canvas_lms_python_client.SubmissionsApiApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    course_id = 'course_id_example' # str | Scope response to course_id
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # Upload a file
        await api_instance.submissions_api_create_file(assignment_id, course_id, user_id)
    except Exception as e:
        print("Exception when calling SubmissionsApiApi->submissions_api_create_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **course_id** | **str**| Scope response to course_id | 
 **user_id** | **str**| Scope response to user_id | 

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

# **submissions_api_create_file_for_sections**
> submissions_api_create_file_for_sections(assignment_id, section_id, user_id)

Upload a file

Upload a file to a submission.

This API endpoint is the first step in uploading a file to a submission as a student.
See the {file:file.file_uploads.html File Upload Documentation} for details on the file upload workflow.

The final step of the file upload workflow will return the attachment data,
including the new file id. The caller can then POST to submit the
+online_upload+ assignment with these file ids.

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
    api_instance = canvas_lms_python_client.SubmissionsApiApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    section_id = 'section_id_example' # str | Scope response to section_id
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # Upload a file
        await api_instance.submissions_api_create_file_for_sections(assignment_id, section_id, user_id)
    except Exception as e:
        print("Exception when calling SubmissionsApiApi->submissions_api_create_file_for_sections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **section_id** | **str**| Scope response to section_id | 
 **user_id** | **str**| Scope response to user_id | 

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

# **submissions_api_document_annotations_read_state**
> submissions_api_document_annotations_read_state(assignment_id, course_id, user_id)

Get document annotations read state

Return whether annotations made on a submitted document have been read by the student

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
    api_instance = canvas_lms_python_client.SubmissionsApiApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    course_id = 'course_id_example' # str | Scope response to course_id
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # Get document annotations read state
        await api_instance.submissions_api_document_annotations_read_state(assignment_id, course_id, user_id)
    except Exception as e:
        print("Exception when calling SubmissionsApiApi->submissions_api_document_annotations_read_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **course_id** | **str**| Scope response to course_id | 
 **user_id** | **str**| Scope response to user_id | 

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
**0** | Get document annotations read state |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submissions_api_document_annotations_read_state_for_sections**
> submissions_api_document_annotations_read_state_for_sections(assignment_id, section_id, user_id)

Get document annotations read state

Return whether annotations made on a submitted document have been read by the student

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
    api_instance = canvas_lms_python_client.SubmissionsApiApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    section_id = 'section_id_example' # str | Scope response to section_id
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # Get document annotations read state
        await api_instance.submissions_api_document_annotations_read_state_for_sections(assignment_id, section_id, user_id)
    except Exception as e:
        print("Exception when calling SubmissionsApiApi->submissions_api_document_annotations_read_state_for_sections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **section_id** | **str**| Scope response to section_id | 
 **user_id** | **str**| Scope response to user_id | 

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
**0** | Get document annotations read state |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submissions_api_for_students**
> List[Submission] submissions_api_for_students(course_id, student_ids=student_ids, assignment_ids=assignment_ids, grouped=grouped, post_to_sis=post_to_sis, submitted_since=submitted_since, graded_since=graded_since, grading_period_id=grading_period_id, workflow_state=workflow_state, enrollment_state=enrollment_state, state_based_on_date=state_based_on_date, order=order, order_direction=order_direction, include=include, page=page, per_page=per_page)

List submissions for multiple assignments

A paginated list of all existing submissions for a given set of students and assignments.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.submission import Submission
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
    api_instance = canvas_lms_python_client.SubmissionsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    student_ids = ['student_ids_example'] # List[str] | List of student ids to return submissions for. If this argument is omitted, return submissions for the calling user. Students may only list their own submissions. Observers may only list those of associated students. The special id \"all\" will return submissions for all students in the course/section as appropriate. (optional)
    assignment_ids = ['assignment_ids_example'] # List[str] | List of assignments to return submissions for. If none are given, submissions for all assignments are returned. (optional)
    grouped = True # bool | If this argument is present, the response will be grouped by student, rather than a flat array of submissions. (optional)
    post_to_sis = True # bool | If this argument is set to true, the response will only include submissions for assignments that have the post_to_sis flag set to true and user enrollments that were added through sis. (optional)
    submitted_since = 'submitted_since_example' # str | If this argument is set, the response will only include submissions that were submitted after the specified date_time. This will exclude submissions that do not have a submitted_at which will exclude unsubmitted submissions. The value must be formatted as ISO 8601 YYYY-MM-DDTHH:MM:SSZ. (optional)
    graded_since = 'graded_since_example' # str | If this argument is set, the response will only include submissions that were graded after the specified date_time. This will exclude submissions that have not been graded. The value must be formatted as ISO 8601 YYYY-MM-DDTHH:MM:SSZ. (optional)
    grading_period_id = 56 # int | The id of the grading period in which submissions are being requested (Requires grading periods to exist on the account) (optional)
    workflow_state = 'workflow_state_example' # str | The current status of the submission (optional)
    enrollment_state = 'enrollment_state_example' # str | The current state of the enrollments. If omitted will include all enrollments that are not deleted. (optional)
    state_based_on_date = True # bool | If omitted it is set to true. When set to false it will ignore the effective state of the student enrollments and use the workflow_state for the enrollments. The argument is ignored unless enrollment_state argument is also passed. (optional)
    order = 'order_example' # str | The order submissions will be returned in.  Defaults to \"id\".  Doesn't affect results for \"grouped\" mode. (optional)
    order_direction = 'order_direction_example' # str | Determines whether ordered results are returned in ascending or descending order.  Defaults to \"ascending\".  Doesn't affect results for \"grouped\" mode. (optional)
    include = ['include_example'] # List[str] | Associations to include with the group. `total_scores` requires the `grouped` argument. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List submissions for multiple assignments
        api_response = await api_instance.submissions_api_for_students(course_id, student_ids=student_ids, assignment_ids=assignment_ids, grouped=grouped, post_to_sis=post_to_sis, submitted_since=submitted_since, graded_since=graded_since, grading_period_id=grading_period_id, workflow_state=workflow_state, enrollment_state=enrollment_state, state_based_on_date=state_based_on_date, order=order, order_direction=order_direction, include=include, page=page, per_page=per_page)
        print("The response of SubmissionsApiApi->submissions_api_for_students:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubmissionsApiApi->submissions_api_for_students: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **student_ids** | [**List[str]**](str.md)| List of student ids to return submissions for. If this argument is omitted, return submissions for the calling user. Students may only list their own submissions. Observers may only list those of associated students. The special id \&quot;all\&quot; will return submissions for all students in the course/section as appropriate. | [optional] 
 **assignment_ids** | [**List[str]**](str.md)| List of assignments to return submissions for. If none are given, submissions for all assignments are returned. | [optional] 
 **grouped** | **bool**| If this argument is present, the response will be grouped by student, rather than a flat array of submissions. | [optional] 
 **post_to_sis** | **bool**| If this argument is set to true, the response will only include submissions for assignments that have the post_to_sis flag set to true and user enrollments that were added through sis. | [optional] 
 **submitted_since** | **str**| If this argument is set, the response will only include submissions that were submitted after the specified date_time. This will exclude submissions that do not have a submitted_at which will exclude unsubmitted submissions. The value must be formatted as ISO 8601 YYYY-MM-DDTHH:MM:SSZ. | [optional] 
 **graded_since** | **str**| If this argument is set, the response will only include submissions that were graded after the specified date_time. This will exclude submissions that have not been graded. The value must be formatted as ISO 8601 YYYY-MM-DDTHH:MM:SSZ. | [optional] 
 **grading_period_id** | **int**| The id of the grading period in which submissions are being requested (Requires grading periods to exist on the account) | [optional] 
 **workflow_state** | **str**| The current status of the submission | [optional] 
 **enrollment_state** | **str**| The current state of the enrollments. If omitted will include all enrollments that are not deleted. | [optional] 
 **state_based_on_date** | **bool**| If omitted it is set to true. When set to false it will ignore the effective state of the student enrollments and use the workflow_state for the enrollments. The argument is ignored unless enrollment_state argument is also passed. | [optional] 
 **order** | **str**| The order submissions will be returned in.  Defaults to \&quot;id\&quot;.  Doesn&#39;t affect results for \&quot;grouped\&quot; mode. | [optional] 
 **order_direction** | **str**| Determines whether ordered results are returned in ascending or descending order.  Defaults to \&quot;ascending\&quot;.  Doesn&#39;t affect results for \&quot;grouped\&quot; mode. | [optional] 
 **include** | [**List[str]**](str.md)| Associations to include with the group. &#x60;total_scores&#x60; requires the &#x60;grouped&#x60; argument. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[Submission]**](Submission.md)

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

# **submissions_api_for_students_for_sections**
> List[Submission] submissions_api_for_students_for_sections(section_id, student_ids=student_ids, assignment_ids=assignment_ids, grouped=grouped, post_to_sis=post_to_sis, submitted_since=submitted_since, graded_since=graded_since, grading_period_id=grading_period_id, workflow_state=workflow_state, enrollment_state=enrollment_state, state_based_on_date=state_based_on_date, order=order, order_direction=order_direction, include=include, page=page, per_page=per_page)

List submissions for multiple assignments

A paginated list of all existing submissions for a given set of students and assignments.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.submission import Submission
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
    api_instance = canvas_lms_python_client.SubmissionsApiApi(api_client)
    section_id = 'section_id_example' # str | Scope response to section_id
    student_ids = ['student_ids_example'] # List[str] | List of student ids to return submissions for. If this argument is omitted, return submissions for the calling user. Students may only list their own submissions. Observers may only list those of associated students. The special id \"all\" will return submissions for all students in the course/section as appropriate. (optional)
    assignment_ids = ['assignment_ids_example'] # List[str] | List of assignments to return submissions for. If none are given, submissions for all assignments are returned. (optional)
    grouped = True # bool | If this argument is present, the response will be grouped by student, rather than a flat array of submissions. (optional)
    post_to_sis = True # bool | If this argument is set to true, the response will only include submissions for assignments that have the post_to_sis flag set to true and user enrollments that were added through sis. (optional)
    submitted_since = 'submitted_since_example' # str | If this argument is set, the response will only include submissions that were submitted after the specified date_time. This will exclude submissions that do not have a submitted_at which will exclude unsubmitted submissions. The value must be formatted as ISO 8601 YYYY-MM-DDTHH:MM:SSZ. (optional)
    graded_since = 'graded_since_example' # str | If this argument is set, the response will only include submissions that were graded after the specified date_time. This will exclude submissions that have not been graded. The value must be formatted as ISO 8601 YYYY-MM-DDTHH:MM:SSZ. (optional)
    grading_period_id = 56 # int | The id of the grading period in which submissions are being requested (Requires grading periods to exist on the account) (optional)
    workflow_state = 'workflow_state_example' # str | The current status of the submission (optional)
    enrollment_state = 'enrollment_state_example' # str | The current state of the enrollments. If omitted will include all enrollments that are not deleted. (optional)
    state_based_on_date = True # bool | If omitted it is set to true. When set to false it will ignore the effective state of the student enrollments and use the workflow_state for the enrollments. The argument is ignored unless enrollment_state argument is also passed. (optional)
    order = 'order_example' # str | The order submissions will be returned in.  Defaults to \"id\".  Doesn't affect results for \"grouped\" mode. (optional)
    order_direction = 'order_direction_example' # str | Determines whether ordered results are returned in ascending or descending order.  Defaults to \"ascending\".  Doesn't affect results for \"grouped\" mode. (optional)
    include = ['include_example'] # List[str] | Associations to include with the group. `total_scores` requires the `grouped` argument. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List submissions for multiple assignments
        api_response = await api_instance.submissions_api_for_students_for_sections(section_id, student_ids=student_ids, assignment_ids=assignment_ids, grouped=grouped, post_to_sis=post_to_sis, submitted_since=submitted_since, graded_since=graded_since, grading_period_id=grading_period_id, workflow_state=workflow_state, enrollment_state=enrollment_state, state_based_on_date=state_based_on_date, order=order, order_direction=order_direction, include=include, page=page, per_page=per_page)
        print("The response of SubmissionsApiApi->submissions_api_for_students_for_sections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubmissionsApiApi->submissions_api_for_students_for_sections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **section_id** | **str**| Scope response to section_id | 
 **student_ids** | [**List[str]**](str.md)| List of student ids to return submissions for. If this argument is omitted, return submissions for the calling user. Students may only list their own submissions. Observers may only list those of associated students. The special id \&quot;all\&quot; will return submissions for all students in the course/section as appropriate. | [optional] 
 **assignment_ids** | [**List[str]**](str.md)| List of assignments to return submissions for. If none are given, submissions for all assignments are returned. | [optional] 
 **grouped** | **bool**| If this argument is present, the response will be grouped by student, rather than a flat array of submissions. | [optional] 
 **post_to_sis** | **bool**| If this argument is set to true, the response will only include submissions for assignments that have the post_to_sis flag set to true and user enrollments that were added through sis. | [optional] 
 **submitted_since** | **str**| If this argument is set, the response will only include submissions that were submitted after the specified date_time. This will exclude submissions that do not have a submitted_at which will exclude unsubmitted submissions. The value must be formatted as ISO 8601 YYYY-MM-DDTHH:MM:SSZ. | [optional] 
 **graded_since** | **str**| If this argument is set, the response will only include submissions that were graded after the specified date_time. This will exclude submissions that have not been graded. The value must be formatted as ISO 8601 YYYY-MM-DDTHH:MM:SSZ. | [optional] 
 **grading_period_id** | **int**| The id of the grading period in which submissions are being requested (Requires grading periods to exist on the account) | [optional] 
 **workflow_state** | **str**| The current status of the submission | [optional] 
 **enrollment_state** | **str**| The current state of the enrollments. If omitted will include all enrollments that are not deleted. | [optional] 
 **state_based_on_date** | **bool**| If omitted it is set to true. When set to false it will ignore the effective state of the student enrollments and use the workflow_state for the enrollments. The argument is ignored unless enrollment_state argument is also passed. | [optional] 
 **order** | **str**| The order submissions will be returned in.  Defaults to \&quot;id\&quot;.  Doesn&#39;t affect results for \&quot;grouped\&quot; mode. | [optional] 
 **order_direction** | **str**| Determines whether ordered results are returned in ascending or descending order.  Defaults to \&quot;ascending\&quot;.  Doesn&#39;t affect results for \&quot;grouped\&quot; mode. | [optional] 
 **include** | [**List[str]**](str.md)| Associations to include with the group. &#x60;total_scores&#x60; requires the &#x60;grouped&#x60; argument. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[Submission]**](Submission.md)

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

# **submissions_api_gradeable_students**
> List[AnonymousUserDisplay] submissions_api_gradeable_students(assignment_id, course_id, sort=sort, order=order, page=page, per_page=per_page)

List gradeable students

A paginated list of gradeable students for the assignment. The caller must have permission to view grades.

If anonymous grading is enabled for the current assignment and the allow_new_anonymous_id parameter is passed,
the returned data will not include any values identifying the student, but will instead include an
assignment-specific anonymous ID for each student.

Section-limited instructors will only see students in their own sections.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.anonymous_user_display import AnonymousUserDisplay
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
    api_instance = canvas_lms_python_client.SubmissionsApiApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    course_id = 'course_id_example' # str | Scope response to course_id
    sort = 'sort_example' # str | Sort results by this field. (optional)
    order = 'order_example' # str | The sorting order. Defaults to 'asc'. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List gradeable students
        api_response = await api_instance.submissions_api_gradeable_students(assignment_id, course_id, sort=sort, order=order, page=page, per_page=per_page)
        print("The response of SubmissionsApiApi->submissions_api_gradeable_students:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubmissionsApiApi->submissions_api_gradeable_students: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **course_id** | **str**| Scope response to course_id | 
 **sort** | **str**| Sort results by this field. | [optional] 
 **order** | **str**| The sorting order. Defaults to &#39;asc&#39;. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[AnonymousUserDisplay]**](AnonymousUserDisplay.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | if anonymous grading is enabled for the assignment and the allow_new_anonymous_id parameter is true |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submissions_api_index**
> List[Submission] submissions_api_index(assignment_id, course_id, include=include, grouped=grouped, page=page, per_page=per_page)

List assignment submissions

A paginated list of all existing submissions for an assignment.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.submission import Submission
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
    api_instance = canvas_lms_python_client.SubmissionsApiApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    course_id = 'course_id_example' # str | Scope response to course_id
    include = ['include_example'] # List[str] | Associations to include with the group.  \"group\" will add group_id and group_name. (optional)
    grouped = True # bool | If this argument is true, the response will be grouped by student groups. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List assignment submissions
        api_response = await api_instance.submissions_api_index(assignment_id, course_id, include=include, grouped=grouped, page=page, per_page=per_page)
        print("The response of SubmissionsApiApi->submissions_api_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubmissionsApiApi->submissions_api_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **course_id** | **str**| Scope response to course_id | 
 **include** | [**List[str]**](str.md)| Associations to include with the group.  \&quot;group\&quot; will add group_id and group_name. | [optional] 
 **grouped** | **bool**| If this argument is true, the response will be grouped by student groups. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[Submission]**](Submission.md)

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

# **submissions_api_index_for_sections**
> List[Submission] submissions_api_index_for_sections(assignment_id, section_id, include=include, grouped=grouped, page=page, per_page=per_page)

List assignment submissions

A paginated list of all existing submissions for an assignment.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.submission import Submission
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
    api_instance = canvas_lms_python_client.SubmissionsApiApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    section_id = 'section_id_example' # str | Scope response to section_id
    include = ['include_example'] # List[str] | Associations to include with the group.  \"group\" will add group_id and group_name. (optional)
    grouped = True # bool | If this argument is true, the response will be grouped by student groups. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List assignment submissions
        api_response = await api_instance.submissions_api_index_for_sections(assignment_id, section_id, include=include, grouped=grouped, page=page, per_page=per_page)
        print("The response of SubmissionsApiApi->submissions_api_index_for_sections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubmissionsApiApi->submissions_api_index_for_sections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **section_id** | **str**| Scope response to section_id | 
 **include** | [**List[str]**](str.md)| Associations to include with the group.  \&quot;group\&quot; will add group_id and group_name. | [optional] 
 **grouped** | **bool**| If this argument is true, the response will be grouped by student groups. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[Submission]**](Submission.md)

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

# **submissions_api_mark_bulk_submissions_as_read**
> submissions_api_mark_bulk_submissions_as_read(course_id, submissions_api_mark_bulk_submissions_as_read_request=submissions_api_mark_bulk_submissions_as_read_request)

Mark bulk submissions as read

Accepts a string array of submission ids. Loops through and marks each submission as read

On success, the response will be 204 No Content with an empty body.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.submissions_api_mark_bulk_submissions_as_read_request import SubmissionsApiMarkBulkSubmissionsAsReadRequest
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
    api_instance = canvas_lms_python_client.SubmissionsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    submissions_api_mark_bulk_submissions_as_read_request = canvas_lms_python_client.SubmissionsApiMarkBulkSubmissionsAsReadRequest() # SubmissionsApiMarkBulkSubmissionsAsReadRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/courses/<course_id>/submissions/bulk_mark_read.json' \\      -X PUT \\      -H \"Authorization: Bearer <token>\" \\      -H \"Content-Length: 0\" \\      -F 'submissionIds=['88']' ``` (optional)

    try:
        # Mark bulk submissions as read
        await api_instance.submissions_api_mark_bulk_submissions_as_read(course_id, submissions_api_mark_bulk_submissions_as_read_request=submissions_api_mark_bulk_submissions_as_read_request)
    except Exception as e:
        print("Exception when calling SubmissionsApiApi->submissions_api_mark_bulk_submissions_as_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **submissions_api_mark_bulk_submissions_as_read_request** | [**SubmissionsApiMarkBulkSubmissionsAsReadRequest**](SubmissionsApiMarkBulkSubmissionsAsReadRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/courses/&lt;course_id&gt;/submissions/bulk_mark_read.json&#39; \\      -X PUT \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; \\      -H \&quot;Content-Length: 0\&quot; \\      -F &#39;submissionIds&#x3D;[&#39;88&#39;]&#39; &#x60;&#x60;&#x60; | [optional] 

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
**0** | Mark bulk submissions as read |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submissions_api_mark_bulk_submissions_as_read_for_sections**
> submissions_api_mark_bulk_submissions_as_read_for_sections(section_id, submissions_api_mark_bulk_submissions_as_read_request=submissions_api_mark_bulk_submissions_as_read_request)

Mark bulk submissions as read

Accepts a string array of submission ids. Loops through and marks each submission as read

On success, the response will be 204 No Content with an empty body.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.submissions_api_mark_bulk_submissions_as_read_request import SubmissionsApiMarkBulkSubmissionsAsReadRequest
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
    api_instance = canvas_lms_python_client.SubmissionsApiApi(api_client)
    section_id = 'section_id_example' # str | Scope response to section_id
    submissions_api_mark_bulk_submissions_as_read_request = canvas_lms_python_client.SubmissionsApiMarkBulkSubmissionsAsReadRequest() # SubmissionsApiMarkBulkSubmissionsAsReadRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/courses/<course_id>/submissions/bulk_mark_read.json' \\      -X PUT \\      -H \"Authorization: Bearer <token>\" \\      -H \"Content-Length: 0\" \\      -F 'submissionIds=['88']' ``` (optional)

    try:
        # Mark bulk submissions as read
        await api_instance.submissions_api_mark_bulk_submissions_as_read_for_sections(section_id, submissions_api_mark_bulk_submissions_as_read_request=submissions_api_mark_bulk_submissions_as_read_request)
    except Exception as e:
        print("Exception when calling SubmissionsApiApi->submissions_api_mark_bulk_submissions_as_read_for_sections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **section_id** | **str**| Scope response to section_id | 
 **submissions_api_mark_bulk_submissions_as_read_request** | [**SubmissionsApiMarkBulkSubmissionsAsReadRequest**](SubmissionsApiMarkBulkSubmissionsAsReadRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/courses/&lt;course_id&gt;/submissions/bulk_mark_read.json&#39; \\      -X PUT \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; \\      -H \&quot;Content-Length: 0\&quot; \\      -F &#39;submissionIds&#x3D;[&#39;88&#39;]&#39; &#x60;&#x60;&#x60; | [optional] 

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
**0** | Mark bulk submissions as read |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submissions_api_mark_document_annotations_read**
> submissions_api_mark_document_annotations_read(assignment_id, course_id, user_id)

Mark document annotations as read

Indicate that annotations made on a submitted document have been read by the student.
Only the student who owns the submission can use this endpoint.

NOTE: Document annotations will be marked as read automatically when they are viewed in Canvas web.

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
    api_instance = canvas_lms_python_client.SubmissionsApiApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    course_id = 'course_id_example' # str | Scope response to course_id
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # Mark document annotations as read
        await api_instance.submissions_api_mark_document_annotations_read(assignment_id, course_id, user_id)
    except Exception as e:
        print("Exception when calling SubmissionsApiApi->submissions_api_mark_document_annotations_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **course_id** | **str**| Scope response to course_id | 
 **user_id** | **str**| Scope response to user_id | 

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
**0** | Mark document annotations as read |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submissions_api_mark_document_annotations_read_for_sections**
> submissions_api_mark_document_annotations_read_for_sections(assignment_id, section_id, user_id)

Mark document annotations as read

Indicate that annotations made on a submitted document have been read by the student.
Only the student who owns the submission can use this endpoint.

NOTE: Document annotations will be marked as read automatically when they are viewed in Canvas web.

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
    api_instance = canvas_lms_python_client.SubmissionsApiApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    section_id = 'section_id_example' # str | Scope response to section_id
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # Mark document annotations as read
        await api_instance.submissions_api_mark_document_annotations_read_for_sections(assignment_id, section_id, user_id)
    except Exception as e:
        print("Exception when calling SubmissionsApiApi->submissions_api_mark_document_annotations_read_for_sections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **section_id** | **str**| Scope response to section_id | 
 **user_id** | **str**| Scope response to user_id | 

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
**0** | Mark document annotations as read |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submissions_api_mark_rubric_assessments_read**
> submissions_api_mark_rubric_assessments_read(assignment_id, course_id, user_id)

Mark rubric assessments as read

Indicate that rubric comments/grading made on a submission have been read by the student being assessed.
Only the student who owns the submission can use this endpoint.

NOTE: Rubric assessments will be marked as read automatically when they are viewed in Canvas web.

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
    api_instance = canvas_lms_python_client.SubmissionsApiApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    course_id = 'course_id_example' # str | Scope response to course_id
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # Mark rubric assessments as read
        await api_instance.submissions_api_mark_rubric_assessments_read(assignment_id, course_id, user_id)
    except Exception as e:
        print("Exception when calling SubmissionsApiApi->submissions_api_mark_rubric_assessments_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **course_id** | **str**| Scope response to course_id | 
 **user_id** | **str**| Scope response to user_id | 

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
**0** | Mark rubric assessments as read |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submissions_api_mark_rubric_assessments_read_by_user_id_for_sections**
> submissions_api_mark_rubric_assessments_read_by_user_id_for_sections(assignment_id, section_id, user_id)

Mark rubric assessments as read

Indicate that rubric comments/grading made on a submission have been read by the student being assessed.
Only the student who owns the submission can use this endpoint.

NOTE: Rubric assessments will be marked as read automatically when they are viewed in Canvas web.

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
    api_instance = canvas_lms_python_client.SubmissionsApiApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    section_id = 'section_id_example' # str | Scope response to section_id
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # Mark rubric assessments as read
        await api_instance.submissions_api_mark_rubric_assessments_read_by_user_id_for_sections(assignment_id, section_id, user_id)
    except Exception as e:
        print("Exception when calling SubmissionsApiApi->submissions_api_mark_rubric_assessments_read_by_user_id_for_sections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **section_id** | **str**| Scope response to section_id | 
 **user_id** | **str**| Scope response to user_id | 

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
**0** | Mark rubric assessments as read |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submissions_api_mark_rubric_assessments_read_for_courses**
> submissions_api_mark_rubric_assessments_read_for_courses(assignment_id, course_id, user_id)

Mark rubric assessments as read

Indicate that rubric comments/grading made on a submission have been read by the student being assessed.
Only the student who owns the submission can use this endpoint.

NOTE: Rubric assessments will be marked as read automatically when they are viewed in Canvas web.

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
    api_instance = canvas_lms_python_client.SubmissionsApiApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    course_id = 'course_id_example' # str | Scope response to course_id
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # Mark rubric assessments as read
        await api_instance.submissions_api_mark_rubric_assessments_read_for_courses(assignment_id, course_id, user_id)
    except Exception as e:
        print("Exception when calling SubmissionsApiApi->submissions_api_mark_rubric_assessments_read_for_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **course_id** | **str**| Scope response to course_id | 
 **user_id** | **str**| Scope response to user_id | 

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
**0** | Mark rubric assessments as read |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submissions_api_mark_rubric_assessments_read_for_sections**
> submissions_api_mark_rubric_assessments_read_for_sections(assignment_id, section_id, user_id)

Mark rubric assessments as read

Indicate that rubric comments/grading made on a submission have been read by the student being assessed.
Only the student who owns the submission can use this endpoint.

NOTE: Rubric assessments will be marked as read automatically when they are viewed in Canvas web.

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
    api_instance = canvas_lms_python_client.SubmissionsApiApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    section_id = 'section_id_example' # str | Scope response to section_id
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # Mark rubric assessments as read
        await api_instance.submissions_api_mark_rubric_assessments_read_for_sections(assignment_id, section_id, user_id)
    except Exception as e:
        print("Exception when calling SubmissionsApiApi->submissions_api_mark_rubric_assessments_read_for_sections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **section_id** | **str**| Scope response to section_id | 
 **user_id** | **str**| Scope response to user_id | 

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
**0** | Mark rubric assessments as read |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submissions_api_mark_submission_item_read**
> submissions_api_mark_submission_item_read(assignment_id, course_id, item, user_id)

Mark submission item as read

No request fields are necessary.

A submission item can be "grade", "comment" or "rubric"

On success, the response will be 204 No Content with an empty body.

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
    api_instance = canvas_lms_python_client.SubmissionsApiApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    course_id = 'course_id_example' # str | Scope response to course_id
    item = 'item_example' # str | Scope response to item
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # Mark submission item as read
        await api_instance.submissions_api_mark_submission_item_read(assignment_id, course_id, item, user_id)
    except Exception as e:
        print("Exception when calling SubmissionsApiApi->submissions_api_mark_submission_item_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **course_id** | **str**| Scope response to course_id | 
 **item** | **str**| Scope response to item | 
 **user_id** | **str**| Scope response to user_id | 

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
**0** | Mark submission item as read |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submissions_api_mark_submission_item_read_for_sections**
> submissions_api_mark_submission_item_read_for_sections(assignment_id, item, section_id, user_id)

Mark submission item as read

No request fields are necessary.

A submission item can be "grade", "comment" or "rubric"

On success, the response will be 204 No Content with an empty body.

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
    api_instance = canvas_lms_python_client.SubmissionsApiApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    item = 'item_example' # str | Scope response to item
    section_id = 'section_id_example' # str | Scope response to section_id
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # Mark submission item as read
        await api_instance.submissions_api_mark_submission_item_read_for_sections(assignment_id, item, section_id, user_id)
    except Exception as e:
        print("Exception when calling SubmissionsApiApi->submissions_api_mark_submission_item_read_for_sections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **item** | **str**| Scope response to item | 
 **section_id** | **str**| Scope response to section_id | 
 **user_id** | **str**| Scope response to user_id | 

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
**0** | Mark submission item as read |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submissions_api_mark_submission_read**
> submissions_api_mark_submission_read(assignment_id, course_id, user_id)

Mark submission as read

No request fields are necessary.

On success, the response will be 204 No Content with an empty body.

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
    api_instance = canvas_lms_python_client.SubmissionsApiApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    course_id = 'course_id_example' # str | Scope response to course_id
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # Mark submission as read
        await api_instance.submissions_api_mark_submission_read(assignment_id, course_id, user_id)
    except Exception as e:
        print("Exception when calling SubmissionsApiApi->submissions_api_mark_submission_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **course_id** | **str**| Scope response to course_id | 
 **user_id** | **str**| Scope response to user_id | 

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
**0** | Mark submission as read |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submissions_api_mark_submission_read_for_sections**
> submissions_api_mark_submission_read_for_sections(assignment_id, section_id, user_id)

Mark submission as read

No request fields are necessary.

On success, the response will be 204 No Content with an empty body.

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
    api_instance = canvas_lms_python_client.SubmissionsApiApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    section_id = 'section_id_example' # str | Scope response to section_id
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # Mark submission as read
        await api_instance.submissions_api_mark_submission_read_for_sections(assignment_id, section_id, user_id)
    except Exception as e:
        print("Exception when calling SubmissionsApiApi->submissions_api_mark_submission_read_for_sections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **section_id** | **str**| Scope response to section_id | 
 **user_id** | **str**| Scope response to user_id | 

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
**0** | Mark submission as read |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submissions_api_mark_submission_unread**
> submissions_api_mark_submission_unread(assignment_id, course_id, user_id)

Mark submission as unread

No request fields are necessary.

On success, the response will be 204 No Content with an empty body.

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
    api_instance = canvas_lms_python_client.SubmissionsApiApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    course_id = 'course_id_example' # str | Scope response to course_id
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # Mark submission as unread
        await api_instance.submissions_api_mark_submission_unread(assignment_id, course_id, user_id)
    except Exception as e:
        print("Exception when calling SubmissionsApiApi->submissions_api_mark_submission_unread: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **course_id** | **str**| Scope response to course_id | 
 **user_id** | **str**| Scope response to user_id | 

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
**0** | Mark submission as unread |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submissions_api_mark_submission_unread_for_sections**
> submissions_api_mark_submission_unread_for_sections(assignment_id, section_id, user_id)

Mark submission as unread

No request fields are necessary.

On success, the response will be 204 No Content with an empty body.

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
    api_instance = canvas_lms_python_client.SubmissionsApiApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    section_id = 'section_id_example' # str | Scope response to section_id
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # Mark submission as unread
        await api_instance.submissions_api_mark_submission_unread_for_sections(assignment_id, section_id, user_id)
    except Exception as e:
        print("Exception when calling SubmissionsApiApi->submissions_api_mark_submission_unread_for_sections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **section_id** | **str**| Scope response to section_id | 
 **user_id** | **str**| Scope response to user_id | 

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
**0** | Mark submission as unread |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submissions_api_multiple_gradeable_students**
> List[MultipleGradeableStudent] submissions_api_multiple_gradeable_students(course_id, assignment_ids=assignment_ids, page=page, per_page=per_page)

List multiple assignments gradeable students

A paginated list of students eligible to submit a list of assignments. The caller must have
permission to view grades for the requested course.

Section-limited instructors will only see students in their own sections.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.multiple_gradeable_student import MultipleGradeableStudent
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
    api_instance = canvas_lms_python_client.SubmissionsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    assignment_ids = ['assignment_ids_example'] # List[str] | Assignments being requested (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List multiple assignments gradeable students
        api_response = await api_instance.submissions_api_multiple_gradeable_students(course_id, assignment_ids=assignment_ids, page=page, per_page=per_page)
        print("The response of SubmissionsApiApi->submissions_api_multiple_gradeable_students:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubmissionsApiApi->submissions_api_multiple_gradeable_students: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **assignment_ids** | [**List[str]**](str.md)| Assignments being requested | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[MultipleGradeableStudent]**](MultipleGradeableStudent.md)

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

# **submissions_api_rubric_assessments_read_state**
> submissions_api_rubric_assessments_read_state(assignment_id, course_id, user_id)

Get rubric assessments read state

Return whether new rubric comments/grading made on a submission have been seen by the student being assessed.

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
    api_instance = canvas_lms_python_client.SubmissionsApiApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    course_id = 'course_id_example' # str | Scope response to course_id
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # Get rubric assessments read state
        await api_instance.submissions_api_rubric_assessments_read_state(assignment_id, course_id, user_id)
    except Exception as e:
        print("Exception when calling SubmissionsApiApi->submissions_api_rubric_assessments_read_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **course_id** | **str**| Scope response to course_id | 
 **user_id** | **str**| Scope response to user_id | 

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
**0** | Get rubric assessments read state |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submissions_api_rubric_assessments_read_state_by_user_id_for_sections**
> submissions_api_rubric_assessments_read_state_by_user_id_for_sections(assignment_id, section_id, user_id)

Get rubric assessments read state

Return whether new rubric comments/grading made on a submission have been seen by the student being assessed.

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
    api_instance = canvas_lms_python_client.SubmissionsApiApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    section_id = 'section_id_example' # str | Scope response to section_id
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # Get rubric assessments read state
        await api_instance.submissions_api_rubric_assessments_read_state_by_user_id_for_sections(assignment_id, section_id, user_id)
    except Exception as e:
        print("Exception when calling SubmissionsApiApi->submissions_api_rubric_assessments_read_state_by_user_id_for_sections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **section_id** | **str**| Scope response to section_id | 
 **user_id** | **str**| Scope response to user_id | 

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
**0** | Get rubric assessments read state |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submissions_api_rubric_assessments_read_state_for_courses**
> submissions_api_rubric_assessments_read_state_for_courses(assignment_id, course_id, user_id)

Get rubric assessments read state

Return whether new rubric comments/grading made on a submission have been seen by the student being assessed.

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
    api_instance = canvas_lms_python_client.SubmissionsApiApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    course_id = 'course_id_example' # str | Scope response to course_id
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # Get rubric assessments read state
        await api_instance.submissions_api_rubric_assessments_read_state_for_courses(assignment_id, course_id, user_id)
    except Exception as e:
        print("Exception when calling SubmissionsApiApi->submissions_api_rubric_assessments_read_state_for_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **course_id** | **str**| Scope response to course_id | 
 **user_id** | **str**| Scope response to user_id | 

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
**0** | Get rubric assessments read state |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submissions_api_rubric_assessments_read_state_for_sections**
> submissions_api_rubric_assessments_read_state_for_sections(assignment_id, section_id, user_id)

Get rubric assessments read state

Return whether new rubric comments/grading made on a submission have been seen by the student being assessed.

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
    api_instance = canvas_lms_python_client.SubmissionsApiApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    section_id = 'section_id_example' # str | Scope response to section_id
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # Get rubric assessments read state
        await api_instance.submissions_api_rubric_assessments_read_state_for_sections(assignment_id, section_id, user_id)
    except Exception as e:
        print("Exception when calling SubmissionsApiApi->submissions_api_rubric_assessments_read_state_for_sections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **section_id** | **str**| Scope response to section_id | 
 **user_id** | **str**| Scope response to user_id | 

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
**0** | Get rubric assessments read state |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submissions_api_show**
> submissions_api_show(assignment_id, course_id, user_id, include=include)

Get a single submission

Get a single submission, based on user id.

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
    api_instance = canvas_lms_python_client.SubmissionsApiApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    course_id = 'course_id_example' # str | Scope response to course_id
    user_id = 'user_id_example' # str | Scope response to user_id
    include = ['include_example'] # List[str] | Associations to include with the group. (optional)

    try:
        # Get a single submission
        await api_instance.submissions_api_show(assignment_id, course_id, user_id, include=include)
    except Exception as e:
        print("Exception when calling SubmissionsApiApi->submissions_api_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **course_id** | **str**| Scope response to course_id | 
 **user_id** | **str**| Scope response to user_id | 
 **include** | [**List[str]**](str.md)| Associations to include with the group. | [optional] 

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
**0** | Get a single submission |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submissions_api_show_anonymous**
> Submission submissions_api_show_anonymous(anonymous_id, assignment_id, course_id, include=include)

Get a single submission by anonymous id

Get a single submission, based on the submission's anonymous id.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.submission import Submission
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
    api_instance = canvas_lms_python_client.SubmissionsApiApi(api_client)
    anonymous_id = 'anonymous_id_example' # str | Scope response to anonymous_id
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    course_id = 'course_id_example' # str | Scope response to course_id
    include = ['include_example'] # List[str] | Associations to include with the group. (optional)

    try:
        # Get a single submission by anonymous id
        api_response = await api_instance.submissions_api_show_anonymous(anonymous_id, assignment_id, course_id, include=include)
        print("The response of SubmissionsApiApi->submissions_api_show_anonymous:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubmissionsApiApi->submissions_api_show_anonymous: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anonymous_id** | **str**| Scope response to anonymous_id | 
 **assignment_id** | **str**| Scope response to assignment_id | 
 **course_id** | **str**| Scope response to course_id | 
 **include** | [**List[str]**](str.md)| Associations to include with the group. | [optional] 

### Return type

[**Submission**](Submission.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Submission |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submissions_api_show_anonymous_for_sections**
> Submission submissions_api_show_anonymous_for_sections(anonymous_id, assignment_id, section_id, include=include)

Get a single submission by anonymous id

Get a single submission, based on the submission's anonymous id.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.submission import Submission
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
    api_instance = canvas_lms_python_client.SubmissionsApiApi(api_client)
    anonymous_id = 'anonymous_id_example' # str | Scope response to anonymous_id
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    section_id = 'section_id_example' # str | Scope response to section_id
    include = ['include_example'] # List[str] | Associations to include with the group. (optional)

    try:
        # Get a single submission by anonymous id
        api_response = await api_instance.submissions_api_show_anonymous_for_sections(anonymous_id, assignment_id, section_id, include=include)
        print("The response of SubmissionsApiApi->submissions_api_show_anonymous_for_sections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubmissionsApiApi->submissions_api_show_anonymous_for_sections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anonymous_id** | **str**| Scope response to anonymous_id | 
 **assignment_id** | **str**| Scope response to assignment_id | 
 **section_id** | **str**| Scope response to section_id | 
 **include** | [**List[str]**](str.md)| Associations to include with the group. | [optional] 

### Return type

[**Submission**](Submission.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Submission |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submissions_api_show_for_sections**
> submissions_api_show_for_sections(assignment_id, section_id, user_id, include=include)

Get a single submission

Get a single submission, based on user id.

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
    api_instance = canvas_lms_python_client.SubmissionsApiApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    section_id = 'section_id_example' # str | Scope response to section_id
    user_id = 'user_id_example' # str | Scope response to user_id
    include = ['include_example'] # List[str] | Associations to include with the group. (optional)

    try:
        # Get a single submission
        await api_instance.submissions_api_show_for_sections(assignment_id, section_id, user_id, include=include)
    except Exception as e:
        print("Exception when calling SubmissionsApiApi->submissions_api_show_for_sections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **section_id** | **str**| Scope response to section_id | 
 **user_id** | **str**| Scope response to user_id | 
 **include** | [**List[str]**](str.md)| Associations to include with the group. | [optional] 

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
**0** | Get a single submission |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submissions_api_submission_summary**
> submissions_api_submission_summary(assignment_id, course_id, grouped=grouped, include_deactivated=include_deactivated)

Submission Summary

Returns the number of submissions for the given assignment based on gradeable students
that fall into three categories: graded, ungraded, not submitted.

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
    api_instance = canvas_lms_python_client.SubmissionsApiApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    course_id = 'course_id_example' # str | Scope response to course_id
    grouped = True # bool | If this argument is true, the response will take into account student groups. (optional)
    include_deactivated = True # bool | If this argument is true, the response will include deactivated students in the summary (defaults to false). (optional)

    try:
        # Submission Summary
        await api_instance.submissions_api_submission_summary(assignment_id, course_id, grouped=grouped, include_deactivated=include_deactivated)
    except Exception as e:
        print("Exception when calling SubmissionsApiApi->submissions_api_submission_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **course_id** | **str**| Scope response to course_id | 
 **grouped** | **bool**| If this argument is true, the response will take into account student groups. | [optional] 
 **include_deactivated** | **bool**| If this argument is true, the response will include deactivated students in the summary (defaults to false). | [optional] 

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
**0** | Submission Summary |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submissions_api_submission_summary_for_sections**
> submissions_api_submission_summary_for_sections(assignment_id, section_id, grouped=grouped, include_deactivated=include_deactivated)

Submission Summary

Returns the number of submissions for the given assignment based on gradeable students
that fall into three categories: graded, ungraded, not submitted.

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
    api_instance = canvas_lms_python_client.SubmissionsApiApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    section_id = 'section_id_example' # str | Scope response to section_id
    grouped = True # bool | If this argument is true, the response will take into account student groups. (optional)
    include_deactivated = True # bool | If this argument is true, the response will include deactivated students in the summary (defaults to false). (optional)

    try:
        # Submission Summary
        await api_instance.submissions_api_submission_summary_for_sections(assignment_id, section_id, grouped=grouped, include_deactivated=include_deactivated)
    except Exception as e:
        print("Exception when calling SubmissionsApiApi->submissions_api_submission_summary_for_sections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **section_id** | **str**| Scope response to section_id | 
 **grouped** | **bool**| If this argument is true, the response will take into account student groups. | [optional] 
 **include_deactivated** | **bool**| If this argument is true, the response will include deactivated students in the summary (defaults to false). | [optional] 

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
**0** | Submission Summary |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submissions_api_submissions_clear_unread**
> submissions_api_submissions_clear_unread(course_id, user_id)

Clear unread status for all submissions.

Site-admin-only endpoint.

No request fields are necessary.

On success, the response will be 204 No Content with an empty body.

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
    api_instance = canvas_lms_python_client.SubmissionsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # Clear unread status for all submissions.
        await api_instance.submissions_api_submissions_clear_unread(course_id, user_id)
    except Exception as e:
        print("Exception when calling SubmissionsApiApi->submissions_api_submissions_clear_unread: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **user_id** | **str**| Scope response to user_id | 

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
**0** | Clear unread status for all submissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submissions_api_submissions_clear_unread_for_sections**
> submissions_api_submissions_clear_unread_for_sections(section_id, user_id)

Clear unread status for all submissions.

Site-admin-only endpoint.

No request fields are necessary.

On success, the response will be 204 No Content with an empty body.

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
    api_instance = canvas_lms_python_client.SubmissionsApiApi(api_client)
    section_id = 'section_id_example' # str | Scope response to section_id
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # Clear unread status for all submissions.
        await api_instance.submissions_api_submissions_clear_unread_for_sections(section_id, user_id)
    except Exception as e:
        print("Exception when calling SubmissionsApiApi->submissions_api_submissions_clear_unread_for_sections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **section_id** | **str**| Scope response to section_id | 
 **user_id** | **str**| Scope response to user_id | 

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
**0** | Clear unread status for all submissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submissions_api_update**
> submissions_api_update(assignment_id, course_id, user_id, submissions_api_update_request=submissions_api_update_request)

Grade or comment on a submission

Comment on and/or update the grading for a student's assignment submission.
If any submission or rubric_assessment arguments are provided, the user
must have permission to manage grades in the appropriate context (course or
section).

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.submissions_api_update_request import SubmissionsApiUpdateRequest
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
    api_instance = canvas_lms_python_client.SubmissionsApiApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    course_id = 'course_id_example' # str | Scope response to course_id
    user_id = 'user_id_example' # str | Scope response to user_id
    submissions_api_update_request = canvas_lms_python_client.SubmissionsApiUpdateRequest() # SubmissionsApiUpdateRequest | Request body parameters (optional)

    try:
        # Grade or comment on a submission
        await api_instance.submissions_api_update(assignment_id, course_id, user_id, submissions_api_update_request=submissions_api_update_request)
    except Exception as e:
        print("Exception when calling SubmissionsApiApi->submissions_api_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **course_id** | **str**| Scope response to course_id | 
 **user_id** | **str**| Scope response to user_id | 
 **submissions_api_update_request** | [**SubmissionsApiUpdateRequest**](SubmissionsApiUpdateRequest.md)| Request body parameters | [optional] 

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
**0** | Grade or comment on a submission |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submissions_api_update_anonymous**
> submissions_api_update_anonymous(anonymous_id, assignment_id, course_id, submissions_api_update_anonymous_request=submissions_api_update_anonymous_request)

Grade or comment on a submission by anonymous id

Comment on and/or update the grading for a student's assignment submission,
fetching the submission by anonymous id (instead of user id). If any
submission or rubric_assessment arguments are provided, the user must
have permission to manage grades in the appropriate context (course or
section).

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.submissions_api_update_anonymous_request import SubmissionsApiUpdateAnonymousRequest
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
    api_instance = canvas_lms_python_client.SubmissionsApiApi(api_client)
    anonymous_id = 'anonymous_id_example' # str | Scope response to anonymous_id
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    course_id = 'course_id_example' # str | Scope response to course_id
    submissions_api_update_anonymous_request = canvas_lms_python_client.SubmissionsApiUpdateAnonymousRequest() # SubmissionsApiUpdateAnonymousRequest | Request body parameters (optional)

    try:
        # Grade or comment on a submission by anonymous id
        await api_instance.submissions_api_update_anonymous(anonymous_id, assignment_id, course_id, submissions_api_update_anonymous_request=submissions_api_update_anonymous_request)
    except Exception as e:
        print("Exception when calling SubmissionsApiApi->submissions_api_update_anonymous: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anonymous_id** | **str**| Scope response to anonymous_id | 
 **assignment_id** | **str**| Scope response to assignment_id | 
 **course_id** | **str**| Scope response to course_id | 
 **submissions_api_update_anonymous_request** | [**SubmissionsApiUpdateAnonymousRequest**](SubmissionsApiUpdateAnonymousRequest.md)| Request body parameters | [optional] 

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
**0** | Grade or comment on a submission by anonymous id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submissions_api_update_anonymous_for_sections**
> submissions_api_update_anonymous_for_sections(anonymous_id, assignment_id, section_id, submissions_api_update_anonymous_request=submissions_api_update_anonymous_request)

Grade or comment on a submission by anonymous id

Comment on and/or update the grading for a student's assignment submission,
fetching the submission by anonymous id (instead of user id). If any
submission or rubric_assessment arguments are provided, the user must
have permission to manage grades in the appropriate context (course or
section).

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.submissions_api_update_anonymous_request import SubmissionsApiUpdateAnonymousRequest
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
    api_instance = canvas_lms_python_client.SubmissionsApiApi(api_client)
    anonymous_id = 'anonymous_id_example' # str | Scope response to anonymous_id
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    section_id = 'section_id_example' # str | Scope response to section_id
    submissions_api_update_anonymous_request = canvas_lms_python_client.SubmissionsApiUpdateAnonymousRequest() # SubmissionsApiUpdateAnonymousRequest | Request body parameters (optional)

    try:
        # Grade or comment on a submission by anonymous id
        await api_instance.submissions_api_update_anonymous_for_sections(anonymous_id, assignment_id, section_id, submissions_api_update_anonymous_request=submissions_api_update_anonymous_request)
    except Exception as e:
        print("Exception when calling SubmissionsApiApi->submissions_api_update_anonymous_for_sections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anonymous_id** | **str**| Scope response to anonymous_id | 
 **assignment_id** | **str**| Scope response to assignment_id | 
 **section_id** | **str**| Scope response to section_id | 
 **submissions_api_update_anonymous_request** | [**SubmissionsApiUpdateAnonymousRequest**](SubmissionsApiUpdateAnonymousRequest.md)| Request body parameters | [optional] 

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
**0** | Grade or comment on a submission by anonymous id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submissions_api_update_for_sections**
> submissions_api_update_for_sections(assignment_id, section_id, user_id, submissions_api_update_request=submissions_api_update_request)

Grade or comment on a submission

Comment on and/or update the grading for a student's assignment submission.
If any submission or rubric_assessment arguments are provided, the user
must have permission to manage grades in the appropriate context (course or
section).

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.submissions_api_update_request import SubmissionsApiUpdateRequest
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
    api_instance = canvas_lms_python_client.SubmissionsApiApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    section_id = 'section_id_example' # str | Scope response to section_id
    user_id = 'user_id_example' # str | Scope response to user_id
    submissions_api_update_request = canvas_lms_python_client.SubmissionsApiUpdateRequest() # SubmissionsApiUpdateRequest | Request body parameters (optional)

    try:
        # Grade or comment on a submission
        await api_instance.submissions_api_update_for_sections(assignment_id, section_id, user_id, submissions_api_update_request=submissions_api_update_request)
    except Exception as e:
        print("Exception when calling SubmissionsApiApi->submissions_api_update_for_sections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **section_id** | **str**| Scope response to section_id | 
 **user_id** | **str**| Scope response to user_id | 
 **submissions_api_update_request** | [**SubmissionsApiUpdateRequest**](SubmissionsApiUpdateRequest.md)| Request body parameters | [optional] 

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
**0** | Grade or comment on a submission |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

