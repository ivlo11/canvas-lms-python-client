# canvas_lms_python_client.DiscussionEntriesApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**discussion_entries_destroy**](DiscussionEntriesApi.md#discussion_entries_destroy) | **DELETE** /api/v1/courses/{course_id}/discussion_topics/{topic_id}/entries/{id} | Delete an entry
[**discussion_entries_destroy_for_groups**](DiscussionEntriesApi.md#discussion_entries_destroy_for_groups) | **DELETE** /api/v1/groups/{group_id}/discussion_topics/{topic_id}/entries/{id} | Delete an entry
[**discussion_entries_update**](DiscussionEntriesApi.md#discussion_entries_update) | **PUT** /api/v1/courses/{course_id}/discussion_topics/{topic_id}/entries/{id} | Update an entry
[**discussion_entries_update_for_groups**](DiscussionEntriesApi.md#discussion_entries_update_for_groups) | **PUT** /api/v1/groups/{group_id}/discussion_topics/{topic_id}/entries/{id} | Update an entry


# **discussion_entries_destroy**
> discussion_entries_destroy(course_id, id, topic_id)

Delete an entry

Delete a discussion entry.

The entry must have been created by the current user, or the current user
must have admin rights to the discussion. If the delete is not allowed, a 401 will be returned.

The discussion will be marked deleted, and the user_id and message will be cleared out.

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
    api_instance = canvas_lms_python_client.DiscussionEntriesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    topic_id = 'topic_id_example' # str | Scope response to topic_id

    try:
        # Delete an entry
        await api_instance.discussion_entries_destroy(course_id, id, topic_id)
    except Exception as e:
        print("Exception when calling DiscussionEntriesApi->discussion_entries_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **topic_id** | **str**| Scope response to topic_id | 

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
**0** | Delete an entry |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discussion_entries_destroy_for_groups**
> discussion_entries_destroy_for_groups(group_id, id, topic_id)

Delete an entry

Delete a discussion entry.

The entry must have been created by the current user, or the current user
must have admin rights to the discussion. If the delete is not allowed, a 401 will be returned.

The discussion will be marked deleted, and the user_id and message will be cleared out.

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
    api_instance = canvas_lms_python_client.DiscussionEntriesApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    id = 'id_example' # str | Scope response to id
    topic_id = 'topic_id_example' # str | Scope response to topic_id

    try:
        # Delete an entry
        await api_instance.discussion_entries_destroy_for_groups(group_id, id, topic_id)
    except Exception as e:
        print("Exception when calling DiscussionEntriesApi->discussion_entries_destroy_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **id** | **str**| Scope response to id | 
 **topic_id** | **str**| Scope response to topic_id | 

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
**0** | Delete an entry |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discussion_entries_update**
> discussion_entries_update(course_id, id, topic_id, discussion_entries_update_request=discussion_entries_update_request)

Update an entry

Update an existing discussion entry.

The entry must have been created by the current user, or the current user
must have admin rights to the discussion. If the edit is not allowed, a 401 will be returned.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.discussion_entries_update_request import DiscussionEntriesUpdateRequest
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
    api_instance = canvas_lms_python_client.DiscussionEntriesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    topic_id = 'topic_id_example' # str | Scope response to topic_id
    discussion_entries_update_request = canvas_lms_python_client.DiscussionEntriesUpdateRequest() # DiscussionEntriesUpdateRequest | Request body parameters  **Example Request:** ``` curl -X PUT 'https://<canvas>/api/v1/courses/<course_id>/discussion_topics/<topic_id>/entries/<entry_id>' \\      -F 'message=<message>' \\      -H \"Authorization: Bearer <token>\" ``` (optional)

    try:
        # Update an entry
        await api_instance.discussion_entries_update(course_id, id, topic_id, discussion_entries_update_request=discussion_entries_update_request)
    except Exception as e:
        print("Exception when calling DiscussionEntriesApi->discussion_entries_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **topic_id** | **str**| Scope response to topic_id | 
 **discussion_entries_update_request** | [**DiscussionEntriesUpdateRequest**](DiscussionEntriesUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl -X PUT &#39;https://&lt;canvas&gt;/api/v1/courses/&lt;course_id&gt;/discussion_topics/&lt;topic_id&gt;/entries/&lt;entry_id&gt;&#39; \\      -F &#39;message&#x3D;&lt;message&gt;&#39; \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; &#x60;&#x60;&#x60; | [optional] 

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
**0** | Update an entry |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discussion_entries_update_for_groups**
> discussion_entries_update_for_groups(group_id, id, topic_id, discussion_entries_update_request=discussion_entries_update_request)

Update an entry

Update an existing discussion entry.

The entry must have been created by the current user, or the current user
must have admin rights to the discussion. If the edit is not allowed, a 401 will be returned.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.discussion_entries_update_request import DiscussionEntriesUpdateRequest
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
    api_instance = canvas_lms_python_client.DiscussionEntriesApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    id = 'id_example' # str | Scope response to id
    topic_id = 'topic_id_example' # str | Scope response to topic_id
    discussion_entries_update_request = canvas_lms_python_client.DiscussionEntriesUpdateRequest() # DiscussionEntriesUpdateRequest | Request body parameters  **Example Request:** ``` curl -X PUT 'https://<canvas>/api/v1/courses/<course_id>/discussion_topics/<topic_id>/entries/<entry_id>' \\      -F 'message=<message>' \\      -H \"Authorization: Bearer <token>\" ``` (optional)

    try:
        # Update an entry
        await api_instance.discussion_entries_update_for_groups(group_id, id, topic_id, discussion_entries_update_request=discussion_entries_update_request)
    except Exception as e:
        print("Exception when calling DiscussionEntriesApi->discussion_entries_update_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **id** | **str**| Scope response to id | 
 **topic_id** | **str**| Scope response to topic_id | 
 **discussion_entries_update_request** | [**DiscussionEntriesUpdateRequest**](DiscussionEntriesUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl -X PUT &#39;https://&lt;canvas&gt;/api/v1/courses/&lt;course_id&gt;/discussion_topics/&lt;topic_id&gt;/entries/&lt;entry_id&gt;&#39; \\      -F &#39;message&#x3D;&lt;message&gt;&#39; \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; &#x60;&#x60;&#x60; | [optional] 

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
**0** | Update an entry |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

