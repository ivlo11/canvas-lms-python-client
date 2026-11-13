# canvas_lms_python_client.AiExperiencesApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ai_experiences_ai_conversation_show**](AiExperiencesApi.md#ai_experiences_ai_conversation_show) | **GET** /api/v1/courses/{course_id}/ai_experiences/{id}/ai_conversations/{conversation_id} | Show student AI conversation
[**ai_experiences_ai_conversations_index**](AiExperiencesApi.md#ai_experiences_ai_conversations_index) | **GET** /api/v1/courses/{course_id}/ai_experiences/{id}/ai_conversations | List student AI conversations
[**ai_experiences_create**](AiExperiencesApi.md#ai_experiences_create) | **POST** /api/v1/courses/{course_id}/ai_experiences | Create an AI experience
[**ai_experiences_destroy**](AiExperiencesApi.md#ai_experiences_destroy) | **DELETE** /api/v1/courses/{course_id}/ai_experiences/{id} | Delete an AI experience
[**ai_experiences_edit**](AiExperiencesApi.md#ai_experiences_edit) | **GET** /api/v1/courses/{course_id}/ai_experiences/{id}/edit | Show edit AI experience form
[**ai_experiences_index**](AiExperiencesApi.md#ai_experiences_index) | **GET** /api/v1/courses/{course_id}/ai_experiences | List AI experiences
[**ai_experiences_new**](AiExperiencesApi.md#ai_experiences_new) | **GET** /api/v1/courses/{course_id}/ai_experiences/new | Show new AI experience form
[**ai_experiences_show**](AiExperiencesApi.md#ai_experiences_show) | **GET** /api/v1/courses/{course_id}/ai_experiences/{id} | Show an AI experience
[**ai_experiences_update**](AiExperiencesApi.md#ai_experiences_update) | **PUT** /api/v1/courses/{course_id}/ai_experiences/{id} | Update an AI experience


# **ai_experiences_ai_conversation_show**
> AiExperiencesAiConversationShowResponse ai_experiences_ai_conversation_show(conversation_id, course_id, id)

Show student AI conversation

Retrieve a specific student's AI conversation with full message history.
Only available to teachers and course managers.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.ai_experiences_ai_conversation_show_response import AiExperiencesAiConversationShowResponse
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
    api_instance = canvas_lms_python_client.AiExperiencesApi(api_client)
    conversation_id = 'conversation_id_example' # str | Scope response to conversation_id
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id

    try:
        # Show student AI conversation
        api_response = await api_instance.ai_experiences_ai_conversation_show(conversation_id, course_id, id)
        print("The response of AiExperiencesApi->ai_experiences_ai_conversation_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AiExperiencesApi->ai_experiences_ai_conversation_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_id** | **str**| Scope response to conversation_id | 
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**AiExperiencesAiConversationShowResponse**](AiExperiencesAiConversationShowResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | AiExperiencesAiConversationShowResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_experiences_ai_conversations_index**
> AiConversation ai_experiences_ai_conversations_index(course_id, id)

List student AI conversations

Retrieve the latest AI conversation for each student in the course for this AI experience.
Only available to teachers and course managers.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.ai_conversation import AiConversation
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
    api_instance = canvas_lms_python_client.AiExperiencesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id

    try:
        # List student AI conversations
        api_response = await api_instance.ai_experiences_ai_conversations_index(course_id, id)
        print("The response of AiExperiencesApi->ai_experiences_ai_conversations_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AiExperiencesApi->ai_experiences_ai_conversations_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**AiConversation**](AiConversation.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | AiConversation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_experiences_create**
> AiExperience ai_experiences_create(course_id, ai_experiences_create_request=ai_experiences_create_request)

Create an AI experience

Create a new AI experience for the specified course

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.ai_experience import AiExperience
from canvas_lms_python_client.models.ai_experiences_create_request import AiExperiencesCreateRequest
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
    api_instance = canvas_lms_python_client.AiExperiencesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    ai_experiences_create_request = canvas_lms_python_client.AiExperiencesCreateRequest() # AiExperiencesCreateRequest | Request body parameters (optional)

    try:
        # Create an AI experience
        api_response = await api_instance.ai_experiences_create(course_id, ai_experiences_create_request=ai_experiences_create_request)
        print("The response of AiExperiencesApi->ai_experiences_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AiExperiencesApi->ai_experiences_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **ai_experiences_create_request** | [**AiExperiencesCreateRequest**](AiExperiencesCreateRequest.md)| Request body parameters | [optional] 

### Return type

[**AiExperience**](AiExperience.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | AiExperience |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_experiences_destroy**
> AiExperience ai_experiences_destroy(course_id, id)

Delete an AI experience

Delete an AI experience (soft delete - marks as deleted)

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.ai_experience import AiExperience
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
    api_instance = canvas_lms_python_client.AiExperiencesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id

    try:
        # Delete an AI experience
        api_response = await api_instance.ai_experiences_destroy(course_id, id)
        print("The response of AiExperiencesApi->ai_experiences_destroy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AiExperiencesApi->ai_experiences_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**AiExperience**](AiExperience.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | AiExperience |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_experiences_edit**
> ai_experiences_edit(course_id, id)

Show edit AI experience form

Display the form for editing an existing AI experience

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
    api_instance = canvas_lms_python_client.AiExperiencesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id

    try:
        # Show edit AI experience form
        await api_instance.ai_experiences_edit(course_id, id)
    except Exception as e:
        print("Exception when calling AiExperiencesApi->ai_experiences_edit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 

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
**0** | Show edit AI experience form |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_experiences_index**
> AiExperiencesIndexResponse ai_experiences_index(course_id, workflow_state=workflow_state)

List AI experiences

Retrieve the paginated list of AI experiences for a course

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.ai_experiences_index_response import AiExperiencesIndexResponse
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
    api_instance = canvas_lms_python_client.AiExperiencesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    workflow_state = 'workflow_state_example' # str | Only return experiences with the specified workflow state. Allowed values: published, unpublished, deleted (optional)

    try:
        # List AI experiences
        api_response = await api_instance.ai_experiences_index(course_id, workflow_state=workflow_state)
        print("The response of AiExperiencesApi->ai_experiences_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AiExperiencesApi->ai_experiences_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **workflow_state** | **str**| Only return experiences with the specified workflow state. Allowed values: published, unpublished, deleted | [optional] 

### Return type

[**AiExperiencesIndexResponse**](AiExperiencesIndexResponse.md)

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

# **ai_experiences_new**
> ai_experiences_new(course_id)

Show new AI experience form

Display the form for creating a new AI experience

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
    api_instance = canvas_lms_python_client.AiExperiencesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id

    try:
        # Show new AI experience form
        await api_instance.ai_experiences_new(course_id)
    except Exception as e:
        print("Exception when calling AiExperiencesApi->ai_experiences_new: %s\n" % e)
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
**0** | Show new AI experience form |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_experiences_show**
> AiExperience ai_experiences_show(course_id, id)

Show an AI experience

Retrieve an AI experience by ID

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.ai_experience import AiExperience
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
    api_instance = canvas_lms_python_client.AiExperiencesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id

    try:
        # Show an AI experience
        api_response = await api_instance.ai_experiences_show(course_id, id)
        print("The response of AiExperiencesApi->ai_experiences_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AiExperiencesApi->ai_experiences_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**AiExperience**](AiExperience.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | AiExperience |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_experiences_update**
> AiExperience ai_experiences_update(course_id, id, ai_experiences_update_request=ai_experiences_update_request)

Update an AI experience

Update an existing AI experience

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.ai_experience import AiExperience
from canvas_lms_python_client.models.ai_experiences_update_request import AiExperiencesUpdateRequest
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
    api_instance = canvas_lms_python_client.AiExperiencesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    ai_experiences_update_request = canvas_lms_python_client.AiExperiencesUpdateRequest() # AiExperiencesUpdateRequest | Request body parameters (optional)

    try:
        # Update an AI experience
        api_response = await api_instance.ai_experiences_update(course_id, id, ai_experiences_update_request=ai_experiences_update_request)
        print("The response of AiExperiencesApi->ai_experiences_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AiExperiencesApi->ai_experiences_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **ai_experiences_update_request** | [**AiExperiencesUpdateRequest**](AiExperiencesUpdateRequest.md)| Request body parameters | [optional] 

### Return type

[**AiExperience**](AiExperience.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | AiExperience |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

