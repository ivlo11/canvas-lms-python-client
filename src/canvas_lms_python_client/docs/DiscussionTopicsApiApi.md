# canvas_lms_python_client.DiscussionTopicsApiApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**discussion_topics_api_add_entry**](DiscussionTopicsApiApi.md#discussion_topics_api_add_entry) | **POST** /api/v1/courses/{course_id}/discussion_topics/{topic_id}/entries | Post an entry
[**discussion_topics_api_add_entry_for_groups**](DiscussionTopicsApiApi.md#discussion_topics_api_add_entry_for_groups) | **POST** /api/v1/groups/{group_id}/discussion_topics/{topic_id}/entries | Post an entry
[**discussion_topics_api_add_reply**](DiscussionTopicsApiApi.md#discussion_topics_api_add_reply) | **POST** /api/v1/courses/{course_id}/discussion_topics/{topic_id}/entries/{entry_id}/replies | Post a reply
[**discussion_topics_api_add_reply_for_groups**](DiscussionTopicsApiApi.md#discussion_topics_api_add_reply_for_groups) | **POST** /api/v1/groups/{group_id}/discussion_topics/{topic_id}/entries/{entry_id}/replies | Post a reply
[**discussion_topics_api_disable_summary**](DiscussionTopicsApiApi.md#discussion_topics_api_disable_summary) | **PUT** /api/v1/courses/{course_id}/discussion_topics/{topic_id}/summaries/disable | Disable summary
[**discussion_topics_api_disable_summary_for_groups**](DiscussionTopicsApiApi.md#discussion_topics_api_disable_summary_for_groups) | **PUT** /api/v1/groups/{group_id}/discussion_topics/{topic_id}/summaries/disable | Disable summary
[**discussion_topics_api_duplicate**](DiscussionTopicsApiApi.md#discussion_topics_api_duplicate) | **POST** /api/v1/courses/{course_id}/discussion_topics/{topic_id}/duplicate | Duplicate discussion topic
[**discussion_topics_api_duplicate_for_groups**](DiscussionTopicsApiApi.md#discussion_topics_api_duplicate_for_groups) | **POST** /api/v1/groups/{group_id}/discussion_topics/{topic_id}/duplicate | Duplicate discussion topic
[**discussion_topics_api_entries**](DiscussionTopicsApiApi.md#discussion_topics_api_entries) | **GET** /api/v1/courses/{course_id}/discussion_topics/{topic_id}/entries | List topic entries
[**discussion_topics_api_entries_for_groups**](DiscussionTopicsApiApi.md#discussion_topics_api_entries_for_groups) | **GET** /api/v1/groups/{group_id}/discussion_topics/{topic_id}/entries | List topic entries
[**discussion_topics_api_entry_list**](DiscussionTopicsApiApi.md#discussion_topics_api_entry_list) | **GET** /api/v1/courses/{course_id}/discussion_topics/{topic_id}/entry_list | List entries
[**discussion_topics_api_entry_list_for_groups**](DiscussionTopicsApiApi.md#discussion_topics_api_entry_list_for_groups) | **GET** /api/v1/groups/{group_id}/discussion_topics/{topic_id}/entry_list | List entries
[**discussion_topics_api_find_or_create_summary**](DiscussionTopicsApiApi.md#discussion_topics_api_find_or_create_summary) | **POST** /api/v1/courses/{course_id}/discussion_topics/{topic_id}/summaries | Find or Create Summary
[**discussion_topics_api_find_or_create_summary_for_groups**](DiscussionTopicsApiApi.md#discussion_topics_api_find_or_create_summary_for_groups) | **POST** /api/v1/groups/{group_id}/discussion_topics/{topic_id}/summaries | Find or Create Summary
[**discussion_topics_api_find_summary**](DiscussionTopicsApiApi.md#discussion_topics_api_find_summary) | **GET** /api/v1/courses/{course_id}/discussion_topics/{topic_id}/summaries | Find Last Summary
[**discussion_topics_api_find_summary_for_groups**](DiscussionTopicsApiApi.md#discussion_topics_api_find_summary_for_groups) | **GET** /api/v1/groups/{group_id}/discussion_topics/{topic_id}/summaries | Find Last Summary
[**discussion_topics_api_mark_all_read**](DiscussionTopicsApiApi.md#discussion_topics_api_mark_all_read) | **PUT** /api/v1/courses/{course_id}/discussion_topics/{topic_id}/read_all | Mark all entries as read
[**discussion_topics_api_mark_all_read_for_groups**](DiscussionTopicsApiApi.md#discussion_topics_api_mark_all_read_for_groups) | **PUT** /api/v1/groups/{group_id}/discussion_topics/{topic_id}/read_all | Mark all entries as read
[**discussion_topics_api_mark_all_topic_read**](DiscussionTopicsApiApi.md#discussion_topics_api_mark_all_topic_read) | **PUT** /api/v1/courses/{course_id}/discussion_topics/read_all | Mark all topic as read
[**discussion_topics_api_mark_all_topic_read_for_groups**](DiscussionTopicsApiApi.md#discussion_topics_api_mark_all_topic_read_for_groups) | **PUT** /api/v1/groups/{group_id}/discussion_topics/read_all | Mark all topic as read
[**discussion_topics_api_mark_all_unread**](DiscussionTopicsApiApi.md#discussion_topics_api_mark_all_unread) | **DELETE** /api/v1/courses/{course_id}/discussion_topics/{topic_id}/read_all | Mark all entries as unread
[**discussion_topics_api_mark_all_unread_for_groups**](DiscussionTopicsApiApi.md#discussion_topics_api_mark_all_unread_for_groups) | **DELETE** /api/v1/groups/{group_id}/discussion_topics/{topic_id}/read_all | Mark all entries as unread
[**discussion_topics_api_mark_entry_read**](DiscussionTopicsApiApi.md#discussion_topics_api_mark_entry_read) | **PUT** /api/v1/courses/{course_id}/discussion_topics/{topic_id}/entries/{entry_id}/read | Mark entry as read
[**discussion_topics_api_mark_entry_read_for_groups**](DiscussionTopicsApiApi.md#discussion_topics_api_mark_entry_read_for_groups) | **PUT** /api/v1/groups/{group_id}/discussion_topics/{topic_id}/entries/{entry_id}/read | Mark entry as read
[**discussion_topics_api_mark_entry_unread**](DiscussionTopicsApiApi.md#discussion_topics_api_mark_entry_unread) | **DELETE** /api/v1/courses/{course_id}/discussion_topics/{topic_id}/entries/{entry_id}/read | Mark entry as unread
[**discussion_topics_api_mark_entry_unread_for_groups**](DiscussionTopicsApiApi.md#discussion_topics_api_mark_entry_unread_for_groups) | **DELETE** /api/v1/groups/{group_id}/discussion_topics/{topic_id}/entries/{entry_id}/read | Mark entry as unread
[**discussion_topics_api_mark_topic_read**](DiscussionTopicsApiApi.md#discussion_topics_api_mark_topic_read) | **PUT** /api/v1/courses/{course_id}/discussion_topics/{topic_id}/read | Mark topic as read
[**discussion_topics_api_mark_topic_read_for_groups**](DiscussionTopicsApiApi.md#discussion_topics_api_mark_topic_read_for_groups) | **PUT** /api/v1/groups/{group_id}/discussion_topics/{topic_id}/read | Mark topic as read
[**discussion_topics_api_mark_topic_unread**](DiscussionTopicsApiApi.md#discussion_topics_api_mark_topic_unread) | **DELETE** /api/v1/courses/{course_id}/discussion_topics/{topic_id}/read | Mark topic as unread
[**discussion_topics_api_mark_topic_unread_for_groups**](DiscussionTopicsApiApi.md#discussion_topics_api_mark_topic_unread_for_groups) | **DELETE** /api/v1/groups/{group_id}/discussion_topics/{topic_id}/read | Mark topic as unread
[**discussion_topics_api_rate_entry**](DiscussionTopicsApiApi.md#discussion_topics_api_rate_entry) | **POST** /api/v1/courses/{course_id}/discussion_topics/{topic_id}/entries/{entry_id}/rating | Rate entry
[**discussion_topics_api_rate_entry_for_groups**](DiscussionTopicsApiApi.md#discussion_topics_api_rate_entry_for_groups) | **POST** /api/v1/groups/{group_id}/discussion_topics/{topic_id}/entries/{entry_id}/rating | Rate entry
[**discussion_topics_api_replies**](DiscussionTopicsApiApi.md#discussion_topics_api_replies) | **GET** /api/v1/courses/{course_id}/discussion_topics/{topic_id}/entries/{entry_id}/replies | List entry replies
[**discussion_topics_api_replies_for_groups**](DiscussionTopicsApiApi.md#discussion_topics_api_replies_for_groups) | **GET** /api/v1/groups/{group_id}/discussion_topics/{topic_id}/entries/{entry_id}/replies | List entry replies
[**discussion_topics_api_show**](DiscussionTopicsApiApi.md#discussion_topics_api_show) | **GET** /api/v1/courses/{course_id}/discussion_topics/{topic_id} | Get a single topic
[**discussion_topics_api_show_for_groups**](DiscussionTopicsApiApi.md#discussion_topics_api_show_for_groups) | **GET** /api/v1/groups/{group_id}/discussion_topics/{topic_id} | Get a single topic
[**discussion_topics_api_subscribe_topic**](DiscussionTopicsApiApi.md#discussion_topics_api_subscribe_topic) | **PUT** /api/v1/courses/{course_id}/discussion_topics/{topic_id}/subscribed | Subscribe to a topic
[**discussion_topics_api_subscribe_topic_for_groups**](DiscussionTopicsApiApi.md#discussion_topics_api_subscribe_topic_for_groups) | **PUT** /api/v1/groups/{group_id}/discussion_topics/{topic_id}/subscribed | Subscribe to a topic
[**discussion_topics_api_summary_feedback**](DiscussionTopicsApiApi.md#discussion_topics_api_summary_feedback) | **POST** /api/v1/courses/{course_id}/discussion_topics/{topic_id}/summaries/{summary_id}/feedback | Summary Feedback
[**discussion_topics_api_summary_feedback_for_groups**](DiscussionTopicsApiApi.md#discussion_topics_api_summary_feedback_for_groups) | **POST** /api/v1/groups/{group_id}/discussion_topics/{topic_id}/summaries/{summary_id}/feedback | Summary Feedback
[**discussion_topics_api_unsubscribe_topic**](DiscussionTopicsApiApi.md#discussion_topics_api_unsubscribe_topic) | **DELETE** /api/v1/courses/{course_id}/discussion_topics/{topic_id}/subscribed | Unsubscribe from a topic
[**discussion_topics_api_unsubscribe_topic_for_groups**](DiscussionTopicsApiApi.md#discussion_topics_api_unsubscribe_topic_for_groups) | **DELETE** /api/v1/groups/{group_id}/discussion_topics/{topic_id}/subscribed | Unsubscribe from a topic
[**discussion_topics_api_view**](DiscussionTopicsApiApi.md#discussion_topics_api_view) | **GET** /api/v1/courses/{course_id}/discussion_topics/{topic_id}/view | Get the full topic
[**discussion_topics_api_view_for_groups**](DiscussionTopicsApiApi.md#discussion_topics_api_view_for_groups) | **GET** /api/v1/groups/{group_id}/discussion_topics/{topic_id}/view | Get the full topic


# **discussion_topics_api_add_entry**
> DiscussionEntry discussion_topics_api_add_entry(course_id, topic_id, discussion_topics_api_add_entry_request=discussion_topics_api_add_entry_request)

Post an entry

Create a new entry in a discussion topic. Returns a json representation of
the created entry (see documentation for 'entries' method) on success.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.discussion_entry import DiscussionEntry
from canvas_lms_python_client.models.discussion_topics_api_add_entry_request import DiscussionTopicsApiAddEntryRequest
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
    api_instance = canvas_lms_python_client.DiscussionTopicsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    topic_id = 'topic_id_example' # str | Scope response to topic_id
    discussion_topics_api_add_entry_request = canvas_lms_python_client.DiscussionTopicsApiAddEntryRequest() # DiscussionTopicsApiAddEntryRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/courses/<course_id>/discussion_topics/<topic_id>/entries.json' \\      -F 'message=<message>' \\      -F 'attachment=@<filename>' \\      -H \"Authorization: Bearer <token>\" ``` (optional)

    try:
        # Post an entry
        api_response = await api_instance.discussion_topics_api_add_entry(course_id, topic_id, discussion_topics_api_add_entry_request=discussion_topics_api_add_entry_request)
        print("The response of DiscussionTopicsApiApi->discussion_topics_api_add_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscussionTopicsApiApi->discussion_topics_api_add_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **topic_id** | **str**| Scope response to topic_id | 
 **discussion_topics_api_add_entry_request** | [**DiscussionTopicsApiAddEntryRequest**](DiscussionTopicsApiAddEntryRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/courses/&lt;course_id&gt;/discussion_topics/&lt;topic_id&gt;/entries.json&#39; \\      -F &#39;message&#x3D;&lt;message&gt;&#39; \\      -F &#39;attachment&#x3D;@&lt;filename&gt;&#39; \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**DiscussionEntry**](DiscussionEntry.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | DiscussionEntry |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discussion_topics_api_add_entry_for_groups**
> DiscussionEntry discussion_topics_api_add_entry_for_groups(group_id, topic_id, discussion_topics_api_add_entry_request=discussion_topics_api_add_entry_request)

Post an entry

Create a new entry in a discussion topic. Returns a json representation of
the created entry (see documentation for 'entries' method) on success.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.discussion_entry import DiscussionEntry
from canvas_lms_python_client.models.discussion_topics_api_add_entry_request import DiscussionTopicsApiAddEntryRequest
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
    api_instance = canvas_lms_python_client.DiscussionTopicsApiApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    topic_id = 'topic_id_example' # str | Scope response to topic_id
    discussion_topics_api_add_entry_request = canvas_lms_python_client.DiscussionTopicsApiAddEntryRequest() # DiscussionTopicsApiAddEntryRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/courses/<course_id>/discussion_topics/<topic_id>/entries.json' \\      -F 'message=<message>' \\      -F 'attachment=@<filename>' \\      -H \"Authorization: Bearer <token>\" ``` (optional)

    try:
        # Post an entry
        api_response = await api_instance.discussion_topics_api_add_entry_for_groups(group_id, topic_id, discussion_topics_api_add_entry_request=discussion_topics_api_add_entry_request)
        print("The response of DiscussionTopicsApiApi->discussion_topics_api_add_entry_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscussionTopicsApiApi->discussion_topics_api_add_entry_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **topic_id** | **str**| Scope response to topic_id | 
 **discussion_topics_api_add_entry_request** | [**DiscussionTopicsApiAddEntryRequest**](DiscussionTopicsApiAddEntryRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/courses/&lt;course_id&gt;/discussion_topics/&lt;topic_id&gt;/entries.json&#39; \\      -F &#39;message&#x3D;&lt;message&gt;&#39; \\      -F &#39;attachment&#x3D;@&lt;filename&gt;&#39; \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**DiscussionEntry**](DiscussionEntry.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | DiscussionEntry |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discussion_topics_api_add_reply**
> DiscussionEntry discussion_topics_api_add_reply(course_id, entry_id, topic_id, discussion_topics_api_add_entry_request=discussion_topics_api_add_entry_request)

Post a reply

Add a reply to an entry in a discussion topic. Returns a json
representation of the created reply (see documentation for 'replies'
method) on success.

May require (depending on the topic) that the user has posted in the topic.
If it is required, and the user has not posted, will respond with a 403
Forbidden status and the body 'require_initial_post'.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.discussion_entry import DiscussionEntry
from canvas_lms_python_client.models.discussion_topics_api_add_entry_request import DiscussionTopicsApiAddEntryRequest
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
    api_instance = canvas_lms_python_client.DiscussionTopicsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    entry_id = 'entry_id_example' # str | Scope response to entry_id
    topic_id = 'topic_id_example' # str | Scope response to topic_id
    discussion_topics_api_add_entry_request = canvas_lms_python_client.DiscussionTopicsApiAddEntryRequest() # DiscussionTopicsApiAddEntryRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/courses/<course_id>/discussion_topics/<topic_id>/entries/<entry_id>/replies.json' \\      -F 'message=<message>' \\      -F 'attachment=@<filename>' \\      -H \"Authorization: Bearer <token>\" ``` (optional)

    try:
        # Post a reply
        api_response = await api_instance.discussion_topics_api_add_reply(course_id, entry_id, topic_id, discussion_topics_api_add_entry_request=discussion_topics_api_add_entry_request)
        print("The response of DiscussionTopicsApiApi->discussion_topics_api_add_reply:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscussionTopicsApiApi->discussion_topics_api_add_reply: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **entry_id** | **str**| Scope response to entry_id | 
 **topic_id** | **str**| Scope response to topic_id | 
 **discussion_topics_api_add_entry_request** | [**DiscussionTopicsApiAddEntryRequest**](DiscussionTopicsApiAddEntryRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/courses/&lt;course_id&gt;/discussion_topics/&lt;topic_id&gt;/entries/&lt;entry_id&gt;/replies.json&#39; \\      -F &#39;message&#x3D;&lt;message&gt;&#39; \\      -F &#39;attachment&#x3D;@&lt;filename&gt;&#39; \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**DiscussionEntry**](DiscussionEntry.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | DiscussionEntry |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discussion_topics_api_add_reply_for_groups**
> DiscussionEntry discussion_topics_api_add_reply_for_groups(entry_id, group_id, topic_id, discussion_topics_api_add_entry_request=discussion_topics_api_add_entry_request)

Post a reply

Add a reply to an entry in a discussion topic. Returns a json
representation of the created reply (see documentation for 'replies'
method) on success.

May require (depending on the topic) that the user has posted in the topic.
If it is required, and the user has not posted, will respond with a 403
Forbidden status and the body 'require_initial_post'.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.discussion_entry import DiscussionEntry
from canvas_lms_python_client.models.discussion_topics_api_add_entry_request import DiscussionTopicsApiAddEntryRequest
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
    api_instance = canvas_lms_python_client.DiscussionTopicsApiApi(api_client)
    entry_id = 'entry_id_example' # str | Scope response to entry_id
    group_id = 'group_id_example' # str | Scope response to group_id
    topic_id = 'topic_id_example' # str | Scope response to topic_id
    discussion_topics_api_add_entry_request = canvas_lms_python_client.DiscussionTopicsApiAddEntryRequest() # DiscussionTopicsApiAddEntryRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/courses/<course_id>/discussion_topics/<topic_id>/entries/<entry_id>/replies.json' \\      -F 'message=<message>' \\      -F 'attachment=@<filename>' \\      -H \"Authorization: Bearer <token>\" ``` (optional)

    try:
        # Post a reply
        api_response = await api_instance.discussion_topics_api_add_reply_for_groups(entry_id, group_id, topic_id, discussion_topics_api_add_entry_request=discussion_topics_api_add_entry_request)
        print("The response of DiscussionTopicsApiApi->discussion_topics_api_add_reply_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscussionTopicsApiApi->discussion_topics_api_add_reply_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entry_id** | **str**| Scope response to entry_id | 
 **group_id** | **str**| Scope response to group_id | 
 **topic_id** | **str**| Scope response to topic_id | 
 **discussion_topics_api_add_entry_request** | [**DiscussionTopicsApiAddEntryRequest**](DiscussionTopicsApiAddEntryRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/courses/&lt;course_id&gt;/discussion_topics/&lt;topic_id&gt;/entries/&lt;entry_id&gt;/replies.json&#39; \\      -F &#39;message&#x3D;&lt;message&gt;&#39; \\      -F &#39;attachment&#x3D;@&lt;filename&gt;&#39; \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**DiscussionEntry**](DiscussionEntry.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | DiscussionEntry |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discussion_topics_api_disable_summary**
> DiscussionTopicsDisableSummaryResponse discussion_topics_api_disable_summary(course_id, topic_id)

Disable summary

Deprecated, to remove after VICE-5047 gets merged
Disables the summary for a discussion topic.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.discussion_topics_disable_summary_response import DiscussionTopicsDisableSummaryResponse
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
    api_instance = canvas_lms_python_client.DiscussionTopicsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    topic_id = 'topic_id_example' # str | Scope response to topic_id

    try:
        # Disable summary
        api_response = await api_instance.discussion_topics_api_disable_summary(course_id, topic_id)
        print("The response of DiscussionTopicsApiApi->discussion_topics_api_disable_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscussionTopicsApiApi->discussion_topics_api_disable_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **topic_id** | **str**| Scope response to topic_id | 

### Return type

[**DiscussionTopicsDisableSummaryResponse**](DiscussionTopicsDisableSummaryResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | DiscussionTopicsDisableSummaryResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discussion_topics_api_disable_summary_for_groups**
> DiscussionTopicsDisableSummaryResponse discussion_topics_api_disable_summary_for_groups(group_id, topic_id)

Disable summary

Deprecated, to remove after VICE-5047 gets merged
Disables the summary for a discussion topic.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.discussion_topics_disable_summary_response import DiscussionTopicsDisableSummaryResponse
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
    api_instance = canvas_lms_python_client.DiscussionTopicsApiApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    topic_id = 'topic_id_example' # str | Scope response to topic_id

    try:
        # Disable summary
        api_response = await api_instance.discussion_topics_api_disable_summary_for_groups(group_id, topic_id)
        print("The response of DiscussionTopicsApiApi->discussion_topics_api_disable_summary_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscussionTopicsApiApi->discussion_topics_api_disable_summary_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **topic_id** | **str**| Scope response to topic_id | 

### Return type

[**DiscussionTopicsDisableSummaryResponse**](DiscussionTopicsDisableSummaryResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | DiscussionTopicsDisableSummaryResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discussion_topics_api_duplicate**
> DiscussionTopic discussion_topics_api_duplicate(course_id, topic_id)

Duplicate discussion topic

Duplicate a discussion topic according to context (Course/Group)

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.discussion_topic import DiscussionTopic
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
    api_instance = canvas_lms_python_client.DiscussionTopicsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    topic_id = 'topic_id_example' # str | Scope response to topic_id

    try:
        # Duplicate discussion topic
        api_response = await api_instance.discussion_topics_api_duplicate(course_id, topic_id)
        print("The response of DiscussionTopicsApiApi->discussion_topics_api_duplicate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscussionTopicsApiApi->discussion_topics_api_duplicate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **topic_id** | **str**| Scope response to topic_id | 

### Return type

[**DiscussionTopic**](DiscussionTopic.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | DiscussionTopic |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discussion_topics_api_duplicate_for_groups**
> DiscussionTopic discussion_topics_api_duplicate_for_groups(group_id, topic_id)

Duplicate discussion topic

Duplicate a discussion topic according to context (Course/Group)

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.discussion_topic import DiscussionTopic
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
    api_instance = canvas_lms_python_client.DiscussionTopicsApiApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    topic_id = 'topic_id_example' # str | Scope response to topic_id

    try:
        # Duplicate discussion topic
        api_response = await api_instance.discussion_topics_api_duplicate_for_groups(group_id, topic_id)
        print("The response of DiscussionTopicsApiApi->discussion_topics_api_duplicate_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscussionTopicsApiApi->discussion_topics_api_duplicate_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **topic_id** | **str**| Scope response to topic_id | 

### Return type

[**DiscussionTopic**](DiscussionTopic.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | DiscussionTopic |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discussion_topics_api_entries**
> List[DiscussionEntry] discussion_topics_api_entries(course_id, topic_id, page=page, per_page=per_page)

List topic entries

Retrieve the (paginated) top-level entries in a discussion topic.

May require (depending on the topic) that the user has posted in the topic.
If it is required, and the user has not posted, will respond with a 403
Forbidden status and the body 'require_initial_post'.

Will include the 10 most recent replies, if any, for each entry returned.

If the topic is a root topic with children corresponding to groups of a
group assignment, entries from those subtopics for which the user belongs
to the corresponding group will be returned.

Ordering of returned entries is newest-first by posting timestamp (reply
activity is ignored).

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.discussion_entry import DiscussionEntry
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
    api_instance = canvas_lms_python_client.DiscussionTopicsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    topic_id = 'topic_id_example' # str | Scope response to topic_id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List topic entries
        api_response = await api_instance.discussion_topics_api_entries(course_id, topic_id, page=page, per_page=per_page)
        print("The response of DiscussionTopicsApiApi->discussion_topics_api_entries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscussionTopicsApiApi->discussion_topics_api_entries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **topic_id** | **str**| Scope response to topic_id | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[DiscussionEntry]**](DiscussionEntry.md)

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

# **discussion_topics_api_entries_for_groups**
> List[DiscussionEntry] discussion_topics_api_entries_for_groups(group_id, topic_id, page=page, per_page=per_page)

List topic entries

Retrieve the (paginated) top-level entries in a discussion topic.

May require (depending on the topic) that the user has posted in the topic.
If it is required, and the user has not posted, will respond with a 403
Forbidden status and the body 'require_initial_post'.

Will include the 10 most recent replies, if any, for each entry returned.

If the topic is a root topic with children corresponding to groups of a
group assignment, entries from those subtopics for which the user belongs
to the corresponding group will be returned.

Ordering of returned entries is newest-first by posting timestamp (reply
activity is ignored).

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.discussion_entry import DiscussionEntry
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
    api_instance = canvas_lms_python_client.DiscussionTopicsApiApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    topic_id = 'topic_id_example' # str | Scope response to topic_id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List topic entries
        api_response = await api_instance.discussion_topics_api_entries_for_groups(group_id, topic_id, page=page, per_page=per_page)
        print("The response of DiscussionTopicsApiApi->discussion_topics_api_entries_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscussionTopicsApiApi->discussion_topics_api_entries_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **topic_id** | **str**| Scope response to topic_id | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[DiscussionEntry]**](DiscussionEntry.md)

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

# **discussion_topics_api_entry_list**
> List[DiscussionEntry] discussion_topics_api_entry_list(course_id, topic_id, ids=ids, page=page, per_page=per_page)

List entries

Retrieve a paginated list of discussion entries, given a list of ids.

May require (depending on the topic) that the user has posted in the topic.
If it is required, and the user has not posted, will respond with a 403
Forbidden status and the body 'require_initial_post'.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.discussion_entry import DiscussionEntry
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
    api_instance = canvas_lms_python_client.DiscussionTopicsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    topic_id = 'topic_id_example' # str | Scope response to topic_id
    ids = ['ids_example'] # List[str] | A list of entry ids to retrieve. Entries will be returned in id order, smallest id first. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List entries
        api_response = await api_instance.discussion_topics_api_entry_list(course_id, topic_id, ids=ids, page=page, per_page=per_page)
        print("The response of DiscussionTopicsApiApi->discussion_topics_api_entry_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscussionTopicsApiApi->discussion_topics_api_entry_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **topic_id** | **str**| Scope response to topic_id | 
 **ids** | [**List[str]**](str.md)| A list of entry ids to retrieve. Entries will be returned in id order, smallest id first. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[DiscussionEntry]**](DiscussionEntry.md)

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

# **discussion_topics_api_entry_list_for_groups**
> List[DiscussionEntry] discussion_topics_api_entry_list_for_groups(group_id, topic_id, ids=ids, page=page, per_page=per_page)

List entries

Retrieve a paginated list of discussion entries, given a list of ids.

May require (depending on the topic) that the user has posted in the topic.
If it is required, and the user has not posted, will respond with a 403
Forbidden status and the body 'require_initial_post'.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.discussion_entry import DiscussionEntry
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
    api_instance = canvas_lms_python_client.DiscussionTopicsApiApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    topic_id = 'topic_id_example' # str | Scope response to topic_id
    ids = ['ids_example'] # List[str] | A list of entry ids to retrieve. Entries will be returned in id order, smallest id first. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List entries
        api_response = await api_instance.discussion_topics_api_entry_list_for_groups(group_id, topic_id, ids=ids, page=page, per_page=per_page)
        print("The response of DiscussionTopicsApiApi->discussion_topics_api_entry_list_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscussionTopicsApiApi->discussion_topics_api_entry_list_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **topic_id** | **str**| Scope response to topic_id | 
 **ids** | [**List[str]**](str.md)| A list of entry ids to retrieve. Entries will be returned in id order, smallest id first. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[DiscussionEntry]**](DiscussionEntry.md)

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

# **discussion_topics_api_find_or_create_summary**
> DiscussionTopicsFindOrCreateSummaryResponse discussion_topics_api_find_or_create_summary(course_id, topic_id, discussion_topics_api_find_or_create_summary_request=discussion_topics_api_find_or_create_summary_request)

Find or Create Summary

Generates a summary for a discussion topic. Returns the summary text and usage information.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.discussion_topics_api_find_or_create_summary_request import DiscussionTopicsApiFindOrCreateSummaryRequest
from canvas_lms_python_client.models.discussion_topics_find_or_create_summary_response import DiscussionTopicsFindOrCreateSummaryResponse
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
    api_instance = canvas_lms_python_client.DiscussionTopicsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    topic_id = 'topic_id_example' # str | Scope response to topic_id
    discussion_topics_api_find_or_create_summary_request = canvas_lms_python_client.DiscussionTopicsApiFindOrCreateSummaryRequest() # DiscussionTopicsApiFindOrCreateSummaryRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/courses/<course_id>/discussion_topics/<topic_id>/summaries \\     -X POST \\     -H 'Authorization: Bearer <token>' ``` (optional)

    try:
        # Find or Create Summary
        api_response = await api_instance.discussion_topics_api_find_or_create_summary(course_id, topic_id, discussion_topics_api_find_or_create_summary_request=discussion_topics_api_find_or_create_summary_request)
        print("The response of DiscussionTopicsApiApi->discussion_topics_api_find_or_create_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscussionTopicsApiApi->discussion_topics_api_find_or_create_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **topic_id** | **str**| Scope response to topic_id | 
 **discussion_topics_api_find_or_create_summary_request** | [**DiscussionTopicsApiFindOrCreateSummaryRequest**](DiscussionTopicsApiFindOrCreateSummaryRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/courses/&lt;course_id&gt;/discussion_topics/&lt;topic_id&gt;/summaries \\     -X POST \\     -H &#39;Authorization: Bearer &lt;token&gt;&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**DiscussionTopicsFindOrCreateSummaryResponse**](DiscussionTopicsFindOrCreateSummaryResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | DiscussionTopicsFindOrCreateSummaryResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discussion_topics_api_find_or_create_summary_for_groups**
> DiscussionTopicsFindOrCreateSummaryResponse discussion_topics_api_find_or_create_summary_for_groups(group_id, topic_id, discussion_topics_api_find_or_create_summary_request=discussion_topics_api_find_or_create_summary_request)

Find or Create Summary

Generates a summary for a discussion topic. Returns the summary text and usage information.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.discussion_topics_api_find_or_create_summary_request import DiscussionTopicsApiFindOrCreateSummaryRequest
from canvas_lms_python_client.models.discussion_topics_find_or_create_summary_response import DiscussionTopicsFindOrCreateSummaryResponse
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
    api_instance = canvas_lms_python_client.DiscussionTopicsApiApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    topic_id = 'topic_id_example' # str | Scope response to topic_id
    discussion_topics_api_find_or_create_summary_request = canvas_lms_python_client.DiscussionTopicsApiFindOrCreateSummaryRequest() # DiscussionTopicsApiFindOrCreateSummaryRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/courses/<course_id>/discussion_topics/<topic_id>/summaries \\     -X POST \\     -H 'Authorization: Bearer <token>' ``` (optional)

    try:
        # Find or Create Summary
        api_response = await api_instance.discussion_topics_api_find_or_create_summary_for_groups(group_id, topic_id, discussion_topics_api_find_or_create_summary_request=discussion_topics_api_find_or_create_summary_request)
        print("The response of DiscussionTopicsApiApi->discussion_topics_api_find_or_create_summary_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscussionTopicsApiApi->discussion_topics_api_find_or_create_summary_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **topic_id** | **str**| Scope response to topic_id | 
 **discussion_topics_api_find_or_create_summary_request** | [**DiscussionTopicsApiFindOrCreateSummaryRequest**](DiscussionTopicsApiFindOrCreateSummaryRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/courses/&lt;course_id&gt;/discussion_topics/&lt;topic_id&gt;/summaries \\     -X POST \\     -H &#39;Authorization: Bearer &lt;token&gt;&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**DiscussionTopicsFindOrCreateSummaryResponse**](DiscussionTopicsFindOrCreateSummaryResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | DiscussionTopicsFindOrCreateSummaryResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discussion_topics_api_find_summary**
> DiscussionTopicsFindSummaryResponse discussion_topics_api_find_summary(course_id, topic_id)

Find Last Summary

Returns:
(1) last userInput (what current user had keyed in to produce the last discussion summary),
(2) last discussion summary generated by the current user for current discussion topic, based on userInput,
(3) and some usage information.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.discussion_topics_find_summary_response import DiscussionTopicsFindSummaryResponse
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
    api_instance = canvas_lms_python_client.DiscussionTopicsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    topic_id = 'topic_id_example' # str | Scope response to topic_id

    try:
        # Find Last Summary
        api_response = await api_instance.discussion_topics_api_find_summary(course_id, topic_id)
        print("The response of DiscussionTopicsApiApi->discussion_topics_api_find_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscussionTopicsApiApi->discussion_topics_api_find_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **topic_id** | **str**| Scope response to topic_id | 

### Return type

[**DiscussionTopicsFindSummaryResponse**](DiscussionTopicsFindSummaryResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | DiscussionTopicsFindSummaryResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discussion_topics_api_find_summary_for_groups**
> DiscussionTopicsFindSummaryResponse discussion_topics_api_find_summary_for_groups(group_id, topic_id)

Find Last Summary

Returns:
(1) last userInput (what current user had keyed in to produce the last discussion summary),
(2) last discussion summary generated by the current user for current discussion topic, based on userInput,
(3) and some usage information.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.discussion_topics_find_summary_response import DiscussionTopicsFindSummaryResponse
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
    api_instance = canvas_lms_python_client.DiscussionTopicsApiApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    topic_id = 'topic_id_example' # str | Scope response to topic_id

    try:
        # Find Last Summary
        api_response = await api_instance.discussion_topics_api_find_summary_for_groups(group_id, topic_id)
        print("The response of DiscussionTopicsApiApi->discussion_topics_api_find_summary_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscussionTopicsApiApi->discussion_topics_api_find_summary_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **topic_id** | **str**| Scope response to topic_id | 

### Return type

[**DiscussionTopicsFindSummaryResponse**](DiscussionTopicsFindSummaryResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | DiscussionTopicsFindSummaryResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discussion_topics_api_mark_all_read**
> discussion_topics_api_mark_all_read(course_id, topic_id, discussion_topics_api_mark_all_read_request=discussion_topics_api_mark_all_read_request)

Mark all entries as read

Mark the discussion topic and all its entries as read.

No request fields are necessary.

On success, the response will be 204 No Content with an empty body.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.discussion_topics_api_mark_all_read_request import DiscussionTopicsApiMarkAllReadRequest
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
    api_instance = canvas_lms_python_client.DiscussionTopicsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    topic_id = 'topic_id_example' # str | Scope response to topic_id
    discussion_topics_api_mark_all_read_request = canvas_lms_python_client.DiscussionTopicsApiMarkAllReadRequest() # DiscussionTopicsApiMarkAllReadRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/courses/<course_id>/discussion_topics/<topic_id>/read_all.json' \\      -X PUT \\      -H \"Authorization: Bearer <token>\" \\      -H \"Content-Length: 0\" ``` (optional)

    try:
        # Mark all entries as read
        await api_instance.discussion_topics_api_mark_all_read(course_id, topic_id, discussion_topics_api_mark_all_read_request=discussion_topics_api_mark_all_read_request)
    except Exception as e:
        print("Exception when calling DiscussionTopicsApiApi->discussion_topics_api_mark_all_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **topic_id** | **str**| Scope response to topic_id | 
 **discussion_topics_api_mark_all_read_request** | [**DiscussionTopicsApiMarkAllReadRequest**](DiscussionTopicsApiMarkAllReadRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/courses/&lt;course_id&gt;/discussion_topics/&lt;topic_id&gt;/read_all.json&#39; \\      -X PUT \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; \\      -H \&quot;Content-Length: 0\&quot; &#x60;&#x60;&#x60; | [optional] 

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
**0** | Mark all entries as read |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discussion_topics_api_mark_all_read_for_groups**
> discussion_topics_api_mark_all_read_for_groups(group_id, topic_id, discussion_topics_api_mark_all_read_request=discussion_topics_api_mark_all_read_request)

Mark all entries as read

Mark the discussion topic and all its entries as read.

No request fields are necessary.

On success, the response will be 204 No Content with an empty body.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.discussion_topics_api_mark_all_read_request import DiscussionTopicsApiMarkAllReadRequest
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
    api_instance = canvas_lms_python_client.DiscussionTopicsApiApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    topic_id = 'topic_id_example' # str | Scope response to topic_id
    discussion_topics_api_mark_all_read_request = canvas_lms_python_client.DiscussionTopicsApiMarkAllReadRequest() # DiscussionTopicsApiMarkAllReadRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/courses/<course_id>/discussion_topics/<topic_id>/read_all.json' \\      -X PUT \\      -H \"Authorization: Bearer <token>\" \\      -H \"Content-Length: 0\" ``` (optional)

    try:
        # Mark all entries as read
        await api_instance.discussion_topics_api_mark_all_read_for_groups(group_id, topic_id, discussion_topics_api_mark_all_read_request=discussion_topics_api_mark_all_read_request)
    except Exception as e:
        print("Exception when calling DiscussionTopicsApiApi->discussion_topics_api_mark_all_read_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **topic_id** | **str**| Scope response to topic_id | 
 **discussion_topics_api_mark_all_read_request** | [**DiscussionTopicsApiMarkAllReadRequest**](DiscussionTopicsApiMarkAllReadRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/courses/&lt;course_id&gt;/discussion_topics/&lt;topic_id&gt;/read_all.json&#39; \\      -X PUT \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; \\      -H \&quot;Content-Length: 0\&quot; &#x60;&#x60;&#x60; | [optional] 

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
**0** | Mark all entries as read |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discussion_topics_api_mark_all_topic_read**
> discussion_topics_api_mark_all_topic_read(course_id)

Mark all topic as read

Mark the initial text of all the discussion topics as read in  the context.

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
    api_instance = canvas_lms_python_client.DiscussionTopicsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id

    try:
        # Mark all topic as read
        await api_instance.discussion_topics_api_mark_all_topic_read(course_id)
    except Exception as e:
        print("Exception when calling DiscussionTopicsApiApi->discussion_topics_api_mark_all_topic_read: %s\n" % e)
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
**0** | Mark all topic as read |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discussion_topics_api_mark_all_topic_read_for_groups**
> discussion_topics_api_mark_all_topic_read_for_groups(group_id)

Mark all topic as read

Mark the initial text of all the discussion topics as read in  the context.

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
    api_instance = canvas_lms_python_client.DiscussionTopicsApiApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id

    try:
        # Mark all topic as read
        await api_instance.discussion_topics_api_mark_all_topic_read_for_groups(group_id)
    except Exception as e:
        print("Exception when calling DiscussionTopicsApiApi->discussion_topics_api_mark_all_topic_read_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 

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
**0** | Mark all topic as read |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discussion_topics_api_mark_all_unread**
> discussion_topics_api_mark_all_unread(course_id, topic_id, forced_read_state=forced_read_state)

Mark all entries as unread

Mark the discussion topic and all its entries as unread.

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
    api_instance = canvas_lms_python_client.DiscussionTopicsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    topic_id = 'topic_id_example' # str | Scope response to topic_id
    forced_read_state = True # bool | A boolean value to set all of the entries' forced_read_state. No change is made if this argument is not specified. (optional)

    try:
        # Mark all entries as unread
        await api_instance.discussion_topics_api_mark_all_unread(course_id, topic_id, forced_read_state=forced_read_state)
    except Exception as e:
        print("Exception when calling DiscussionTopicsApiApi->discussion_topics_api_mark_all_unread: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **topic_id** | **str**| Scope response to topic_id | 
 **forced_read_state** | **bool**| A boolean value to set all of the entries&#39; forced_read_state. No change is made if this argument is not specified. | [optional] 

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
**0** | Mark all entries as unread |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discussion_topics_api_mark_all_unread_for_groups**
> discussion_topics_api_mark_all_unread_for_groups(group_id, topic_id, forced_read_state=forced_read_state)

Mark all entries as unread

Mark the discussion topic and all its entries as unread.

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
    api_instance = canvas_lms_python_client.DiscussionTopicsApiApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    topic_id = 'topic_id_example' # str | Scope response to topic_id
    forced_read_state = True # bool | A boolean value to set all of the entries' forced_read_state. No change is made if this argument is not specified. (optional)

    try:
        # Mark all entries as unread
        await api_instance.discussion_topics_api_mark_all_unread_for_groups(group_id, topic_id, forced_read_state=forced_read_state)
    except Exception as e:
        print("Exception when calling DiscussionTopicsApiApi->discussion_topics_api_mark_all_unread_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **topic_id** | **str**| Scope response to topic_id | 
 **forced_read_state** | **bool**| A boolean value to set all of the entries&#39; forced_read_state. No change is made if this argument is not specified. | [optional] 

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
**0** | Mark all entries as unread |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discussion_topics_api_mark_entry_read**
> discussion_topics_api_mark_entry_read(course_id, entry_id, topic_id, discussion_topics_api_mark_entry_read_request=discussion_topics_api_mark_entry_read_request)

Mark entry as read

Mark a discussion entry as read.

No request fields are necessary.

On success, the response will be 204 No Content with an empty body.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.discussion_topics_api_mark_entry_read_request import DiscussionTopicsApiMarkEntryReadRequest
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
    api_instance = canvas_lms_python_client.DiscussionTopicsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    entry_id = 'entry_id_example' # str | Scope response to entry_id
    topic_id = 'topic_id_example' # str | Scope response to topic_id
    discussion_topics_api_mark_entry_read_request = canvas_lms_python_client.DiscussionTopicsApiMarkEntryReadRequest() # DiscussionTopicsApiMarkEntryReadRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/courses/<course_id>/discussion_topics/<topic_id>/entries/<entry_id>/read.json' \\      -X PUT \\      -H \"Authorization: Bearer <token>\"\\      -H \"Content-Length: 0\" ``` (optional)

    try:
        # Mark entry as read
        await api_instance.discussion_topics_api_mark_entry_read(course_id, entry_id, topic_id, discussion_topics_api_mark_entry_read_request=discussion_topics_api_mark_entry_read_request)
    except Exception as e:
        print("Exception when calling DiscussionTopicsApiApi->discussion_topics_api_mark_entry_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **entry_id** | **str**| Scope response to entry_id | 
 **topic_id** | **str**| Scope response to topic_id | 
 **discussion_topics_api_mark_entry_read_request** | [**DiscussionTopicsApiMarkEntryReadRequest**](DiscussionTopicsApiMarkEntryReadRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/courses/&lt;course_id&gt;/discussion_topics/&lt;topic_id&gt;/entries/&lt;entry_id&gt;/read.json&#39; \\      -X PUT \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot;\\      -H \&quot;Content-Length: 0\&quot; &#x60;&#x60;&#x60; | [optional] 

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
**0** | Mark entry as read |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discussion_topics_api_mark_entry_read_for_groups**
> discussion_topics_api_mark_entry_read_for_groups(entry_id, group_id, topic_id, discussion_topics_api_mark_entry_read_request=discussion_topics_api_mark_entry_read_request)

Mark entry as read

Mark a discussion entry as read.

No request fields are necessary.

On success, the response will be 204 No Content with an empty body.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.discussion_topics_api_mark_entry_read_request import DiscussionTopicsApiMarkEntryReadRequest
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
    api_instance = canvas_lms_python_client.DiscussionTopicsApiApi(api_client)
    entry_id = 'entry_id_example' # str | Scope response to entry_id
    group_id = 'group_id_example' # str | Scope response to group_id
    topic_id = 'topic_id_example' # str | Scope response to topic_id
    discussion_topics_api_mark_entry_read_request = canvas_lms_python_client.DiscussionTopicsApiMarkEntryReadRequest() # DiscussionTopicsApiMarkEntryReadRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/courses/<course_id>/discussion_topics/<topic_id>/entries/<entry_id>/read.json' \\      -X PUT \\      -H \"Authorization: Bearer <token>\"\\      -H \"Content-Length: 0\" ``` (optional)

    try:
        # Mark entry as read
        await api_instance.discussion_topics_api_mark_entry_read_for_groups(entry_id, group_id, topic_id, discussion_topics_api_mark_entry_read_request=discussion_topics_api_mark_entry_read_request)
    except Exception as e:
        print("Exception when calling DiscussionTopicsApiApi->discussion_topics_api_mark_entry_read_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entry_id** | **str**| Scope response to entry_id | 
 **group_id** | **str**| Scope response to group_id | 
 **topic_id** | **str**| Scope response to topic_id | 
 **discussion_topics_api_mark_entry_read_request** | [**DiscussionTopicsApiMarkEntryReadRequest**](DiscussionTopicsApiMarkEntryReadRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/courses/&lt;course_id&gt;/discussion_topics/&lt;topic_id&gt;/entries/&lt;entry_id&gt;/read.json&#39; \\      -X PUT \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot;\\      -H \&quot;Content-Length: 0\&quot; &#x60;&#x60;&#x60; | [optional] 

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
**0** | Mark entry as read |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discussion_topics_api_mark_entry_unread**
> discussion_topics_api_mark_entry_unread(course_id, entry_id, topic_id, forced_read_state=forced_read_state)

Mark entry as unread

Mark a discussion entry as unread.

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
    api_instance = canvas_lms_python_client.DiscussionTopicsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    entry_id = 'entry_id_example' # str | Scope response to entry_id
    topic_id = 'topic_id_example' # str | Scope response to topic_id
    forced_read_state = True # bool | A boolean value to set the entry's forced_read_state. No change is made if this argument is not specified. (optional)

    try:
        # Mark entry as unread
        await api_instance.discussion_topics_api_mark_entry_unread(course_id, entry_id, topic_id, forced_read_state=forced_read_state)
    except Exception as e:
        print("Exception when calling DiscussionTopicsApiApi->discussion_topics_api_mark_entry_unread: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **entry_id** | **str**| Scope response to entry_id | 
 **topic_id** | **str**| Scope response to topic_id | 
 **forced_read_state** | **bool**| A boolean value to set the entry&#39;s forced_read_state. No change is made if this argument is not specified. | [optional] 

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
**0** | Mark entry as unread |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discussion_topics_api_mark_entry_unread_for_groups**
> discussion_topics_api_mark_entry_unread_for_groups(entry_id, group_id, topic_id, forced_read_state=forced_read_state)

Mark entry as unread

Mark a discussion entry as unread.

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
    api_instance = canvas_lms_python_client.DiscussionTopicsApiApi(api_client)
    entry_id = 'entry_id_example' # str | Scope response to entry_id
    group_id = 'group_id_example' # str | Scope response to group_id
    topic_id = 'topic_id_example' # str | Scope response to topic_id
    forced_read_state = True # bool | A boolean value to set the entry's forced_read_state. No change is made if this argument is not specified. (optional)

    try:
        # Mark entry as unread
        await api_instance.discussion_topics_api_mark_entry_unread_for_groups(entry_id, group_id, topic_id, forced_read_state=forced_read_state)
    except Exception as e:
        print("Exception when calling DiscussionTopicsApiApi->discussion_topics_api_mark_entry_unread_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entry_id** | **str**| Scope response to entry_id | 
 **group_id** | **str**| Scope response to group_id | 
 **topic_id** | **str**| Scope response to topic_id | 
 **forced_read_state** | **bool**| A boolean value to set the entry&#39;s forced_read_state. No change is made if this argument is not specified. | [optional] 

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
**0** | Mark entry as unread |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discussion_topics_api_mark_topic_read**
> discussion_topics_api_mark_topic_read(course_id, topic_id)

Mark topic as read

Mark the initial text of the discussion topic as read.

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
    api_instance = canvas_lms_python_client.DiscussionTopicsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    topic_id = 'topic_id_example' # str | Scope response to topic_id

    try:
        # Mark topic as read
        await api_instance.discussion_topics_api_mark_topic_read(course_id, topic_id)
    except Exception as e:
        print("Exception when calling DiscussionTopicsApiApi->discussion_topics_api_mark_topic_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
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
**0** | Mark topic as read |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discussion_topics_api_mark_topic_read_for_groups**
> discussion_topics_api_mark_topic_read_for_groups(group_id, topic_id)

Mark topic as read

Mark the initial text of the discussion topic as read.

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
    api_instance = canvas_lms_python_client.DiscussionTopicsApiApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    topic_id = 'topic_id_example' # str | Scope response to topic_id

    try:
        # Mark topic as read
        await api_instance.discussion_topics_api_mark_topic_read_for_groups(group_id, topic_id)
    except Exception as e:
        print("Exception when calling DiscussionTopicsApiApi->discussion_topics_api_mark_topic_read_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
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
**0** | Mark topic as read |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discussion_topics_api_mark_topic_unread**
> discussion_topics_api_mark_topic_unread(course_id, topic_id)

Mark topic as unread

Mark the initial text of the discussion topic as unread.

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
    api_instance = canvas_lms_python_client.DiscussionTopicsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    topic_id = 'topic_id_example' # str | Scope response to topic_id

    try:
        # Mark topic as unread
        await api_instance.discussion_topics_api_mark_topic_unread(course_id, topic_id)
    except Exception as e:
        print("Exception when calling DiscussionTopicsApiApi->discussion_topics_api_mark_topic_unread: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
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
**0** | Mark topic as unread |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discussion_topics_api_mark_topic_unread_for_groups**
> discussion_topics_api_mark_topic_unread_for_groups(group_id, topic_id)

Mark topic as unread

Mark the initial text of the discussion topic as unread.

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
    api_instance = canvas_lms_python_client.DiscussionTopicsApiApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    topic_id = 'topic_id_example' # str | Scope response to topic_id

    try:
        # Mark topic as unread
        await api_instance.discussion_topics_api_mark_topic_unread_for_groups(group_id, topic_id)
    except Exception as e:
        print("Exception when calling DiscussionTopicsApiApi->discussion_topics_api_mark_topic_unread_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
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
**0** | Mark topic as unread |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discussion_topics_api_rate_entry**
> discussion_topics_api_rate_entry(course_id, entry_id, topic_id, discussion_topics_api_rate_entry_request=discussion_topics_api_rate_entry_request)

Rate entry

Rate a discussion entry.

On success, the response will be 204 No Content with an empty body.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.discussion_topics_api_rate_entry_request import DiscussionTopicsApiRateEntryRequest
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
    api_instance = canvas_lms_python_client.DiscussionTopicsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    entry_id = 'entry_id_example' # str | Scope response to entry_id
    topic_id = 'topic_id_example' # str | Scope response to topic_id
    discussion_topics_api_rate_entry_request = canvas_lms_python_client.DiscussionTopicsApiRateEntryRequest() # DiscussionTopicsApiRateEntryRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/courses/<course_id>/discussion_topics/<topic_id>/entries/<entry_id>/rating.json' \\      -X POST \\      -H \"Authorization: Bearer <token>\" ``` (optional)

    try:
        # Rate entry
        await api_instance.discussion_topics_api_rate_entry(course_id, entry_id, topic_id, discussion_topics_api_rate_entry_request=discussion_topics_api_rate_entry_request)
    except Exception as e:
        print("Exception when calling DiscussionTopicsApiApi->discussion_topics_api_rate_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **entry_id** | **str**| Scope response to entry_id | 
 **topic_id** | **str**| Scope response to topic_id | 
 **discussion_topics_api_rate_entry_request** | [**DiscussionTopicsApiRateEntryRequest**](DiscussionTopicsApiRateEntryRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/courses/&lt;course_id&gt;/discussion_topics/&lt;topic_id&gt;/entries/&lt;entry_id&gt;/rating.json&#39; \\      -X POST \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; &#x60;&#x60;&#x60; | [optional] 

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
**0** | Rate entry |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discussion_topics_api_rate_entry_for_groups**
> discussion_topics_api_rate_entry_for_groups(entry_id, group_id, topic_id, discussion_topics_api_rate_entry_request=discussion_topics_api_rate_entry_request)

Rate entry

Rate a discussion entry.

On success, the response will be 204 No Content with an empty body.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.discussion_topics_api_rate_entry_request import DiscussionTopicsApiRateEntryRequest
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
    api_instance = canvas_lms_python_client.DiscussionTopicsApiApi(api_client)
    entry_id = 'entry_id_example' # str | Scope response to entry_id
    group_id = 'group_id_example' # str | Scope response to group_id
    topic_id = 'topic_id_example' # str | Scope response to topic_id
    discussion_topics_api_rate_entry_request = canvas_lms_python_client.DiscussionTopicsApiRateEntryRequest() # DiscussionTopicsApiRateEntryRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/courses/<course_id>/discussion_topics/<topic_id>/entries/<entry_id>/rating.json' \\      -X POST \\      -H \"Authorization: Bearer <token>\" ``` (optional)

    try:
        # Rate entry
        await api_instance.discussion_topics_api_rate_entry_for_groups(entry_id, group_id, topic_id, discussion_topics_api_rate_entry_request=discussion_topics_api_rate_entry_request)
    except Exception as e:
        print("Exception when calling DiscussionTopicsApiApi->discussion_topics_api_rate_entry_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entry_id** | **str**| Scope response to entry_id | 
 **group_id** | **str**| Scope response to group_id | 
 **topic_id** | **str**| Scope response to topic_id | 
 **discussion_topics_api_rate_entry_request** | [**DiscussionTopicsApiRateEntryRequest**](DiscussionTopicsApiRateEntryRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/courses/&lt;course_id&gt;/discussion_topics/&lt;topic_id&gt;/entries/&lt;entry_id&gt;/rating.json&#39; \\      -X POST \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; &#x60;&#x60;&#x60; | [optional] 

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
**0** | Rate entry |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discussion_topics_api_replies**
> List[DiscussionEntry] discussion_topics_api_replies(course_id, entry_id, topic_id, page=page, per_page=per_page)

List entry replies

Retrieve the (paginated) replies to a top-level entry in a discussion
topic.

May require (depending on the topic) that the user has posted in the topic.
If it is required, and the user has not posted, will respond with a 403
Forbidden status and the body 'require_initial_post'.

Ordering of returned entries is newest-first by creation timestamp.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.discussion_entry import DiscussionEntry
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
    api_instance = canvas_lms_python_client.DiscussionTopicsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    entry_id = 'entry_id_example' # str | Scope response to entry_id
    topic_id = 'topic_id_example' # str | Scope response to topic_id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List entry replies
        api_response = await api_instance.discussion_topics_api_replies(course_id, entry_id, topic_id, page=page, per_page=per_page)
        print("The response of DiscussionTopicsApiApi->discussion_topics_api_replies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscussionTopicsApiApi->discussion_topics_api_replies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **entry_id** | **str**| Scope response to entry_id | 
 **topic_id** | **str**| Scope response to topic_id | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[DiscussionEntry]**](DiscussionEntry.md)

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

# **discussion_topics_api_replies_for_groups**
> List[DiscussionEntry] discussion_topics_api_replies_for_groups(entry_id, group_id, topic_id, page=page, per_page=per_page)

List entry replies

Retrieve the (paginated) replies to a top-level entry in a discussion
topic.

May require (depending on the topic) that the user has posted in the topic.
If it is required, and the user has not posted, will respond with a 403
Forbidden status and the body 'require_initial_post'.

Ordering of returned entries is newest-first by creation timestamp.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.discussion_entry import DiscussionEntry
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
    api_instance = canvas_lms_python_client.DiscussionTopicsApiApi(api_client)
    entry_id = 'entry_id_example' # str | Scope response to entry_id
    group_id = 'group_id_example' # str | Scope response to group_id
    topic_id = 'topic_id_example' # str | Scope response to topic_id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List entry replies
        api_response = await api_instance.discussion_topics_api_replies_for_groups(entry_id, group_id, topic_id, page=page, per_page=per_page)
        print("The response of DiscussionTopicsApiApi->discussion_topics_api_replies_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscussionTopicsApiApi->discussion_topics_api_replies_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entry_id** | **str**| Scope response to entry_id | 
 **group_id** | **str**| Scope response to group_id | 
 **topic_id** | **str**| Scope response to topic_id | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[DiscussionEntry]**](DiscussionEntry.md)

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

# **discussion_topics_api_show**
> DiscussionTopic discussion_topics_api_show(course_id, topic_id, include=include)

Get a single topic

Returns data on an individual discussion topic. See the List action for the response formatting.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.discussion_topic import DiscussionTopic
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
    api_instance = canvas_lms_python_client.DiscussionTopicsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    topic_id = 'topic_id_example' # str | Scope response to topic_id
    include = ['include_example'] # List[str] | If \"all_dates\" is passed, all dates associated with graded discussions' assignments will be included. if \"sections\" is passed, includes the course sections that are associated with the topic, if the topic is specific to certain sections of the course. If \"sections_user_count\" is passed, then:   (a) If sections were asked for *and* the topic is specific to certain       course sections, includes the number of users in each       section. (as part of the section json asked for above)   (b) Else, includes at the root level the total number of users in the       topic's context (group or course) that the topic applies to. If \"overrides\" is passed, the overrides for the assignment will be included (optional)

    try:
        # Get a single topic
        api_response = await api_instance.discussion_topics_api_show(course_id, topic_id, include=include)
        print("The response of DiscussionTopicsApiApi->discussion_topics_api_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscussionTopicsApiApi->discussion_topics_api_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **topic_id** | **str**| Scope response to topic_id | 
 **include** | [**List[str]**](str.md)| If \&quot;all_dates\&quot; is passed, all dates associated with graded discussions&#39; assignments will be included. if \&quot;sections\&quot; is passed, includes the course sections that are associated with the topic, if the topic is specific to certain sections of the course. If \&quot;sections_user_count\&quot; is passed, then:   (a) If sections were asked for *and* the topic is specific to certain       course sections, includes the number of users in each       section. (as part of the section json asked for above)   (b) Else, includes at the root level the total number of users in the       topic&#39;s context (group or course) that the topic applies to. If \&quot;overrides\&quot; is passed, the overrides for the assignment will be included | [optional] 

### Return type

[**DiscussionTopic**](DiscussionTopic.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | DiscussionTopic |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discussion_topics_api_show_for_groups**
> DiscussionTopic discussion_topics_api_show_for_groups(group_id, topic_id, include=include)

Get a single topic

Returns data on an individual discussion topic. See the List action for the response formatting.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.discussion_topic import DiscussionTopic
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
    api_instance = canvas_lms_python_client.DiscussionTopicsApiApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    topic_id = 'topic_id_example' # str | Scope response to topic_id
    include = ['include_example'] # List[str] | If \"all_dates\" is passed, all dates associated with graded discussions' assignments will be included. if \"sections\" is passed, includes the course sections that are associated with the topic, if the topic is specific to certain sections of the course. If \"sections_user_count\" is passed, then:   (a) If sections were asked for *and* the topic is specific to certain       course sections, includes the number of users in each       section. (as part of the section json asked for above)   (b) Else, includes at the root level the total number of users in the       topic's context (group or course) that the topic applies to. If \"overrides\" is passed, the overrides for the assignment will be included (optional)

    try:
        # Get a single topic
        api_response = await api_instance.discussion_topics_api_show_for_groups(group_id, topic_id, include=include)
        print("The response of DiscussionTopicsApiApi->discussion_topics_api_show_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscussionTopicsApiApi->discussion_topics_api_show_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **topic_id** | **str**| Scope response to topic_id | 
 **include** | [**List[str]**](str.md)| If \&quot;all_dates\&quot; is passed, all dates associated with graded discussions&#39; assignments will be included. if \&quot;sections\&quot; is passed, includes the course sections that are associated with the topic, if the topic is specific to certain sections of the course. If \&quot;sections_user_count\&quot; is passed, then:   (a) If sections were asked for *and* the topic is specific to certain       course sections, includes the number of users in each       section. (as part of the section json asked for above)   (b) Else, includes at the root level the total number of users in the       topic&#39;s context (group or course) that the topic applies to. If \&quot;overrides\&quot; is passed, the overrides for the assignment will be included | [optional] 

### Return type

[**DiscussionTopic**](DiscussionTopic.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | DiscussionTopic |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discussion_topics_api_subscribe_topic**
> discussion_topics_api_subscribe_topic(course_id, topic_id)

Subscribe to a topic

Subscribe to a topic to receive notifications about new entries

On success, the response will be 204 No Content with an empty body

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
    api_instance = canvas_lms_python_client.DiscussionTopicsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    topic_id = 'topic_id_example' # str | Scope response to topic_id

    try:
        # Subscribe to a topic
        await api_instance.discussion_topics_api_subscribe_topic(course_id, topic_id)
    except Exception as e:
        print("Exception when calling DiscussionTopicsApiApi->discussion_topics_api_subscribe_topic: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
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
**0** | Subscribe to a topic |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discussion_topics_api_subscribe_topic_for_groups**
> discussion_topics_api_subscribe_topic_for_groups(group_id, topic_id)

Subscribe to a topic

Subscribe to a topic to receive notifications about new entries

On success, the response will be 204 No Content with an empty body

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
    api_instance = canvas_lms_python_client.DiscussionTopicsApiApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    topic_id = 'topic_id_example' # str | Scope response to topic_id

    try:
        # Subscribe to a topic
        await api_instance.discussion_topics_api_subscribe_topic_for_groups(group_id, topic_id)
    except Exception as e:
        print("Exception when calling DiscussionTopicsApiApi->discussion_topics_api_subscribe_topic_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
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
**0** | Subscribe to a topic |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discussion_topics_api_summary_feedback**
> DiscussionTopicsSummaryFeedbackResponse discussion_topics_api_summary_feedback(course_id, summary_id, topic_id, discussion_topics_api_summary_feedback_request=discussion_topics_api_summary_feedback_request)

Summary Feedback

Persists feedback on a discussion topic summary.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.discussion_topics_api_summary_feedback_request import DiscussionTopicsApiSummaryFeedbackRequest
from canvas_lms_python_client.models.discussion_topics_summary_feedback_response import DiscussionTopicsSummaryFeedbackResponse
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
    api_instance = canvas_lms_python_client.DiscussionTopicsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    summary_id = 'summary_id_example' # str | Scope response to summary_id
    topic_id = 'topic_id_example' # str | Scope response to topic_id
    discussion_topics_api_summary_feedback_request = canvas_lms_python_client.DiscussionTopicsApiSummaryFeedbackRequest() # DiscussionTopicsApiSummaryFeedbackRequest | Request body parameters  **Example Request:** ``` curl -X POST https://<canvas>/api/v1/courses/<course_id>/discussion_topics/<topic_id>/summaries/<summary_id>/feedback \\      -F '_action=like' \\      -H \"Authorization: Bearer ``` (optional)

    try:
        # Summary Feedback
        api_response = await api_instance.discussion_topics_api_summary_feedback(course_id, summary_id, topic_id, discussion_topics_api_summary_feedback_request=discussion_topics_api_summary_feedback_request)
        print("The response of DiscussionTopicsApiApi->discussion_topics_api_summary_feedback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscussionTopicsApiApi->discussion_topics_api_summary_feedback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **summary_id** | **str**| Scope response to summary_id | 
 **topic_id** | **str**| Scope response to topic_id | 
 **discussion_topics_api_summary_feedback_request** | [**DiscussionTopicsApiSummaryFeedbackRequest**](DiscussionTopicsApiSummaryFeedbackRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl -X POST https://&lt;canvas&gt;/api/v1/courses/&lt;course_id&gt;/discussion_topics/&lt;topic_id&gt;/summaries/&lt;summary_id&gt;/feedback \\      -F &#39;_action&#x3D;like&#39; \\      -H \&quot;Authorization: Bearer &#x60;&#x60;&#x60; | [optional] 

### Return type

[**DiscussionTopicsSummaryFeedbackResponse**](DiscussionTopicsSummaryFeedbackResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | DiscussionTopicsSummaryFeedbackResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discussion_topics_api_summary_feedback_for_groups**
> DiscussionTopicsSummaryFeedbackResponse discussion_topics_api_summary_feedback_for_groups(group_id, summary_id, topic_id, discussion_topics_api_summary_feedback_request=discussion_topics_api_summary_feedback_request)

Summary Feedback

Persists feedback on a discussion topic summary.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.discussion_topics_api_summary_feedback_request import DiscussionTopicsApiSummaryFeedbackRequest
from canvas_lms_python_client.models.discussion_topics_summary_feedback_response import DiscussionTopicsSummaryFeedbackResponse
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
    api_instance = canvas_lms_python_client.DiscussionTopicsApiApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    summary_id = 'summary_id_example' # str | Scope response to summary_id
    topic_id = 'topic_id_example' # str | Scope response to topic_id
    discussion_topics_api_summary_feedback_request = canvas_lms_python_client.DiscussionTopicsApiSummaryFeedbackRequest() # DiscussionTopicsApiSummaryFeedbackRequest | Request body parameters  **Example Request:** ``` curl -X POST https://<canvas>/api/v1/courses/<course_id>/discussion_topics/<topic_id>/summaries/<summary_id>/feedback \\      -F '_action=like' \\      -H \"Authorization: Bearer ``` (optional)

    try:
        # Summary Feedback
        api_response = await api_instance.discussion_topics_api_summary_feedback_for_groups(group_id, summary_id, topic_id, discussion_topics_api_summary_feedback_request=discussion_topics_api_summary_feedback_request)
        print("The response of DiscussionTopicsApiApi->discussion_topics_api_summary_feedback_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscussionTopicsApiApi->discussion_topics_api_summary_feedback_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **summary_id** | **str**| Scope response to summary_id | 
 **topic_id** | **str**| Scope response to topic_id | 
 **discussion_topics_api_summary_feedback_request** | [**DiscussionTopicsApiSummaryFeedbackRequest**](DiscussionTopicsApiSummaryFeedbackRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl -X POST https://&lt;canvas&gt;/api/v1/courses/&lt;course_id&gt;/discussion_topics/&lt;topic_id&gt;/summaries/&lt;summary_id&gt;/feedback \\      -F &#39;_action&#x3D;like&#39; \\      -H \&quot;Authorization: Bearer &#x60;&#x60;&#x60; | [optional] 

### Return type

[**DiscussionTopicsSummaryFeedbackResponse**](DiscussionTopicsSummaryFeedbackResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | DiscussionTopicsSummaryFeedbackResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discussion_topics_api_unsubscribe_topic**
> discussion_topics_api_unsubscribe_topic(course_id, topic_id)

Unsubscribe from a topic

Unsubscribe from a topic to stop receiving notifications about new entries

On success, the response will be 204 No Content with an empty body

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
    api_instance = canvas_lms_python_client.DiscussionTopicsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    topic_id = 'topic_id_example' # str | Scope response to topic_id

    try:
        # Unsubscribe from a topic
        await api_instance.discussion_topics_api_unsubscribe_topic(course_id, topic_id)
    except Exception as e:
        print("Exception when calling DiscussionTopicsApiApi->discussion_topics_api_unsubscribe_topic: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
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
**0** | Unsubscribe from a topic |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discussion_topics_api_unsubscribe_topic_for_groups**
> discussion_topics_api_unsubscribe_topic_for_groups(group_id, topic_id)

Unsubscribe from a topic

Unsubscribe from a topic to stop receiving notifications about new entries

On success, the response will be 204 No Content with an empty body

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
    api_instance = canvas_lms_python_client.DiscussionTopicsApiApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    topic_id = 'topic_id_example' # str | Scope response to topic_id

    try:
        # Unsubscribe from a topic
        await api_instance.discussion_topics_api_unsubscribe_topic_for_groups(group_id, topic_id)
    except Exception as e:
        print("Exception when calling DiscussionTopicsApiApi->discussion_topics_api_unsubscribe_topic_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
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
**0** | Unsubscribe from a topic |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discussion_topics_api_view**
> DiscussionTopicsViewResponse discussion_topics_api_view(course_id, topic_id)

Get the full topic

Return a cached structure of the discussion topic, containing all entries,
their authors, and their message bodies.

May require (depending on the topic) that the user has posted in the topic.
If it is required, and the user has not posted, will respond with a 403
Forbidden status and the body 'require_initial_post'.

In some rare situations, this cached structure may not be available yet. In
that case, the server will respond with a 503 error, and the caller should
try again soon.

The response is an object containing the following keys:
* "participants": A list of summary information on users who have posted to
  the discussion. Each value is an object containing their id, display_name,
  and avatar_url.
* "unread_entries": A list of entry ids that are unread by the current
  user. this implies that any entry not in this list is read.
* "entry_ratings": A map of entry ids to ratings by the current user. Entries
  not in this list have no rating. Only populated if rating is enabled.
* "forced_entries": A list of entry ids that have forced_read_state set to
  true. This flag is meant to indicate the entry's read_state has been
  manually set to 'unread' by the user, so the entry should not be
  automatically marked as read.
* "view": A threaded view of all the entries in the discussion, containing
  the id, user_id, and message.
* "new_entries": Because this view is eventually consistent, it's possible
  that newly created or updated entries won't yet be reflected in the view.
  If the application wants to also get a flat list of all entries not yet
  reflected in the view, pass include_new_entries=1 to the request and this
  array of entries will be returned. These entries are returned in a flat
  array, in ascending created_at order.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.discussion_topics_view_response import DiscussionTopicsViewResponse
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
    api_instance = canvas_lms_python_client.DiscussionTopicsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    topic_id = 'topic_id_example' # str | Scope response to topic_id

    try:
        # Get the full topic
        api_response = await api_instance.discussion_topics_api_view(course_id, topic_id)
        print("The response of DiscussionTopicsApiApi->discussion_topics_api_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscussionTopicsApiApi->discussion_topics_api_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **topic_id** | **str**| Scope response to topic_id | 

### Return type

[**DiscussionTopicsViewResponse**](DiscussionTopicsViewResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | DiscussionTopicsViewResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discussion_topics_api_view_for_groups**
> DiscussionTopicsViewResponse discussion_topics_api_view_for_groups(group_id, topic_id)

Get the full topic

Return a cached structure of the discussion topic, containing all entries,
their authors, and their message bodies.

May require (depending on the topic) that the user has posted in the topic.
If it is required, and the user has not posted, will respond with a 403
Forbidden status and the body 'require_initial_post'.

In some rare situations, this cached structure may not be available yet. In
that case, the server will respond with a 503 error, and the caller should
try again soon.

The response is an object containing the following keys:
* "participants": A list of summary information on users who have posted to
  the discussion. Each value is an object containing their id, display_name,
  and avatar_url.
* "unread_entries": A list of entry ids that are unread by the current
  user. this implies that any entry not in this list is read.
* "entry_ratings": A map of entry ids to ratings by the current user. Entries
  not in this list have no rating. Only populated if rating is enabled.
* "forced_entries": A list of entry ids that have forced_read_state set to
  true. This flag is meant to indicate the entry's read_state has been
  manually set to 'unread' by the user, so the entry should not be
  automatically marked as read.
* "view": A threaded view of all the entries in the discussion, containing
  the id, user_id, and message.
* "new_entries": Because this view is eventually consistent, it's possible
  that newly created or updated entries won't yet be reflected in the view.
  If the application wants to also get a flat list of all entries not yet
  reflected in the view, pass include_new_entries=1 to the request and this
  array of entries will be returned. These entries are returned in a flat
  array, in ascending created_at order.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.discussion_topics_view_response import DiscussionTopicsViewResponse
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
    api_instance = canvas_lms_python_client.DiscussionTopicsApiApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    topic_id = 'topic_id_example' # str | Scope response to topic_id

    try:
        # Get the full topic
        api_response = await api_instance.discussion_topics_api_view_for_groups(group_id, topic_id)
        print("The response of DiscussionTopicsApiApi->discussion_topics_api_view_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscussionTopicsApiApi->discussion_topics_api_view_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **topic_id** | **str**| Scope response to topic_id | 

### Return type

[**DiscussionTopicsViewResponse**](DiscussionTopicsViewResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | DiscussionTopicsViewResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

