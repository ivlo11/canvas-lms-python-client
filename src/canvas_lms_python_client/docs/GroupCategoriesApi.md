# canvas_lms_python_client.GroupCategoriesApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**group_categories_assign_unassigned_members**](GroupCategoriesApi.md#group_categories_assign_unassigned_members) | **POST** /api/v1/group_categories/{group_category_id}/assign_unassigned_members | Assign unassigned members
[**group_categories_bulk_manage_differentiation_tag**](GroupCategoriesApi.md#group_categories_bulk_manage_differentiation_tag) | **POST** /api/v1/courses/{course_id}/group_categories/bulk_manage_differentiation_tag | Bulk manage differentiation tags
[**group_categories_create**](GroupCategoriesApi.md#group_categories_create) | **POST** /api/v1/accounts/{account_id}/group_categories | Create a Group Category
[**group_categories_create_for_courses**](GroupCategoriesApi.md#group_categories_create_for_courses) | **POST** /api/v1/courses/{course_id}/group_categories | Create a Group Category
[**group_categories_destroy**](GroupCategoriesApi.md#group_categories_destroy) | **DELETE** /api/v1/group_categories/{group_category_id} | Delete a Group Category
[**group_categories_export**](GroupCategoriesApi.md#group_categories_export) | **GET** /api/v1/group_categories/{group_category_id}/export | export groups in and users in category
[**group_categories_export_tags**](GroupCategoriesApi.md#group_categories_export_tags) | **GET** /api/v1/courses/{course_id}/group_categories/export_tags | export tags and users in course
[**group_categories_groups**](GroupCategoriesApi.md#group_categories_groups) | **GET** /api/v1/group_categories/{group_category_id}/groups | List groups in group category
[**group_categories_import**](GroupCategoriesApi.md#group_categories_import) | **POST** /api/v1/group_categories/{group_category_id}/import | Import category groups
[**group_categories_import_tags**](GroupCategoriesApi.md#group_categories_import_tags) | **POST** /api/v1/courses/{course_id}/group_categories/import_tags | Import differentiation tags
[**group_categories_index**](GroupCategoriesApi.md#group_categories_index) | **GET** /api/v1/accounts/{account_id}/group_categories | List group categories for a context
[**group_categories_index_for_courses**](GroupCategoriesApi.md#group_categories_index_for_courses) | **GET** /api/v1/courses/{course_id}/group_categories | List group categories for a context
[**group_categories_show**](GroupCategoriesApi.md#group_categories_show) | **GET** /api/v1/group_categories/{group_category_id} | Get a single group category
[**group_categories_update**](GroupCategoriesApi.md#group_categories_update) | **PUT** /api/v1/group_categories/{group_category_id} | Update a Group Category
[**group_categories_users**](GroupCategoriesApi.md#group_categories_users) | **GET** /api/v1/group_categories/{group_category_id}/users | List users in group category


# **group_categories_assign_unassigned_members**
> object group_categories_assign_unassigned_members(group_category_id, group_categories_assign_unassigned_members_request=group_categories_assign_unassigned_members_request)

Assign unassigned members

Assign all unassigned members as evenly as possible among the existing
student groups.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.group_categories_assign_unassigned_members_request import GroupCategoriesAssignUnassignedMembersRequest
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
    api_instance = canvas_lms_python_client.GroupCategoriesApi(api_client)
    group_category_id = 'group_category_id_example' # str | Scope response to group_category_id
    group_categories_assign_unassigned_members_request = canvas_lms_python_client.GroupCategoriesAssignUnassignedMembersRequest() # GroupCategoriesAssignUnassignedMembersRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/group_categories/1/assign_unassigned_members \\      -H 'Authorization: Bearer <token>' ``` (optional)

    try:
        # Assign unassigned members
        api_response = await api_instance.group_categories_assign_unassigned_members(group_category_id, group_categories_assign_unassigned_members_request=group_categories_assign_unassigned_members_request)
        print("The response of GroupCategoriesApi->group_categories_assign_unassigned_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupCategoriesApi->group_categories_assign_unassigned_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_category_id** | **str**| Scope response to group_category_id | 
 **group_categories_assign_unassigned_members_request** | [**GroupCategoriesAssignUnassignedMembersRequest**](GroupCategoriesAssignUnassignedMembersRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/group_categories/1/assign_unassigned_members \\      -H &#39;Authorization: Bearer &lt;token&gt;&#39; &#x60;&#x60;&#x60; | [optional] 

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
**0** | GroupMembership | Progress |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_categories_bulk_manage_differentiation_tag**
> object group_categories_bulk_manage_differentiation_tag(course_id, group_categories_bulk_manage_differentiation_tag_request=group_categories_bulk_manage_differentiation_tag_request)

Bulk manage differentiation tags

This API is only meant for Groups and GroupCategories where non_collaborative is true.

Perform bulk operations on groups within a group category, or create a new group category
along with the groups in one transaction. If creation of the GroupCategory or any Group fails, the entire operation will be rolled back.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.group_categories_bulk_manage_differentiation_tag_request import GroupCategoriesBulkManageDifferentiationTagRequest
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
    api_instance = canvas_lms_python_client.GroupCategoriesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    group_categories_bulk_manage_differentiation_tag_request = canvas_lms_python_client.GroupCategoriesBulkManageDifferentiationTagRequest() # GroupCategoriesBulkManageDifferentiationTagRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/courses/:course_id/group_categories/bulk_manage_differentiation_tag \\      -X POST \\      -H 'Authorization: Bearer <token>' \\      -H 'Content-Type: application/json' \\      -d '{            \"operations\": {              \"create\": [{\"name\": \"New Group\"}],              \"update\": [{\"id\": 123, \"name\": \"Updated Group\"}],              \"delete\": [{\"id\": 456}]            },            \"group_category\": {\"id\": 1, \"name\": \"New Category Name\"}          }' ``` (optional)

    try:
        # Bulk manage differentiation tags
        api_response = await api_instance.group_categories_bulk_manage_differentiation_tag(course_id, group_categories_bulk_manage_differentiation_tag_request=group_categories_bulk_manage_differentiation_tag_request)
        print("The response of GroupCategoriesApi->group_categories_bulk_manage_differentiation_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupCategoriesApi->group_categories_bulk_manage_differentiation_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **group_categories_bulk_manage_differentiation_tag_request** | [**GroupCategoriesBulkManageDifferentiationTagRequest**](GroupCategoriesBulkManageDifferentiationTagRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/courses/:course_id/group_categories/bulk_manage_differentiation_tag \\      -X POST \\      -H &#39;Authorization: Bearer &lt;token&gt;&#39; \\      -H &#39;Content-Type: application/json&#39; \\      -d &#39;{            \&quot;operations\&quot;: {              \&quot;create\&quot;: [{\&quot;name\&quot;: \&quot;New Group\&quot;}],              \&quot;update\&quot;: [{\&quot;id\&quot;: 123, \&quot;name\&quot;: \&quot;Updated Group\&quot;}],              \&quot;delete\&quot;: [{\&quot;id\&quot;: 456}]            },            \&quot;group_category\&quot;: {\&quot;id\&quot;: 1, \&quot;name\&quot;: \&quot;New Category Name\&quot;}          }&#39; &#x60;&#x60;&#x60; | [optional] 

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
**0** | GroupCategory and groups operation results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_categories_create**
> GroupCategory group_categories_create(account_id, group_categories_create_request=group_categories_create_request)

Create a Group Category

Create a new group category

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.group_categories_create_request import GroupCategoriesCreateRequest
from canvas_lms_python_client.models.group_category import GroupCategory
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
    api_instance = canvas_lms_python_client.GroupCategoriesApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    group_categories_create_request = canvas_lms_python_client.GroupCategoriesCreateRequest() # GroupCategoriesCreateRequest | Request body parameters  **Example Request:** ``` curl htps://<canvas>/api/v1/courses/<course_id>/group_categories \\     -F 'name=Project Groups' \\     -H 'Authorization: Bearer <token>' ``` (optional)

    try:
        # Create a Group Category
        api_response = await api_instance.group_categories_create(account_id, group_categories_create_request=group_categories_create_request)
        print("The response of GroupCategoriesApi->group_categories_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupCategoriesApi->group_categories_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **group_categories_create_request** | [**GroupCategoriesCreateRequest**](GroupCategoriesCreateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl htps://&lt;canvas&gt;/api/v1/courses/&lt;course_id&gt;/group_categories \\     -F &#39;name&#x3D;Project Groups&#39; \\     -H &#39;Authorization: Bearer &lt;token&gt;&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**GroupCategory**](GroupCategory.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | GroupCategory |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_categories_create_for_courses**
> GroupCategory group_categories_create_for_courses(course_id, group_categories_create_request=group_categories_create_request)

Create a Group Category

Create a new group category

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.group_categories_create_request import GroupCategoriesCreateRequest
from canvas_lms_python_client.models.group_category import GroupCategory
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
    api_instance = canvas_lms_python_client.GroupCategoriesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    group_categories_create_request = canvas_lms_python_client.GroupCategoriesCreateRequest() # GroupCategoriesCreateRequest | Request body parameters  **Example Request:** ``` curl htps://<canvas>/api/v1/courses/<course_id>/group_categories \\     -F 'name=Project Groups' \\     -H 'Authorization: Bearer <token>' ``` (optional)

    try:
        # Create a Group Category
        api_response = await api_instance.group_categories_create_for_courses(course_id, group_categories_create_request=group_categories_create_request)
        print("The response of GroupCategoriesApi->group_categories_create_for_courses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupCategoriesApi->group_categories_create_for_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **group_categories_create_request** | [**GroupCategoriesCreateRequest**](GroupCategoriesCreateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl htps://&lt;canvas&gt;/api/v1/courses/&lt;course_id&gt;/group_categories \\     -F &#39;name&#x3D;Project Groups&#39; \\     -H &#39;Authorization: Bearer &lt;token&gt;&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**GroupCategory**](GroupCategory.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | GroupCategory |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_categories_destroy**
> group_categories_destroy(group_category_id)

Delete a Group Category

Deletes a group category and all groups under it. Protected group
categories can not be deleted, i.e. "communities" and "student_organized".

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
    api_instance = canvas_lms_python_client.GroupCategoriesApi(api_client)
    group_category_id = 'group_category_id_example' # str | Scope response to group_category_id

    try:
        # Delete a Group Category
        await api_instance.group_categories_destroy(group_category_id)
    except Exception as e:
        print("Exception when calling GroupCategoriesApi->group_categories_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_category_id** | **str**| Scope response to group_category_id | 

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
**0** | Delete a Group Category |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_categories_export**
> group_categories_export(group_category_id)

export groups in and users in category

Returns a csv file of users in format ready to import.

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
    api_instance = canvas_lms_python_client.GroupCategoriesApi(api_client)
    group_category_id = 'group_category_id_example' # str | Scope response to group_category_id

    try:
        # export groups in and users in category
        await api_instance.group_categories_export(group_category_id)
    except Exception as e:
        print("Exception when calling GroupCategoriesApi->group_categories_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_category_id** | **str**| Scope response to group_category_id | 

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
**0** | export groups in and users in category |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_categories_export_tags**
> group_categories_export_tags(course_id)

export tags and users in course

Returns a csv file of users in format ready to import.

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
    api_instance = canvas_lms_python_client.GroupCategoriesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id

    try:
        # export tags and users in course
        await api_instance.group_categories_export_tags(course_id)
    except Exception as e:
        print("Exception when calling GroupCategoriesApi->group_categories_export_tags: %s\n" % e)
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
**0** | export tags and users in course |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_categories_groups**
> List[Group] group_categories_groups(group_category_id, page=page, per_page=per_page)

List groups in group category

Returns a paginated list of groups in a group category

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
    api_instance = canvas_lms_python_client.GroupCategoriesApi(api_client)
    group_category_id = 'group_category_id_example' # str | Scope response to group_category_id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List groups in group category
        api_response = await api_instance.group_categories_groups(group_category_id, page=page, per_page=per_page)
        print("The response of GroupCategoriesApi->group_categories_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupCategoriesApi->group_categories_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_category_id** | **str**| Scope response to group_category_id | 
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

# **group_categories_import**
> Progress group_categories_import(group_category_id, group_categories_import_request=group_categories_import_request)

Import category groups

Create Groups in a Group Category through a CSV import

For more information on the format that's expected here, please see the
"Group Category CSV" section in the API docs.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.group_categories_import_request import GroupCategoriesImportRequest
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
    api_instance = canvas_lms_python_client.GroupCategoriesApi(api_client)
    group_category_id = 'group_category_id_example' # str | Scope response to group_category_id
    group_categories_import_request = canvas_lms_python_client.GroupCategoriesImportRequest() # GroupCategoriesImportRequest | Request body parameters (optional)

    try:
        # Import category groups
        api_response = await api_instance.group_categories_import(group_category_id, group_categories_import_request=group_categories_import_request)
        print("The response of GroupCategoriesApi->group_categories_import:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupCategoriesApi->group_categories_import: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_category_id** | **str**| Scope response to group_category_id | 
 **group_categories_import_request** | [**GroupCategoriesImportRequest**](GroupCategoriesImportRequest.md)| Request body parameters | [optional] 

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

# **group_categories_import_tags**
> Progress group_categories_import_tags(course_id, group_categories_import_tags_request=group_categories_import_tags_request)

Import differentiation tags

Create Differentiation Tags through a CSV import

For more information on the format that's expected here, please see the
"Differentiation Tag CSV" section in the API docs.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.group_categories_import_tags_request import GroupCategoriesImportTagsRequest
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
    api_instance = canvas_lms_python_client.GroupCategoriesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    group_categories_import_tags_request = canvas_lms_python_client.GroupCategoriesImportTagsRequest() # GroupCategoriesImportTagsRequest | Request body parameters (optional)

    try:
        # Import differentiation tags
        api_response = await api_instance.group_categories_import_tags(course_id, group_categories_import_tags_request=group_categories_import_tags_request)
        print("The response of GroupCategoriesApi->group_categories_import_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupCategoriesApi->group_categories_import_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **group_categories_import_tags_request** | [**GroupCategoriesImportTagsRequest**](GroupCategoriesImportTagsRequest.md)| Request body parameters | [optional] 

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

# **group_categories_index**
> List[GroupCategory] group_categories_index(account_id, collaboration_state=collaboration_state, page=page, per_page=per_page)

List group categories for a context

Returns a paginated list of group categories in a context. The list returned
depends on the permissions of the current user and the specified collaboration state.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.group_category import GroupCategory
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
    api_instance = canvas_lms_python_client.GroupCategoriesApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    collaboration_state = 'collaboration_state_example' # str | Filter group categories by their collaboration state: - \"all\": Return both collaborative and non-collaborative group categories - \"collaborative\": Return only collaborative group categories (default) - \"non_collaborative\": Return only non-collaborative group categories (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List group categories for a context
        api_response = await api_instance.group_categories_index(account_id, collaboration_state=collaboration_state, page=page, per_page=per_page)
        print("The response of GroupCategoriesApi->group_categories_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupCategoriesApi->group_categories_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **collaboration_state** | **str**| Filter group categories by their collaboration state: - \&quot;all\&quot;: Return both collaborative and non-collaborative group categories - \&quot;collaborative\&quot;: Return only collaborative group categories (default) - \&quot;non_collaborative\&quot;: Return only non-collaborative group categories | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[GroupCategory]**](GroupCategory.md)

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

# **group_categories_index_for_courses**
> List[GroupCategory] group_categories_index_for_courses(course_id, collaboration_state=collaboration_state, page=page, per_page=per_page)

List group categories for a context

Returns a paginated list of group categories in a context. The list returned
depends on the permissions of the current user and the specified collaboration state.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.group_category import GroupCategory
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
    api_instance = canvas_lms_python_client.GroupCategoriesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    collaboration_state = 'collaboration_state_example' # str | Filter group categories by their collaboration state: - \"all\": Return both collaborative and non-collaborative group categories - \"collaborative\": Return only collaborative group categories (default) - \"non_collaborative\": Return only non-collaborative group categories (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List group categories for a context
        api_response = await api_instance.group_categories_index_for_courses(course_id, collaboration_state=collaboration_state, page=page, per_page=per_page)
        print("The response of GroupCategoriesApi->group_categories_index_for_courses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupCategoriesApi->group_categories_index_for_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **collaboration_state** | **str**| Filter group categories by their collaboration state: - \&quot;all\&quot;: Return both collaborative and non-collaborative group categories - \&quot;collaborative\&quot;: Return only collaborative group categories (default) - \&quot;non_collaborative\&quot;: Return only non-collaborative group categories | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[GroupCategory]**](GroupCategory.md)

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

# **group_categories_show**
> GroupCategory group_categories_show(group_category_id)

Get a single group category

Returns the data for a single group category, or a 401 if the caller doesn't have
the rights to see it.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.group_category import GroupCategory
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
    api_instance = canvas_lms_python_client.GroupCategoriesApi(api_client)
    group_category_id = 'group_category_id_example' # str | Scope response to group_category_id

    try:
        # Get a single group category
        api_response = await api_instance.group_categories_show(group_category_id)
        print("The response of GroupCategoriesApi->group_categories_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupCategoriesApi->group_categories_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_category_id** | **str**| Scope response to group_category_id | 

### Return type

[**GroupCategory**](GroupCategory.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | GroupCategory |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_categories_update**
> GroupCategory group_categories_update(group_category_id, group_categories_update_request=group_categories_update_request)

Update a Group Category

Modifies an existing group category.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.group_categories_update_request import GroupCategoriesUpdateRequest
from canvas_lms_python_client.models.group_category import GroupCategory
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
    api_instance = canvas_lms_python_client.GroupCategoriesApi(api_client)
    group_category_id = 'group_category_id_example' # str | Scope response to group_category_id
    group_categories_update_request = canvas_lms_python_client.GroupCategoriesUpdateRequest() # GroupCategoriesUpdateRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/group_categories/<group_category_id> \\     -X PUT \\     -F 'name=Project Groups' \\     -H 'Authorization: Bearer <token>' ``` (optional)

    try:
        # Update a Group Category
        api_response = await api_instance.group_categories_update(group_category_id, group_categories_update_request=group_categories_update_request)
        print("The response of GroupCategoriesApi->group_categories_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupCategoriesApi->group_categories_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_category_id** | **str**| Scope response to group_category_id | 
 **group_categories_update_request** | [**GroupCategoriesUpdateRequest**](GroupCategoriesUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/group_categories/&lt;group_category_id&gt; \\     -X PUT \\     -F &#39;name&#x3D;Project Groups&#39; \\     -H &#39;Authorization: Bearer &lt;token&gt;&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**GroupCategory**](GroupCategory.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | GroupCategory |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_categories_users**
> List[User] group_categories_users(group_category_id, search_term=search_term, unassigned=unassigned, page=page, per_page=per_page)

List users in group category

Returns a paginated list of users in the group category.

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
    api_instance = canvas_lms_python_client.GroupCategoriesApi(api_client)
    group_category_id = 'group_category_id_example' # str | Scope response to group_category_id
    search_term = 'search_term_example' # str | The partial name or full ID of the users to match and return in the results list. Must be at least 3 characters. (optional)
    unassigned = True # bool | Set this value to true if you wish only to search unassigned users in the group category. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List users in group category
        api_response = await api_instance.group_categories_users(group_category_id, search_term=search_term, unassigned=unassigned, page=page, per_page=per_page)
        print("The response of GroupCategoriesApi->group_categories_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupCategoriesApi->group_categories_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_category_id** | **str**| Scope response to group_category_id | 
 **search_term** | **str**| The partial name or full ID of the users to match and return in the results list. Must be at least 3 characters. | [optional] 
 **unassigned** | **bool**| Set this value to true if you wish only to search unassigned users in the group category. | [optional] 
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

