# canvas_lms_python_client.WikiPagesApiApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**wiki_pages_api_create**](WikiPagesApiApi.md#wiki_pages_api_create) | **POST** /api/v1/courses/{course_id}/pages | Create page
[**wiki_pages_api_create_for_groups**](WikiPagesApiApi.md#wiki_pages_api_create_for_groups) | **POST** /api/v1/groups/{group_id}/pages | Create page
[**wiki_pages_api_destroy**](WikiPagesApiApi.md#wiki_pages_api_destroy) | **DELETE** /api/v1/courses/{course_id}/pages/{url_or_id} | Delete page
[**wiki_pages_api_destroy_for_groups**](WikiPagesApiApi.md#wiki_pages_api_destroy_for_groups) | **DELETE** /api/v1/groups/{group_id}/pages/{url_or_id} | Delete page
[**wiki_pages_api_duplicate**](WikiPagesApiApi.md#wiki_pages_api_duplicate) | **POST** /api/v1/courses/{course_id}/pages/{url_or_id}/duplicate | Duplicate page
[**wiki_pages_api_index**](WikiPagesApiApi.md#wiki_pages_api_index) | **GET** /api/v1/courses/{course_id}/pages | List pages
[**wiki_pages_api_index_for_groups**](WikiPagesApiApi.md#wiki_pages_api_index_for_groups) | **GET** /api/v1/groups/{group_id}/pages | List pages
[**wiki_pages_api_revert**](WikiPagesApiApi.md#wiki_pages_api_revert) | **POST** /api/v1/courses/{course_id}/pages/{url_or_id}/revisions/{revision_id} | Revert to revision
[**wiki_pages_api_revert_for_groups**](WikiPagesApiApi.md#wiki_pages_api_revert_for_groups) | **POST** /api/v1/groups/{group_id}/pages/{url_or_id}/revisions/{revision_id} | Revert to revision
[**wiki_pages_api_revisions**](WikiPagesApiApi.md#wiki_pages_api_revisions) | **GET** /api/v1/courses/{course_id}/pages/{url_or_id}/revisions | List revisions
[**wiki_pages_api_revisions_for_groups**](WikiPagesApiApi.md#wiki_pages_api_revisions_for_groups) | **GET** /api/v1/groups/{group_id}/pages/{url_or_id}/revisions | List revisions
[**wiki_pages_api_show**](WikiPagesApiApi.md#wiki_pages_api_show) | **GET** /api/v1/courses/{course_id}/pages/{url_or_id} | Show page
[**wiki_pages_api_show_for_groups**](WikiPagesApiApi.md#wiki_pages_api_show_for_groups) | **GET** /api/v1/groups/{group_id}/pages/{url_or_id} | Show page
[**wiki_pages_api_show_front_page**](WikiPagesApiApi.md#wiki_pages_api_show_front_page) | **GET** /api/v1/courses/{course_id}/front_page | Show front page
[**wiki_pages_api_show_front_page_for_groups**](WikiPagesApiApi.md#wiki_pages_api_show_front_page_for_groups) | **GET** /api/v1/groups/{group_id}/front_page | Show front page
[**wiki_pages_api_show_revision**](WikiPagesApiApi.md#wiki_pages_api_show_revision) | **GET** /api/v1/courses/{course_id}/pages/{url_or_id}/revisions/latest | Show revision
[**wiki_pages_api_show_revision_by_revision_id_for_groups**](WikiPagesApiApi.md#wiki_pages_api_show_revision_by_revision_id_for_groups) | **GET** /api/v1/groups/{group_id}/pages/{url_or_id}/revisions/{revision_id} | Show revision
[**wiki_pages_api_show_revision_for_courses**](WikiPagesApiApi.md#wiki_pages_api_show_revision_for_courses) | **GET** /api/v1/courses/{course_id}/pages/{url_or_id}/revisions/{revision_id} | Show revision
[**wiki_pages_api_show_revision_for_groups**](WikiPagesApiApi.md#wiki_pages_api_show_revision_for_groups) | **GET** /api/v1/groups/{group_id}/pages/{url_or_id}/revisions/latest | Show revision
[**wiki_pages_api_update**](WikiPagesApiApi.md#wiki_pages_api_update) | **PUT** /api/v1/courses/{course_id}/pages/{url_or_id} | Update/create page
[**wiki_pages_api_update_for_groups**](WikiPagesApiApi.md#wiki_pages_api_update_for_groups) | **PUT** /api/v1/groups/{group_id}/pages/{url_or_id} | Update/create page
[**wiki_pages_api_update_front_page**](WikiPagesApiApi.md#wiki_pages_api_update_front_page) | **PUT** /api/v1/courses/{course_id}/front_page | Update/create front page
[**wiki_pages_api_update_front_page_for_groups**](WikiPagesApiApi.md#wiki_pages_api_update_front_page_for_groups) | **PUT** /api/v1/groups/{group_id}/front_page | Update/create front page


# **wiki_pages_api_create**
> Page wiki_pages_api_create(course_id, wiki_pages_api_create_request=wiki_pages_api_create_request)

Create page

Create a new wiki page

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.page import Page
from canvas_lms_python_client.models.wiki_pages_api_create_request import WikiPagesApiCreateRequest
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
    api_instance = canvas_lms_python_client.WikiPagesApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    wiki_pages_api_create_request = canvas_lms_python_client.WikiPagesApiCreateRequest() # WikiPagesApiCreateRequest | Request body parameters  **Example Request:** ``` curl -X POST -H 'Authorization: Bearer <token>' \\ https://<canvas>/api/v1/courses/123/pages \\ -d wiki_page[title]=New+page -d wiki_page[body]=New+body+text ``` (optional)

    try:
        # Create page
        api_response = await api_instance.wiki_pages_api_create(course_id, wiki_pages_api_create_request=wiki_pages_api_create_request)
        print("The response of WikiPagesApiApi->wiki_pages_api_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WikiPagesApiApi->wiki_pages_api_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **wiki_pages_api_create_request** | [**WikiPagesApiCreateRequest**](WikiPagesApiCreateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl -X POST -H &#39;Authorization: Bearer &lt;token&gt;&#39; \\ https://&lt;canvas&gt;/api/v1/courses/123/pages \\ -d wiki_page[title]&#x3D;New+page -d wiki_page[body]&#x3D;New+body+text &#x60;&#x60;&#x60; | [optional] 

### Return type

[**Page**](Page.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Page |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wiki_pages_api_create_for_groups**
> Page wiki_pages_api_create_for_groups(group_id, wiki_pages_api_create_request=wiki_pages_api_create_request)

Create page

Create a new wiki page

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.page import Page
from canvas_lms_python_client.models.wiki_pages_api_create_request import WikiPagesApiCreateRequest
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
    api_instance = canvas_lms_python_client.WikiPagesApiApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    wiki_pages_api_create_request = canvas_lms_python_client.WikiPagesApiCreateRequest() # WikiPagesApiCreateRequest | Request body parameters  **Example Request:** ``` curl -X POST -H 'Authorization: Bearer <token>' \\ https://<canvas>/api/v1/courses/123/pages \\ -d wiki_page[title]=New+page -d wiki_page[body]=New+body+text ``` (optional)

    try:
        # Create page
        api_response = await api_instance.wiki_pages_api_create_for_groups(group_id, wiki_pages_api_create_request=wiki_pages_api_create_request)
        print("The response of WikiPagesApiApi->wiki_pages_api_create_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WikiPagesApiApi->wiki_pages_api_create_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **wiki_pages_api_create_request** | [**WikiPagesApiCreateRequest**](WikiPagesApiCreateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl -X POST -H &#39;Authorization: Bearer &lt;token&gt;&#39; \\ https://&lt;canvas&gt;/api/v1/courses/123/pages \\ -d wiki_page[title]&#x3D;New+page -d wiki_page[body]&#x3D;New+body+text &#x60;&#x60;&#x60; | [optional] 

### Return type

[**Page**](Page.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Page |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wiki_pages_api_destroy**
> Page wiki_pages_api_destroy(course_id, url_or_id)

Delete page

Delete a wiki page

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.page import Page
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
    api_instance = canvas_lms_python_client.WikiPagesApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    url_or_id = 'url_or_id_example' # str | Scope response to url_or_id

    try:
        # Delete page
        api_response = await api_instance.wiki_pages_api_destroy(course_id, url_or_id)
        print("The response of WikiPagesApiApi->wiki_pages_api_destroy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WikiPagesApiApi->wiki_pages_api_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **url_or_id** | **str**| Scope response to url_or_id | 

### Return type

[**Page**](Page.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Page |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wiki_pages_api_destroy_for_groups**
> Page wiki_pages_api_destroy_for_groups(group_id, url_or_id)

Delete page

Delete a wiki page

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.page import Page
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
    api_instance = canvas_lms_python_client.WikiPagesApiApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    url_or_id = 'url_or_id_example' # str | Scope response to url_or_id

    try:
        # Delete page
        api_response = await api_instance.wiki_pages_api_destroy_for_groups(group_id, url_or_id)
        print("The response of WikiPagesApiApi->wiki_pages_api_destroy_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WikiPagesApiApi->wiki_pages_api_destroy_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **url_or_id** | **str**| Scope response to url_or_id | 

### Return type

[**Page**](Page.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Page |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wiki_pages_api_duplicate**
> Page wiki_pages_api_duplicate(course_id, url_or_id)

Duplicate page

Duplicate a wiki page

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.page import Page
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
    api_instance = canvas_lms_python_client.WikiPagesApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    url_or_id = 'url_or_id_example' # str | Scope response to url_or_id

    try:
        # Duplicate page
        api_response = await api_instance.wiki_pages_api_duplicate(course_id, url_or_id)
        print("The response of WikiPagesApiApi->wiki_pages_api_duplicate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WikiPagesApiApi->wiki_pages_api_duplicate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **url_or_id** | **str**| Scope response to url_or_id | 

### Return type

[**Page**](Page.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Page |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wiki_pages_api_index**
> List[Page] wiki_pages_api_index(course_id, sort=sort, order=order, search_term=search_term, published=published, include=include, page=page, per_page=per_page)

List pages

A paginated list of the wiki pages associated with a course or group

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.page import Page
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
    api_instance = canvas_lms_python_client.WikiPagesApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    sort = 'sort_example' # str | Sort results by this field. (optional)
    order = 'order_example' # str | The sorting order. Defaults to 'asc'. (optional)
    search_term = 'search_term_example' # str | The partial title of the pages to match and return. (optional)
    published = True # bool | If true, include only published paqes. If false, exclude published pages. If not present, do not filter on published status. (optional)
    include = ['include_example'] # List[str] | - \"body\": Optionally include the page body with each Page. If this is a block_editor page, returns the block_editor_attributes. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List pages
        api_response = await api_instance.wiki_pages_api_index(course_id, sort=sort, order=order, search_term=search_term, published=published, include=include, page=page, per_page=per_page)
        print("The response of WikiPagesApiApi->wiki_pages_api_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WikiPagesApiApi->wiki_pages_api_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **sort** | **str**| Sort results by this field. | [optional] 
 **order** | **str**| The sorting order. Defaults to &#39;asc&#39;. | [optional] 
 **search_term** | **str**| The partial title of the pages to match and return. | [optional] 
 **published** | **bool**| If true, include only published paqes. If false, exclude published pages. If not present, do not filter on published status. | [optional] 
 **include** | [**List[str]**](str.md)| - \&quot;body\&quot;: Optionally include the page body with each Page. If this is a block_editor page, returns the block_editor_attributes. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[Page]**](Page.md)

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

# **wiki_pages_api_index_for_groups**
> List[Page] wiki_pages_api_index_for_groups(group_id, sort=sort, order=order, search_term=search_term, published=published, include=include, page=page, per_page=per_page)

List pages

A paginated list of the wiki pages associated with a course or group

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.page import Page
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
    api_instance = canvas_lms_python_client.WikiPagesApiApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    sort = 'sort_example' # str | Sort results by this field. (optional)
    order = 'order_example' # str | The sorting order. Defaults to 'asc'. (optional)
    search_term = 'search_term_example' # str | The partial title of the pages to match and return. (optional)
    published = True # bool | If true, include only published paqes. If false, exclude published pages. If not present, do not filter on published status. (optional)
    include = ['include_example'] # List[str] | - \"body\": Optionally include the page body with each Page. If this is a block_editor page, returns the block_editor_attributes. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List pages
        api_response = await api_instance.wiki_pages_api_index_for_groups(group_id, sort=sort, order=order, search_term=search_term, published=published, include=include, page=page, per_page=per_page)
        print("The response of WikiPagesApiApi->wiki_pages_api_index_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WikiPagesApiApi->wiki_pages_api_index_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **sort** | **str**| Sort results by this field. | [optional] 
 **order** | **str**| The sorting order. Defaults to &#39;asc&#39;. | [optional] 
 **search_term** | **str**| The partial title of the pages to match and return. | [optional] 
 **published** | **bool**| If true, include only published paqes. If false, exclude published pages. If not present, do not filter on published status. | [optional] 
 **include** | [**List[str]**](str.md)| - \&quot;body\&quot;: Optionally include the page body with each Page. If this is a block_editor page, returns the block_editor_attributes. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[Page]**](Page.md)

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

# **wiki_pages_api_revert**
> PageRevision wiki_pages_api_revert(course_id, revision_id, url_or_id)

Revert to revision

Revert a page to a prior revision.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.page_revision import PageRevision
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
    api_instance = canvas_lms_python_client.WikiPagesApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    revision_id = 'revision_id_example' # str | The revision to revert to (use the {api:WikiPagesApiController#revisions List Revisions API} to see available revisions)
    url_or_id = 'url_or_id_example' # str | Scope response to url_or_id

    try:
        # Revert to revision
        api_response = await api_instance.wiki_pages_api_revert(course_id, revision_id, url_or_id)
        print("The response of WikiPagesApiApi->wiki_pages_api_revert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WikiPagesApiApi->wiki_pages_api_revert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **revision_id** | **str**| The revision to revert to (use the {api:WikiPagesApiController#revisions List Revisions API} to see available revisions) | 
 **url_or_id** | **str**| Scope response to url_or_id | 

### Return type

[**PageRevision**](PageRevision.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | PageRevision |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wiki_pages_api_revert_for_groups**
> PageRevision wiki_pages_api_revert_for_groups(group_id, revision_id, url_or_id)

Revert to revision

Revert a page to a prior revision.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.page_revision import PageRevision
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
    api_instance = canvas_lms_python_client.WikiPagesApiApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    revision_id = 'revision_id_example' # str | The revision to revert to (use the {api:WikiPagesApiController#revisions List Revisions API} to see available revisions)
    url_or_id = 'url_or_id_example' # str | Scope response to url_or_id

    try:
        # Revert to revision
        api_response = await api_instance.wiki_pages_api_revert_for_groups(group_id, revision_id, url_or_id)
        print("The response of WikiPagesApiApi->wiki_pages_api_revert_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WikiPagesApiApi->wiki_pages_api_revert_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **revision_id** | **str**| The revision to revert to (use the {api:WikiPagesApiController#revisions List Revisions API} to see available revisions) | 
 **url_or_id** | **str**| Scope response to url_or_id | 

### Return type

[**PageRevision**](PageRevision.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | PageRevision |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wiki_pages_api_revisions**
> List[PageRevision] wiki_pages_api_revisions(course_id, url_or_id, page=page, per_page=per_page)

List revisions

A paginated list of the revisions of a page. Callers must have update rights on the page in order to see page history.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.page_revision import PageRevision
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
    api_instance = canvas_lms_python_client.WikiPagesApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    url_or_id = 'url_or_id_example' # str | Scope response to url_or_id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List revisions
        api_response = await api_instance.wiki_pages_api_revisions(course_id, url_or_id, page=page, per_page=per_page)
        print("The response of WikiPagesApiApi->wiki_pages_api_revisions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WikiPagesApiApi->wiki_pages_api_revisions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **url_or_id** | **str**| Scope response to url_or_id | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[PageRevision]**](PageRevision.md)

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

# **wiki_pages_api_revisions_for_groups**
> List[PageRevision] wiki_pages_api_revisions_for_groups(group_id, url_or_id, page=page, per_page=per_page)

List revisions

A paginated list of the revisions of a page. Callers must have update rights on the page in order to see page history.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.page_revision import PageRevision
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
    api_instance = canvas_lms_python_client.WikiPagesApiApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    url_or_id = 'url_or_id_example' # str | Scope response to url_or_id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List revisions
        api_response = await api_instance.wiki_pages_api_revisions_for_groups(group_id, url_or_id, page=page, per_page=per_page)
        print("The response of WikiPagesApiApi->wiki_pages_api_revisions_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WikiPagesApiApi->wiki_pages_api_revisions_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **url_or_id** | **str**| Scope response to url_or_id | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[PageRevision]**](PageRevision.md)

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

# **wiki_pages_api_show**
> Page wiki_pages_api_show(course_id, url_or_id)

Show page

Retrieve the content of a wiki page

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.page import Page
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
    api_instance = canvas_lms_python_client.WikiPagesApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    url_or_id = 'url_or_id_example' # str | Scope response to url_or_id

    try:
        # Show page
        api_response = await api_instance.wiki_pages_api_show(course_id, url_or_id)
        print("The response of WikiPagesApiApi->wiki_pages_api_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WikiPagesApiApi->wiki_pages_api_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **url_or_id** | **str**| Scope response to url_or_id | 

### Return type

[**Page**](Page.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Page |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wiki_pages_api_show_for_groups**
> Page wiki_pages_api_show_for_groups(group_id, url_or_id)

Show page

Retrieve the content of a wiki page

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.page import Page
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
    api_instance = canvas_lms_python_client.WikiPagesApiApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    url_or_id = 'url_or_id_example' # str | Scope response to url_or_id

    try:
        # Show page
        api_response = await api_instance.wiki_pages_api_show_for_groups(group_id, url_or_id)
        print("The response of WikiPagesApiApi->wiki_pages_api_show_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WikiPagesApiApi->wiki_pages_api_show_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **url_or_id** | **str**| Scope response to url_or_id | 

### Return type

[**Page**](Page.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Page |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wiki_pages_api_show_front_page**
> Page wiki_pages_api_show_front_page(course_id)

Show front page

Retrieve the content of the front page

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.page import Page
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
    api_instance = canvas_lms_python_client.WikiPagesApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id

    try:
        # Show front page
        api_response = await api_instance.wiki_pages_api_show_front_page(course_id)
        print("The response of WikiPagesApiApi->wiki_pages_api_show_front_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WikiPagesApiApi->wiki_pages_api_show_front_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 

### Return type

[**Page**](Page.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Page |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wiki_pages_api_show_front_page_for_groups**
> Page wiki_pages_api_show_front_page_for_groups(group_id)

Show front page

Retrieve the content of the front page

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.page import Page
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
    api_instance = canvas_lms_python_client.WikiPagesApiApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id

    try:
        # Show front page
        api_response = await api_instance.wiki_pages_api_show_front_page_for_groups(group_id)
        print("The response of WikiPagesApiApi->wiki_pages_api_show_front_page_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WikiPagesApiApi->wiki_pages_api_show_front_page_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 

### Return type

[**Page**](Page.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Page |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wiki_pages_api_show_revision**
> PageRevision wiki_pages_api_show_revision(course_id, url_or_id, summary=summary)

Show revision

Retrieve the metadata and optionally content of a revision of the page.
Note that retrieving historic versions of pages requires edit rights.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.page_revision import PageRevision
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
    api_instance = canvas_lms_python_client.WikiPagesApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    url_or_id = 'url_or_id_example' # str | Scope response to url_or_id
    summary = True # bool | If set, exclude page content from results (optional)

    try:
        # Show revision
        api_response = await api_instance.wiki_pages_api_show_revision(course_id, url_or_id, summary=summary)
        print("The response of WikiPagesApiApi->wiki_pages_api_show_revision:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WikiPagesApiApi->wiki_pages_api_show_revision: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **url_or_id** | **str**| Scope response to url_or_id | 
 **summary** | **bool**| If set, exclude page content from results | [optional] 

### Return type

[**PageRevision**](PageRevision.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | PageRevision |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wiki_pages_api_show_revision_by_revision_id_for_groups**
> PageRevision wiki_pages_api_show_revision_by_revision_id_for_groups(group_id, revision_id, url_or_id, summary=summary)

Show revision

Retrieve the metadata and optionally content of a revision of the page.
Note that retrieving historic versions of pages requires edit rights.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.page_revision import PageRevision
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
    api_instance = canvas_lms_python_client.WikiPagesApiApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    revision_id = 'revision_id_example' # str | Scope response to revision_id
    url_or_id = 'url_or_id_example' # str | Scope response to url_or_id
    summary = True # bool | If set, exclude page content from results (optional)

    try:
        # Show revision
        api_response = await api_instance.wiki_pages_api_show_revision_by_revision_id_for_groups(group_id, revision_id, url_or_id, summary=summary)
        print("The response of WikiPagesApiApi->wiki_pages_api_show_revision_by_revision_id_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WikiPagesApiApi->wiki_pages_api_show_revision_by_revision_id_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **revision_id** | **str**| Scope response to revision_id | 
 **url_or_id** | **str**| Scope response to url_or_id | 
 **summary** | **bool**| If set, exclude page content from results | [optional] 

### Return type

[**PageRevision**](PageRevision.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | PageRevision |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wiki_pages_api_show_revision_for_courses**
> PageRevision wiki_pages_api_show_revision_for_courses(course_id, revision_id, url_or_id, summary=summary)

Show revision

Retrieve the metadata and optionally content of a revision of the page.
Note that retrieving historic versions of pages requires edit rights.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.page_revision import PageRevision
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
    api_instance = canvas_lms_python_client.WikiPagesApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    revision_id = 'revision_id_example' # str | Scope response to revision_id
    url_or_id = 'url_or_id_example' # str | Scope response to url_or_id
    summary = True # bool | If set, exclude page content from results (optional)

    try:
        # Show revision
        api_response = await api_instance.wiki_pages_api_show_revision_for_courses(course_id, revision_id, url_or_id, summary=summary)
        print("The response of WikiPagesApiApi->wiki_pages_api_show_revision_for_courses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WikiPagesApiApi->wiki_pages_api_show_revision_for_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **revision_id** | **str**| Scope response to revision_id | 
 **url_or_id** | **str**| Scope response to url_or_id | 
 **summary** | **bool**| If set, exclude page content from results | [optional] 

### Return type

[**PageRevision**](PageRevision.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | PageRevision |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wiki_pages_api_show_revision_for_groups**
> PageRevision wiki_pages_api_show_revision_for_groups(group_id, url_or_id, summary=summary)

Show revision

Retrieve the metadata and optionally content of a revision of the page.
Note that retrieving historic versions of pages requires edit rights.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.page_revision import PageRevision
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
    api_instance = canvas_lms_python_client.WikiPagesApiApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    url_or_id = 'url_or_id_example' # str | Scope response to url_or_id
    summary = True # bool | If set, exclude page content from results (optional)

    try:
        # Show revision
        api_response = await api_instance.wiki_pages_api_show_revision_for_groups(group_id, url_or_id, summary=summary)
        print("The response of WikiPagesApiApi->wiki_pages_api_show_revision_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WikiPagesApiApi->wiki_pages_api_show_revision_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **url_or_id** | **str**| Scope response to url_or_id | 
 **summary** | **bool**| If set, exclude page content from results | [optional] 

### Return type

[**PageRevision**](PageRevision.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | PageRevision |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wiki_pages_api_update**
> Page wiki_pages_api_update(course_id, url_or_id, wiki_pages_api_update_request=wiki_pages_api_update_request)

Update/create page

Update the title or contents of a wiki page

NOTE: You cannot specify the ID when creating a page. If you pass a numeric value
as the page identifier and that does not represent a page ID that already
exists, it will be interpreted as a URL.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.page import Page
from canvas_lms_python_client.models.wiki_pages_api_update_request import WikiPagesApiUpdateRequest
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
    api_instance = canvas_lms_python_client.WikiPagesApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    url_or_id = 'url_or_id_example' # str | Scope response to url_or_id
    wiki_pages_api_update_request = canvas_lms_python_client.WikiPagesApiUpdateRequest() # WikiPagesApiUpdateRequest | Request body parameters  **Example Request:** ``` curl -X PUT -H 'Authorization: Bearer <token>' \\ https://<canvas>/api/v1/courses/123/pages/the-page-identifier \\ -d 'wiki_page[body]=Updated+body+text' ``` (optional)

    try:
        # Update/create page
        api_response = await api_instance.wiki_pages_api_update(course_id, url_or_id, wiki_pages_api_update_request=wiki_pages_api_update_request)
        print("The response of WikiPagesApiApi->wiki_pages_api_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WikiPagesApiApi->wiki_pages_api_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **url_or_id** | **str**| Scope response to url_or_id | 
 **wiki_pages_api_update_request** | [**WikiPagesApiUpdateRequest**](WikiPagesApiUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl -X PUT -H &#39;Authorization: Bearer &lt;token&gt;&#39; \\ https://&lt;canvas&gt;/api/v1/courses/123/pages/the-page-identifier \\ -d &#39;wiki_page[body]&#x3D;Updated+body+text&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**Page**](Page.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Page |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wiki_pages_api_update_for_groups**
> Page wiki_pages_api_update_for_groups(group_id, url_or_id, wiki_pages_api_update_request=wiki_pages_api_update_request)

Update/create page

Update the title or contents of a wiki page

NOTE: You cannot specify the ID when creating a page. If you pass a numeric value
as the page identifier and that does not represent a page ID that already
exists, it will be interpreted as a URL.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.page import Page
from canvas_lms_python_client.models.wiki_pages_api_update_request import WikiPagesApiUpdateRequest
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
    api_instance = canvas_lms_python_client.WikiPagesApiApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    url_or_id = 'url_or_id_example' # str | Scope response to url_or_id
    wiki_pages_api_update_request = canvas_lms_python_client.WikiPagesApiUpdateRequest() # WikiPagesApiUpdateRequest | Request body parameters  **Example Request:** ``` curl -X PUT -H 'Authorization: Bearer <token>' \\ https://<canvas>/api/v1/courses/123/pages/the-page-identifier \\ -d 'wiki_page[body]=Updated+body+text' ``` (optional)

    try:
        # Update/create page
        api_response = await api_instance.wiki_pages_api_update_for_groups(group_id, url_or_id, wiki_pages_api_update_request=wiki_pages_api_update_request)
        print("The response of WikiPagesApiApi->wiki_pages_api_update_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WikiPagesApiApi->wiki_pages_api_update_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **url_or_id** | **str**| Scope response to url_or_id | 
 **wiki_pages_api_update_request** | [**WikiPagesApiUpdateRequest**](WikiPagesApiUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl -X PUT -H &#39;Authorization: Bearer &lt;token&gt;&#39; \\ https://&lt;canvas&gt;/api/v1/courses/123/pages/the-page-identifier \\ -d &#39;wiki_page[body]&#x3D;Updated+body+text&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**Page**](Page.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Page |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wiki_pages_api_update_front_page**
> Page wiki_pages_api_update_front_page(course_id, wiki_pages_api_update_front_page_request=wiki_pages_api_update_front_page_request)

Update/create front page

Update the title or contents of the front page

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.page import Page
from canvas_lms_python_client.models.wiki_pages_api_update_front_page_request import WikiPagesApiUpdateFrontPageRequest
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
    api_instance = canvas_lms_python_client.WikiPagesApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    wiki_pages_api_update_front_page_request = canvas_lms_python_client.WikiPagesApiUpdateFrontPageRequest() # WikiPagesApiUpdateFrontPageRequest | Request body parameters  **Example Request:** ``` curl -X PUT -H 'Authorization: Bearer <token>' \\ https://<canvas>/api/v1/courses/123/front_page \\ -d wiki_page[body]=Updated+body+text ``` (optional)

    try:
        # Update/create front page
        api_response = await api_instance.wiki_pages_api_update_front_page(course_id, wiki_pages_api_update_front_page_request=wiki_pages_api_update_front_page_request)
        print("The response of WikiPagesApiApi->wiki_pages_api_update_front_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WikiPagesApiApi->wiki_pages_api_update_front_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **wiki_pages_api_update_front_page_request** | [**WikiPagesApiUpdateFrontPageRequest**](WikiPagesApiUpdateFrontPageRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl -X PUT -H &#39;Authorization: Bearer &lt;token&gt;&#39; \\ https://&lt;canvas&gt;/api/v1/courses/123/front_page \\ -d wiki_page[body]&#x3D;Updated+body+text &#x60;&#x60;&#x60; | [optional] 

### Return type

[**Page**](Page.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Page |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wiki_pages_api_update_front_page_for_groups**
> Page wiki_pages_api_update_front_page_for_groups(group_id, wiki_pages_api_update_front_page_request=wiki_pages_api_update_front_page_request)

Update/create front page

Update the title or contents of the front page

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.page import Page
from canvas_lms_python_client.models.wiki_pages_api_update_front_page_request import WikiPagesApiUpdateFrontPageRequest
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
    api_instance = canvas_lms_python_client.WikiPagesApiApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    wiki_pages_api_update_front_page_request = canvas_lms_python_client.WikiPagesApiUpdateFrontPageRequest() # WikiPagesApiUpdateFrontPageRequest | Request body parameters  **Example Request:** ``` curl -X PUT -H 'Authorization: Bearer <token>' \\ https://<canvas>/api/v1/courses/123/front_page \\ -d wiki_page[body]=Updated+body+text ``` (optional)

    try:
        # Update/create front page
        api_response = await api_instance.wiki_pages_api_update_front_page_for_groups(group_id, wiki_pages_api_update_front_page_request=wiki_pages_api_update_front_page_request)
        print("The response of WikiPagesApiApi->wiki_pages_api_update_front_page_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WikiPagesApiApi->wiki_pages_api_update_front_page_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **wiki_pages_api_update_front_page_request** | [**WikiPagesApiUpdateFrontPageRequest**](WikiPagesApiUpdateFrontPageRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl -X PUT -H &#39;Authorization: Bearer &lt;token&gt;&#39; \\ https://&lt;canvas&gt;/api/v1/courses/123/front_page \\ -d wiki_page[body]&#x3D;Updated+body+text &#x60;&#x60;&#x60; | [optional] 

### Return type

[**Page**](Page.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Page |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

