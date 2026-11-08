# canvas_lms_python_client.ConversationsApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**conversations_add_message**](ConversationsApi.md#conversations_add_message) | **POST** /api/v1/conversations/{id}/add_message | Add a message
[**conversations_add_recipients**](ConversationsApi.md#conversations_add_recipients) | **POST** /api/v1/conversations/{id}/add_recipients | Add recipients
[**conversations_batch_update**](ConversationsApi.md#conversations_batch_update) | **PUT** /api/v1/conversations | Batch update conversations
[**conversations_batches**](ConversationsApi.md#conversations_batches) | **GET** /api/v1/conversations/batches | Get running batches
[**conversations_create**](ConversationsApi.md#conversations_create) | **POST** /api/v1/conversations | Create a conversation
[**conversations_destroy**](ConversationsApi.md#conversations_destroy) | **DELETE** /api/v1/conversations/{id} | Delete a conversation
[**conversations_index**](ConversationsApi.md#conversations_index) | **GET** /api/v1/conversations | List conversations
[**conversations_mark_all_as_read**](ConversationsApi.md#conversations_mark_all_as_read) | **POST** /api/v1/conversations/mark_all_as_read | Mark all as read
[**conversations_remove_messages**](ConversationsApi.md#conversations_remove_messages) | **POST** /api/v1/conversations/{id}/remove_messages | Delete a message
[**conversations_show**](ConversationsApi.md#conversations_show) | **GET** /api/v1/conversations/{id} | Get a single conversation
[**conversations_unread_count**](ConversationsApi.md#conversations_unread_count) | **GET** /api/v1/conversations/unread_count | Unread count
[**conversations_update**](ConversationsApi.md#conversations_update) | **PUT** /api/v1/conversations/{id} | Edit a conversation


# **conversations_add_message**
> conversations_add_message(id, conversations_add_message_request=conversations_add_message_request)

Add a message

Add a message to an existing conversation. Response is similar to the
GET/show action, except that only includes the
latest message (i.e. what we just sent)

An array of user ids. Defaults to all of the current conversation
recipients. To explicitly send a message to no other recipients,
this array should consist of the logged-in user id.

An array of message ids from this conversation to send to recipients
of the new message. Recipients who already had a copy of included
messages will not be affected.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.conversations_add_message_request import ConversationsAddMessageRequest
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
    api_instance = canvas_lms_python_client.ConversationsApi(api_client)
    id = 'id_example' # str | Scope response to id
    conversations_add_message_request = canvas_lms_python_client.ConversationsAddMessageRequest() # ConversationsAddMessageRequest | Request body parameters (optional)

    try:
        # Add a message
        await api_instance.conversations_add_message(id, conversations_add_message_request=conversations_add_message_request)
    except Exception as e:
        print("Exception when calling ConversationsApi->conversations_add_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **conversations_add_message_request** | [**ConversationsAddMessageRequest**](ConversationsAddMessageRequest.md)| Request body parameters | [optional] 

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
**0** | Add a message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **conversations_add_recipients**
> Conversation conversations_add_recipients(id, conversations_add_recipients_request=conversations_add_recipients_request)

Add recipients

Add recipients to an existing group conversation. Response is similar to
the GET/show action, except that only includes the
latest message (e.g. "joe was added to the conversation by bob")

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.conversation import Conversation
from canvas_lms_python_client.models.conversations_add_recipients_request import ConversationsAddRecipientsRequest
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
    api_instance = canvas_lms_python_client.ConversationsApi(api_client)
    id = 'id_example' # str | Scope response to id
    conversations_add_recipients_request = canvas_lms_python_client.ConversationsAddRecipientsRequest() # ConversationsAddRecipientsRequest | Request body parameters (optional)

    try:
        # Add recipients
        api_response = await api_instance.conversations_add_recipients(id, conversations_add_recipients_request=conversations_add_recipients_request)
        print("The response of ConversationsApi->conversations_add_recipients:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationsApi->conversations_add_recipients: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **conversations_add_recipients_request** | [**ConversationsAddRecipientsRequest**](ConversationsAddRecipientsRequest.md)| Request body parameters | [optional] 

### Return type

[**Conversation**](Conversation.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Conversation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **conversations_batch_update**
> Progress conversations_batch_update(conversations_batch_update_request=conversations_batch_update_request)

Batch update conversations

Perform a change on a set of conversations. Operates asynchronously; use the {api:ProgressController#show progress endpoint}
to query the status of an operation.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.conversations_batch_update_request import ConversationsBatchUpdateRequest
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
    api_instance = canvas_lms_python_client.ConversationsApi(api_client)
    conversations_batch_update_request = canvas_lms_python_client.ConversationsBatchUpdateRequest() # ConversationsBatchUpdateRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/conversations \\   -X PUT \\   -H 'Authorization: Bearer <token>' \\   -d 'event=mark_as_read' \\   -d 'conversation_ids[]=1' \\   -d 'conversation_ids[]=2' ``` (optional)

    try:
        # Batch update conversations
        api_response = await api_instance.conversations_batch_update(conversations_batch_update_request=conversations_batch_update_request)
        print("The response of ConversationsApi->conversations_batch_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationsApi->conversations_batch_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversations_batch_update_request** | [**ConversationsBatchUpdateRequest**](ConversationsBatchUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/conversations \\   -X PUT \\   -H &#39;Authorization: Bearer &lt;token&gt;&#39; \\   -d &#39;event&#x3D;mark_as_read&#39; \\   -d &#39;conversation_ids[]&#x3D;1&#39; \\   -d &#39;conversation_ids[]&#x3D;2&#39; &#x60;&#x60;&#x60; | [optional] 

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

# **conversations_batches**
> List[ConversationBatch] conversations_batches(page=page, per_page=per_page)

Get running batches

Returns any currently running conversation batches for the current user.
Conversation batches are created when a bulk private message is sent
asynchronously (see the mode argument to the {api:ConversationsController#create create API action}).

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.conversation_batch import ConversationBatch
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
    api_instance = canvas_lms_python_client.ConversationsApi(api_client)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # Get running batches
        api_response = await api_instance.conversations_batches(page=page, per_page=per_page)
        print("The response of ConversationsApi->conversations_batches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationsApi->conversations_batches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[ConversationBatch]**](ConversationBatch.md)

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

# **conversations_create**
> List[Conversation] conversations_create(conversations_create_request=conversations_create_request)

Create a conversation

Create a new conversation with one or more recipients. If there is already
an existing private conversation with the given recipients, it will be
reused.

 (either numeric IDs or UUIDs prefixed with "uuid:"),
  or course/group ids prefixed with "course_" or "group_" respectively, e.g.
  recipients[]=1&recipients[]=uuid:W9GQIcdoDTqwX8mxIunDQQVL6WZTaGmpa5xovmCBx&recipients[]=course_3.
  If the course/group has over 100 enrollments, 'bulk_message' and 'group_conversation' must be
  set to true.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.conversation import Conversation
from canvas_lms_python_client.models.conversations_create_request import ConversationsCreateRequest
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
    api_instance = canvas_lms_python_client.ConversationsApi(api_client)
    conversations_create_request = canvas_lms_python_client.ConversationsCreateRequest() # ConversationsCreateRequest | Request body parameters (optional)

    try:
        # Create a conversation
        api_response = await api_instance.conversations_create(conversations_create_request=conversations_create_request)
        print("The response of ConversationsApi->conversations_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationsApi->conversations_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversations_create_request** | [**ConversationsCreateRequest**](ConversationsCreateRequest.md)| Request body parameters | [optional] 

### Return type

[**List[Conversation]**](Conversation.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **conversations_destroy**
> Conversation conversations_destroy(id)

Delete a conversation

Delete this conversation and its messages. Note that this only deletes
this user's view of the conversation.

Response includes same fields as UPDATE action

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.conversation import Conversation
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
    api_instance = canvas_lms_python_client.ConversationsApi(api_client)
    id = 'id_example' # str | Scope response to id

    try:
        # Delete a conversation
        api_response = await api_instance.conversations_destroy(id)
        print("The response of ConversationsApi->conversations_destroy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationsApi->conversations_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 

### Return type

[**Conversation**](Conversation.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Conversation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **conversations_index**
> List[Conversation] conversations_index(scope=scope, filter=filter, filter_mode_and_or=filter_mode_and_or, interleave_submissions=interleave_submissions, include_all_conversation_ids=include_all_conversation_ids, include=include, page=page, per_page=per_page)

List conversations

Returns the paginated list of conversations for the current user, most
recent ones first.

 "uuid:W9GQIcdoDTqwX8mxIunDQQVL6WZTaGmpa5xovmCB", or "course_456".
 For users, you can use either their numeric ID or UUID prefixed with "uuid:".
 Can be an array (by setting "filter[]") or single value (by setting "filter")

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.conversation import Conversation
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
    api_instance = canvas_lms_python_client.ConversationsApi(api_client)
    scope = 'scope_example' # str | When set, only return conversations of the specified type. For example, set to \"unread\" to return only conversations that haven't been read. The default behavior is to return all non-archived conversations (i.e. read and unread). (optional)
    filter = ['filter_example'] # List[str] | When set, only return conversations for the specified courses, groups or users. The id should be prefixed with its type, e.g. \"user_123\", (optional)
    filter_mode_and_or = 'filter_mode_and_or_example' # str | When filter[] contains multiple filters, combine them with this mode, filtering conversations that at have at least all of the contexts (\"and\") or at least one of the contexts (\"or\") (optional)
    interleave_submissions = True # bool | (Obsolete) Submissions are no longer linked to conversations. This parameter is ignored. (optional)
    include_all_conversation_ids = True # bool | Default is false. If true, the top-level element of the response will be an object rather than an array, and will have the keys \"conversations\" which will contain the paged conversation data, and \"conversation_ids\" which will contain the ids of all conversations under this scope/filter in the same order. (optional)
    include = ['include_example'] # List[str] | \"participant_avatars\":: Optionally include an \"avatar_url\" key for each user participating in the conversation \"uuid\":: Optionally include an \"uuid\" key for each user participating in the conversation (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List conversations
        api_response = await api_instance.conversations_index(scope=scope, filter=filter, filter_mode_and_or=filter_mode_and_or, interleave_submissions=interleave_submissions, include_all_conversation_ids=include_all_conversation_ids, include=include, page=page, per_page=per_page)
        print("The response of ConversationsApi->conversations_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationsApi->conversations_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| When set, only return conversations of the specified type. For example, set to \&quot;unread\&quot; to return only conversations that haven&#39;t been read. The default behavior is to return all non-archived conversations (i.e. read and unread). | [optional] 
 **filter** | [**List[str]**](str.md)| When set, only return conversations for the specified courses, groups or users. The id should be prefixed with its type, e.g. \&quot;user_123\&quot;, | [optional] 
 **filter_mode_and_or** | **str**| When filter[] contains multiple filters, combine them with this mode, filtering conversations that at have at least all of the contexts (\&quot;and\&quot;) or at least one of the contexts (\&quot;or\&quot;) | [optional] 
 **interleave_submissions** | **bool**| (Obsolete) Submissions are no longer linked to conversations. This parameter is ignored. | [optional] 
 **include_all_conversation_ids** | **bool**| Default is false. If true, the top-level element of the response will be an object rather than an array, and will have the keys \&quot;conversations\&quot; which will contain the paged conversation data, and \&quot;conversation_ids\&quot; which will contain the ids of all conversations under this scope/filter in the same order. | [optional] 
 **include** | [**List[str]**](str.md)| \&quot;participant_avatars\&quot;:: Optionally include an \&quot;avatar_url\&quot; key for each user participating in the conversation \&quot;uuid\&quot;:: Optionally include an \&quot;uuid\&quot; key for each user participating in the conversation | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[Conversation]**](Conversation.md)

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

# **conversations_mark_all_as_read**
> conversations_mark_all_as_read()

Mark all as read

Mark all conversations as read.

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
    api_instance = canvas_lms_python_client.ConversationsApi(api_client)

    try:
        # Mark all as read
        await api_instance.conversations_mark_all_as_read()
    except Exception as e:
        print("Exception when calling ConversationsApi->conversations_mark_all_as_read: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**0** | Mark all as read |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **conversations_remove_messages**
> Conversation conversations_remove_messages(id, conversations_remove_messages_request=conversations_remove_messages_request)

Delete a message

Delete messages from this conversation. Note that this only affects this
user's view of the conversation. If all messages are deleted, the
conversation will be as well (equivalent to DELETE)

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.conversation import Conversation
from canvas_lms_python_client.models.conversations_remove_messages_request import ConversationsRemoveMessagesRequest
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
    api_instance = canvas_lms_python_client.ConversationsApi(api_client)
    id = 'id_example' # str | Scope response to id
    conversations_remove_messages_request = canvas_lms_python_client.ConversationsRemoveMessagesRequest() # ConversationsRemoveMessagesRequest | Request body parameters (optional)

    try:
        # Delete a message
        api_response = await api_instance.conversations_remove_messages(id, conversations_remove_messages_request=conversations_remove_messages_request)
        print("The response of ConversationsApi->conversations_remove_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationsApi->conversations_remove_messages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **conversations_remove_messages_request** | [**ConversationsRemoveMessagesRequest**](ConversationsRemoveMessagesRequest.md)| Request body parameters | [optional] 

### Return type

[**Conversation**](Conversation.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Conversation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **conversations_show**
> Conversation conversations_show(id, interleave_submissions=interleave_submissions, scope=scope, filter=filter, filter_mode_and_or=filter_mode_and_or, auto_mark_as_read=auto_mark_as_read)

Get a single conversation

Returns information for a single conversation for the current user. Response includes all
fields that are present in the list/index action as well as messages
and extended participant information.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.conversation import Conversation
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
    api_instance = canvas_lms_python_client.ConversationsApi(api_client)
    id = 'id_example' # str | Scope response to id
    interleave_submissions = True # bool | (Obsolete) Submissions are no longer linked to conversations. This parameter is ignored. (optional)
    scope = 'scope_example' # str | Used when generating \"visible\" in the API response. See the explanation under the {api:ConversationsController#index index API action} (optional)
    filter = ['filter_example'] # List[str] | Used when generating \"visible\" in the API response. See the explanation under the {api:ConversationsController#index index API action} (optional)
    filter_mode_and_or = 'filter_mode_and_or_example' # str | Used when generating \"visible\" in the API response. See the explanation under the {api:ConversationsController#index index API action} (optional)
    auto_mark_as_read = True # bool | Default true. If true, unread conversations will be automatically marked as read. This will default to false in a future API release, so clients should explicitly send true if that is the desired behavior. (optional)

    try:
        # Get a single conversation
        api_response = await api_instance.conversations_show(id, interleave_submissions=interleave_submissions, scope=scope, filter=filter, filter_mode_and_or=filter_mode_and_or, auto_mark_as_read=auto_mark_as_read)
        print("The response of ConversationsApi->conversations_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationsApi->conversations_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **interleave_submissions** | **bool**| (Obsolete) Submissions are no longer linked to conversations. This parameter is ignored. | [optional] 
 **scope** | **str**| Used when generating \&quot;visible\&quot; in the API response. See the explanation under the {api:ConversationsController#index index API action} | [optional] 
 **filter** | [**List[str]**](str.md)| Used when generating \&quot;visible\&quot; in the API response. See the explanation under the {api:ConversationsController#index index API action} | [optional] 
 **filter_mode_and_or** | **str**| Used when generating \&quot;visible\&quot; in the API response. See the explanation under the {api:ConversationsController#index index API action} | [optional] 
 **auto_mark_as_read** | **bool**| Default true. If true, unread conversations will be automatically marked as read. This will default to false in a future API release, so clients should explicitly send true if that is the desired behavior. | [optional] 

### Return type

[**Conversation**](Conversation.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Conversation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **conversations_unread_count**
> ConversationsUnreadCountResponse conversations_unread_count()

Unread count

Get the number of unread conversations for the current user

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.conversations_unread_count_response import ConversationsUnreadCountResponse
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
    api_instance = canvas_lms_python_client.ConversationsApi(api_client)

    try:
        # Unread count
        api_response = await api_instance.conversations_unread_count()
        print("The response of ConversationsApi->conversations_unread_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationsApi->conversations_unread_count: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ConversationsUnreadCountResponse**](ConversationsUnreadCountResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ConversationsUnreadCountResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **conversations_update**
> Conversation conversations_update(id, conversations_update_request=conversations_update_request)

Edit a conversation

Updates attributes for a single conversation.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.conversation import Conversation
from canvas_lms_python_client.models.conversations_update_request import ConversationsUpdateRequest
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
    api_instance = canvas_lms_python_client.ConversationsApi(api_client)
    id = 'id_example' # str | Scope response to id
    conversations_update_request = canvas_lms_python_client.ConversationsUpdateRequest() # ConversationsUpdateRequest | Request body parameters (optional)

    try:
        # Edit a conversation
        api_response = await api_instance.conversations_update(id, conversations_update_request=conversations_update_request)
        print("The response of ConversationsApi->conversations_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationsApi->conversations_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **conversations_update_request** | [**ConversationsUpdateRequest**](ConversationsUpdateRequest.md)| Request body parameters | [optional] 

### Return type

[**Conversation**](Conversation.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Conversation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

