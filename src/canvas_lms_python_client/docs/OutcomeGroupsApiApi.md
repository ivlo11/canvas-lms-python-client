# canvas_lms_python_client.OutcomeGroupsApiApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**outcome_groups_api_create**](OutcomeGroupsApiApi.md#outcome_groups_api_create) | **POST** /api/v1/global/outcome_groups/{id}/subgroups | Create a subgroup
[**outcome_groups_api_create_for_accounts**](OutcomeGroupsApiApi.md#outcome_groups_api_create_for_accounts) | **POST** /api/v1/accounts/{account_id}/outcome_groups/{id}/subgroups | Create a subgroup
[**outcome_groups_api_create_for_courses**](OutcomeGroupsApiApi.md#outcome_groups_api_create_for_courses) | **POST** /api/v1/courses/{course_id}/outcome_groups/{id}/subgroups | Create a subgroup
[**outcome_groups_api_destroy**](OutcomeGroupsApiApi.md#outcome_groups_api_destroy) | **DELETE** /api/v1/global/outcome_groups/{id} | Delete an outcome group
[**outcome_groups_api_destroy_for_accounts**](OutcomeGroupsApiApi.md#outcome_groups_api_destroy_for_accounts) | **DELETE** /api/v1/accounts/{account_id}/outcome_groups/{id} | Delete an outcome group
[**outcome_groups_api_destroy_for_courses**](OutcomeGroupsApiApi.md#outcome_groups_api_destroy_for_courses) | **DELETE** /api/v1/courses/{course_id}/outcome_groups/{id} | Delete an outcome group
[**outcome_groups_api_import**](OutcomeGroupsApiApi.md#outcome_groups_api_import) | **POST** /api/v1/global/outcome_groups/{id}/import | Import an outcome group
[**outcome_groups_api_import_for_accounts**](OutcomeGroupsApiApi.md#outcome_groups_api_import_for_accounts) | **POST** /api/v1/accounts/{account_id}/outcome_groups/{id}/import | Import an outcome group
[**outcome_groups_api_import_for_courses**](OutcomeGroupsApiApi.md#outcome_groups_api_import_for_courses) | **POST** /api/v1/courses/{course_id}/outcome_groups/{id}/import | Import an outcome group
[**outcome_groups_api_index**](OutcomeGroupsApiApi.md#outcome_groups_api_index) | **GET** /api/v1/accounts/{account_id}/outcome_groups | Get all outcome groups for context
[**outcome_groups_api_index_for_courses**](OutcomeGroupsApiApi.md#outcome_groups_api_index_for_courses) | **GET** /api/v1/courses/{course_id}/outcome_groups | Get all outcome groups for context
[**outcome_groups_api_link**](OutcomeGroupsApiApi.md#outcome_groups_api_link) | **POST** /api/v1/global/outcome_groups/{id}/outcomes | Create/link an outcome
[**outcome_groups_api_link_by_outcome_id_for_accounts**](OutcomeGroupsApiApi.md#outcome_groups_api_link_by_outcome_id_for_accounts) | **PUT** /api/v1/accounts/{account_id}/outcome_groups/{id}/outcomes/{outcome_id} | Create/link an outcome
[**outcome_groups_api_link_by_outcome_id_for_courses**](OutcomeGroupsApiApi.md#outcome_groups_api_link_by_outcome_id_for_courses) | **PUT** /api/v1/courses/{course_id}/outcome_groups/{id}/outcomes/{outcome_id} | Create/link an outcome
[**outcome_groups_api_link_for_accounts**](OutcomeGroupsApiApi.md#outcome_groups_api_link_for_accounts) | **POST** /api/v1/accounts/{account_id}/outcome_groups/{id}/outcomes | Create/link an outcome
[**outcome_groups_api_link_for_courses**](OutcomeGroupsApiApi.md#outcome_groups_api_link_for_courses) | **POST** /api/v1/courses/{course_id}/outcome_groups/{id}/outcomes | Create/link an outcome
[**outcome_groups_api_link_for_other**](OutcomeGroupsApiApi.md#outcome_groups_api_link_for_other) | **PUT** /api/v1/global/outcome_groups/{id}/outcomes/{outcome_id} | Create/link an outcome
[**outcome_groups_api_link_index**](OutcomeGroupsApiApi.md#outcome_groups_api_link_index) | **GET** /api/v1/accounts/{account_id}/outcome_group_links | Get all outcome links for context
[**outcome_groups_api_link_index_for_courses**](OutcomeGroupsApiApi.md#outcome_groups_api_link_index_for_courses) | **GET** /api/v1/courses/{course_id}/outcome_group_links | Get all outcome links for context
[**outcome_groups_api_outcomes**](OutcomeGroupsApiApi.md#outcome_groups_api_outcomes) | **GET** /api/v1/global/outcome_groups/{id}/outcomes | List linked outcomes
[**outcome_groups_api_outcomes_for_accounts**](OutcomeGroupsApiApi.md#outcome_groups_api_outcomes_for_accounts) | **GET** /api/v1/accounts/{account_id}/outcome_groups/{id}/outcomes | List linked outcomes
[**outcome_groups_api_outcomes_for_courses**](OutcomeGroupsApiApi.md#outcome_groups_api_outcomes_for_courses) | **GET** /api/v1/courses/{course_id}/outcome_groups/{id}/outcomes | List linked outcomes
[**outcome_groups_api_redirect**](OutcomeGroupsApiApi.md#outcome_groups_api_redirect) | **GET** /api/v1/global/root_outcome_group | Redirect to root outcome group for context
[**outcome_groups_api_redirect_for_accounts**](OutcomeGroupsApiApi.md#outcome_groups_api_redirect_for_accounts) | **GET** /api/v1/accounts/{account_id}/root_outcome_group | Redirect to root outcome group for context
[**outcome_groups_api_redirect_for_courses**](OutcomeGroupsApiApi.md#outcome_groups_api_redirect_for_courses) | **GET** /api/v1/courses/{course_id}/root_outcome_group | Redirect to root outcome group for context
[**outcome_groups_api_show**](OutcomeGroupsApiApi.md#outcome_groups_api_show) | **GET** /api/v1/global/outcome_groups/{id} | Show an outcome group
[**outcome_groups_api_show_for_accounts**](OutcomeGroupsApiApi.md#outcome_groups_api_show_for_accounts) | **GET** /api/v1/accounts/{account_id}/outcome_groups/{id} | Show an outcome group
[**outcome_groups_api_show_for_courses**](OutcomeGroupsApiApi.md#outcome_groups_api_show_for_courses) | **GET** /api/v1/courses/{course_id}/outcome_groups/{id} | Show an outcome group
[**outcome_groups_api_subgroups**](OutcomeGroupsApiApi.md#outcome_groups_api_subgroups) | **GET** /api/v1/global/outcome_groups/{id}/subgroups | List subgroups
[**outcome_groups_api_subgroups_for_accounts**](OutcomeGroupsApiApi.md#outcome_groups_api_subgroups_for_accounts) | **GET** /api/v1/accounts/{account_id}/outcome_groups/{id}/subgroups | List subgroups
[**outcome_groups_api_subgroups_for_courses**](OutcomeGroupsApiApi.md#outcome_groups_api_subgroups_for_courses) | **GET** /api/v1/courses/{course_id}/outcome_groups/{id}/subgroups | List subgroups
[**outcome_groups_api_unlink**](OutcomeGroupsApiApi.md#outcome_groups_api_unlink) | **DELETE** /api/v1/global/outcome_groups/{id}/outcomes/{outcome_id} | Unlink an outcome
[**outcome_groups_api_unlink_for_accounts**](OutcomeGroupsApiApi.md#outcome_groups_api_unlink_for_accounts) | **DELETE** /api/v1/accounts/{account_id}/outcome_groups/{id}/outcomes/{outcome_id} | Unlink an outcome
[**outcome_groups_api_unlink_for_courses**](OutcomeGroupsApiApi.md#outcome_groups_api_unlink_for_courses) | **DELETE** /api/v1/courses/{course_id}/outcome_groups/{id}/outcomes/{outcome_id} | Unlink an outcome
[**outcome_groups_api_update**](OutcomeGroupsApiApi.md#outcome_groups_api_update) | **PUT** /api/v1/global/outcome_groups/{id} | Update an outcome group
[**outcome_groups_api_update_for_accounts**](OutcomeGroupsApiApi.md#outcome_groups_api_update_for_accounts) | **PUT** /api/v1/accounts/{account_id}/outcome_groups/{id} | Update an outcome group
[**outcome_groups_api_update_for_courses**](OutcomeGroupsApiApi.md#outcome_groups_api_update_for_courses) | **PUT** /api/v1/courses/{course_id}/outcome_groups/{id} | Update an outcome group


# **outcome_groups_api_create**
> OutcomeGroup outcome_groups_api_create(id, outcome_groups_api_create_request=outcome_groups_api_create_request)

Create a subgroup

Creates a new empty subgroup under the outcome group with the given title
and description.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.outcome_group import OutcomeGroup
from canvas_lms_python_client.models.outcome_groups_api_create_request import OutcomeGroupsApiCreateRequest
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
    api_instance = canvas_lms_python_client.OutcomeGroupsApiApi(api_client)
    id = 'id_example' # str | Scope response to id
    outcome_groups_api_create_request = canvas_lms_python_client.OutcomeGroupsApiCreateRequest() # OutcomeGroupsApiCreateRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/accounts/1/outcome_groups/1/subgroups.json' \\      -X POST \\      -F 'title=Outcome Group Title' \\      -F 'description=Outcome group description' \\      -F 'vendor_guid=customid9000' \\      -H \"Authorization: Bearer <token>\" ``` (optional)

    try:
        # Create a subgroup
        api_response = await api_instance.outcome_groups_api_create(id, outcome_groups_api_create_request=outcome_groups_api_create_request)
        print("The response of OutcomeGroupsApiApi->outcome_groups_api_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutcomeGroupsApiApi->outcome_groups_api_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **outcome_groups_api_create_request** | [**OutcomeGroupsApiCreateRequest**](OutcomeGroupsApiCreateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/accounts/1/outcome_groups/1/subgroups.json&#39; \\      -X POST \\      -F &#39;title&#x3D;Outcome Group Title&#39; \\      -F &#39;description&#x3D;Outcome group description&#39; \\      -F &#39;vendor_guid&#x3D;customid9000&#39; \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**OutcomeGroup**](OutcomeGroup.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | OutcomeGroup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **outcome_groups_api_create_for_accounts**
> OutcomeGroup outcome_groups_api_create_for_accounts(account_id, id, outcome_groups_api_create_request=outcome_groups_api_create_request)

Create a subgroup

Creates a new empty subgroup under the outcome group with the given title
and description.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.outcome_group import OutcomeGroup
from canvas_lms_python_client.models.outcome_groups_api_create_request import OutcomeGroupsApiCreateRequest
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
    api_instance = canvas_lms_python_client.OutcomeGroupsApiApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id
    outcome_groups_api_create_request = canvas_lms_python_client.OutcomeGroupsApiCreateRequest() # OutcomeGroupsApiCreateRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/accounts/1/outcome_groups/1/subgroups.json' \\      -X POST \\      -F 'title=Outcome Group Title' \\      -F 'description=Outcome group description' \\      -F 'vendor_guid=customid9000' \\      -H \"Authorization: Bearer <token>\" ``` (optional)

    try:
        # Create a subgroup
        api_response = await api_instance.outcome_groups_api_create_for_accounts(account_id, id, outcome_groups_api_create_request=outcome_groups_api_create_request)
        print("The response of OutcomeGroupsApiApi->outcome_groups_api_create_for_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutcomeGroupsApiApi->outcome_groups_api_create_for_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 
 **outcome_groups_api_create_request** | [**OutcomeGroupsApiCreateRequest**](OutcomeGroupsApiCreateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/accounts/1/outcome_groups/1/subgroups.json&#39; \\      -X POST \\      -F &#39;title&#x3D;Outcome Group Title&#39; \\      -F &#39;description&#x3D;Outcome group description&#39; \\      -F &#39;vendor_guid&#x3D;customid9000&#39; \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**OutcomeGroup**](OutcomeGroup.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | OutcomeGroup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **outcome_groups_api_create_for_courses**
> OutcomeGroup outcome_groups_api_create_for_courses(course_id, id, outcome_groups_api_create_request=outcome_groups_api_create_request)

Create a subgroup

Creates a new empty subgroup under the outcome group with the given title
and description.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.outcome_group import OutcomeGroup
from canvas_lms_python_client.models.outcome_groups_api_create_request import OutcomeGroupsApiCreateRequest
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
    api_instance = canvas_lms_python_client.OutcomeGroupsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    outcome_groups_api_create_request = canvas_lms_python_client.OutcomeGroupsApiCreateRequest() # OutcomeGroupsApiCreateRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/accounts/1/outcome_groups/1/subgroups.json' \\      -X POST \\      -F 'title=Outcome Group Title' \\      -F 'description=Outcome group description' \\      -F 'vendor_guid=customid9000' \\      -H \"Authorization: Bearer <token>\" ``` (optional)

    try:
        # Create a subgroup
        api_response = await api_instance.outcome_groups_api_create_for_courses(course_id, id, outcome_groups_api_create_request=outcome_groups_api_create_request)
        print("The response of OutcomeGroupsApiApi->outcome_groups_api_create_for_courses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutcomeGroupsApiApi->outcome_groups_api_create_for_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **outcome_groups_api_create_request** | [**OutcomeGroupsApiCreateRequest**](OutcomeGroupsApiCreateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/accounts/1/outcome_groups/1/subgroups.json&#39; \\      -X POST \\      -F &#39;title&#x3D;Outcome Group Title&#39; \\      -F &#39;description&#x3D;Outcome group description&#39; \\      -F &#39;vendor_guid&#x3D;customid9000&#39; \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**OutcomeGroup**](OutcomeGroup.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | OutcomeGroup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **outcome_groups_api_destroy**
> OutcomeGroup outcome_groups_api_destroy(id)

Delete an outcome group

Deleting an outcome group deletes descendant outcome groups and outcome
links. The linked outcomes themselves are only deleted if all links to the
outcome were deleted.

Aligned outcomes cannot be deleted; as such, if all remaining links to an
aligned outcome are included in this group's descendants, the group
deletion will fail.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.outcome_group import OutcomeGroup
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
    api_instance = canvas_lms_python_client.OutcomeGroupsApiApi(api_client)
    id = 'id_example' # str | Scope response to id

    try:
        # Delete an outcome group
        api_response = await api_instance.outcome_groups_api_destroy(id)
        print("The response of OutcomeGroupsApiApi->outcome_groups_api_destroy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutcomeGroupsApiApi->outcome_groups_api_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 

### Return type

[**OutcomeGroup**](OutcomeGroup.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | OutcomeGroup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **outcome_groups_api_destroy_for_accounts**
> OutcomeGroup outcome_groups_api_destroy_for_accounts(account_id, id)

Delete an outcome group

Deleting an outcome group deletes descendant outcome groups and outcome
links. The linked outcomes themselves are only deleted if all links to the
outcome were deleted.

Aligned outcomes cannot be deleted; as such, if all remaining links to an
aligned outcome are included in this group's descendants, the group
deletion will fail.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.outcome_group import OutcomeGroup
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
    api_instance = canvas_lms_python_client.OutcomeGroupsApiApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id

    try:
        # Delete an outcome group
        api_response = await api_instance.outcome_groups_api_destroy_for_accounts(account_id, id)
        print("The response of OutcomeGroupsApiApi->outcome_groups_api_destroy_for_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutcomeGroupsApiApi->outcome_groups_api_destroy_for_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**OutcomeGroup**](OutcomeGroup.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | OutcomeGroup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **outcome_groups_api_destroy_for_courses**
> OutcomeGroup outcome_groups_api_destroy_for_courses(course_id, id)

Delete an outcome group

Deleting an outcome group deletes descendant outcome groups and outcome
links. The linked outcomes themselves are only deleted if all links to the
outcome were deleted.

Aligned outcomes cannot be deleted; as such, if all remaining links to an
aligned outcome are included in this group's descendants, the group
deletion will fail.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.outcome_group import OutcomeGroup
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
    api_instance = canvas_lms_python_client.OutcomeGroupsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id

    try:
        # Delete an outcome group
        api_response = await api_instance.outcome_groups_api_destroy_for_courses(course_id, id)
        print("The response of OutcomeGroupsApiApi->outcome_groups_api_destroy_for_courses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutcomeGroupsApiApi->outcome_groups_api_destroy_for_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**OutcomeGroup**](OutcomeGroup.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | OutcomeGroup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **outcome_groups_api_import**
> OutcomeGroup outcome_groups_api_import(id, outcome_groups_api_import_request=outcome_groups_api_import_request)

Import an outcome group

Creates a new subgroup of the outcome group with the same title and
description as the source group, then creates links in that new subgroup to
the same outcomes that are linked in the source group. Recurses on the
subgroups of the source group, importing them each in turn into the new
subgroup.

Allows you to copy organizational structure, but does not create copies of
the outcomes themselves, only new links.

The source group must be either global, from the same context as this
outcome group, or from an associated account. The source group cannot be
the root outcome group of its context.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.outcome_group import OutcomeGroup
from canvas_lms_python_client.models.outcome_groups_api_import_request import OutcomeGroupsApiImportRequest
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
    api_instance = canvas_lms_python_client.OutcomeGroupsApiApi(api_client)
    id = 'id_example' # str | Scope response to id
    outcome_groups_api_import_request = canvas_lms_python_client.OutcomeGroupsApiImportRequest() # OutcomeGroupsApiImportRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/accounts/2/outcome_groups/3/import.json' \\      -X POST \\      -F 'source_outcome_group_id=2' \\      -H \"Authorization: Bearer <token>\" ``` (optional)

    try:
        # Import an outcome group
        api_response = await api_instance.outcome_groups_api_import(id, outcome_groups_api_import_request=outcome_groups_api_import_request)
        print("The response of OutcomeGroupsApiApi->outcome_groups_api_import:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutcomeGroupsApiApi->outcome_groups_api_import: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **outcome_groups_api_import_request** | [**OutcomeGroupsApiImportRequest**](OutcomeGroupsApiImportRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/accounts/2/outcome_groups/3/import.json&#39; \\      -X POST \\      -F &#39;source_outcome_group_id&#x3D;2&#39; \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**OutcomeGroup**](OutcomeGroup.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | OutcomeGroup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **outcome_groups_api_import_for_accounts**
> OutcomeGroup outcome_groups_api_import_for_accounts(account_id, id, outcome_groups_api_import_request=outcome_groups_api_import_request)

Import an outcome group

Creates a new subgroup of the outcome group with the same title and
description as the source group, then creates links in that new subgroup to
the same outcomes that are linked in the source group. Recurses on the
subgroups of the source group, importing them each in turn into the new
subgroup.

Allows you to copy organizational structure, but does not create copies of
the outcomes themselves, only new links.

The source group must be either global, from the same context as this
outcome group, or from an associated account. The source group cannot be
the root outcome group of its context.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.outcome_group import OutcomeGroup
from canvas_lms_python_client.models.outcome_groups_api_import_request import OutcomeGroupsApiImportRequest
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
    api_instance = canvas_lms_python_client.OutcomeGroupsApiApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id
    outcome_groups_api_import_request = canvas_lms_python_client.OutcomeGroupsApiImportRequest() # OutcomeGroupsApiImportRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/accounts/2/outcome_groups/3/import.json' \\      -X POST \\      -F 'source_outcome_group_id=2' \\      -H \"Authorization: Bearer <token>\" ``` (optional)

    try:
        # Import an outcome group
        api_response = await api_instance.outcome_groups_api_import_for_accounts(account_id, id, outcome_groups_api_import_request=outcome_groups_api_import_request)
        print("The response of OutcomeGroupsApiApi->outcome_groups_api_import_for_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutcomeGroupsApiApi->outcome_groups_api_import_for_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 
 **outcome_groups_api_import_request** | [**OutcomeGroupsApiImportRequest**](OutcomeGroupsApiImportRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/accounts/2/outcome_groups/3/import.json&#39; \\      -X POST \\      -F &#39;source_outcome_group_id&#x3D;2&#39; \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**OutcomeGroup**](OutcomeGroup.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | OutcomeGroup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **outcome_groups_api_import_for_courses**
> OutcomeGroup outcome_groups_api_import_for_courses(course_id, id, outcome_groups_api_import_request=outcome_groups_api_import_request)

Import an outcome group

Creates a new subgroup of the outcome group with the same title and
description as the source group, then creates links in that new subgroup to
the same outcomes that are linked in the source group. Recurses on the
subgroups of the source group, importing them each in turn into the new
subgroup.

Allows you to copy organizational structure, but does not create copies of
the outcomes themselves, only new links.

The source group must be either global, from the same context as this
outcome group, or from an associated account. The source group cannot be
the root outcome group of its context.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.outcome_group import OutcomeGroup
from canvas_lms_python_client.models.outcome_groups_api_import_request import OutcomeGroupsApiImportRequest
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
    api_instance = canvas_lms_python_client.OutcomeGroupsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    outcome_groups_api_import_request = canvas_lms_python_client.OutcomeGroupsApiImportRequest() # OutcomeGroupsApiImportRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/accounts/2/outcome_groups/3/import.json' \\      -X POST \\      -F 'source_outcome_group_id=2' \\      -H \"Authorization: Bearer <token>\" ``` (optional)

    try:
        # Import an outcome group
        api_response = await api_instance.outcome_groups_api_import_for_courses(course_id, id, outcome_groups_api_import_request=outcome_groups_api_import_request)
        print("The response of OutcomeGroupsApiApi->outcome_groups_api_import_for_courses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutcomeGroupsApiApi->outcome_groups_api_import_for_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **outcome_groups_api_import_request** | [**OutcomeGroupsApiImportRequest**](OutcomeGroupsApiImportRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/accounts/2/outcome_groups/3/import.json&#39; \\      -X POST \\      -F &#39;source_outcome_group_id&#x3D;2&#39; \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**OutcomeGroup**](OutcomeGroup.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | OutcomeGroup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **outcome_groups_api_index**
> List[OutcomeGroup] outcome_groups_api_index(account_id, page=page, per_page=per_page)

Get all outcome groups for context

Returns a list of all outcome groups in the specified context.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.outcome_group import OutcomeGroup
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
    api_instance = canvas_lms_python_client.OutcomeGroupsApiApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # Get all outcome groups for context
        api_response = await api_instance.outcome_groups_api_index(account_id, page=page, per_page=per_page)
        print("The response of OutcomeGroupsApiApi->outcome_groups_api_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutcomeGroupsApiApi->outcome_groups_api_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[OutcomeGroup]**](OutcomeGroup.md)

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

# **outcome_groups_api_index_for_courses**
> List[OutcomeGroup] outcome_groups_api_index_for_courses(course_id, page=page, per_page=per_page)

Get all outcome groups for context

Returns a list of all outcome groups in the specified context.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.outcome_group import OutcomeGroup
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
    api_instance = canvas_lms_python_client.OutcomeGroupsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # Get all outcome groups for context
        api_response = await api_instance.outcome_groups_api_index_for_courses(course_id, page=page, per_page=per_page)
        print("The response of OutcomeGroupsApiApi->outcome_groups_api_index_for_courses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutcomeGroupsApiApi->outcome_groups_api_index_for_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[OutcomeGroup]**](OutcomeGroup.md)

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

# **outcome_groups_api_link**
> OutcomeLink outcome_groups_api_link(id, outcome_groups_api_link_request=outcome_groups_api_link_request)

Create/link an outcome

Link an outcome into the outcome group. The outcome to link can either be
specified by a PUT to the link URL for a specific outcome (the outcome_id
in the PUT URLs) or by supplying the information for a new outcome (title,
description, ratings, mastery_points) in a POST to the collection.

If linking an existing outcome, the outcome_id must identify an outcome
available to this context; i.e. an outcome owned by this group's context,
an outcome owned by an associated account, or a global outcome. With
outcome_id present, any other parameters (except move_from) are ignored.

If defining a new outcome, the outcome is created in the outcome group's
context using the provided title, description, ratings, and mastery points;
the title is required but all other fields are optional. The new outcome
is then linked into the outcome group.

If ratings are provided when creating a new outcome, an embedded rubric
criterion is included in the new outcome. This criterion's mastery_points
default to the maximum points in the highest rating if not specified in the
mastery_points parameter. Any ratings lacking a description are given a
default of "No description". Any ratings lacking a point value are given a
default of 0. If no ratings are provided, the mastery_points parameter is
ignored.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.outcome_groups_api_link_request import OutcomeGroupsApiLinkRequest
from canvas_lms_python_client.models.outcome_link import OutcomeLink
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
    api_instance = canvas_lms_python_client.OutcomeGroupsApiApi(api_client)
    id = 'id_example' # str | Scope response to id
    outcome_groups_api_link_request = canvas_lms_python_client.OutcomeGroupsApiLinkRequest() # OutcomeGroupsApiLinkRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/accounts/1/outcome_groups/1/outcomes/1.json' \\      -X PUT \\      -H \"Authorization: Bearer <token>\" ``` (optional)

    try:
        # Create/link an outcome
        api_response = await api_instance.outcome_groups_api_link(id, outcome_groups_api_link_request=outcome_groups_api_link_request)
        print("The response of OutcomeGroupsApiApi->outcome_groups_api_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutcomeGroupsApiApi->outcome_groups_api_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **outcome_groups_api_link_request** | [**OutcomeGroupsApiLinkRequest**](OutcomeGroupsApiLinkRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/accounts/1/outcome_groups/1/outcomes/1.json&#39; \\      -X PUT \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**OutcomeLink**](OutcomeLink.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | OutcomeLink |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **outcome_groups_api_link_by_outcome_id_for_accounts**
> OutcomeLink outcome_groups_api_link_by_outcome_id_for_accounts(account_id, id, outcome_id, outcome_groups_api_link_for_other_request=outcome_groups_api_link_for_other_request)

Create/link an outcome

Link an outcome into the outcome group. The outcome to link can either be
specified by a PUT to the link URL for a specific outcome (the outcome_id
in the PUT URLs) or by supplying the information for a new outcome (title,
description, ratings, mastery_points) in a POST to the collection.

If linking an existing outcome, the outcome_id must identify an outcome
available to this context; i.e. an outcome owned by this group's context,
an outcome owned by an associated account, or a global outcome. With
outcome_id present, any other parameters (except move_from) are ignored.

If defining a new outcome, the outcome is created in the outcome group's
context using the provided title, description, ratings, and mastery points;
the title is required but all other fields are optional. The new outcome
is then linked into the outcome group.

If ratings are provided when creating a new outcome, an embedded rubric
criterion is included in the new outcome. This criterion's mastery_points
default to the maximum points in the highest rating if not specified in the
mastery_points parameter. Any ratings lacking a description are given a
default of "No description". Any ratings lacking a point value are given a
default of 0. If no ratings are provided, the mastery_points parameter is
ignored.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.outcome_groups_api_link_for_other_request import OutcomeGroupsApiLinkForOtherRequest
from canvas_lms_python_client.models.outcome_link import OutcomeLink
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
    api_instance = canvas_lms_python_client.OutcomeGroupsApiApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id
    outcome_id = 'outcome_id_example' # str | The ID of the existing outcome to link.
    outcome_groups_api_link_for_other_request = canvas_lms_python_client.OutcomeGroupsApiLinkForOtherRequest() # OutcomeGroupsApiLinkForOtherRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/accounts/1/outcome_groups/1/outcomes/1.json' \\      -X PUT \\      -H \"Authorization: Bearer <token>\" ``` (optional)

    try:
        # Create/link an outcome
        api_response = await api_instance.outcome_groups_api_link_by_outcome_id_for_accounts(account_id, id, outcome_id, outcome_groups_api_link_for_other_request=outcome_groups_api_link_for_other_request)
        print("The response of OutcomeGroupsApiApi->outcome_groups_api_link_by_outcome_id_for_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutcomeGroupsApiApi->outcome_groups_api_link_by_outcome_id_for_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 
 **outcome_id** | **str**| The ID of the existing outcome to link. | 
 **outcome_groups_api_link_for_other_request** | [**OutcomeGroupsApiLinkForOtherRequest**](OutcomeGroupsApiLinkForOtherRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/accounts/1/outcome_groups/1/outcomes/1.json&#39; \\      -X PUT \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**OutcomeLink**](OutcomeLink.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | OutcomeLink |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **outcome_groups_api_link_by_outcome_id_for_courses**
> OutcomeLink outcome_groups_api_link_by_outcome_id_for_courses(course_id, id, outcome_id, outcome_groups_api_link_for_other_request=outcome_groups_api_link_for_other_request)

Create/link an outcome

Link an outcome into the outcome group. The outcome to link can either be
specified by a PUT to the link URL for a specific outcome (the outcome_id
in the PUT URLs) or by supplying the information for a new outcome (title,
description, ratings, mastery_points) in a POST to the collection.

If linking an existing outcome, the outcome_id must identify an outcome
available to this context; i.e. an outcome owned by this group's context,
an outcome owned by an associated account, or a global outcome. With
outcome_id present, any other parameters (except move_from) are ignored.

If defining a new outcome, the outcome is created in the outcome group's
context using the provided title, description, ratings, and mastery points;
the title is required but all other fields are optional. The new outcome
is then linked into the outcome group.

If ratings are provided when creating a new outcome, an embedded rubric
criterion is included in the new outcome. This criterion's mastery_points
default to the maximum points in the highest rating if not specified in the
mastery_points parameter. Any ratings lacking a description are given a
default of "No description". Any ratings lacking a point value are given a
default of 0. If no ratings are provided, the mastery_points parameter is
ignored.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.outcome_groups_api_link_for_other_request import OutcomeGroupsApiLinkForOtherRequest
from canvas_lms_python_client.models.outcome_link import OutcomeLink
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
    api_instance = canvas_lms_python_client.OutcomeGroupsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    outcome_id = 'outcome_id_example' # str | The ID of the existing outcome to link.
    outcome_groups_api_link_for_other_request = canvas_lms_python_client.OutcomeGroupsApiLinkForOtherRequest() # OutcomeGroupsApiLinkForOtherRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/accounts/1/outcome_groups/1/outcomes/1.json' \\      -X PUT \\      -H \"Authorization: Bearer <token>\" ``` (optional)

    try:
        # Create/link an outcome
        api_response = await api_instance.outcome_groups_api_link_by_outcome_id_for_courses(course_id, id, outcome_id, outcome_groups_api_link_for_other_request=outcome_groups_api_link_for_other_request)
        print("The response of OutcomeGroupsApiApi->outcome_groups_api_link_by_outcome_id_for_courses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutcomeGroupsApiApi->outcome_groups_api_link_by_outcome_id_for_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **outcome_id** | **str**| The ID of the existing outcome to link. | 
 **outcome_groups_api_link_for_other_request** | [**OutcomeGroupsApiLinkForOtherRequest**](OutcomeGroupsApiLinkForOtherRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/accounts/1/outcome_groups/1/outcomes/1.json&#39; \\      -X PUT \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**OutcomeLink**](OutcomeLink.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | OutcomeLink |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **outcome_groups_api_link_for_accounts**
> OutcomeLink outcome_groups_api_link_for_accounts(account_id, id, outcome_groups_api_link_request=outcome_groups_api_link_request)

Create/link an outcome

Link an outcome into the outcome group. The outcome to link can either be
specified by a PUT to the link URL for a specific outcome (the outcome_id
in the PUT URLs) or by supplying the information for a new outcome (title,
description, ratings, mastery_points) in a POST to the collection.

If linking an existing outcome, the outcome_id must identify an outcome
available to this context; i.e. an outcome owned by this group's context,
an outcome owned by an associated account, or a global outcome. With
outcome_id present, any other parameters (except move_from) are ignored.

If defining a new outcome, the outcome is created in the outcome group's
context using the provided title, description, ratings, and mastery points;
the title is required but all other fields are optional. The new outcome
is then linked into the outcome group.

If ratings are provided when creating a new outcome, an embedded rubric
criterion is included in the new outcome. This criterion's mastery_points
default to the maximum points in the highest rating if not specified in the
mastery_points parameter. Any ratings lacking a description are given a
default of "No description". Any ratings lacking a point value are given a
default of 0. If no ratings are provided, the mastery_points parameter is
ignored.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.outcome_groups_api_link_request import OutcomeGroupsApiLinkRequest
from canvas_lms_python_client.models.outcome_link import OutcomeLink
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
    api_instance = canvas_lms_python_client.OutcomeGroupsApiApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id
    outcome_groups_api_link_request = canvas_lms_python_client.OutcomeGroupsApiLinkRequest() # OutcomeGroupsApiLinkRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/accounts/1/outcome_groups/1/outcomes/1.json' \\      -X PUT \\      -H \"Authorization: Bearer <token>\" ``` (optional)

    try:
        # Create/link an outcome
        api_response = await api_instance.outcome_groups_api_link_for_accounts(account_id, id, outcome_groups_api_link_request=outcome_groups_api_link_request)
        print("The response of OutcomeGroupsApiApi->outcome_groups_api_link_for_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutcomeGroupsApiApi->outcome_groups_api_link_for_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 
 **outcome_groups_api_link_request** | [**OutcomeGroupsApiLinkRequest**](OutcomeGroupsApiLinkRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/accounts/1/outcome_groups/1/outcomes/1.json&#39; \\      -X PUT \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**OutcomeLink**](OutcomeLink.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | OutcomeLink |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **outcome_groups_api_link_for_courses**
> OutcomeLink outcome_groups_api_link_for_courses(course_id, id, outcome_groups_api_link_request=outcome_groups_api_link_request)

Create/link an outcome

Link an outcome into the outcome group. The outcome to link can either be
specified by a PUT to the link URL for a specific outcome (the outcome_id
in the PUT URLs) or by supplying the information for a new outcome (title,
description, ratings, mastery_points) in a POST to the collection.

If linking an existing outcome, the outcome_id must identify an outcome
available to this context; i.e. an outcome owned by this group's context,
an outcome owned by an associated account, or a global outcome. With
outcome_id present, any other parameters (except move_from) are ignored.

If defining a new outcome, the outcome is created in the outcome group's
context using the provided title, description, ratings, and mastery points;
the title is required but all other fields are optional. The new outcome
is then linked into the outcome group.

If ratings are provided when creating a new outcome, an embedded rubric
criterion is included in the new outcome. This criterion's mastery_points
default to the maximum points in the highest rating if not specified in the
mastery_points parameter. Any ratings lacking a description are given a
default of "No description". Any ratings lacking a point value are given a
default of 0. If no ratings are provided, the mastery_points parameter is
ignored.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.outcome_groups_api_link_request import OutcomeGroupsApiLinkRequest
from canvas_lms_python_client.models.outcome_link import OutcomeLink
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
    api_instance = canvas_lms_python_client.OutcomeGroupsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    outcome_groups_api_link_request = canvas_lms_python_client.OutcomeGroupsApiLinkRequest() # OutcomeGroupsApiLinkRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/accounts/1/outcome_groups/1/outcomes/1.json' \\      -X PUT \\      -H \"Authorization: Bearer <token>\" ``` (optional)

    try:
        # Create/link an outcome
        api_response = await api_instance.outcome_groups_api_link_for_courses(course_id, id, outcome_groups_api_link_request=outcome_groups_api_link_request)
        print("The response of OutcomeGroupsApiApi->outcome_groups_api_link_for_courses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutcomeGroupsApiApi->outcome_groups_api_link_for_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **outcome_groups_api_link_request** | [**OutcomeGroupsApiLinkRequest**](OutcomeGroupsApiLinkRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/accounts/1/outcome_groups/1/outcomes/1.json&#39; \\      -X PUT \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**OutcomeLink**](OutcomeLink.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | OutcomeLink |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **outcome_groups_api_link_for_other**
> OutcomeLink outcome_groups_api_link_for_other(id, outcome_id, outcome_groups_api_link_for_other_request=outcome_groups_api_link_for_other_request)

Create/link an outcome

Link an outcome into the outcome group. The outcome to link can either be
specified by a PUT to the link URL for a specific outcome (the outcome_id
in the PUT URLs) or by supplying the information for a new outcome (title,
description, ratings, mastery_points) in a POST to the collection.

If linking an existing outcome, the outcome_id must identify an outcome
available to this context; i.e. an outcome owned by this group's context,
an outcome owned by an associated account, or a global outcome. With
outcome_id present, any other parameters (except move_from) are ignored.

If defining a new outcome, the outcome is created in the outcome group's
context using the provided title, description, ratings, and mastery points;
the title is required but all other fields are optional. The new outcome
is then linked into the outcome group.

If ratings are provided when creating a new outcome, an embedded rubric
criterion is included in the new outcome. This criterion's mastery_points
default to the maximum points in the highest rating if not specified in the
mastery_points parameter. Any ratings lacking a description are given a
default of "No description". Any ratings lacking a point value are given a
default of 0. If no ratings are provided, the mastery_points parameter is
ignored.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.outcome_groups_api_link_for_other_request import OutcomeGroupsApiLinkForOtherRequest
from canvas_lms_python_client.models.outcome_link import OutcomeLink
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
    api_instance = canvas_lms_python_client.OutcomeGroupsApiApi(api_client)
    id = 'id_example' # str | Scope response to id
    outcome_id = 'outcome_id_example' # str | The ID of the existing outcome to link.
    outcome_groups_api_link_for_other_request = canvas_lms_python_client.OutcomeGroupsApiLinkForOtherRequest() # OutcomeGroupsApiLinkForOtherRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/accounts/1/outcome_groups/1/outcomes/1.json' \\      -X PUT \\      -H \"Authorization: Bearer <token>\" ``` (optional)

    try:
        # Create/link an outcome
        api_response = await api_instance.outcome_groups_api_link_for_other(id, outcome_id, outcome_groups_api_link_for_other_request=outcome_groups_api_link_for_other_request)
        print("The response of OutcomeGroupsApiApi->outcome_groups_api_link_for_other:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutcomeGroupsApiApi->outcome_groups_api_link_for_other: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **outcome_id** | **str**| The ID of the existing outcome to link. | 
 **outcome_groups_api_link_for_other_request** | [**OutcomeGroupsApiLinkForOtherRequest**](OutcomeGroupsApiLinkForOtherRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/accounts/1/outcome_groups/1/outcomes/1.json&#39; \\      -X PUT \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**OutcomeLink**](OutcomeLink.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | OutcomeLink |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **outcome_groups_api_link_index**
> List[OutcomeLink] outcome_groups_api_link_index(account_id, outcome_style=outcome_style, outcome_group_style=outcome_group_style, page=page, per_page=per_page)

Get all outcome links for context

Returns a list of all outcome links in the specified context.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.outcome_link import OutcomeLink
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
    api_instance = canvas_lms_python_client.OutcomeGroupsApiApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    outcome_style = 'outcome_style_example' # str | The detail level of the outcomes. Defaults to \"abbrev\". Specify \"full\" for more information. (optional)
    outcome_group_style = 'outcome_group_style_example' # str | The detail level of the outcome groups. Defaults to \"abbrev\". Specify \"full\" for more information. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # Get all outcome links for context
        api_response = await api_instance.outcome_groups_api_link_index(account_id, outcome_style=outcome_style, outcome_group_style=outcome_group_style, page=page, per_page=per_page)
        print("The response of OutcomeGroupsApiApi->outcome_groups_api_link_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutcomeGroupsApiApi->outcome_groups_api_link_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **outcome_style** | **str**| The detail level of the outcomes. Defaults to \&quot;abbrev\&quot;. Specify \&quot;full\&quot; for more information. | [optional] 
 **outcome_group_style** | **str**| The detail level of the outcome groups. Defaults to \&quot;abbrev\&quot;. Specify \&quot;full\&quot; for more information. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[OutcomeLink]**](OutcomeLink.md)

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

# **outcome_groups_api_link_index_for_courses**
> List[OutcomeLink] outcome_groups_api_link_index_for_courses(course_id, outcome_style=outcome_style, outcome_group_style=outcome_group_style, page=page, per_page=per_page)

Get all outcome links for context

Returns a list of all outcome links in the specified context.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.outcome_link import OutcomeLink
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
    api_instance = canvas_lms_python_client.OutcomeGroupsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    outcome_style = 'outcome_style_example' # str | The detail level of the outcomes. Defaults to \"abbrev\". Specify \"full\" for more information. (optional)
    outcome_group_style = 'outcome_group_style_example' # str | The detail level of the outcome groups. Defaults to \"abbrev\". Specify \"full\" for more information. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # Get all outcome links for context
        api_response = await api_instance.outcome_groups_api_link_index_for_courses(course_id, outcome_style=outcome_style, outcome_group_style=outcome_group_style, page=page, per_page=per_page)
        print("The response of OutcomeGroupsApiApi->outcome_groups_api_link_index_for_courses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutcomeGroupsApiApi->outcome_groups_api_link_index_for_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **outcome_style** | **str**| The detail level of the outcomes. Defaults to \&quot;abbrev\&quot;. Specify \&quot;full\&quot; for more information. | [optional] 
 **outcome_group_style** | **str**| The detail level of the outcome groups. Defaults to \&quot;abbrev\&quot;. Specify \&quot;full\&quot; for more information. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[OutcomeLink]**](OutcomeLink.md)

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

# **outcome_groups_api_outcomes**
> List[OutcomeLink] outcome_groups_api_outcomes(id, outcome_style=outcome_style, page=page, per_page=per_page)

List linked outcomes

A paginated list of the immediate OutcomeLink children of the outcome group.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.outcome_link import OutcomeLink
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
    api_instance = canvas_lms_python_client.OutcomeGroupsApiApi(api_client)
    id = 'id_example' # str | Scope response to id
    outcome_style = 'outcome_style_example' # str | The detail level of the outcomes. Defaults to \"abbrev\". Specify \"full\" for more information. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List linked outcomes
        api_response = await api_instance.outcome_groups_api_outcomes(id, outcome_style=outcome_style, page=page, per_page=per_page)
        print("The response of OutcomeGroupsApiApi->outcome_groups_api_outcomes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutcomeGroupsApiApi->outcome_groups_api_outcomes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **outcome_style** | **str**| The detail level of the outcomes. Defaults to \&quot;abbrev\&quot;. Specify \&quot;full\&quot; for more information. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[OutcomeLink]**](OutcomeLink.md)

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

# **outcome_groups_api_outcomes_for_accounts**
> List[OutcomeLink] outcome_groups_api_outcomes_for_accounts(account_id, id, outcome_style=outcome_style, page=page, per_page=per_page)

List linked outcomes

A paginated list of the immediate OutcomeLink children of the outcome group.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.outcome_link import OutcomeLink
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
    api_instance = canvas_lms_python_client.OutcomeGroupsApiApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id
    outcome_style = 'outcome_style_example' # str | The detail level of the outcomes. Defaults to \"abbrev\". Specify \"full\" for more information. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List linked outcomes
        api_response = await api_instance.outcome_groups_api_outcomes_for_accounts(account_id, id, outcome_style=outcome_style, page=page, per_page=per_page)
        print("The response of OutcomeGroupsApiApi->outcome_groups_api_outcomes_for_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutcomeGroupsApiApi->outcome_groups_api_outcomes_for_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 
 **outcome_style** | **str**| The detail level of the outcomes. Defaults to \&quot;abbrev\&quot;. Specify \&quot;full\&quot; for more information. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[OutcomeLink]**](OutcomeLink.md)

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

# **outcome_groups_api_outcomes_for_courses**
> List[OutcomeLink] outcome_groups_api_outcomes_for_courses(course_id, id, outcome_style=outcome_style, page=page, per_page=per_page)

List linked outcomes

A paginated list of the immediate OutcomeLink children of the outcome group.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.outcome_link import OutcomeLink
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
    api_instance = canvas_lms_python_client.OutcomeGroupsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    outcome_style = 'outcome_style_example' # str | The detail level of the outcomes. Defaults to \"abbrev\". Specify \"full\" for more information. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List linked outcomes
        api_response = await api_instance.outcome_groups_api_outcomes_for_courses(course_id, id, outcome_style=outcome_style, page=page, per_page=per_page)
        print("The response of OutcomeGroupsApiApi->outcome_groups_api_outcomes_for_courses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutcomeGroupsApiApi->outcome_groups_api_outcomes_for_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **outcome_style** | **str**| The detail level of the outcomes. Defaults to \&quot;abbrev\&quot;. Specify \&quot;full\&quot; for more information. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[OutcomeLink]**](OutcomeLink.md)

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

# **outcome_groups_api_redirect**
> outcome_groups_api_redirect()

Redirect to root outcome group for context

Convenience redirect to find the root outcome group for a particular
context. Will redirect to the appropriate outcome group's URL.

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
    api_instance = canvas_lms_python_client.OutcomeGroupsApiApi(api_client)

    try:
        # Redirect to root outcome group for context
        await api_instance.outcome_groups_api_redirect()
    except Exception as e:
        print("Exception when calling OutcomeGroupsApiApi->outcome_groups_api_redirect: %s\n" % e)
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
**0** | Redirect to root outcome group for context |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **outcome_groups_api_redirect_for_accounts**
> outcome_groups_api_redirect_for_accounts(account_id)

Redirect to root outcome group for context

Convenience redirect to find the root outcome group for a particular
context. Will redirect to the appropriate outcome group's URL.

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
    api_instance = canvas_lms_python_client.OutcomeGroupsApiApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id

    try:
        # Redirect to root outcome group for context
        await api_instance.outcome_groups_api_redirect_for_accounts(account_id)
    except Exception as e:
        print("Exception when calling OutcomeGroupsApiApi->outcome_groups_api_redirect_for_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 

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
**0** | Redirect to root outcome group for context |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **outcome_groups_api_redirect_for_courses**
> outcome_groups_api_redirect_for_courses(course_id)

Redirect to root outcome group for context

Convenience redirect to find the root outcome group for a particular
context. Will redirect to the appropriate outcome group's URL.

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
    api_instance = canvas_lms_python_client.OutcomeGroupsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id

    try:
        # Redirect to root outcome group for context
        await api_instance.outcome_groups_api_redirect_for_courses(course_id)
    except Exception as e:
        print("Exception when calling OutcomeGroupsApiApi->outcome_groups_api_redirect_for_courses: %s\n" % e)
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
**0** | Redirect to root outcome group for context |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **outcome_groups_api_show**
> OutcomeGroup outcome_groups_api_show(id)

Show an outcome group

Returns detailed information about a specific outcome group.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.outcome_group import OutcomeGroup
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
    api_instance = canvas_lms_python_client.OutcomeGroupsApiApi(api_client)
    id = 'id_example' # str | Scope response to id

    try:
        # Show an outcome group
        api_response = await api_instance.outcome_groups_api_show(id)
        print("The response of OutcomeGroupsApiApi->outcome_groups_api_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutcomeGroupsApiApi->outcome_groups_api_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 

### Return type

[**OutcomeGroup**](OutcomeGroup.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | OutcomeGroup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **outcome_groups_api_show_for_accounts**
> OutcomeGroup outcome_groups_api_show_for_accounts(account_id, id)

Show an outcome group

Returns detailed information about a specific outcome group.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.outcome_group import OutcomeGroup
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
    api_instance = canvas_lms_python_client.OutcomeGroupsApiApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id

    try:
        # Show an outcome group
        api_response = await api_instance.outcome_groups_api_show_for_accounts(account_id, id)
        print("The response of OutcomeGroupsApiApi->outcome_groups_api_show_for_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutcomeGroupsApiApi->outcome_groups_api_show_for_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**OutcomeGroup**](OutcomeGroup.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | OutcomeGroup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **outcome_groups_api_show_for_courses**
> OutcomeGroup outcome_groups_api_show_for_courses(course_id, id)

Show an outcome group

Returns detailed information about a specific outcome group.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.outcome_group import OutcomeGroup
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
    api_instance = canvas_lms_python_client.OutcomeGroupsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id

    try:
        # Show an outcome group
        api_response = await api_instance.outcome_groups_api_show_for_courses(course_id, id)
        print("The response of OutcomeGroupsApiApi->outcome_groups_api_show_for_courses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutcomeGroupsApiApi->outcome_groups_api_show_for_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**OutcomeGroup**](OutcomeGroup.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | OutcomeGroup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **outcome_groups_api_subgroups**
> List[OutcomeGroup] outcome_groups_api_subgroups(id, page=page, per_page=per_page)

List subgroups

A paginated list of the immediate OutcomeGroup children of the outcome group.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.outcome_group import OutcomeGroup
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
    api_instance = canvas_lms_python_client.OutcomeGroupsApiApi(api_client)
    id = 'id_example' # str | Scope response to id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List subgroups
        api_response = await api_instance.outcome_groups_api_subgroups(id, page=page, per_page=per_page)
        print("The response of OutcomeGroupsApiApi->outcome_groups_api_subgroups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutcomeGroupsApiApi->outcome_groups_api_subgroups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[OutcomeGroup]**](OutcomeGroup.md)

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

# **outcome_groups_api_subgroups_for_accounts**
> List[OutcomeGroup] outcome_groups_api_subgroups_for_accounts(account_id, id, page=page, per_page=per_page)

List subgroups

A paginated list of the immediate OutcomeGroup children of the outcome group.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.outcome_group import OutcomeGroup
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
    api_instance = canvas_lms_python_client.OutcomeGroupsApiApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List subgroups
        api_response = await api_instance.outcome_groups_api_subgroups_for_accounts(account_id, id, page=page, per_page=per_page)
        print("The response of OutcomeGroupsApiApi->outcome_groups_api_subgroups_for_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutcomeGroupsApiApi->outcome_groups_api_subgroups_for_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[OutcomeGroup]**](OutcomeGroup.md)

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

# **outcome_groups_api_subgroups_for_courses**
> List[OutcomeGroup] outcome_groups_api_subgroups_for_courses(course_id, id, page=page, per_page=per_page)

List subgroups

A paginated list of the immediate OutcomeGroup children of the outcome group.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.outcome_group import OutcomeGroup
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
    api_instance = canvas_lms_python_client.OutcomeGroupsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List subgroups
        api_response = await api_instance.outcome_groups_api_subgroups_for_courses(course_id, id, page=page, per_page=per_page)
        print("The response of OutcomeGroupsApiApi->outcome_groups_api_subgroups_for_courses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutcomeGroupsApiApi->outcome_groups_api_subgroups_for_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[OutcomeGroup]**](OutcomeGroup.md)

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

# **outcome_groups_api_unlink**
> OutcomeLink outcome_groups_api_unlink(id, outcome_id)

Unlink an outcome

Unlinking an outcome only deletes the outcome itself if this was the last
link to the outcome in any group in any context. Aligned outcomes cannot be
deleted; as such, if this is the last link to an aligned outcome, the
unlinking will fail.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.outcome_link import OutcomeLink
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
    api_instance = canvas_lms_python_client.OutcomeGroupsApiApi(api_client)
    id = 'id_example' # str | Scope response to id
    outcome_id = 'outcome_id_example' # str | Scope response to outcome_id

    try:
        # Unlink an outcome
        api_response = await api_instance.outcome_groups_api_unlink(id, outcome_id)
        print("The response of OutcomeGroupsApiApi->outcome_groups_api_unlink:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutcomeGroupsApiApi->outcome_groups_api_unlink: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **outcome_id** | **str**| Scope response to outcome_id | 

### Return type

[**OutcomeLink**](OutcomeLink.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | OutcomeLink |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **outcome_groups_api_unlink_for_accounts**
> OutcomeLink outcome_groups_api_unlink_for_accounts(account_id, id, outcome_id)

Unlink an outcome

Unlinking an outcome only deletes the outcome itself if this was the last
link to the outcome in any group in any context. Aligned outcomes cannot be
deleted; as such, if this is the last link to an aligned outcome, the
unlinking will fail.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.outcome_link import OutcomeLink
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
    api_instance = canvas_lms_python_client.OutcomeGroupsApiApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id
    outcome_id = 'outcome_id_example' # str | Scope response to outcome_id

    try:
        # Unlink an outcome
        api_response = await api_instance.outcome_groups_api_unlink_for_accounts(account_id, id, outcome_id)
        print("The response of OutcomeGroupsApiApi->outcome_groups_api_unlink_for_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutcomeGroupsApiApi->outcome_groups_api_unlink_for_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 
 **outcome_id** | **str**| Scope response to outcome_id | 

### Return type

[**OutcomeLink**](OutcomeLink.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | OutcomeLink |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **outcome_groups_api_unlink_for_courses**
> OutcomeLink outcome_groups_api_unlink_for_courses(course_id, id, outcome_id)

Unlink an outcome

Unlinking an outcome only deletes the outcome itself if this was the last
link to the outcome in any group in any context. Aligned outcomes cannot be
deleted; as such, if this is the last link to an aligned outcome, the
unlinking will fail.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.outcome_link import OutcomeLink
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
    api_instance = canvas_lms_python_client.OutcomeGroupsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    outcome_id = 'outcome_id_example' # str | Scope response to outcome_id

    try:
        # Unlink an outcome
        api_response = await api_instance.outcome_groups_api_unlink_for_courses(course_id, id, outcome_id)
        print("The response of OutcomeGroupsApiApi->outcome_groups_api_unlink_for_courses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutcomeGroupsApiApi->outcome_groups_api_unlink_for_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **outcome_id** | **str**| Scope response to outcome_id | 

### Return type

[**OutcomeLink**](OutcomeLink.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | OutcomeLink |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **outcome_groups_api_update**
> OutcomeGroup outcome_groups_api_update(id, outcome_groups_api_update_request=outcome_groups_api_update_request)

Update an outcome group

Modify an existing outcome group. Fields not provided are left as is;
unrecognized fields are ignored.

When changing the parent outcome group, the new parent group must belong to
the same context as this outcome group, and must not be a descendant of
this outcome group (i.e. no cycles allowed).

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.outcome_group import OutcomeGroup
from canvas_lms_python_client.models.outcome_groups_api_update_request import OutcomeGroupsApiUpdateRequest
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
    api_instance = canvas_lms_python_client.OutcomeGroupsApiApi(api_client)
    id = 'id_example' # str | Scope response to id
    outcome_groups_api_update_request = canvas_lms_python_client.OutcomeGroupsApiUpdateRequest() # OutcomeGroupsApiUpdateRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/accounts/1/outcome_groups/2.json' \\      -X PUT \\      -F 'title=Outcome Group Title' \\      -F 'description=Outcome group description' \\      -F 'vendor_guid=customid9000' \\      -F 'parent_outcome_group_id=1' \\      -H \"Authorization: Bearer <token>\" ``` (optional)

    try:
        # Update an outcome group
        api_response = await api_instance.outcome_groups_api_update(id, outcome_groups_api_update_request=outcome_groups_api_update_request)
        print("The response of OutcomeGroupsApiApi->outcome_groups_api_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutcomeGroupsApiApi->outcome_groups_api_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **outcome_groups_api_update_request** | [**OutcomeGroupsApiUpdateRequest**](OutcomeGroupsApiUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/accounts/1/outcome_groups/2.json&#39; \\      -X PUT \\      -F &#39;title&#x3D;Outcome Group Title&#39; \\      -F &#39;description&#x3D;Outcome group description&#39; \\      -F &#39;vendor_guid&#x3D;customid9000&#39; \\      -F &#39;parent_outcome_group_id&#x3D;1&#39; \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**OutcomeGroup**](OutcomeGroup.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | OutcomeGroup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **outcome_groups_api_update_for_accounts**
> OutcomeGroup outcome_groups_api_update_for_accounts(account_id, id, outcome_groups_api_update_request=outcome_groups_api_update_request)

Update an outcome group

Modify an existing outcome group. Fields not provided are left as is;
unrecognized fields are ignored.

When changing the parent outcome group, the new parent group must belong to
the same context as this outcome group, and must not be a descendant of
this outcome group (i.e. no cycles allowed).

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.outcome_group import OutcomeGroup
from canvas_lms_python_client.models.outcome_groups_api_update_request import OutcomeGroupsApiUpdateRequest
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
    api_instance = canvas_lms_python_client.OutcomeGroupsApiApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id
    outcome_groups_api_update_request = canvas_lms_python_client.OutcomeGroupsApiUpdateRequest() # OutcomeGroupsApiUpdateRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/accounts/1/outcome_groups/2.json' \\      -X PUT \\      -F 'title=Outcome Group Title' \\      -F 'description=Outcome group description' \\      -F 'vendor_guid=customid9000' \\      -F 'parent_outcome_group_id=1' \\      -H \"Authorization: Bearer <token>\" ``` (optional)

    try:
        # Update an outcome group
        api_response = await api_instance.outcome_groups_api_update_for_accounts(account_id, id, outcome_groups_api_update_request=outcome_groups_api_update_request)
        print("The response of OutcomeGroupsApiApi->outcome_groups_api_update_for_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutcomeGroupsApiApi->outcome_groups_api_update_for_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 
 **outcome_groups_api_update_request** | [**OutcomeGroupsApiUpdateRequest**](OutcomeGroupsApiUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/accounts/1/outcome_groups/2.json&#39; \\      -X PUT \\      -F &#39;title&#x3D;Outcome Group Title&#39; \\      -F &#39;description&#x3D;Outcome group description&#39; \\      -F &#39;vendor_guid&#x3D;customid9000&#39; \\      -F &#39;parent_outcome_group_id&#x3D;1&#39; \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**OutcomeGroup**](OutcomeGroup.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | OutcomeGroup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **outcome_groups_api_update_for_courses**
> OutcomeGroup outcome_groups_api_update_for_courses(course_id, id, outcome_groups_api_update_request=outcome_groups_api_update_request)

Update an outcome group

Modify an existing outcome group. Fields not provided are left as is;
unrecognized fields are ignored.

When changing the parent outcome group, the new parent group must belong to
the same context as this outcome group, and must not be a descendant of
this outcome group (i.e. no cycles allowed).

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.outcome_group import OutcomeGroup
from canvas_lms_python_client.models.outcome_groups_api_update_request import OutcomeGroupsApiUpdateRequest
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
    api_instance = canvas_lms_python_client.OutcomeGroupsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    outcome_groups_api_update_request = canvas_lms_python_client.OutcomeGroupsApiUpdateRequest() # OutcomeGroupsApiUpdateRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/accounts/1/outcome_groups/2.json' \\      -X PUT \\      -F 'title=Outcome Group Title' \\      -F 'description=Outcome group description' \\      -F 'vendor_guid=customid9000' \\      -F 'parent_outcome_group_id=1' \\      -H \"Authorization: Bearer <token>\" ``` (optional)

    try:
        # Update an outcome group
        api_response = await api_instance.outcome_groups_api_update_for_courses(course_id, id, outcome_groups_api_update_request=outcome_groups_api_update_request)
        print("The response of OutcomeGroupsApiApi->outcome_groups_api_update_for_courses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutcomeGroupsApiApi->outcome_groups_api_update_for_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **outcome_groups_api_update_request** | [**OutcomeGroupsApiUpdateRequest**](OutcomeGroupsApiUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/accounts/1/outcome_groups/2.json&#39; \\      -X PUT \\      -F &#39;title&#x3D;Outcome Group Title&#39; \\      -F &#39;description&#x3D;Outcome group description&#39; \\      -F &#39;vendor_guid&#x3D;customid9000&#39; \\      -F &#39;parent_outcome_group_id&#x3D;1&#39; \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**OutcomeGroup**](OutcomeGroup.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | OutcomeGroup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

