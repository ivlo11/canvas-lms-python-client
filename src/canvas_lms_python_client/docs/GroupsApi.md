# canvas_lms_python_client.GroupsApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**groups_activity_stream**](GroupsApi.md#groups_activity_stream) | **GET** /api/v1/groups/{group_id}/activity_stream | Group activity stream
[**groups_activity_stream_summary**](GroupsApi.md#groups_activity_stream_summary) | **GET** /api/v1/groups/{group_id}/activity_stream/summary | Group activity stream summary
[**groups_bulk_user_tags**](GroupsApi.md#groups_bulk_user_tags) | **GET** /api/v1/courses/{course_id}/bulk_user_tags | Bulk fetch user tags for multiple users in a course
[**groups_context_index**](GroupsApi.md#groups_context_index) | **GET** /api/v1/accounts/{account_id}/groups | List the groups available in a context.
[**groups_context_index_for_courses**](GroupsApi.md#groups_context_index_for_courses) | **GET** /api/v1/courses/{course_id}/groups | List the groups available in a context.
[**groups_create_file**](GroupsApi.md#groups_create_file) | **POST** /api/v1/groups/{group_id}/files | Upload a file
[**groups_create_for_group_categories**](GroupsApi.md#groups_create_for_group_categories) | **POST** /api/v1/group_categories/{group_category_id}/groups | Create a group
[**groups_create_for_other**](GroupsApi.md#groups_create_for_other) | **POST** /api/v1/groups | Create a group
[**groups_destroy_for_other**](GroupsApi.md#groups_destroy_for_other) | **DELETE** /api/v1/groups/{group_id} | Delete a group
[**groups_index**](GroupsApi.md#groups_index) | **GET** /api/v1/users/self/groups | List your groups
[**groups_invite**](GroupsApi.md#groups_invite) | **POST** /api/v1/groups/{group_id}/invite | Invite others to a group
[**groups_permissions**](GroupsApi.md#groups_permissions) | **GET** /api/v1/groups/{group_id}/permissions | Permissions
[**groups_preview_html**](GroupsApi.md#groups_preview_html) | **POST** /api/v1/groups/{group_id}/preview_html | Preview processed html
[**groups_show_for_other**](GroupsApi.md#groups_show_for_other) | **GET** /api/v1/groups/{group_id} | Get a single group
[**groups_update**](GroupsApi.md#groups_update) | **PUT** /api/v1/groups/{group_id} | Edit a group
[**groups_users**](GroupsApi.md#groups_users) | **GET** /api/v1/groups/{group_id}/users | List group&#39;s users


# **groups_activity_stream**
> List[GroupsActivityStreamResponse] groups_activity_stream(group_id, page=page, per_page=per_page)

Group activity stream

Returns the current user's group-specific activity stream, paginated.

For full documentation, see the API documentation for the user activity
stream, in the user api.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.groups_activity_stream_response import GroupsActivityStreamResponse
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
    api_instance = canvas_lms_python_client.GroupsApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # Group activity stream
        api_response = await api_instance.groups_activity_stream(group_id, page=page, per_page=per_page)
        print("The response of GroupsApi->groups_activity_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->groups_activity_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[GroupsActivityStreamResponse]**](GroupsActivityStreamResponse.md)

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

# **groups_activity_stream_summary**
> List[GroupsActivityStreamSummaryResponse] groups_activity_stream_summary(group_id)

Group activity stream summary

Returns a summary of the current user's group-specific activity stream.

For full documentation, see the API documentation for the user activity
stream summary, in the user api.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.groups_activity_stream_summary_response import GroupsActivityStreamSummaryResponse
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
    api_instance = canvas_lms_python_client.GroupsApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id

    try:
        # Group activity stream summary
        api_response = await api_instance.groups_activity_stream_summary(group_id)
        print("The response of GroupsApi->groups_activity_stream_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->groups_activity_stream_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 

### Return type

[**List[GroupsActivityStreamSummaryResponse]**](GroupsActivityStreamSummaryResponse.md)

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

# **groups_bulk_user_tags**
> object groups_bulk_user_tags(course_id, user_ids=user_ids)

Bulk fetch user tags for multiple users in a course

Returns a mapping of user IDs to arrays of non-collaborative group (tag) IDs for each user in the given course.

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
    api_instance = canvas_lms_python_client.GroupsApi(api_client)
    course_id = 'course_id_example' # str | The ID of the course context (from the route).
    user_ids = [56] # List[int] | An array of user IDs to fetch tags for. (optional)

    try:
        # Bulk fetch user tags for multiple users in a course
        api_response = await api_instance.groups_bulk_user_tags(course_id, user_ids=user_ids)
        print("The response of GroupsApi->groups_bulk_user_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->groups_bulk_user_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| The ID of the course context (from the route). | 
 **user_ids** | [**List[int]**](int.md)| An array of user IDs to fetch tags for. | [optional] 

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
**0** | Hash A mapping of user IDs to arrays of tag (group) IDs. Example:   {     \&quot;35\&quot;: [5],     \&quot;79\&quot;: [3, 4, 5]   } |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_context_index**
> List[Group] groups_context_index(account_id, only_own_groups=only_own_groups, include=include, collaboration_state=collaboration_state, page=page, per_page=per_page)

List the groups available in a context.

Returns the paginated list of active groups in the given context that are visible to user.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.group import Group
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
    api_instance = canvas_lms_python_client.GroupsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    only_own_groups = True # bool | Will only include groups that the user belongs to if this is set (optional)
    include = ['include_example'] # List[str] | - \"tabs\": Include the list of tabs configured for each group.  See the   {api:TabsController#index List available tabs API} for more information. (optional)
    collaboration_state = 'collaboration_state_example' # str | Filter groups by their collaboration state: - \"all\": Return both collaborative and non-collaborative groups - \"collaborative\": Return only collaborative groups (default) - \"non_collaborative\": Return only non-collaborative groups (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List the groups available in a context.
        api_response = await api_instance.groups_context_index(account_id, only_own_groups=only_own_groups, include=include, collaboration_state=collaboration_state, page=page, per_page=per_page)
        print("The response of GroupsApi->groups_context_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->groups_context_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **only_own_groups** | **bool**| Will only include groups that the user belongs to if this is set | [optional] 
 **include** | [**List[str]**](str.md)| - \&quot;tabs\&quot;: Include the list of tabs configured for each group.  See the   {api:TabsController#index List available tabs API} for more information. | [optional] 
 **collaboration_state** | **str**| Filter groups by their collaboration state: - \&quot;all\&quot;: Return both collaborative and non-collaborative groups - \&quot;collaborative\&quot;: Return only collaborative groups (default) - \&quot;non_collaborative\&quot;: Return only non-collaborative groups | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[Group]**](Group.md)

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

# **groups_context_index_for_courses**
> List[Group] groups_context_index_for_courses(course_id, only_own_groups=only_own_groups, include=include, collaboration_state=collaboration_state, page=page, per_page=per_page)

List the groups available in a context.

Returns the paginated list of active groups in the given context that are visible to user.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.group import Group
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
    api_instance = canvas_lms_python_client.GroupsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    only_own_groups = True # bool | Will only include groups that the user belongs to if this is set (optional)
    include = ['include_example'] # List[str] | - \"tabs\": Include the list of tabs configured for each group.  See the   {api:TabsController#index List available tabs API} for more information. (optional)
    collaboration_state = 'collaboration_state_example' # str | Filter groups by their collaboration state: - \"all\": Return both collaborative and non-collaborative groups - \"collaborative\": Return only collaborative groups (default) - \"non_collaborative\": Return only non-collaborative groups (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List the groups available in a context.
        api_response = await api_instance.groups_context_index_for_courses(course_id, only_own_groups=only_own_groups, include=include, collaboration_state=collaboration_state, page=page, per_page=per_page)
        print("The response of GroupsApi->groups_context_index_for_courses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->groups_context_index_for_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **only_own_groups** | **bool**| Will only include groups that the user belongs to if this is set | [optional] 
 **include** | [**List[str]**](str.md)| - \&quot;tabs\&quot;: Include the list of tabs configured for each group.  See the   {api:TabsController#index List available tabs API} for more information. | [optional] 
 **collaboration_state** | **str**| Filter groups by their collaboration state: - \&quot;all\&quot;: Return both collaborative and non-collaborative groups - \&quot;collaborative\&quot;: Return only collaborative groups (default) - \&quot;non_collaborative\&quot;: Return only non-collaborative groups | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[Group]**](Group.md)

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

# **groups_create_file**
> GroupsCreateFileResponse groups_create_file(group_id)

Upload a file

Upload a file to the group.

This API endpoint is the first step in uploading a file to a group.
See the {file:file.file_uploads.html File Upload Documentation} for details on
the file upload workflow.

Only those with the "Manage Files" permission on a group can upload files
to the group. By default, this is anybody participating in the
group, or any admin over the group.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.groups_create_file_response import GroupsCreateFileResponse
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
    api_instance = canvas_lms_python_client.GroupsApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id

    try:
        # Upload a file
        api_response = await api_instance.groups_create_file(group_id)
        print("The response of GroupsApi->groups_create_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->groups_create_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 

### Return type

[**GroupsCreateFileResponse**](GroupsCreateFileResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | GroupsCreateFileResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_create_for_group_categories**
> Group groups_create_for_group_categories(group_category_id, groups_create_for_group_categories_request=groups_create_for_group_categories_request)

Create a group

Creates a new group. Groups created using the "/api/v1/groups/"
endpoint will be community groups.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.group import Group
from canvas_lms_python_client.models.groups_create_for_group_categories_request import GroupsCreateForGroupCategoriesRequest
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
    api_instance = canvas_lms_python_client.GroupsApi(api_client)
    group_category_id = 'group_category_id_example' # str | Scope response to group_category_id
    groups_create_for_group_categories_request = canvas_lms_python_client.GroupsCreateForGroupCategoriesRequest() # GroupsCreateForGroupCategoriesRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/groups \\      -F 'name=Math Teachers' \\      -F 'description=A place to gather resources for our classes.' \\      -F 'is_public=true' \\      -F 'join_level=parent_context_auto_join' \\      -H 'Authorization: Bearer <token>' ``` (optional)

    try:
        # Create a group
        api_response = await api_instance.groups_create_for_group_categories(group_category_id, groups_create_for_group_categories_request=groups_create_for_group_categories_request)
        print("The response of GroupsApi->groups_create_for_group_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->groups_create_for_group_categories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_category_id** | **str**| Scope response to group_category_id | 
 **groups_create_for_group_categories_request** | [**GroupsCreateForGroupCategoriesRequest**](GroupsCreateForGroupCategoriesRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/groups \\      -F &#39;name&#x3D;Math Teachers&#39; \\      -F &#39;description&#x3D;A place to gather resources for our classes.&#39; \\      -F &#39;is_public&#x3D;true&#39; \\      -F &#39;join_level&#x3D;parent_context_auto_join&#39; \\      -H &#39;Authorization: Bearer &lt;token&gt;&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**Group**](Group.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Group |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_create_for_other**
> Group groups_create_for_other(groups_create_for_group_categories_request=groups_create_for_group_categories_request)

Create a group

Creates a new group. Groups created using the "/api/v1/groups/"
endpoint will be community groups.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.group import Group
from canvas_lms_python_client.models.groups_create_for_group_categories_request import GroupsCreateForGroupCategoriesRequest
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
    api_instance = canvas_lms_python_client.GroupsApi(api_client)
    groups_create_for_group_categories_request = canvas_lms_python_client.GroupsCreateForGroupCategoriesRequest() # GroupsCreateForGroupCategoriesRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/groups \\      -F 'name=Math Teachers' \\      -F 'description=A place to gather resources for our classes.' \\      -F 'is_public=true' \\      -F 'join_level=parent_context_auto_join' \\      -H 'Authorization: Bearer <token>' ``` (optional)

    try:
        # Create a group
        api_response = await api_instance.groups_create_for_other(groups_create_for_group_categories_request=groups_create_for_group_categories_request)
        print("The response of GroupsApi->groups_create_for_other:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->groups_create_for_other: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groups_create_for_group_categories_request** | [**GroupsCreateForGroupCategoriesRequest**](GroupsCreateForGroupCategoriesRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/groups \\      -F &#39;name&#x3D;Math Teachers&#39; \\      -F &#39;description&#x3D;A place to gather resources for our classes.&#39; \\      -F &#39;is_public&#x3D;true&#39; \\      -F &#39;join_level&#x3D;parent_context_auto_join&#39; \\      -H &#39;Authorization: Bearer &lt;token&gt;&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**Group**](Group.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Group |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_destroy_for_other**
> Group groups_destroy_for_other(group_id)

Delete a group

Deletes a group and removes all members.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.group import Group
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
    api_instance = canvas_lms_python_client.GroupsApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id

    try:
        # Delete a group
        api_response = await api_instance.groups_destroy_for_other(group_id)
        print("The response of GroupsApi->groups_destroy_for_other:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->groups_destroy_for_other: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 

### Return type

[**Group**](Group.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Group |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_index**
> List[Group] groups_index(context_type=context_type, include=include, page=page, per_page=per_page)

List your groups

Returns a paginated list of active groups for the current user.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.group import Group
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
    api_instance = canvas_lms_python_client.GroupsApi(api_client)
    context_type = 'context_type_example' # str | Only include groups that are in this type of context. (optional)
    include = ['include_example'] # List[str] | - \"tabs\": Include the list of tabs configured for each group.  See the   {api:TabsController#index List available tabs API} for more information. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List your groups
        api_response = await api_instance.groups_index(context_type=context_type, include=include, page=page, per_page=per_page)
        print("The response of GroupsApi->groups_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->groups_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context_type** | **str**| Only include groups that are in this type of context. | [optional] 
 **include** | [**List[str]**](str.md)| - \&quot;tabs\&quot;: Include the list of tabs configured for each group.  See the   {api:TabsController#index List available tabs API} for more information. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[Group]**](Group.md)

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

# **groups_invite**
> List[GroupMembership] groups_invite(group_id, groups_invite_request=groups_invite_request)

Invite others to a group

Sends an invitation to all supplied email addresses which will allow the
receivers to join the group.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.group_membership import GroupMembership
from canvas_lms_python_client.models.groups_invite_request import GroupsInviteRequest
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
    api_instance = canvas_lms_python_client.GroupsApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    groups_invite_request = canvas_lms_python_client.GroupsInviteRequest() # GroupsInviteRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/groups/<group_id>/invite \\      -F 'invitees[]=leonard@example.com' \\      -F 'invitees[]=sheldon@example.com' \\      -H 'Authorization: Bearer <token>' ``` (optional)

    try:
        # Invite others to a group
        api_response = await api_instance.groups_invite(group_id, groups_invite_request=groups_invite_request)
        print("The response of GroupsApi->groups_invite:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->groups_invite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **groups_invite_request** | [**GroupsInviteRequest**](GroupsInviteRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/groups/&lt;group_id&gt;/invite \\      -F &#39;invitees[]&#x3D;leonard@example.com&#39; \\      -F &#39;invitees[]&#x3D;sheldon@example.com&#39; \\      -H &#39;Authorization: Bearer &lt;token&gt;&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**List[GroupMembership]**](GroupMembership.md)

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

# **groups_permissions**
> GroupsPermissionsResponse groups_permissions(group_id, permissions=permissions)

Permissions

Returns permission information for the calling user in the given group.
See also the {api:AccountsController#permissions Account} and
{api:CoursesController#permissions Course} counterparts.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.groups_permissions_response import GroupsPermissionsResponse
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
    api_instance = canvas_lms_python_client.GroupsApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    permissions = ['permissions_example'] # List[str] | List of permissions to check against the authenticated user. Permission names are documented in the {api:RoleOverridesController#manageable_permissions List assignable permissions} endpoint. (optional)

    try:
        # Permissions
        api_response = await api_instance.groups_permissions(group_id, permissions=permissions)
        print("The response of GroupsApi->groups_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->groups_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **permissions** | [**List[str]**](str.md)| List of permissions to check against the authenticated user. Permission names are documented in the {api:RoleOverridesController#manageable_permissions List assignable permissions} endpoint. | [optional] 

### Return type

[**GroupsPermissionsResponse**](GroupsPermissionsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | GroupsPermissionsResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_preview_html**
> GroupsPreviewHtmlResponse groups_preview_html(group_id, courses_preview_html_request=courses_preview_html_request)

Preview processed html

Preview html content processed for this group

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.courses_preview_html_request import CoursesPreviewHtmlRequest
from canvas_lms_python_client.models.groups_preview_html_response import GroupsPreviewHtmlResponse
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
    api_instance = canvas_lms_python_client.GroupsApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    courses_preview_html_request = canvas_lms_python_client.CoursesPreviewHtmlRequest() # CoursesPreviewHtmlRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/groups/<group_id>/preview_html \\      -F 'html=<p><badhtml></badhtml>processed html</p>' \\      -H 'Authorization: Bearer <token>' ``` (optional)

    try:
        # Preview processed html
        api_response = await api_instance.groups_preview_html(group_id, courses_preview_html_request=courses_preview_html_request)
        print("The response of GroupsApi->groups_preview_html:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->groups_preview_html: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **courses_preview_html_request** | [**CoursesPreviewHtmlRequest**](CoursesPreviewHtmlRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/groups/&lt;group_id&gt;/preview_html \\      -F &#39;html&#x3D;&lt;p&gt;&lt;badhtml&gt;&lt;/badhtml&gt;processed html&lt;/p&gt;&#39; \\      -H &#39;Authorization: Bearer &lt;token&gt;&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**GroupsPreviewHtmlResponse**](GroupsPreviewHtmlResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | GroupsPreviewHtmlResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_show_for_other**
> Group groups_show_for_other(group_id, include=include)

Get a single group

Returns the data for a single group, or a 401 if the caller doesn't have
the rights to see it.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.group import Group
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
    api_instance = canvas_lms_python_client.GroupsApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    include = ['include_example'] # List[str] | - \"permissions\": Include permissions the current user has   for the group. - \"tabs\": Include the list of tabs configured for each group.  See the   {api:TabsController#index List available tabs API} for more information. (optional)

    try:
        # Get a single group
        api_response = await api_instance.groups_show_for_other(group_id, include=include)
        print("The response of GroupsApi->groups_show_for_other:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->groups_show_for_other: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **include** | [**List[str]**](str.md)| - \&quot;permissions\&quot;: Include permissions the current user has   for the group. - \&quot;tabs\&quot;: Include the list of tabs configured for each group.  See the   {api:TabsController#index List available tabs API} for more information. | [optional] 

### Return type

[**Group**](Group.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Group |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_update**
> Group groups_update(group_id, groups_update_request=groups_update_request)

Edit a group

Modifies an existing group.  Note that to set an avatar image for the
group, you must first upload the image file to the group, and the use the
id in the response as the argument to this function.  See the
{file:file.file_uploads.html File Upload Documentation} for details on the file
upload workflow.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.group import Group
from canvas_lms_python_client.models.groups_update_request import GroupsUpdateRequest
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
    api_instance = canvas_lms_python_client.GroupsApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    groups_update_request = canvas_lms_python_client.GroupsUpdateRequest() # GroupsUpdateRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/groups/<group_id> \\      -X PUT \\      -F 'name=Algebra Teachers' \\      -F 'join_level=parent_context_request' \\      -H 'Authorization: Bearer <token>' ``` (optional)

    try:
        # Edit a group
        api_response = await api_instance.groups_update(group_id, groups_update_request=groups_update_request)
        print("The response of GroupsApi->groups_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->groups_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **groups_update_request** | [**GroupsUpdateRequest**](GroupsUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/groups/&lt;group_id&gt; \\      -X PUT \\      -F &#39;name&#x3D;Algebra Teachers&#39; \\      -F &#39;join_level&#x3D;parent_context_request&#39; \\      -H &#39;Authorization: Bearer &lt;token&gt;&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**Group**](Group.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Group |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_users**
> List[User] groups_users(group_id, search_term=search_term, include=include, exclude_inactive=exclude_inactive, page=page, per_page=per_page)

List group's users

Returns a paginated list of users in the group.

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
    api_instance = canvas_lms_python_client.GroupsApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    search_term = 'search_term_example' # str | The partial name or full ID of the users to match and return in the results list. Must be at least 2 characters. (optional)
    include = ['include_example'] # List[str] | \"avatar_url\": Include users' avatar_urls. (optional)
    exclude_inactive = True # bool | Whether to filter out inactive users from the results. Defaults to false unless explicitly provided. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List group's users
        api_response = await api_instance.groups_users(group_id, search_term=search_term, include=include, exclude_inactive=exclude_inactive, page=page, per_page=per_page)
        print("The response of GroupsApi->groups_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->groups_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **search_term** | **str**| The partial name or full ID of the users to match and return in the results list. Must be at least 2 characters. | [optional] 
 **include** | [**List[str]**](str.md)| \&quot;avatar_url\&quot;: Include users&#39; avatar_urls. | [optional] 
 **exclude_inactive** | **bool**| Whether to filter out inactive users from the results. Defaults to false unless explicitly provided. | [optional] 
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

