# canvas_lms_python_client.SearchApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_all_courses**](SearchApi.md#search_all_courses) | **GET** /api/v1/search/all_courses | List all courses
[**search_recipients**](SearchApi.md#search_recipients) | **GET** /api/v1/conversations/find_recipients | Find recipients
[**search_recipients_for_other**](SearchApi.md#search_recipients_for_other) | **GET** /api/v1/search/recipients | Find recipients


# **search_all_courses**
> search_all_courses(search=search, public_only=public_only, open_enrollment_only=open_enrollment_only, page=page, per_page=per_page)

List all courses

A paginated list of all courses visible in the public index

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
    api_instance = canvas_lms_python_client.SearchApi(api_client)
    search = 'search_example' # str | Search terms used for matching users/courses/groups (e.g. \"bob smith\"). If multiple terms are given (separated via whitespace), only results matching all terms will be returned. (optional)
    public_only = True # bool | Only return courses with public content. Defaults to false. (optional)
    open_enrollment_only = True # bool | Only return courses that allow self enrollment. Defaults to false. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List all courses
        await api_instance.search_all_courses(search=search, public_only=public_only, open_enrollment_only=open_enrollment_only, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling SearchApi->search_all_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search terms used for matching users/courses/groups (e.g. \&quot;bob smith\&quot;). If multiple terms are given (separated via whitespace), only results matching all terms will be returned. | [optional] 
 **public_only** | **bool**| Only return courses with public content. Defaults to false. | [optional] 
 **open_enrollment_only** | **bool**| Only return courses that allow self enrollment. Defaults to false. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

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
**0** | List all courses |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_recipients**
> List[Recipient] search_recipients(search=search, context=context, exclude=exclude, type=type, user_id=user_id, from_conversation_id=from_conversation_id, permissions=permissions, page=page, per_page=per_page)

Find recipients

Find valid recipients (users, courses and groups) that the current user
can send messages to. The /api/v1/search/recipients path is the preferred
endpoint, /api/v1/conversations/find_recipients is deprecated.

Pagination is supported.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.recipient import Recipient
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
    api_instance = canvas_lms_python_client.SearchApi(api_client)
    search = 'search_example' # str | Search terms used for matching users/courses/groups (e.g. \"bob smith\"). If multiple terms are given (separated via whitespace), only results matching all terms will be returned. (optional)
    context = 'context_example' # str | Limit the search to a particular course/group (e.g. \"course_3\" or \"group_4\"). (optional)
    exclude = ['exclude_example'] # List[str] | Array of ids to exclude from the search. These may be user ids or course/group ids prefixed with \"course_\" or \"group_\" respectively, e.g. exclude[]=1&exclude[]=2&exclude[]=course_3 (optional)
    type = 'type_example' # str | Limit the search just to users or contexts (groups/courses). (optional)
    user_id = 56 # int | Search for a specific user id. This ignores the other above parameters, and will never return more than one result. (optional)
    from_conversation_id = 56 # int | When searching by user_id, only users that could be normally messaged by this user will be returned. This parameter allows you to specify a conversation that will be referenced for a shared context -- if both the current user and the searched user are in the conversation, the user will be returned. This is used to start new side conversations. (optional)
    permissions = ['permissions_example'] # List[str] | Array of permission strings to be checked for each matched context (e.g. \"send_messages\"). This argument determines which permissions may be returned in the response; it won't prevent contexts from being returned if they don't grant the permission(s). (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # Find recipients
        api_response = await api_instance.search_recipients(search=search, context=context, exclude=exclude, type=type, user_id=user_id, from_conversation_id=from_conversation_id, permissions=permissions, page=page, per_page=per_page)
        print("The response of SearchApi->search_recipients:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_recipients: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search terms used for matching users/courses/groups (e.g. \&quot;bob smith\&quot;). If multiple terms are given (separated via whitespace), only results matching all terms will be returned. | [optional] 
 **context** | **str**| Limit the search to a particular course/group (e.g. \&quot;course_3\&quot; or \&quot;group_4\&quot;). | [optional] 
 **exclude** | [**List[str]**](str.md)| Array of ids to exclude from the search. These may be user ids or course/group ids prefixed with \&quot;course_\&quot; or \&quot;group_\&quot; respectively, e.g. exclude[]&#x3D;1&amp;exclude[]&#x3D;2&amp;exclude[]&#x3D;course_3 | [optional] 
 **type** | **str**| Limit the search just to users or contexts (groups/courses). | [optional] 
 **user_id** | **int**| Search for a specific user id. This ignores the other above parameters, and will never return more than one result. | [optional] 
 **from_conversation_id** | **int**| When searching by user_id, only users that could be normally messaged by this user will be returned. This parameter allows you to specify a conversation that will be referenced for a shared context -- if both the current user and the searched user are in the conversation, the user will be returned. This is used to start new side conversations. | [optional] 
 **permissions** | [**List[str]**](str.md)| Array of permission strings to be checked for each matched context (e.g. \&quot;send_messages\&quot;). This argument determines which permissions may be returned in the response; it won&#39;t prevent contexts from being returned if they don&#39;t grant the permission(s). | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[Recipient]**](Recipient.md)

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

# **search_recipients_for_other**
> List[Recipient] search_recipients_for_other(search=search, context=context, exclude=exclude, type=type, user_id=user_id, from_conversation_id=from_conversation_id, permissions=permissions, page=page, per_page=per_page)

Find recipients

Find valid recipients (users, courses and groups) that the current user
can send messages to. The /api/v1/search/recipients path is the preferred
endpoint, /api/v1/conversations/find_recipients is deprecated.

Pagination is supported.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.recipient import Recipient
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
    api_instance = canvas_lms_python_client.SearchApi(api_client)
    search = 'search_example' # str | Search terms used for matching users/courses/groups (e.g. \"bob smith\"). If multiple terms are given (separated via whitespace), only results matching all terms will be returned. (optional)
    context = 'context_example' # str | Limit the search to a particular course/group (e.g. \"course_3\" or \"group_4\"). (optional)
    exclude = ['exclude_example'] # List[str] | Array of ids to exclude from the search. These may be user ids or course/group ids prefixed with \"course_\" or \"group_\" respectively, e.g. exclude[]=1&exclude[]=2&exclude[]=course_3 (optional)
    type = 'type_example' # str | Limit the search just to users or contexts (groups/courses). (optional)
    user_id = 56 # int | Search for a specific user id. This ignores the other above parameters, and will never return more than one result. (optional)
    from_conversation_id = 56 # int | When searching by user_id, only users that could be normally messaged by this user will be returned. This parameter allows you to specify a conversation that will be referenced for a shared context -- if both the current user and the searched user are in the conversation, the user will be returned. This is used to start new side conversations. (optional)
    permissions = ['permissions_example'] # List[str] | Array of permission strings to be checked for each matched context (e.g. \"send_messages\"). This argument determines which permissions may be returned in the response; it won't prevent contexts from being returned if they don't grant the permission(s). (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # Find recipients
        api_response = await api_instance.search_recipients_for_other(search=search, context=context, exclude=exclude, type=type, user_id=user_id, from_conversation_id=from_conversation_id, permissions=permissions, page=page, per_page=per_page)
        print("The response of SearchApi->search_recipients_for_other:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_recipients_for_other: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search terms used for matching users/courses/groups (e.g. \&quot;bob smith\&quot;). If multiple terms are given (separated via whitespace), only results matching all terms will be returned. | [optional] 
 **context** | **str**| Limit the search to a particular course/group (e.g. \&quot;course_3\&quot; or \&quot;group_4\&quot;). | [optional] 
 **exclude** | [**List[str]**](str.md)| Array of ids to exclude from the search. These may be user ids or course/group ids prefixed with \&quot;course_\&quot; or \&quot;group_\&quot; respectively, e.g. exclude[]&#x3D;1&amp;exclude[]&#x3D;2&amp;exclude[]&#x3D;course_3 | [optional] 
 **type** | **str**| Limit the search just to users or contexts (groups/courses). | [optional] 
 **user_id** | **int**| Search for a specific user id. This ignores the other above parameters, and will never return more than one result. | [optional] 
 **from_conversation_id** | **int**| When searching by user_id, only users that could be normally messaged by this user will be returned. This parameter allows you to specify a conversation that will be referenced for a shared context -- if both the current user and the searched user are in the conversation, the user will be returned. This is used to start new side conversations. | [optional] 
 **permissions** | [**List[str]**](str.md)| Array of permission strings to be checked for each matched context (e.g. \&quot;send_messages\&quot;). This argument determines which permissions may be returned in the response; it won&#39;t prevent contexts from being returned if they don&#39;t grant the permission(s). | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[Recipient]**](Recipient.md)

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

