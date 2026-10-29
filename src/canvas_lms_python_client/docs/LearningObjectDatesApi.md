# canvas_lms_python_client.LearningObjectDatesApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**learning_object_dates_show**](LearningObjectDatesApi.md#learning_object_dates_show) | **GET** /api/v1/courses/{course_id}/modules/{context_module_id}/date_details | Get a learning object&#39;s date information
[**learning_object_dates_show_by_attachment_id_for_courses**](LearningObjectDatesApi.md#learning_object_dates_show_by_attachment_id_for_courses) | **GET** /api/v1/courses/{course_id}/files/{attachment_id}/date_details | Get a learning object&#39;s date information
[**learning_object_dates_show_by_discussion_topic_id_for_courses**](LearningObjectDatesApi.md#learning_object_dates_show_by_discussion_topic_id_for_courses) | **GET** /api/v1/courses/{course_id}/discussion_topics/{discussion_topic_id}/date_details | Get a learning object&#39;s date information
[**learning_object_dates_show_by_quiz_id_for_courses**](LearningObjectDatesApi.md#learning_object_dates_show_by_quiz_id_for_courses) | **GET** /api/v1/courses/{course_id}/quizzes/{quiz_id}/date_details | Get a learning object&#39;s date information
[**learning_object_dates_show_by_url_or_id_for_courses**](LearningObjectDatesApi.md#learning_object_dates_show_by_url_or_id_for_courses) | **GET** /api/v1/courses/{course_id}/pages/{url_or_id}/date_details | Get a learning object&#39;s date information
[**learning_object_dates_show_for_courses**](LearningObjectDatesApi.md#learning_object_dates_show_for_courses) | **GET** /api/v1/courses/{course_id}/assignments/{assignment_id}/date_details | Get a learning object&#39;s date information
[**learning_object_dates_update**](LearningObjectDatesApi.md#learning_object_dates_update) | **PUT** /api/v1/courses/{course_id}/assignments/{assignment_id}/date_details | Update a learning object&#39;s date information
[**learning_object_dates_update_by_attachment_id_for_courses**](LearningObjectDatesApi.md#learning_object_dates_update_by_attachment_id_for_courses) | **PUT** /api/v1/courses/{course_id}/files/{attachment_id}/date_details | Update a learning object&#39;s date information
[**learning_object_dates_update_by_discussion_topic_id_for_courses**](LearningObjectDatesApi.md#learning_object_dates_update_by_discussion_topic_id_for_courses) | **PUT** /api/v1/courses/{course_id}/discussion_topics/{discussion_topic_id}/date_details | Update a learning object&#39;s date information
[**learning_object_dates_update_by_url_or_id_for_courses**](LearningObjectDatesApi.md#learning_object_dates_update_by_url_or_id_for_courses) | **PUT** /api/v1/courses/{course_id}/pages/{url_or_id}/date_details | Update a learning object&#39;s date information
[**learning_object_dates_update_for_courses**](LearningObjectDatesApi.md#learning_object_dates_update_for_courses) | **PUT** /api/v1/courses/{course_id}/quizzes/{quiz_id}/date_details | Update a learning object&#39;s date information


# **learning_object_dates_show**
> LearningObjectDates learning_object_dates_show(context_module_id, course_id, include=include, exclude=exclude, page=page, per_page=per_page)

Get a learning object's date information

Get a learning object's date-related information, including due date, availability dates,
override status, and a paginated list of all assignment overrides for the item.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.learning_object_dates import LearningObjectDates
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
    api_instance = canvas_lms_python_client.LearningObjectDatesApi(api_client)
    context_module_id = 'context_module_id_example' # str | Scope response to context_module_id
    course_id = 'course_id_example' # str | Scope response to course_id
    include = [canvas_lms_python_client.List[str]()] # List[List[str]] | Array of strings indicating what additional data to include in the response. Valid values: - \"peer_review\": includes peer review sub assignment information and overrides in the response.   If a peer review sub assignment exists, it is returned regardless of the Peer Review   Allocation and Grading feature state. If no peer review sub assignment exists,   the feature must be enabled to receive a null value; otherwise the key is omitted. - \"child_peer_review_override_dates\": each assignment override will include a peer_review_dates   field containing the matched peer review override data (id, due_at, unlock_at, lock_at)   for that override. The field will be present as null if no matching peer review override exists. (optional)
    exclude = [canvas_lms_python_client.List[str]()] # List[List[str]] | Array of strings indicating what data to exclude from the response. Valid values: - \"peer_review_overrides\": when include[]=peer_review is also specified, the   peer_review_sub_assignment object will not include the overrides array, reducing the   response payload size. This is useful when using include[]=child_peer_review_override_dates   since the peer review override data is already embedded in the parent assignment overrides. - \"child_override_due_dates\": prevents the sub_assignment_due_dates field from being included   in assignment override responses, even when discussion checkpoints are enabled. This reduces   response payload size when checkpoint due date information is not needed. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # Get a learning object's date information
        api_response = await api_instance.learning_object_dates_show(context_module_id, course_id, include=include, exclude=exclude, page=page, per_page=per_page)
        print("The response of LearningObjectDatesApi->learning_object_dates_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LearningObjectDatesApi->learning_object_dates_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context_module_id** | **str**| Scope response to context_module_id | 
 **course_id** | **str**| Scope response to course_id | 
 **include** | [**List[List[str]]**](List[str].md)| Array of strings indicating what additional data to include in the response. Valid values: - \&quot;peer_review\&quot;: includes peer review sub assignment information and overrides in the response.   If a peer review sub assignment exists, it is returned regardless of the Peer Review   Allocation and Grading feature state. If no peer review sub assignment exists,   the feature must be enabled to receive a null value; otherwise the key is omitted. - \&quot;child_peer_review_override_dates\&quot;: each assignment override will include a peer_review_dates   field containing the matched peer review override data (id, due_at, unlock_at, lock_at)   for that override. The field will be present as null if no matching peer review override exists. | [optional] 
 **exclude** | [**List[List[str]]**](List[str].md)| Array of strings indicating what data to exclude from the response. Valid values: - \&quot;peer_review_overrides\&quot;: when include[]&#x3D;peer_review is also specified, the   peer_review_sub_assignment object will not include the overrides array, reducing the   response payload size. This is useful when using include[]&#x3D;child_peer_review_override_dates   since the peer review override data is already embedded in the parent assignment overrides. - \&quot;child_override_due_dates\&quot;: prevents the sub_assignment_due_dates field from being included   in assignment override responses, even when discussion checkpoints are enabled. This reduces   response payload size when checkpoint due date information is not needed. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**LearningObjectDates**](LearningObjectDates.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | LearningObjectDates |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **learning_object_dates_show_by_attachment_id_for_courses**
> LearningObjectDates learning_object_dates_show_by_attachment_id_for_courses(attachment_id, course_id, include=include, exclude=exclude, page=page, per_page=per_page)

Get a learning object's date information

Get a learning object's date-related information, including due date, availability dates,
override status, and a paginated list of all assignment overrides for the item.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.learning_object_dates import LearningObjectDates
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
    api_instance = canvas_lms_python_client.LearningObjectDatesApi(api_client)
    attachment_id = 'attachment_id_example' # str | Scope response to attachment_id
    course_id = 'course_id_example' # str | Scope response to course_id
    include = [canvas_lms_python_client.List[str]()] # List[List[str]] | Array of strings indicating what additional data to include in the response. Valid values: - \"peer_review\": includes peer review sub assignment information and overrides in the response.   If a peer review sub assignment exists, it is returned regardless of the Peer Review   Allocation and Grading feature state. If no peer review sub assignment exists,   the feature must be enabled to receive a null value; otherwise the key is omitted. - \"child_peer_review_override_dates\": each assignment override will include a peer_review_dates   field containing the matched peer review override data (id, due_at, unlock_at, lock_at)   for that override. The field will be present as null if no matching peer review override exists. (optional)
    exclude = [canvas_lms_python_client.List[str]()] # List[List[str]] | Array of strings indicating what data to exclude from the response. Valid values: - \"peer_review_overrides\": when include[]=peer_review is also specified, the   peer_review_sub_assignment object will not include the overrides array, reducing the   response payload size. This is useful when using include[]=child_peer_review_override_dates   since the peer review override data is already embedded in the parent assignment overrides. - \"child_override_due_dates\": prevents the sub_assignment_due_dates field from being included   in assignment override responses, even when discussion checkpoints are enabled. This reduces   response payload size when checkpoint due date information is not needed. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # Get a learning object's date information
        api_response = await api_instance.learning_object_dates_show_by_attachment_id_for_courses(attachment_id, course_id, include=include, exclude=exclude, page=page, per_page=per_page)
        print("The response of LearningObjectDatesApi->learning_object_dates_show_by_attachment_id_for_courses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LearningObjectDatesApi->learning_object_dates_show_by_attachment_id_for_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | **str**| Scope response to attachment_id | 
 **course_id** | **str**| Scope response to course_id | 
 **include** | [**List[List[str]]**](List[str].md)| Array of strings indicating what additional data to include in the response. Valid values: - \&quot;peer_review\&quot;: includes peer review sub assignment information and overrides in the response.   If a peer review sub assignment exists, it is returned regardless of the Peer Review   Allocation and Grading feature state. If no peer review sub assignment exists,   the feature must be enabled to receive a null value; otherwise the key is omitted. - \&quot;child_peer_review_override_dates\&quot;: each assignment override will include a peer_review_dates   field containing the matched peer review override data (id, due_at, unlock_at, lock_at)   for that override. The field will be present as null if no matching peer review override exists. | [optional] 
 **exclude** | [**List[List[str]]**](List[str].md)| Array of strings indicating what data to exclude from the response. Valid values: - \&quot;peer_review_overrides\&quot;: when include[]&#x3D;peer_review is also specified, the   peer_review_sub_assignment object will not include the overrides array, reducing the   response payload size. This is useful when using include[]&#x3D;child_peer_review_override_dates   since the peer review override data is already embedded in the parent assignment overrides. - \&quot;child_override_due_dates\&quot;: prevents the sub_assignment_due_dates field from being included   in assignment override responses, even when discussion checkpoints are enabled. This reduces   response payload size when checkpoint due date information is not needed. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**LearningObjectDates**](LearningObjectDates.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | LearningObjectDates |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **learning_object_dates_show_by_discussion_topic_id_for_courses**
> LearningObjectDates learning_object_dates_show_by_discussion_topic_id_for_courses(course_id, discussion_topic_id, include=include, exclude=exclude, page=page, per_page=per_page)

Get a learning object's date information

Get a learning object's date-related information, including due date, availability dates,
override status, and a paginated list of all assignment overrides for the item.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.learning_object_dates import LearningObjectDates
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
    api_instance = canvas_lms_python_client.LearningObjectDatesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    discussion_topic_id = 'discussion_topic_id_example' # str | Scope response to discussion_topic_id
    include = [canvas_lms_python_client.List[str]()] # List[List[str]] | Array of strings indicating what additional data to include in the response. Valid values: - \"peer_review\": includes peer review sub assignment information and overrides in the response.   If a peer review sub assignment exists, it is returned regardless of the Peer Review   Allocation and Grading feature state. If no peer review sub assignment exists,   the feature must be enabled to receive a null value; otherwise the key is omitted. - \"child_peer_review_override_dates\": each assignment override will include a peer_review_dates   field containing the matched peer review override data (id, due_at, unlock_at, lock_at)   for that override. The field will be present as null if no matching peer review override exists. (optional)
    exclude = [canvas_lms_python_client.List[str]()] # List[List[str]] | Array of strings indicating what data to exclude from the response. Valid values: - \"peer_review_overrides\": when include[]=peer_review is also specified, the   peer_review_sub_assignment object will not include the overrides array, reducing the   response payload size. This is useful when using include[]=child_peer_review_override_dates   since the peer review override data is already embedded in the parent assignment overrides. - \"child_override_due_dates\": prevents the sub_assignment_due_dates field from being included   in assignment override responses, even when discussion checkpoints are enabled. This reduces   response payload size when checkpoint due date information is not needed. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # Get a learning object's date information
        api_response = await api_instance.learning_object_dates_show_by_discussion_topic_id_for_courses(course_id, discussion_topic_id, include=include, exclude=exclude, page=page, per_page=per_page)
        print("The response of LearningObjectDatesApi->learning_object_dates_show_by_discussion_topic_id_for_courses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LearningObjectDatesApi->learning_object_dates_show_by_discussion_topic_id_for_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **discussion_topic_id** | **str**| Scope response to discussion_topic_id | 
 **include** | [**List[List[str]]**](List[str].md)| Array of strings indicating what additional data to include in the response. Valid values: - \&quot;peer_review\&quot;: includes peer review sub assignment information and overrides in the response.   If a peer review sub assignment exists, it is returned regardless of the Peer Review   Allocation and Grading feature state. If no peer review sub assignment exists,   the feature must be enabled to receive a null value; otherwise the key is omitted. - \&quot;child_peer_review_override_dates\&quot;: each assignment override will include a peer_review_dates   field containing the matched peer review override data (id, due_at, unlock_at, lock_at)   for that override. The field will be present as null if no matching peer review override exists. | [optional] 
 **exclude** | [**List[List[str]]**](List[str].md)| Array of strings indicating what data to exclude from the response. Valid values: - \&quot;peer_review_overrides\&quot;: when include[]&#x3D;peer_review is also specified, the   peer_review_sub_assignment object will not include the overrides array, reducing the   response payload size. This is useful when using include[]&#x3D;child_peer_review_override_dates   since the peer review override data is already embedded in the parent assignment overrides. - \&quot;child_override_due_dates\&quot;: prevents the sub_assignment_due_dates field from being included   in assignment override responses, even when discussion checkpoints are enabled. This reduces   response payload size when checkpoint due date information is not needed. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**LearningObjectDates**](LearningObjectDates.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | LearningObjectDates |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **learning_object_dates_show_by_quiz_id_for_courses**
> LearningObjectDates learning_object_dates_show_by_quiz_id_for_courses(course_id, quiz_id, include=include, exclude=exclude, page=page, per_page=per_page)

Get a learning object's date information

Get a learning object's date-related information, including due date, availability dates,
override status, and a paginated list of all assignment overrides for the item.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.learning_object_dates import LearningObjectDates
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
    api_instance = canvas_lms_python_client.LearningObjectDatesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    quiz_id = 'quiz_id_example' # str | Scope response to quiz_id
    include = [canvas_lms_python_client.List[str]()] # List[List[str]] | Array of strings indicating what additional data to include in the response. Valid values: - \"peer_review\": includes peer review sub assignment information and overrides in the response.   If a peer review sub assignment exists, it is returned regardless of the Peer Review   Allocation and Grading feature state. If no peer review sub assignment exists,   the feature must be enabled to receive a null value; otherwise the key is omitted. - \"child_peer_review_override_dates\": each assignment override will include a peer_review_dates   field containing the matched peer review override data (id, due_at, unlock_at, lock_at)   for that override. The field will be present as null if no matching peer review override exists. (optional)
    exclude = [canvas_lms_python_client.List[str]()] # List[List[str]] | Array of strings indicating what data to exclude from the response. Valid values: - \"peer_review_overrides\": when include[]=peer_review is also specified, the   peer_review_sub_assignment object will not include the overrides array, reducing the   response payload size. This is useful when using include[]=child_peer_review_override_dates   since the peer review override data is already embedded in the parent assignment overrides. - \"child_override_due_dates\": prevents the sub_assignment_due_dates field from being included   in assignment override responses, even when discussion checkpoints are enabled. This reduces   response payload size when checkpoint due date information is not needed. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # Get a learning object's date information
        api_response = await api_instance.learning_object_dates_show_by_quiz_id_for_courses(course_id, quiz_id, include=include, exclude=exclude, page=page, per_page=per_page)
        print("The response of LearningObjectDatesApi->learning_object_dates_show_by_quiz_id_for_courses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LearningObjectDatesApi->learning_object_dates_show_by_quiz_id_for_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **quiz_id** | **str**| Scope response to quiz_id | 
 **include** | [**List[List[str]]**](List[str].md)| Array of strings indicating what additional data to include in the response. Valid values: - \&quot;peer_review\&quot;: includes peer review sub assignment information and overrides in the response.   If a peer review sub assignment exists, it is returned regardless of the Peer Review   Allocation and Grading feature state. If no peer review sub assignment exists,   the feature must be enabled to receive a null value; otherwise the key is omitted. - \&quot;child_peer_review_override_dates\&quot;: each assignment override will include a peer_review_dates   field containing the matched peer review override data (id, due_at, unlock_at, lock_at)   for that override. The field will be present as null if no matching peer review override exists. | [optional] 
 **exclude** | [**List[List[str]]**](List[str].md)| Array of strings indicating what data to exclude from the response. Valid values: - \&quot;peer_review_overrides\&quot;: when include[]&#x3D;peer_review is also specified, the   peer_review_sub_assignment object will not include the overrides array, reducing the   response payload size. This is useful when using include[]&#x3D;child_peer_review_override_dates   since the peer review override data is already embedded in the parent assignment overrides. - \&quot;child_override_due_dates\&quot;: prevents the sub_assignment_due_dates field from being included   in assignment override responses, even when discussion checkpoints are enabled. This reduces   response payload size when checkpoint due date information is not needed. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**LearningObjectDates**](LearningObjectDates.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | LearningObjectDates |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **learning_object_dates_show_by_url_or_id_for_courses**
> LearningObjectDates learning_object_dates_show_by_url_or_id_for_courses(course_id, url_or_id, include=include, exclude=exclude, page=page, per_page=per_page)

Get a learning object's date information

Get a learning object's date-related information, including due date, availability dates,
override status, and a paginated list of all assignment overrides for the item.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.learning_object_dates import LearningObjectDates
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
    api_instance = canvas_lms_python_client.LearningObjectDatesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    url_or_id = 'url_or_id_example' # str | Scope response to url_or_id
    include = [canvas_lms_python_client.List[str]()] # List[List[str]] | Array of strings indicating what additional data to include in the response. Valid values: - \"peer_review\": includes peer review sub assignment information and overrides in the response.   If a peer review sub assignment exists, it is returned regardless of the Peer Review   Allocation and Grading feature state. If no peer review sub assignment exists,   the feature must be enabled to receive a null value; otherwise the key is omitted. - \"child_peer_review_override_dates\": each assignment override will include a peer_review_dates   field containing the matched peer review override data (id, due_at, unlock_at, lock_at)   for that override. The field will be present as null if no matching peer review override exists. (optional)
    exclude = [canvas_lms_python_client.List[str]()] # List[List[str]] | Array of strings indicating what data to exclude from the response. Valid values: - \"peer_review_overrides\": when include[]=peer_review is also specified, the   peer_review_sub_assignment object will not include the overrides array, reducing the   response payload size. This is useful when using include[]=child_peer_review_override_dates   since the peer review override data is already embedded in the parent assignment overrides. - \"child_override_due_dates\": prevents the sub_assignment_due_dates field from being included   in assignment override responses, even when discussion checkpoints are enabled. This reduces   response payload size when checkpoint due date information is not needed. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # Get a learning object's date information
        api_response = await api_instance.learning_object_dates_show_by_url_or_id_for_courses(course_id, url_or_id, include=include, exclude=exclude, page=page, per_page=per_page)
        print("The response of LearningObjectDatesApi->learning_object_dates_show_by_url_or_id_for_courses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LearningObjectDatesApi->learning_object_dates_show_by_url_or_id_for_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **url_or_id** | **str**| Scope response to url_or_id | 
 **include** | [**List[List[str]]**](List[str].md)| Array of strings indicating what additional data to include in the response. Valid values: - \&quot;peer_review\&quot;: includes peer review sub assignment information and overrides in the response.   If a peer review sub assignment exists, it is returned regardless of the Peer Review   Allocation and Grading feature state. If no peer review sub assignment exists,   the feature must be enabled to receive a null value; otherwise the key is omitted. - \&quot;child_peer_review_override_dates\&quot;: each assignment override will include a peer_review_dates   field containing the matched peer review override data (id, due_at, unlock_at, lock_at)   for that override. The field will be present as null if no matching peer review override exists. | [optional] 
 **exclude** | [**List[List[str]]**](List[str].md)| Array of strings indicating what data to exclude from the response. Valid values: - \&quot;peer_review_overrides\&quot;: when include[]&#x3D;peer_review is also specified, the   peer_review_sub_assignment object will not include the overrides array, reducing the   response payload size. This is useful when using include[]&#x3D;child_peer_review_override_dates   since the peer review override data is already embedded in the parent assignment overrides. - \&quot;child_override_due_dates\&quot;: prevents the sub_assignment_due_dates field from being included   in assignment override responses, even when discussion checkpoints are enabled. This reduces   response payload size when checkpoint due date information is not needed. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**LearningObjectDates**](LearningObjectDates.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | LearningObjectDates |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **learning_object_dates_show_for_courses**
> LearningObjectDates learning_object_dates_show_for_courses(assignment_id, course_id, include=include, exclude=exclude, page=page, per_page=per_page)

Get a learning object's date information

Get a learning object's date-related information, including due date, availability dates,
override status, and a paginated list of all assignment overrides for the item.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.learning_object_dates import LearningObjectDates
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
    api_instance = canvas_lms_python_client.LearningObjectDatesApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    course_id = 'course_id_example' # str | Scope response to course_id
    include = [canvas_lms_python_client.List[str]()] # List[List[str]] | Array of strings indicating what additional data to include in the response. Valid values: - \"peer_review\": includes peer review sub assignment information and overrides in the response.   If a peer review sub assignment exists, it is returned regardless of the Peer Review   Allocation and Grading feature state. If no peer review sub assignment exists,   the feature must be enabled to receive a null value; otherwise the key is omitted. - \"child_peer_review_override_dates\": each assignment override will include a peer_review_dates   field containing the matched peer review override data (id, due_at, unlock_at, lock_at)   for that override. The field will be present as null if no matching peer review override exists. (optional)
    exclude = [canvas_lms_python_client.List[str]()] # List[List[str]] | Array of strings indicating what data to exclude from the response. Valid values: - \"peer_review_overrides\": when include[]=peer_review is also specified, the   peer_review_sub_assignment object will not include the overrides array, reducing the   response payload size. This is useful when using include[]=child_peer_review_override_dates   since the peer review override data is already embedded in the parent assignment overrides. - \"child_override_due_dates\": prevents the sub_assignment_due_dates field from being included   in assignment override responses, even when discussion checkpoints are enabled. This reduces   response payload size when checkpoint due date information is not needed. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # Get a learning object's date information
        api_response = await api_instance.learning_object_dates_show_for_courses(assignment_id, course_id, include=include, exclude=exclude, page=page, per_page=per_page)
        print("The response of LearningObjectDatesApi->learning_object_dates_show_for_courses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LearningObjectDatesApi->learning_object_dates_show_for_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **course_id** | **str**| Scope response to course_id | 
 **include** | [**List[List[str]]**](List[str].md)| Array of strings indicating what additional data to include in the response. Valid values: - \&quot;peer_review\&quot;: includes peer review sub assignment information and overrides in the response.   If a peer review sub assignment exists, it is returned regardless of the Peer Review   Allocation and Grading feature state. If no peer review sub assignment exists,   the feature must be enabled to receive a null value; otherwise the key is omitted. - \&quot;child_peer_review_override_dates\&quot;: each assignment override will include a peer_review_dates   field containing the matched peer review override data (id, due_at, unlock_at, lock_at)   for that override. The field will be present as null if no matching peer review override exists. | [optional] 
 **exclude** | [**List[List[str]]**](List[str].md)| Array of strings indicating what data to exclude from the response. Valid values: - \&quot;peer_review_overrides\&quot;: when include[]&#x3D;peer_review is also specified, the   peer_review_sub_assignment object will not include the overrides array, reducing the   response payload size. This is useful when using include[]&#x3D;child_peer_review_override_dates   since the peer review override data is already embedded in the parent assignment overrides. - \&quot;child_override_due_dates\&quot;: prevents the sub_assignment_due_dates field from being included   in assignment override responses, even when discussion checkpoints are enabled. This reduces   response payload size when checkpoint due date information is not needed. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**LearningObjectDates**](LearningObjectDates.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | LearningObjectDates |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **learning_object_dates_update**
> learning_object_dates_update(assignment_id, course_id, learning_object_dates_update_request=learning_object_dates_update_request)

Update a learning object's date information

Updates date-related information for learning objects, including due date, availability dates,
override status, and assignment overrides.

Returns 204 No Content response code if successful.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.learning_object_dates_update_request import LearningObjectDatesUpdateRequest
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
    api_instance = canvas_lms_python_client.LearningObjectDatesApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    course_id = 'course_id_example' # str | Scope response to course_id
    learning_object_dates_update_request = canvas_lms_python_client.LearningObjectDatesUpdateRequest() # LearningObjectDatesUpdateRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/courses/:course_id/assignments/:assignment_id/date_details \\   -X PUT \\   -H 'Authorization: Bearer <token>' \\   -H 'Content-Type: application/json' \\   -d '{         \"due_at\": \"2012-07-01T23:59:00-06:00\",         \"unlock_at\": \"2012-06-01T00:00:00-06:00\",         \"lock_at\": \"2012-08-01T00:00:00-06:00\",         \"only_visible_to_overrides\": true,         \"assignment_overrides\": [           {             \"id\": 212,             \"course_section_id\": 3564           },           {             \"title\": \"an assignment override\",             \"student_ids\": [1, 2, 3]           }         ],         \"peer_review\": {           \"due_at\": \"2012-07-05T23:59:00-06:00\",           \"unlock_at\": \"2012-07-02T23:59:00-06:00\",           \"lock_at\": \"2012-07-10T23:59:00-06:00\",           \"peer_review_overrides\": [             {               \"id\": 312,               \"course_section_id\": 3564,               \"due_at\": \"2012-07-06T23:59:00-06:00\"             }           ]         }       }' ``` (optional)

    try:
        # Update a learning object's date information
        await api_instance.learning_object_dates_update(assignment_id, course_id, learning_object_dates_update_request=learning_object_dates_update_request)
    except Exception as e:
        print("Exception when calling LearningObjectDatesApi->learning_object_dates_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **course_id** | **str**| Scope response to course_id | 
 **learning_object_dates_update_request** | [**LearningObjectDatesUpdateRequest**](LearningObjectDatesUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/courses/:course_id/assignments/:assignment_id/date_details \\   -X PUT \\   -H &#39;Authorization: Bearer &lt;token&gt;&#39; \\   -H &#39;Content-Type: application/json&#39; \\   -d &#39;{         \&quot;due_at\&quot;: \&quot;2012-07-01T23:59:00-06:00\&quot;,         \&quot;unlock_at\&quot;: \&quot;2012-06-01T00:00:00-06:00\&quot;,         \&quot;lock_at\&quot;: \&quot;2012-08-01T00:00:00-06:00\&quot;,         \&quot;only_visible_to_overrides\&quot;: true,         \&quot;assignment_overrides\&quot;: [           {             \&quot;id\&quot;: 212,             \&quot;course_section_id\&quot;: 3564           },           {             \&quot;title\&quot;: \&quot;an assignment override\&quot;,             \&quot;student_ids\&quot;: [1, 2, 3]           }         ],         \&quot;peer_review\&quot;: {           \&quot;due_at\&quot;: \&quot;2012-07-05T23:59:00-06:00\&quot;,           \&quot;unlock_at\&quot;: \&quot;2012-07-02T23:59:00-06:00\&quot;,           \&quot;lock_at\&quot;: \&quot;2012-07-10T23:59:00-06:00\&quot;,           \&quot;peer_review_overrides\&quot;: [             {               \&quot;id\&quot;: 312,               \&quot;course_section_id\&quot;: 3564,               \&quot;due_at\&quot;: \&quot;2012-07-06T23:59:00-06:00\&quot;             }           ]         }       }&#39; &#x60;&#x60;&#x60; | [optional] 

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
**0** | Update a learning object&#39;s date information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **learning_object_dates_update_by_attachment_id_for_courses**
> learning_object_dates_update_by_attachment_id_for_courses(attachment_id, course_id, learning_object_dates_update_request=learning_object_dates_update_request)

Update a learning object's date information

Updates date-related information for learning objects, including due date, availability dates,
override status, and assignment overrides.

Returns 204 No Content response code if successful.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.learning_object_dates_update_request import LearningObjectDatesUpdateRequest
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
    api_instance = canvas_lms_python_client.LearningObjectDatesApi(api_client)
    attachment_id = 'attachment_id_example' # str | Scope response to attachment_id
    course_id = 'course_id_example' # str | Scope response to course_id
    learning_object_dates_update_request = canvas_lms_python_client.LearningObjectDatesUpdateRequest() # LearningObjectDatesUpdateRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/courses/:course_id/assignments/:assignment_id/date_details \\   -X PUT \\   -H 'Authorization: Bearer <token>' \\   -H 'Content-Type: application/json' \\   -d '{         \"due_at\": \"2012-07-01T23:59:00-06:00\",         \"unlock_at\": \"2012-06-01T00:00:00-06:00\",         \"lock_at\": \"2012-08-01T00:00:00-06:00\",         \"only_visible_to_overrides\": true,         \"assignment_overrides\": [           {             \"id\": 212,             \"course_section_id\": 3564           },           {             \"title\": \"an assignment override\",             \"student_ids\": [1, 2, 3]           }         ],         \"peer_review\": {           \"due_at\": \"2012-07-05T23:59:00-06:00\",           \"unlock_at\": \"2012-07-02T23:59:00-06:00\",           \"lock_at\": \"2012-07-10T23:59:00-06:00\",           \"peer_review_overrides\": [             {               \"id\": 312,               \"course_section_id\": 3564,               \"due_at\": \"2012-07-06T23:59:00-06:00\"             }           ]         }       }' ``` (optional)

    try:
        # Update a learning object's date information
        await api_instance.learning_object_dates_update_by_attachment_id_for_courses(attachment_id, course_id, learning_object_dates_update_request=learning_object_dates_update_request)
    except Exception as e:
        print("Exception when calling LearningObjectDatesApi->learning_object_dates_update_by_attachment_id_for_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | **str**| Scope response to attachment_id | 
 **course_id** | **str**| Scope response to course_id | 
 **learning_object_dates_update_request** | [**LearningObjectDatesUpdateRequest**](LearningObjectDatesUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/courses/:course_id/assignments/:assignment_id/date_details \\   -X PUT \\   -H &#39;Authorization: Bearer &lt;token&gt;&#39; \\   -H &#39;Content-Type: application/json&#39; \\   -d &#39;{         \&quot;due_at\&quot;: \&quot;2012-07-01T23:59:00-06:00\&quot;,         \&quot;unlock_at\&quot;: \&quot;2012-06-01T00:00:00-06:00\&quot;,         \&quot;lock_at\&quot;: \&quot;2012-08-01T00:00:00-06:00\&quot;,         \&quot;only_visible_to_overrides\&quot;: true,         \&quot;assignment_overrides\&quot;: [           {             \&quot;id\&quot;: 212,             \&quot;course_section_id\&quot;: 3564           },           {             \&quot;title\&quot;: \&quot;an assignment override\&quot;,             \&quot;student_ids\&quot;: [1, 2, 3]           }         ],         \&quot;peer_review\&quot;: {           \&quot;due_at\&quot;: \&quot;2012-07-05T23:59:00-06:00\&quot;,           \&quot;unlock_at\&quot;: \&quot;2012-07-02T23:59:00-06:00\&quot;,           \&quot;lock_at\&quot;: \&quot;2012-07-10T23:59:00-06:00\&quot;,           \&quot;peer_review_overrides\&quot;: [             {               \&quot;id\&quot;: 312,               \&quot;course_section_id\&quot;: 3564,               \&quot;due_at\&quot;: \&quot;2012-07-06T23:59:00-06:00\&quot;             }           ]         }       }&#39; &#x60;&#x60;&#x60; | [optional] 

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
**0** | Update a learning object&#39;s date information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **learning_object_dates_update_by_discussion_topic_id_for_courses**
> learning_object_dates_update_by_discussion_topic_id_for_courses(course_id, discussion_topic_id, learning_object_dates_update_request=learning_object_dates_update_request)

Update a learning object's date information

Updates date-related information for learning objects, including due date, availability dates,
override status, and assignment overrides.

Returns 204 No Content response code if successful.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.learning_object_dates_update_request import LearningObjectDatesUpdateRequest
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
    api_instance = canvas_lms_python_client.LearningObjectDatesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    discussion_topic_id = 'discussion_topic_id_example' # str | Scope response to discussion_topic_id
    learning_object_dates_update_request = canvas_lms_python_client.LearningObjectDatesUpdateRequest() # LearningObjectDatesUpdateRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/courses/:course_id/assignments/:assignment_id/date_details \\   -X PUT \\   -H 'Authorization: Bearer <token>' \\   -H 'Content-Type: application/json' \\   -d '{         \"due_at\": \"2012-07-01T23:59:00-06:00\",         \"unlock_at\": \"2012-06-01T00:00:00-06:00\",         \"lock_at\": \"2012-08-01T00:00:00-06:00\",         \"only_visible_to_overrides\": true,         \"assignment_overrides\": [           {             \"id\": 212,             \"course_section_id\": 3564           },           {             \"title\": \"an assignment override\",             \"student_ids\": [1, 2, 3]           }         ],         \"peer_review\": {           \"due_at\": \"2012-07-05T23:59:00-06:00\",           \"unlock_at\": \"2012-07-02T23:59:00-06:00\",           \"lock_at\": \"2012-07-10T23:59:00-06:00\",           \"peer_review_overrides\": [             {               \"id\": 312,               \"course_section_id\": 3564,               \"due_at\": \"2012-07-06T23:59:00-06:00\"             }           ]         }       }' ``` (optional)

    try:
        # Update a learning object's date information
        await api_instance.learning_object_dates_update_by_discussion_topic_id_for_courses(course_id, discussion_topic_id, learning_object_dates_update_request=learning_object_dates_update_request)
    except Exception as e:
        print("Exception when calling LearningObjectDatesApi->learning_object_dates_update_by_discussion_topic_id_for_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **discussion_topic_id** | **str**| Scope response to discussion_topic_id | 
 **learning_object_dates_update_request** | [**LearningObjectDatesUpdateRequest**](LearningObjectDatesUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/courses/:course_id/assignments/:assignment_id/date_details \\   -X PUT \\   -H &#39;Authorization: Bearer &lt;token&gt;&#39; \\   -H &#39;Content-Type: application/json&#39; \\   -d &#39;{         \&quot;due_at\&quot;: \&quot;2012-07-01T23:59:00-06:00\&quot;,         \&quot;unlock_at\&quot;: \&quot;2012-06-01T00:00:00-06:00\&quot;,         \&quot;lock_at\&quot;: \&quot;2012-08-01T00:00:00-06:00\&quot;,         \&quot;only_visible_to_overrides\&quot;: true,         \&quot;assignment_overrides\&quot;: [           {             \&quot;id\&quot;: 212,             \&quot;course_section_id\&quot;: 3564           },           {             \&quot;title\&quot;: \&quot;an assignment override\&quot;,             \&quot;student_ids\&quot;: [1, 2, 3]           }         ],         \&quot;peer_review\&quot;: {           \&quot;due_at\&quot;: \&quot;2012-07-05T23:59:00-06:00\&quot;,           \&quot;unlock_at\&quot;: \&quot;2012-07-02T23:59:00-06:00\&quot;,           \&quot;lock_at\&quot;: \&quot;2012-07-10T23:59:00-06:00\&quot;,           \&quot;peer_review_overrides\&quot;: [             {               \&quot;id\&quot;: 312,               \&quot;course_section_id\&quot;: 3564,               \&quot;due_at\&quot;: \&quot;2012-07-06T23:59:00-06:00\&quot;             }           ]         }       }&#39; &#x60;&#x60;&#x60; | [optional] 

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
**0** | Update a learning object&#39;s date information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **learning_object_dates_update_by_url_or_id_for_courses**
> learning_object_dates_update_by_url_or_id_for_courses(course_id, url_or_id, learning_object_dates_update_request=learning_object_dates_update_request)

Update a learning object's date information

Updates date-related information for learning objects, including due date, availability dates,
override status, and assignment overrides.

Returns 204 No Content response code if successful.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.learning_object_dates_update_request import LearningObjectDatesUpdateRequest
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
    api_instance = canvas_lms_python_client.LearningObjectDatesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    url_or_id = 'url_or_id_example' # str | Scope response to url_or_id
    learning_object_dates_update_request = canvas_lms_python_client.LearningObjectDatesUpdateRequest() # LearningObjectDatesUpdateRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/courses/:course_id/assignments/:assignment_id/date_details \\   -X PUT \\   -H 'Authorization: Bearer <token>' \\   -H 'Content-Type: application/json' \\   -d '{         \"due_at\": \"2012-07-01T23:59:00-06:00\",         \"unlock_at\": \"2012-06-01T00:00:00-06:00\",         \"lock_at\": \"2012-08-01T00:00:00-06:00\",         \"only_visible_to_overrides\": true,         \"assignment_overrides\": [           {             \"id\": 212,             \"course_section_id\": 3564           },           {             \"title\": \"an assignment override\",             \"student_ids\": [1, 2, 3]           }         ],         \"peer_review\": {           \"due_at\": \"2012-07-05T23:59:00-06:00\",           \"unlock_at\": \"2012-07-02T23:59:00-06:00\",           \"lock_at\": \"2012-07-10T23:59:00-06:00\",           \"peer_review_overrides\": [             {               \"id\": 312,               \"course_section_id\": 3564,               \"due_at\": \"2012-07-06T23:59:00-06:00\"             }           ]         }       }' ``` (optional)

    try:
        # Update a learning object's date information
        await api_instance.learning_object_dates_update_by_url_or_id_for_courses(course_id, url_or_id, learning_object_dates_update_request=learning_object_dates_update_request)
    except Exception as e:
        print("Exception when calling LearningObjectDatesApi->learning_object_dates_update_by_url_or_id_for_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **url_or_id** | **str**| Scope response to url_or_id | 
 **learning_object_dates_update_request** | [**LearningObjectDatesUpdateRequest**](LearningObjectDatesUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/courses/:course_id/assignments/:assignment_id/date_details \\   -X PUT \\   -H &#39;Authorization: Bearer &lt;token&gt;&#39; \\   -H &#39;Content-Type: application/json&#39; \\   -d &#39;{         \&quot;due_at\&quot;: \&quot;2012-07-01T23:59:00-06:00\&quot;,         \&quot;unlock_at\&quot;: \&quot;2012-06-01T00:00:00-06:00\&quot;,         \&quot;lock_at\&quot;: \&quot;2012-08-01T00:00:00-06:00\&quot;,         \&quot;only_visible_to_overrides\&quot;: true,         \&quot;assignment_overrides\&quot;: [           {             \&quot;id\&quot;: 212,             \&quot;course_section_id\&quot;: 3564           },           {             \&quot;title\&quot;: \&quot;an assignment override\&quot;,             \&quot;student_ids\&quot;: [1, 2, 3]           }         ],         \&quot;peer_review\&quot;: {           \&quot;due_at\&quot;: \&quot;2012-07-05T23:59:00-06:00\&quot;,           \&quot;unlock_at\&quot;: \&quot;2012-07-02T23:59:00-06:00\&quot;,           \&quot;lock_at\&quot;: \&quot;2012-07-10T23:59:00-06:00\&quot;,           \&quot;peer_review_overrides\&quot;: [             {               \&quot;id\&quot;: 312,               \&quot;course_section_id\&quot;: 3564,               \&quot;due_at\&quot;: \&quot;2012-07-06T23:59:00-06:00\&quot;             }           ]         }       }&#39; &#x60;&#x60;&#x60; | [optional] 

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
**0** | Update a learning object&#39;s date information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **learning_object_dates_update_for_courses**
> learning_object_dates_update_for_courses(course_id, quiz_id, learning_object_dates_update_request=learning_object_dates_update_request)

Update a learning object's date information

Updates date-related information for learning objects, including due date, availability dates,
override status, and assignment overrides.

Returns 204 No Content response code if successful.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.learning_object_dates_update_request import LearningObjectDatesUpdateRequest
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
    api_instance = canvas_lms_python_client.LearningObjectDatesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    quiz_id = 'quiz_id_example' # str | Scope response to quiz_id
    learning_object_dates_update_request = canvas_lms_python_client.LearningObjectDatesUpdateRequest() # LearningObjectDatesUpdateRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/courses/:course_id/assignments/:assignment_id/date_details \\   -X PUT \\   -H 'Authorization: Bearer <token>' \\   -H 'Content-Type: application/json' \\   -d '{         \"due_at\": \"2012-07-01T23:59:00-06:00\",         \"unlock_at\": \"2012-06-01T00:00:00-06:00\",         \"lock_at\": \"2012-08-01T00:00:00-06:00\",         \"only_visible_to_overrides\": true,         \"assignment_overrides\": [           {             \"id\": 212,             \"course_section_id\": 3564           },           {             \"title\": \"an assignment override\",             \"student_ids\": [1, 2, 3]           }         ],         \"peer_review\": {           \"due_at\": \"2012-07-05T23:59:00-06:00\",           \"unlock_at\": \"2012-07-02T23:59:00-06:00\",           \"lock_at\": \"2012-07-10T23:59:00-06:00\",           \"peer_review_overrides\": [             {               \"id\": 312,               \"course_section_id\": 3564,               \"due_at\": \"2012-07-06T23:59:00-06:00\"             }           ]         }       }' ``` (optional)

    try:
        # Update a learning object's date information
        await api_instance.learning_object_dates_update_for_courses(course_id, quiz_id, learning_object_dates_update_request=learning_object_dates_update_request)
    except Exception as e:
        print("Exception when calling LearningObjectDatesApi->learning_object_dates_update_for_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **quiz_id** | **str**| Scope response to quiz_id | 
 **learning_object_dates_update_request** | [**LearningObjectDatesUpdateRequest**](LearningObjectDatesUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/courses/:course_id/assignments/:assignment_id/date_details \\   -X PUT \\   -H &#39;Authorization: Bearer &lt;token&gt;&#39; \\   -H &#39;Content-Type: application/json&#39; \\   -d &#39;{         \&quot;due_at\&quot;: \&quot;2012-07-01T23:59:00-06:00\&quot;,         \&quot;unlock_at\&quot;: \&quot;2012-06-01T00:00:00-06:00\&quot;,         \&quot;lock_at\&quot;: \&quot;2012-08-01T00:00:00-06:00\&quot;,         \&quot;only_visible_to_overrides\&quot;: true,         \&quot;assignment_overrides\&quot;: [           {             \&quot;id\&quot;: 212,             \&quot;course_section_id\&quot;: 3564           },           {             \&quot;title\&quot;: \&quot;an assignment override\&quot;,             \&quot;student_ids\&quot;: [1, 2, 3]           }         ],         \&quot;peer_review\&quot;: {           \&quot;due_at\&quot;: \&quot;2012-07-05T23:59:00-06:00\&quot;,           \&quot;unlock_at\&quot;: \&quot;2012-07-02T23:59:00-06:00\&quot;,           \&quot;lock_at\&quot;: \&quot;2012-07-10T23:59:00-06:00\&quot;,           \&quot;peer_review_overrides\&quot;: [             {               \&quot;id\&quot;: 312,               \&quot;course_section_id\&quot;: 3564,               \&quot;due_at\&quot;: \&quot;2012-07-06T23:59:00-06:00\&quot;             }           ]         }       }&#39; &#x60;&#x60;&#x60; | [optional] 

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
**0** | Update a learning object&#39;s date information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

