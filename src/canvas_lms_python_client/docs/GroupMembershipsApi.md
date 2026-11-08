# canvas_lms_python_client.GroupMembershipsApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**group_memberships_create**](GroupMembershipsApi.md#group_memberships_create) | **POST** /api/v1/groups/{group_id}/memberships | Create a membership
[**group_memberships_destroy**](GroupMembershipsApi.md#group_memberships_destroy) | **DELETE** /api/v1/groups/{group_id}/memberships/{membership_id} | Leave a group
[**group_memberships_destroy_bulk**](GroupMembershipsApi.md#group_memberships_destroy_bulk) | **DELETE** /api/v1/groups/{group_id}/users | Bulk delete memberships
[**group_memberships_destroy_for_groups**](GroupMembershipsApi.md#group_memberships_destroy_for_groups) | **DELETE** /api/v1/groups/{group_id}/users/{user_id} | Leave a group
[**group_memberships_index**](GroupMembershipsApi.md#group_memberships_index) | **GET** /api/v1/groups/{group_id}/memberships | List group memberships
[**group_memberships_show**](GroupMembershipsApi.md#group_memberships_show) | **GET** /api/v1/groups/{group_id}/memberships/{membership_id} | Get a single group membership
[**group_memberships_show_for_groups**](GroupMembershipsApi.md#group_memberships_show_for_groups) | **GET** /api/v1/groups/{group_id}/users/{user_id} | Get a single group membership
[**group_memberships_update**](GroupMembershipsApi.md#group_memberships_update) | **PUT** /api/v1/groups/{group_id}/memberships/{membership_id} | Update a membership
[**group_memberships_update_for_groups**](GroupMembershipsApi.md#group_memberships_update_for_groups) | **PUT** /api/v1/groups/{group_id}/users/{user_id} | Update a membership


# **group_memberships_create**
> object group_memberships_create(group_id, group_memberships_create_request=group_memberships_create_request)

Create a membership

Join, or request to join, a group, depending on the join_level of the
group. If the membership or join request already exists, then it is simply
returned.

For differentiation tags, you can bulk add users using one of two methods:

1. Provide an array of user IDs via the `members[]` parameter.

2. Use the course-wide option with the following parameters:
   - `all_in_group_course` [Boolean]: If set to true, the endpoint will add
     every currently enrolled student (from the course context) to the
     differentiation tag.
   - `exclude_user_ids[]` [Integer]: When using `all_in_group_course`, you can
     optionally exclude specific users by providing their IDs in this parameter.

In this context, these parameters only apply to differentiation tag memberships.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.group_memberships_create_request import GroupMembershipsCreateRequest
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
    api_instance = canvas_lms_python_client.GroupMembershipsApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    group_memberships_create_request = canvas_lms_python_client.GroupMembershipsCreateRequest() # GroupMembershipsCreateRequest | Request body parameters  **Example Request:** ``` (Individual membership creation) curl https://<canvas>/api/v1/groups/<group_id>/memberships \\      -F 'user_id=self' \\      -H 'Authorization: Bearer <token>' ``` (optional)

    try:
        # Create a membership
        api_response = await api_instance.group_memberships_create(group_id, group_memberships_create_request=group_memberships_create_request)
        print("The response of GroupMembershipsApi->group_memberships_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupMembershipsApi->group_memberships_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **group_memberships_create_request** | [**GroupMembershipsCreateRequest**](GroupMembershipsCreateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; (Individual membership creation) curl https://&lt;canvas&gt;/api/v1/groups/&lt;group_id&gt;/memberships \\      -F &#39;user_id&#x3D;self&#39; \\      -H &#39;Authorization: Bearer &lt;token&gt;&#39; &#x60;&#x60;&#x60; | [optional] 

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
**0** | GroupMembership or a JSON response detailing partial failures if some memberships could not be created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_memberships_destroy**
> GroupMembershipsDestroyResponse group_memberships_destroy(group_id, membership_id)

Leave a group

Leave a group if you are allowed to leave (some groups, such as sets of
course groups created by teachers, cannot be left). You may also use 'self'
in place of a membership_id.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.group_memberships_destroy_response import GroupMembershipsDestroyResponse
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
    api_instance = canvas_lms_python_client.GroupMembershipsApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    membership_id = 'membership_id_example' # str | Scope response to membership_id

    try:
        # Leave a group
        api_response = await api_instance.group_memberships_destroy(group_id, membership_id)
        print("The response of GroupMembershipsApi->group_memberships_destroy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupMembershipsApi->group_memberships_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **membership_id** | **str**| Scope response to membership_id | 

### Return type

[**GroupMembershipsDestroyResponse**](GroupMembershipsDestroyResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | GroupMembershipsDestroyResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_memberships_destroy_bulk**
> object group_memberships_destroy_bulk(group_id, user_ids=user_ids)

Bulk delete memberships

Bulk deletes memberships by providing an array of user IDs.

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
    api_instance = canvas_lms_python_client.GroupMembershipsApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    user_ids = [56] # List[int] | - An array of user IDs to delete memberships in bulk. (optional)

    try:
        # Bulk delete memberships
        api_response = await api_instance.group_memberships_destroy_bulk(group_id, user_ids=user_ids)
        print("The response of GroupMembershipsApi->group_memberships_destroy_bulk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupMembershipsApi->group_memberships_destroy_bulk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **user_ids** | [**List[int]**](int.md)| - An array of user IDs to delete memberships in bulk. | [optional] 

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
**0** | JSON - For single deletion: &#x60;{ \&quot;ok\&quot;: true }&#x60; - For bulk deletion:   &#x60;&#x60;&#x60;json   {     \&quot;message\&quot;: \&quot;Bulk delete completed\&quot;,     \&quot;deleted_user_ids\&quot;: [123, 456],     \&quot;unauthorized_user_ids\&quot;: [789]   } |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_memberships_destroy_for_groups**
> GroupMembershipsDestroyResponse group_memberships_destroy_for_groups(group_id, user_id)

Leave a group

Leave a group if you are allowed to leave (some groups, such as sets of
course groups created by teachers, cannot be left). You may also use 'self'
in place of a membership_id.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.group_memberships_destroy_response import GroupMembershipsDestroyResponse
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
    api_instance = canvas_lms_python_client.GroupMembershipsApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # Leave a group
        api_response = await api_instance.group_memberships_destroy_for_groups(group_id, user_id)
        print("The response of GroupMembershipsApi->group_memberships_destroy_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupMembershipsApi->group_memberships_destroy_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **user_id** | **str**| Scope response to user_id | 

### Return type

[**GroupMembershipsDestroyResponse**](GroupMembershipsDestroyResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | GroupMembershipsDestroyResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_memberships_index**
> List[GroupMembership] group_memberships_index(group_id, filter_states=filter_states, page=page, per_page=per_page)

List group memberships

A paginated list of the members of a group.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.group_membership import GroupMembership
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
    api_instance = canvas_lms_python_client.GroupMembershipsApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    filter_states = ['filter_states_example'] # List[str] | Only list memberships with the given workflow_states. By default it will return all memberships. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List group memberships
        api_response = await api_instance.group_memberships_index(group_id, filter_states=filter_states, page=page, per_page=per_page)
        print("The response of GroupMembershipsApi->group_memberships_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupMembershipsApi->group_memberships_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **filter_states** | [**List[str]**](str.md)| Only list memberships with the given workflow_states. By default it will return all memberships. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[GroupMembership]**](GroupMembership.md)

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

# **group_memberships_show**
> GroupMembership group_memberships_show(group_id, membership_id)

Get a single group membership

Returns the group membership with the given membership id or user id.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.group_membership import GroupMembership
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
    api_instance = canvas_lms_python_client.GroupMembershipsApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    membership_id = 'membership_id_example' # str | Scope response to membership_id

    try:
        # Get a single group membership
        api_response = await api_instance.group_memberships_show(group_id, membership_id)
        print("The response of GroupMembershipsApi->group_memberships_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupMembershipsApi->group_memberships_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **membership_id** | **str**| Scope response to membership_id | 

### Return type

[**GroupMembership**](GroupMembership.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | GroupMembership |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_memberships_show_for_groups**
> GroupMembership group_memberships_show_for_groups(group_id, user_id)

Get a single group membership

Returns the group membership with the given membership id or user id.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.group_membership import GroupMembership
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
    api_instance = canvas_lms_python_client.GroupMembershipsApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # Get a single group membership
        api_response = await api_instance.group_memberships_show_for_groups(group_id, user_id)
        print("The response of GroupMembershipsApi->group_memberships_show_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupMembershipsApi->group_memberships_show_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **user_id** | **str**| Scope response to user_id | 

### Return type

[**GroupMembership**](GroupMembership.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | GroupMembership |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_memberships_update**
> GroupMembership group_memberships_update(group_id, membership_id, group_memberships_update_request=group_memberships_update_request)

Update a membership

Accept a membership request, or add/remove moderator rights.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.group_membership import GroupMembership
from canvas_lms_python_client.models.group_memberships_update_request import GroupMembershipsUpdateRequest
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
    api_instance = canvas_lms_python_client.GroupMembershipsApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    membership_id = 'membership_id_example' # str | Scope response to membership_id
    group_memberships_update_request = canvas_lms_python_client.GroupMembershipsUpdateRequest() # GroupMembershipsUpdateRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/groups/<group_id>/memberships/<membership_id> \\      -F 'moderator=true'      -H 'Authorization: Bearer <token>' ``` (optional)

    try:
        # Update a membership
        api_response = await api_instance.group_memberships_update(group_id, membership_id, group_memberships_update_request=group_memberships_update_request)
        print("The response of GroupMembershipsApi->group_memberships_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupMembershipsApi->group_memberships_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **membership_id** | **str**| Scope response to membership_id | 
 **group_memberships_update_request** | [**GroupMembershipsUpdateRequest**](GroupMembershipsUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/groups/&lt;group_id&gt;/memberships/&lt;membership_id&gt; \\      -F &#39;moderator&#x3D;true&#39;      -H &#39;Authorization: Bearer &lt;token&gt;&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**GroupMembership**](GroupMembership.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | GroupMembership |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_memberships_update_for_groups**
> GroupMembership group_memberships_update_for_groups(group_id, user_id, group_memberships_update_request=group_memberships_update_request)

Update a membership

Accept a membership request, or add/remove moderator rights.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.group_membership import GroupMembership
from canvas_lms_python_client.models.group_memberships_update_request import GroupMembershipsUpdateRequest
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
    api_instance = canvas_lms_python_client.GroupMembershipsApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    user_id = 'user_id_example' # str | Scope response to user_id
    group_memberships_update_request = canvas_lms_python_client.GroupMembershipsUpdateRequest() # GroupMembershipsUpdateRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/groups/<group_id>/memberships/<membership_id> \\      -F 'moderator=true'      -H 'Authorization: Bearer <token>' ``` (optional)

    try:
        # Update a membership
        api_response = await api_instance.group_memberships_update_for_groups(group_id, user_id, group_memberships_update_request=group_memberships_update_request)
        print("The response of GroupMembershipsApi->group_memberships_update_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupMembershipsApi->group_memberships_update_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **user_id** | **str**| Scope response to user_id | 
 **group_memberships_update_request** | [**GroupMembershipsUpdateRequest**](GroupMembershipsUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/groups/&lt;group_id&gt;/memberships/&lt;membership_id&gt; \\      -F &#39;moderator&#x3D;true&#39;      -H &#39;Authorization: Bearer &lt;token&gt;&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**GroupMembership**](GroupMembership.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | GroupMembership |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

