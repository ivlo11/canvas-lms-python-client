# canvas_lms_python_client.ResourceLinksApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource_links_bulk_create**](ResourceLinksApi.md#resource_links_bulk_create) | **POST** /api/v1/courses/{course_id}/lti_resource_links/bulk | Bulk Create LTI Resource Links
[**resource_links_create**](ResourceLinksApi.md#resource_links_create) | **POST** /api/v1/courses/{course_id}/lti_resource_links | Create an LTI Resource Link
[**resource_links_destroy**](ResourceLinksApi.md#resource_links_destroy) | **DELETE** /api/v1/courses/{course_id}/lti_resource_links/{id} | Delete an LTI Resource Link
[**resource_links_index**](ResourceLinksApi.md#resource_links_index) | **GET** /api/v1/courses/{course_id}/lti_resource_links | List LTI Resource Links
[**resource_links_show**](ResourceLinksApi.md#resource_links_show) | **GET** /api/v1/courses/{course_id}/lti_resource_links/{id} | Show an LTI Resource Link
[**resource_links_update**](ResourceLinksApi.md#resource_links_update) | **PUT** /api/v1/courses/{course_id}/lti_resource_links/{id} | Update an LTI Resource Link


# **resource_links_bulk_create**
> object resource_links_bulk_create(course_id, resource_links_bulk_create_request=resource_links_bulk_create_request)

Bulk Create LTI Resource Links

Create up to 100 new LTI Resource Links in the specified course with the provided parameters.

<b>Caution!</b> Resource Links are usually created by the tool via LTI Deep Linking. The tool has no
knowledge of links created via this API, and may not be able to handle or launch them.

Links created using this API cannot be associated with a specific piece of Canvas content,
like an Assignment, Module Item, or Collaboration. Links created using this API are only suitable
for embedding in rich content using the `canvas_launch_url` provided in the API response.

Each link will be associated with the ContextExternalTool available in this context that matches the provided url.
If a matching tool is not found, or any parameters are invalid, no links will be created and this will return an error.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.resource_links_bulk_create_request import ResourceLinksBulkCreateRequest
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
    api_instance = canvas_lms_python_client.ResourceLinksApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    resource_links_bulk_create_request = canvas_lms_python_client.ResourceLinksBulkCreateRequest() # ResourceLinksBulkCreateRequest | Request body parameters  **Example Request:** ``` This would create a new LTI resource link in the specified course curl -X POST 'https://<canvas>/api/v1/courses/1/lti_resource_links/bulk' \\     -H \"Authorization: Bearer <token>\" \\     --json '[{\"url\":\"https://example.com/lti/launch/new_content_item/456\",\"title\":\"New Content Item\",\"custom\":{\"hello\":\"world\"}}]' ``` (optional)

    try:
        # Bulk Create LTI Resource Links
        api_response = await api_instance.resource_links_bulk_create(course_id, resource_links_bulk_create_request=resource_links_bulk_create_request)
        print("The response of ResourceLinksApi->resource_links_bulk_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceLinksApi->resource_links_bulk_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **resource_links_bulk_create_request** | [**ResourceLinksBulkCreateRequest**](ResourceLinksBulkCreateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; This would create a new LTI resource link in the specified course curl -X POST &#39;https://&lt;canvas&gt;/api/v1/courses/1/lti_resource_links/bulk&#39; \\     -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; \\     --json &#39;[{\&quot;url\&quot;:\&quot;https://example.com/lti/launch/new_content_item/456\&quot;,\&quot;title\&quot;:\&quot;New Content Item\&quot;,\&quot;custom\&quot;:{\&quot;hello\&quot;:\&quot;world\&quot;}}]&#39; &#x60;&#x60;&#x60; | [optional] 

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
**0** | Lti::ResourceLink |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_links_create**
> object resource_links_create(course_id, resource_links_create_request=resource_links_create_request)

Create an LTI Resource Link

Create a new LTI Resource Link in the specified course with the provided parameters.

<b>Caution!</b> Resource Links are usually created by the tool via LTI Deep Linking. The tool has no
knowledge of links created via this API, and may not be able to handle or launch them.

Links created using this API cannot be associated with a specific piece of Canvas content,
like an Assignment, Module Item, or Collaboration. Links created using this API are only suitable
for embedding in rich content using the `canvas_launch_url` provided in the API response.

This link will be associated with the ContextExternalTool available in this context that matches the provided url.
If a matching tool is not found, the link will not be created and this will return an error.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.resource_links_create_request import ResourceLinksCreateRequest
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
    api_instance = canvas_lms_python_client.ResourceLinksApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    resource_links_create_request = canvas_lms_python_client.ResourceLinksCreateRequest() # ResourceLinksCreateRequest | Request body parameters  **Example Request:** ``` This would create a new LTI resource link in the specified course curl -X POST 'https://<canvas>/api/v1/courses/1/lti_resource_links' \\     -H \"Authorization: Bearer <token>\" \\     -d 'url=https://example.com/lti/launch/new_content_item/456' \\     -d 'title=New Content Item' \\     -d 'custom[hello]=world' \\ ``` (optional)

    try:
        # Create an LTI Resource Link
        api_response = await api_instance.resource_links_create(course_id, resource_links_create_request=resource_links_create_request)
        print("The response of ResourceLinksApi->resource_links_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceLinksApi->resource_links_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **resource_links_create_request** | [**ResourceLinksCreateRequest**](ResourceLinksCreateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; This would create a new LTI resource link in the specified course curl -X POST &#39;https://&lt;canvas&gt;/api/v1/courses/1/lti_resource_links&#39; \\     -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; \\     -d &#39;url&#x3D;https://example.com/lti/launch/new_content_item/456&#39; \\     -d &#39;title&#x3D;New Content Item&#39; \\     -d &#39;custom[hello]&#x3D;world&#39; \\ &#x60;&#x60;&#x60; | [optional] 

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
**0** | Lti::ResourceLink |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_links_destroy**
> object resource_links_destroy(course_id, id)

Delete an LTI Resource Link

Delete the specified resource link. The ID can be in the standard
Canvas format ("1"), or in these special formats:

- resource_link_uuid:<uuid> - Find the resource link by its resource_link_uuid
- lookup_uuid:<uuid> - Find the resource link by its lookup_uuid

Only links that are not associated with Assignments, Module Items, or Collaborations can be deleted.

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
    api_instance = canvas_lms_python_client.ResourceLinksApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id

    try:
        # Delete an LTI Resource Link
        api_response = await api_instance.resource_links_destroy(course_id, id)
        print("The response of ResourceLinksApi->resource_links_destroy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceLinksApi->resource_links_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**0** | Lti::ResourceLink |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_links_index**
> List[object] resource_links_index(course_id, include_deleted=include_deleted, per_page=per_page, page=page)

List LTI Resource Links

Returns all Resource Links in the specified course. This includes links
that are associated with Assignments, Module Items, Collaborations, and
that are embedded in rich content. This endpoint is paginated, and will
return 50 links per page by default.
Links are sorted by the order in which they were created.

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
    api_instance = canvas_lms_python_client.ResourceLinksApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    include_deleted = True # bool | Include deleted resource links and links associated with deleted content in response. Default is false. (optional)
    per_page = 56 # int | The number of registrations to return per page. Defaults to 50. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)

    try:
        # List LTI Resource Links
        api_response = await api_instance.resource_links_index(course_id, include_deleted=include_deleted, per_page=per_page, page=page)
        print("The response of ResourceLinksApi->resource_links_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceLinksApi->resource_links_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **include_deleted** | **bool**| Include deleted resource links and links associated with deleted content in response. Default is false. | [optional] 
 **per_page** | **int**| The number of registrations to return per page. Defaults to 50. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 

### Return type

**List[object]**

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

# **resource_links_show**
> object resource_links_show(course_id, id, include_deleted=include_deleted)

Show an LTI Resource Link

Return details about the specified resource link. The ID can be in the standard
Canvas format ("1"), or in these special formats:

- resource_link_uuid:<uuid> - Find the resource link by its resource_link_uuid
- lookup_uuid:<uuid> - Find the resource link by its lookup_uuid

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
    api_instance = canvas_lms_python_client.ResourceLinksApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    include_deleted = True # bool | Include deleted resource links in search. Default is false. (optional)

    try:
        # Show an LTI Resource Link
        api_response = await api_instance.resource_links_show(course_id, id, include_deleted=include_deleted)
        print("The response of ResourceLinksApi->resource_links_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceLinksApi->resource_links_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **include_deleted** | **bool**| Include deleted resource links in search. Default is false. | [optional] 

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
**0** | Lti::ResourceLink |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_links_update**
> object resource_links_update(course_id, id, resource_links_update_request=resource_links_update_request)

Update an LTI Resource Link

Update the specified resource link with the provided parameters.

<b>Caution!</b> Changing existing links may result in launch errors.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.resource_links_update_request import ResourceLinksUpdateRequest
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
    api_instance = canvas_lms_python_client.ResourceLinksApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    resource_links_update_request = canvas_lms_python_client.ResourceLinksUpdateRequest() # ResourceLinksUpdateRequest | Request body parameters  **Example Request:** ``` This would update the specified LTI resource link curl -X PUT 'https://<canvas>/api/v1/courses/1/lti_resource_links/1' \\     -H \"Authorization: Bearer <token>\" \\     -d 'url=https://example.com/lti/launch/new_content_item/456'     -d 'custom[hello]=world' ``` (optional)

    try:
        # Update an LTI Resource Link
        api_response = await api_instance.resource_links_update(course_id, id, resource_links_update_request=resource_links_update_request)
        print("The response of ResourceLinksApi->resource_links_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceLinksApi->resource_links_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **resource_links_update_request** | [**ResourceLinksUpdateRequest**](ResourceLinksUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; This would update the specified LTI resource link curl -X PUT &#39;https://&lt;canvas&gt;/api/v1/courses/1/lti_resource_links/1&#39; \\     -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; \\     -d &#39;url&#x3D;https://example.com/lti/launch/new_content_item/456&#39;     -d &#39;custom[hello]&#x3D;world&#39; &#x60;&#x60;&#x60; | [optional] 

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
**0** | Lti::ResourceLink |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

