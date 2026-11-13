# canvas_lms_python_client.DiscussionTopicsApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**discussion_topics_create**](DiscussionTopicsApi.md#discussion_topics_create) | **POST** /api/v1/courses/{course_id}/discussion_topics | Create a new discussion topic
[**discussion_topics_create_for_groups**](DiscussionTopicsApi.md#discussion_topics_create_for_groups) | **POST** /api/v1/groups/{group_id}/discussion_topics | Create a new discussion topic
[**discussion_topics_destroy**](DiscussionTopicsApi.md#discussion_topics_destroy) | **DELETE** /api/v1/courses/{course_id}/discussion_topics/{topic_id} | Delete a topic
[**discussion_topics_destroy_for_groups**](DiscussionTopicsApi.md#discussion_topics_destroy_for_groups) | **DELETE** /api/v1/groups/{group_id}/discussion_topics/{topic_id} | Delete a topic
[**discussion_topics_index**](DiscussionTopicsApi.md#discussion_topics_index) | **GET** /api/v1/courses/{course_id}/discussion_topics | List discussion topics
[**discussion_topics_index_for_groups**](DiscussionTopicsApi.md#discussion_topics_index_for_groups) | **GET** /api/v1/groups/{group_id}/discussion_topics | List discussion topics
[**discussion_topics_reorder**](DiscussionTopicsApi.md#discussion_topics_reorder) | **POST** /api/v1/courses/{course_id}/discussion_topics/reorder | Reorder pinned topics
[**discussion_topics_reorder_for_groups**](DiscussionTopicsApi.md#discussion_topics_reorder_for_groups) | **POST** /api/v1/groups/{group_id}/discussion_topics/reorder | Reorder pinned topics
[**discussion_topics_update**](DiscussionTopicsApi.md#discussion_topics_update) | **PUT** /api/v1/courses/{course_id}/discussion_topics/{topic_id} | Update a topic
[**discussion_topics_update_for_groups**](DiscussionTopicsApi.md#discussion_topics_update_for_groups) | **PUT** /api/v1/groups/{group_id}/discussion_topics/{topic_id} | Update a topic


# **discussion_topics_create**
> DiscussionTopic discussion_topics_create(course_id, discussion_topics_create_request=discussion_topics_create_request)

Create a new discussion topic

Create an new discussion topic for the course or group.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.discussion_topic import DiscussionTopic
from canvas_lms_python_client.models.discussion_topics_create_request import DiscussionTopicsCreateRequest
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
    api_instance = canvas_lms_python_client.DiscussionTopicsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    discussion_topics_create_request = canvas_lms_python_client.DiscussionTopicsCreateRequest() # DiscussionTopicsCreateRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/courses/<course_id>/discussion_topics \\     -F title='my topic' \\     -F message='initial message' \\     -F podcast_enabled=1 \\     -H 'Authorization: Bearer <token>'     -F 'attachment=@<filename>' \\ ``` (optional)

    try:
        # Create a new discussion topic
        api_response = await api_instance.discussion_topics_create(course_id, discussion_topics_create_request=discussion_topics_create_request)
        print("The response of DiscussionTopicsApi->discussion_topics_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscussionTopicsApi->discussion_topics_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **discussion_topics_create_request** | [**DiscussionTopicsCreateRequest**](DiscussionTopicsCreateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/courses/&lt;course_id&gt;/discussion_topics \\     -F title&#x3D;&#39;my topic&#39; \\     -F message&#x3D;&#39;initial message&#39; \\     -F podcast_enabled&#x3D;1 \\     -H &#39;Authorization: Bearer &lt;token&gt;&#39;     -F &#39;attachment&#x3D;@&lt;filename&gt;&#39; \\ &#x60;&#x60;&#x60; | [optional] 

### Return type

[**DiscussionTopic**](DiscussionTopic.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | DiscussionTopic |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discussion_topics_create_for_groups**
> DiscussionTopic discussion_topics_create_for_groups(group_id, discussion_topics_create_request=discussion_topics_create_request)

Create a new discussion topic

Create an new discussion topic for the course or group.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.discussion_topic import DiscussionTopic
from canvas_lms_python_client.models.discussion_topics_create_request import DiscussionTopicsCreateRequest
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
    api_instance = canvas_lms_python_client.DiscussionTopicsApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    discussion_topics_create_request = canvas_lms_python_client.DiscussionTopicsCreateRequest() # DiscussionTopicsCreateRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/courses/<course_id>/discussion_topics \\     -F title='my topic' \\     -F message='initial message' \\     -F podcast_enabled=1 \\     -H 'Authorization: Bearer <token>'     -F 'attachment=@<filename>' \\ ``` (optional)

    try:
        # Create a new discussion topic
        api_response = await api_instance.discussion_topics_create_for_groups(group_id, discussion_topics_create_request=discussion_topics_create_request)
        print("The response of DiscussionTopicsApi->discussion_topics_create_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscussionTopicsApi->discussion_topics_create_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **discussion_topics_create_request** | [**DiscussionTopicsCreateRequest**](DiscussionTopicsCreateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/courses/&lt;course_id&gt;/discussion_topics \\     -F title&#x3D;&#39;my topic&#39; \\     -F message&#x3D;&#39;initial message&#39; \\     -F podcast_enabled&#x3D;1 \\     -H &#39;Authorization: Bearer &lt;token&gt;&#39;     -F &#39;attachment&#x3D;@&lt;filename&gt;&#39; \\ &#x60;&#x60;&#x60; | [optional] 

### Return type

[**DiscussionTopic**](DiscussionTopic.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | DiscussionTopic |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discussion_topics_destroy**
> DiscussionTopicsDestroyResponse discussion_topics_destroy(course_id, topic_id)

Delete a topic

Deletes the discussion topic. This will also delete the assignment, if it's
an assignment discussion.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.discussion_topics_destroy_response import DiscussionTopicsDestroyResponse
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
    api_instance = canvas_lms_python_client.DiscussionTopicsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    topic_id = 'topic_id_example' # str | Scope response to topic_id

    try:
        # Delete a topic
        api_response = await api_instance.discussion_topics_destroy(course_id, topic_id)
        print("The response of DiscussionTopicsApi->discussion_topics_destroy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscussionTopicsApi->discussion_topics_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **topic_id** | **str**| Scope response to topic_id | 

### Return type

[**DiscussionTopicsDestroyResponse**](DiscussionTopicsDestroyResponse.md)

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

# **discussion_topics_destroy_for_groups**
> DiscussionTopicsDestroyResponse discussion_topics_destroy_for_groups(group_id, topic_id)

Delete a topic

Deletes the discussion topic. This will also delete the assignment, if it's
an assignment discussion.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.discussion_topics_destroy_response import DiscussionTopicsDestroyResponse
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
    api_instance = canvas_lms_python_client.DiscussionTopicsApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    topic_id = 'topic_id_example' # str | Scope response to topic_id

    try:
        # Delete a topic
        api_response = await api_instance.discussion_topics_destroy_for_groups(group_id, topic_id)
        print("The response of DiscussionTopicsApi->discussion_topics_destroy_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscussionTopicsApi->discussion_topics_destroy_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **topic_id** | **str**| Scope response to topic_id | 

### Return type

[**DiscussionTopicsDestroyResponse**](DiscussionTopicsDestroyResponse.md)

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

# **discussion_topics_index**
> List[DiscussionTopic] discussion_topics_index(course_id, include=include, order_by=order_by, scope=scope, only_announcements=only_announcements, filter_by=filter_by, search_term=search_term, exclude_context_module_locked_topics=exclude_context_module_locked_topics, page=page, per_page=per_page)

List discussion topics

Returns the paginated list of discussion topics for this course or group.

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
    api_instance = canvas_lms_python_client.DiscussionTopicsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    include = ['include_example'] # List[str] | If \"all_dates\" is passed, all dates associated with graded discussions' assignments will be included. if \"sections\" is passed, includes the course sections that are associated with the topic, if the topic is specific to certain sections of the course. If \"sections_user_count\" is passed, then:   (a) If sections were asked for *and* the topic is specific to certain       course sections, includes the number of users in each       section. (as part of the section json asked for above)   (b) Else, includes at the root level the total number of users in the       topic's context (group or course) that the topic applies to. If \"overrides\" is passed, the overrides for the assignment will be included (optional)
    order_by = 'order_by_example' # str | Determines the order of the discussion topic list. Defaults to \"position\". (optional)
    scope = 'scope_example' # str | Only return discussion topics in the given state(s). Defaults to including all topics. Filtering is done after pagination, so pages may be smaller than requested if topics are filtered. Can pass multiple states as comma separated string. (optional)
    only_announcements = True # bool | Return announcements instead of discussion topics. Defaults to false (optional)
    filter_by = 'filter_by_example' # str | The state of the discussion topic to return. Currently only supports unread state. (optional)
    search_term = 'search_term_example' # str | The partial title of the discussion topics to match and return. (optional)
    exclude_context_module_locked_topics = True # bool | For students, exclude topics that are locked by module progression. Defaults to false. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List discussion topics
        api_response = await api_instance.discussion_topics_index(course_id, include=include, order_by=order_by, scope=scope, only_announcements=only_announcements, filter_by=filter_by, search_term=search_term, exclude_context_module_locked_topics=exclude_context_module_locked_topics, page=page, per_page=per_page)
        print("The response of DiscussionTopicsApi->discussion_topics_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscussionTopicsApi->discussion_topics_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **include** | [**List[str]**](str.md)| If \&quot;all_dates\&quot; is passed, all dates associated with graded discussions&#39; assignments will be included. if \&quot;sections\&quot; is passed, includes the course sections that are associated with the topic, if the topic is specific to certain sections of the course. If \&quot;sections_user_count\&quot; is passed, then:   (a) If sections were asked for *and* the topic is specific to certain       course sections, includes the number of users in each       section. (as part of the section json asked for above)   (b) Else, includes at the root level the total number of users in the       topic&#39;s context (group or course) that the topic applies to. If \&quot;overrides\&quot; is passed, the overrides for the assignment will be included | [optional] 
 **order_by** | **str**| Determines the order of the discussion topic list. Defaults to \&quot;position\&quot;. | [optional] 
 **scope** | **str**| Only return discussion topics in the given state(s). Defaults to including all topics. Filtering is done after pagination, so pages may be smaller than requested if topics are filtered. Can pass multiple states as comma separated string. | [optional] 
 **only_announcements** | **bool**| Return announcements instead of discussion topics. Defaults to false | [optional] 
 **filter_by** | **str**| The state of the discussion topic to return. Currently only supports unread state. | [optional] 
 **search_term** | **str**| The partial title of the discussion topics to match and return. | [optional] 
 **exclude_context_module_locked_topics** | **bool**| For students, exclude topics that are locked by module progression. Defaults to false. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[DiscussionTopic]**](DiscussionTopic.md)

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

# **discussion_topics_index_for_groups**
> List[DiscussionTopic] discussion_topics_index_for_groups(group_id, include=include, order_by=order_by, scope=scope, only_announcements=only_announcements, filter_by=filter_by, search_term=search_term, exclude_context_module_locked_topics=exclude_context_module_locked_topics, page=page, per_page=per_page)

List discussion topics

Returns the paginated list of discussion topics for this course or group.

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
    api_instance = canvas_lms_python_client.DiscussionTopicsApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    include = ['include_example'] # List[str] | If \"all_dates\" is passed, all dates associated with graded discussions' assignments will be included. if \"sections\" is passed, includes the course sections that are associated with the topic, if the topic is specific to certain sections of the course. If \"sections_user_count\" is passed, then:   (a) If sections were asked for *and* the topic is specific to certain       course sections, includes the number of users in each       section. (as part of the section json asked for above)   (b) Else, includes at the root level the total number of users in the       topic's context (group or course) that the topic applies to. If \"overrides\" is passed, the overrides for the assignment will be included (optional)
    order_by = 'order_by_example' # str | Determines the order of the discussion topic list. Defaults to \"position\". (optional)
    scope = 'scope_example' # str | Only return discussion topics in the given state(s). Defaults to including all topics. Filtering is done after pagination, so pages may be smaller than requested if topics are filtered. Can pass multiple states as comma separated string. (optional)
    only_announcements = True # bool | Return announcements instead of discussion topics. Defaults to false (optional)
    filter_by = 'filter_by_example' # str | The state of the discussion topic to return. Currently only supports unread state. (optional)
    search_term = 'search_term_example' # str | The partial title of the discussion topics to match and return. (optional)
    exclude_context_module_locked_topics = True # bool | For students, exclude topics that are locked by module progression. Defaults to false. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List discussion topics
        api_response = await api_instance.discussion_topics_index_for_groups(group_id, include=include, order_by=order_by, scope=scope, only_announcements=only_announcements, filter_by=filter_by, search_term=search_term, exclude_context_module_locked_topics=exclude_context_module_locked_topics, page=page, per_page=per_page)
        print("The response of DiscussionTopicsApi->discussion_topics_index_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscussionTopicsApi->discussion_topics_index_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **include** | [**List[str]**](str.md)| If \&quot;all_dates\&quot; is passed, all dates associated with graded discussions&#39; assignments will be included. if \&quot;sections\&quot; is passed, includes the course sections that are associated with the topic, if the topic is specific to certain sections of the course. If \&quot;sections_user_count\&quot; is passed, then:   (a) If sections were asked for *and* the topic is specific to certain       course sections, includes the number of users in each       section. (as part of the section json asked for above)   (b) Else, includes at the root level the total number of users in the       topic&#39;s context (group or course) that the topic applies to. If \&quot;overrides\&quot; is passed, the overrides for the assignment will be included | [optional] 
 **order_by** | **str**| Determines the order of the discussion topic list. Defaults to \&quot;position\&quot;. | [optional] 
 **scope** | **str**| Only return discussion topics in the given state(s). Defaults to including all topics. Filtering is done after pagination, so pages may be smaller than requested if topics are filtered. Can pass multiple states as comma separated string. | [optional] 
 **only_announcements** | **bool**| Return announcements instead of discussion topics. Defaults to false | [optional] 
 **filter_by** | **str**| The state of the discussion topic to return. Currently only supports unread state. | [optional] 
 **search_term** | **str**| The partial title of the discussion topics to match and return. | [optional] 
 **exclude_context_module_locked_topics** | **bool**| For students, exclude topics that are locked by module progression. Defaults to false. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[DiscussionTopic]**](DiscussionTopic.md)

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

# **discussion_topics_reorder**
> DiscussionTopicsReorderResponse discussion_topics_reorder(course_id, discussion_topics_reorder_request=discussion_topics_reorder_request)

Reorder pinned topics

Puts the pinned discussion topics in the specified order.
All pinned topics should be included.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.discussion_topics_reorder_request import DiscussionTopicsReorderRequest
from canvas_lms_python_client.models.discussion_topics_reorder_response import DiscussionTopicsReorderResponse
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
    api_instance = canvas_lms_python_client.DiscussionTopicsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    discussion_topics_reorder_request = canvas_lms_python_client.DiscussionTopicsReorderRequest() # DiscussionTopicsReorderRequest | Request body parameters (optional)

    try:
        # Reorder pinned topics
        api_response = await api_instance.discussion_topics_reorder(course_id, discussion_topics_reorder_request=discussion_topics_reorder_request)
        print("The response of DiscussionTopicsApi->discussion_topics_reorder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscussionTopicsApi->discussion_topics_reorder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **discussion_topics_reorder_request** | [**DiscussionTopicsReorderRequest**](DiscussionTopicsReorderRequest.md)| Request body parameters | [optional] 

### Return type

[**DiscussionTopicsReorderResponse**](DiscussionTopicsReorderResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | DiscussionTopicsReorderResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discussion_topics_reorder_for_groups**
> DiscussionTopicsReorderResponse discussion_topics_reorder_for_groups(group_id, discussion_topics_reorder_request=discussion_topics_reorder_request)

Reorder pinned topics

Puts the pinned discussion topics in the specified order.
All pinned topics should be included.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.discussion_topics_reorder_request import DiscussionTopicsReorderRequest
from canvas_lms_python_client.models.discussion_topics_reorder_response import DiscussionTopicsReorderResponse
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
    api_instance = canvas_lms_python_client.DiscussionTopicsApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    discussion_topics_reorder_request = canvas_lms_python_client.DiscussionTopicsReorderRequest() # DiscussionTopicsReorderRequest | Request body parameters (optional)

    try:
        # Reorder pinned topics
        api_response = await api_instance.discussion_topics_reorder_for_groups(group_id, discussion_topics_reorder_request=discussion_topics_reorder_request)
        print("The response of DiscussionTopicsApi->discussion_topics_reorder_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscussionTopicsApi->discussion_topics_reorder_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **discussion_topics_reorder_request** | [**DiscussionTopicsReorderRequest**](DiscussionTopicsReorderRequest.md)| Request body parameters | [optional] 

### Return type

[**DiscussionTopicsReorderResponse**](DiscussionTopicsReorderResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | DiscussionTopicsReorderResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discussion_topics_update**
> DiscussionTopic discussion_topics_update(course_id, topic_id, discussion_topics_update_request=discussion_topics_update_request)

Update a topic

Update an existing discussion topic for the course or group.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.discussion_topic import DiscussionTopic
from canvas_lms_python_client.models.discussion_topics_update_request import DiscussionTopicsUpdateRequest
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
    api_instance = canvas_lms_python_client.DiscussionTopicsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    topic_id = 'topic_id_example' # str | Scope response to topic_id
    discussion_topics_update_request = canvas_lms_python_client.DiscussionTopicsUpdateRequest() # DiscussionTopicsUpdateRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/courses/<course_id>/discussion_topics/<topic_id> \\     -F title='This will be positioned after Topic #1234' \\     -F position_after=1234 \\     -H 'Authorization: Bearer <token>' ``` (optional)

    try:
        # Update a topic
        api_response = await api_instance.discussion_topics_update(course_id, topic_id, discussion_topics_update_request=discussion_topics_update_request)
        print("The response of DiscussionTopicsApi->discussion_topics_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscussionTopicsApi->discussion_topics_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **topic_id** | **str**| Scope response to topic_id | 
 **discussion_topics_update_request** | [**DiscussionTopicsUpdateRequest**](DiscussionTopicsUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/courses/&lt;course_id&gt;/discussion_topics/&lt;topic_id&gt; \\     -F title&#x3D;&#39;This will be positioned after Topic #1234&#39; \\     -F position_after&#x3D;1234 \\     -H &#39;Authorization: Bearer &lt;token&gt;&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**DiscussionTopic**](DiscussionTopic.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | DiscussionTopic |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discussion_topics_update_for_groups**
> DiscussionTopic discussion_topics_update_for_groups(group_id, topic_id, discussion_topics_update_request=discussion_topics_update_request)

Update a topic

Update an existing discussion topic for the course or group.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.discussion_topic import DiscussionTopic
from canvas_lms_python_client.models.discussion_topics_update_request import DiscussionTopicsUpdateRequest
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
    api_instance = canvas_lms_python_client.DiscussionTopicsApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    topic_id = 'topic_id_example' # str | Scope response to topic_id
    discussion_topics_update_request = canvas_lms_python_client.DiscussionTopicsUpdateRequest() # DiscussionTopicsUpdateRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/courses/<course_id>/discussion_topics/<topic_id> \\     -F title='This will be positioned after Topic #1234' \\     -F position_after=1234 \\     -H 'Authorization: Bearer <token>' ``` (optional)

    try:
        # Update a topic
        api_response = await api_instance.discussion_topics_update_for_groups(group_id, topic_id, discussion_topics_update_request=discussion_topics_update_request)
        print("The response of DiscussionTopicsApi->discussion_topics_update_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscussionTopicsApi->discussion_topics_update_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **topic_id** | **str**| Scope response to topic_id | 
 **discussion_topics_update_request** | [**DiscussionTopicsUpdateRequest**](DiscussionTopicsUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/courses/&lt;course_id&gt;/discussion_topics/&lt;topic_id&gt; \\     -F title&#x3D;&#39;This will be positioned after Topic #1234&#39; \\     -F position_after&#x3D;1234 \\     -H &#39;Authorization: Bearer &lt;token&gt;&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**DiscussionTopic**](DiscussionTopic.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | DiscussionTopic |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

