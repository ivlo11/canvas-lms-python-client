# canvas_lms_python_client.AiConversationsApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ai_conversations_active_conversation**](AiConversationsApi.md#ai_conversations_active_conversation) | **GET** /api/v1/courses/{course_id}/ai_experiences/{ai_experience_id}/conversations | Get active conversation
[**ai_conversations_create**](AiConversationsApi.md#ai_conversations_create) | **POST** /api/v1/courses/{course_id}/ai_experiences/{ai_experience_id}/conversations | Create AI conversation
[**ai_conversations_create_feedback**](AiConversationsApi.md#ai_conversations_create_feedback) | **POST** /api/v1/courses/{course_id}/ai_experiences/{ai_experience_id}/conversations/{id}/messages/{message_id}/feedback | Create feedback on a conversation message
[**ai_conversations_delete_feedback**](AiConversationsApi.md#ai_conversations_delete_feedback) | **DELETE** /api/v1/courses/{course_id}/ai_experiences/{ai_experience_id}/conversations/{id}/messages/{message_id}/feedback/{feedback_id} | Delete feedback on a conversation message
[**ai_conversations_destroy**](AiConversationsApi.md#ai_conversations_destroy) | **DELETE** /api/v1/courses/{course_id}/ai_experiences/{ai_experience_id}/conversations/{id} | Delete AI conversation
[**ai_conversations_evaluation**](AiConversationsApi.md#ai_conversations_evaluation) | **GET** /api/v1/courses/{course_id}/ai_experiences/{ai_experience_id}/conversations/{id}/evaluation | Get conversation evaluation
[**ai_conversations_post_message**](AiConversationsApi.md#ai_conversations_post_message) | **POST** /api/v1/courses/{course_id}/ai_experiences/{ai_experience_id}/conversations/{id}/messages | Post message to conversation
[**ai_conversations_show**](AiConversationsApi.md#ai_conversations_show) | **GET** /api/v1/courses/{course_id}/ai_experiences/{ai_experience_id}/conversations/{id} | Show conversation


# **ai_conversations_active_conversation**
> object ai_conversations_active_conversation(ai_experience_id, course_id)

Get active conversation

Get the active conversation for the current user and AI experience

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
    api_instance = canvas_lms_python_client.AiConversationsApi(api_client)
    ai_experience_id = 'ai_experience_id_example' # str | Scope response to ai_experience_id
    course_id = 'course_id_example' # str | Scope response to course_id

    try:
        # Get active conversation
        api_response = await api_instance.ai_conversations_active_conversation(ai_experience_id, course_id)
        print("The response of AiConversationsApi->ai_conversations_active_conversation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AiConversationsApi->ai_conversations_active_conversation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_experience_id** | **str**| Scope response to ai_experience_id | 
 **course_id** | **str**| Scope response to course_id | 

### Return type

**object**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Hash with id and messages array, or empty object if no active conversation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_conversations_create**
> object ai_conversations_create(ai_experience_id, course_id)

Create AI conversation

Initialize a new conversation with the AI experience

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
    api_instance = canvas_lms_python_client.AiConversationsApi(api_client)
    ai_experience_id = 'ai_experience_id_example' # str | Scope response to ai_experience_id
    course_id = 'course_id_example' # str | Scope response to course_id

    try:
        # Create AI conversation
        api_response = await api_instance.ai_conversations_create(ai_experience_id, course_id)
        print("The response of AiConversationsApi->ai_conversations_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AiConversationsApi->ai_conversations_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_experience_id** | **str**| Scope response to ai_experience_id | 
 **course_id** | **str**| Scope response to course_id | 

### Return type

**object**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Hash with conversation_id and initial messages array |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_conversations_create_feedback**
> object ai_conversations_create_feedback(ai_experience_id, course_id, id, message_id, ai_conversations_create_feedback_request=ai_conversations_create_feedback_request)

Create feedback on a conversation message

Submit a like or dislike vote on an AI-generated message.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.ai_conversations_create_feedback_request import AiConversationsCreateFeedbackRequest
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
    api_instance = canvas_lms_python_client.AiConversationsApi(api_client)
    ai_experience_id = 'ai_experience_id_example' # str | Scope response to ai_experience_id
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    message_id = 'message_id_example' # str | llm-conversation message UUID
    ai_conversations_create_feedback_request = canvas_lms_python_client.AiConversationsCreateFeedbackRequest() # AiConversationsCreateFeedbackRequest | Request body parameters (optional)

    try:
        # Create feedback on a conversation message
        api_response = await api_instance.ai_conversations_create_feedback(ai_experience_id, course_id, id, message_id, ai_conversations_create_feedback_request=ai_conversations_create_feedback_request)
        print("The response of AiConversationsApi->ai_conversations_create_feedback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AiConversationsApi->ai_conversations_create_feedback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_experience_id** | **str**| Scope response to ai_experience_id | 
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **message_id** | **str**| llm-conversation message UUID | 
 **ai_conversations_create_feedback_request** | [**AiConversationsCreateFeedbackRequest**](AiConversationsCreateFeedbackRequest.md)| Request body parameters | [optional] 

### Return type

**object**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Hash with feedback record |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_conversations_delete_feedback**
> object ai_conversations_delete_feedback(ai_experience_id, course_id, feedback_id, id, message_id)

Delete feedback on a conversation message

Remove a previously submitted vote (toggling off like/dislike).

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
    api_instance = canvas_lms_python_client.AiConversationsApi(api_client)
    ai_experience_id = 'ai_experience_id_example' # str | Scope response to ai_experience_id
    course_id = 'course_id_example' # str | Scope response to course_id
    feedback_id = 'feedback_id_example' # str | Scope response to feedback_id
    id = 'id_example' # str | Scope response to id
    message_id = 'message_id_example' # str | Scope response to message_id

    try:
        # Delete feedback on a conversation message
        api_response = await api_instance.ai_conversations_delete_feedback(ai_experience_id, course_id, feedback_id, id, message_id)
        print("The response of AiConversationsApi->ai_conversations_delete_feedback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AiConversationsApi->ai_conversations_delete_feedback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_experience_id** | **str**| Scope response to ai_experience_id | 
 **course_id** | **str**| Scope response to course_id | 
 **feedback_id** | **str**| Scope response to feedback_id | 
 **id** | **str**| Scope response to id | 
 **message_id** | **str**| Scope response to message_id | 

### Return type

**object**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Success response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_conversations_destroy**
> object ai_conversations_destroy(ai_experience_id, course_id, id)

Delete AI conversation

Mark a conversation as completed/deleted

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
    api_instance = canvas_lms_python_client.AiConversationsApi(api_client)
    ai_experience_id = 'ai_experience_id_example' # str | Scope response to ai_experience_id
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id

    try:
        # Delete AI conversation
        api_response = await api_instance.ai_conversations_destroy(ai_experience_id, course_id, id)
        print("The response of AiConversationsApi->ai_conversations_destroy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AiConversationsApi->ai_conversations_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_experience_id** | **str**| Scope response to ai_experience_id | 
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 

### Return type

**object**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Success message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_conversations_evaluation**
> object ai_conversations_evaluation(ai_experience_id, course_id, id)

Get conversation evaluation

Fetch evaluation data for a conversation from the llm-conversation service

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
    api_instance = canvas_lms_python_client.AiConversationsApi(api_client)
    ai_experience_id = 'ai_experience_id_example' # str | Scope response to ai_experience_id
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id

    try:
        # Get conversation evaluation
        api_response = await api_instance.ai_conversations_evaluation(ai_experience_id, course_id, id)
        print("The response of AiConversationsApi->ai_conversations_evaluation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AiConversationsApi->ai_conversations_evaluation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_experience_id** | **str**| Scope response to ai_experience_id | 
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 

### Return type

**object**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Hash with evaluation metrics |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_conversations_post_message**
> object ai_conversations_post_message(ai_experience_id, course_id, id, ai_conversations_post_message_request=ai_conversations_post_message_request)

Post message to conversation

Send a message to an existing conversation and get the AI response

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.ai_conversations_post_message_request import AiConversationsPostMessageRequest
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
    api_instance = canvas_lms_python_client.AiConversationsApi(api_client)
    ai_experience_id = 'ai_experience_id_example' # str | Scope response to ai_experience_id
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    ai_conversations_post_message_request = canvas_lms_python_client.AiConversationsPostMessageRequest() # AiConversationsPostMessageRequest | Request body parameters (optional)

    try:
        # Post message to conversation
        api_response = await api_instance.ai_conversations_post_message(ai_experience_id, course_id, id, ai_conversations_post_message_request=ai_conversations_post_message_request)
        print("The response of AiConversationsApi->ai_conversations_post_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AiConversationsApi->ai_conversations_post_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_experience_id** | **str**| Scope response to ai_experience_id | 
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **ai_conversations_post_message_request** | [**AiConversationsPostMessageRequest**](AiConversationsPostMessageRequest.md)| Request body parameters | [optional] 

### Return type

**object**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Hash with id and updated messages array |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_conversations_show**
> object ai_conversations_show(ai_experience_id, course_id, id)

Show conversation

Get a specific conversation by ID (for teachers viewing student conversations)

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
    api_instance = canvas_lms_python_client.AiConversationsApi(api_client)
    ai_experience_id = 'ai_experience_id_example' # str | Scope response to ai_experience_id
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id

    try:
        # Show conversation
        api_response = await api_instance.ai_conversations_show(ai_experience_id, course_id, id)
        print("The response of AiConversationsApi->ai_conversations_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AiConversationsApi->ai_conversations_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_experience_id** | **str**| Scope response to ai_experience_id | 
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 

### Return type

**object**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Hash with conversation details including messages |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

