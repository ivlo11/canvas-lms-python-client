# canvas_lms_python_client.MediaObjectsApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**media_objects_index**](MediaObjectsApi.md#media_objects_index) | **GET** /api/v1/media_objects | List Media Objects
[**media_objects_index_by_media_attachments_for_courses**](MediaObjectsApi.md#media_objects_index_by_media_attachments_for_courses) | **GET** /api/v1/courses/{course_id}/media_attachments | List Media Objects
[**media_objects_index_by_media_attachments_for_groups**](MediaObjectsApi.md#media_objects_index_by_media_attachments_for_groups) | **GET** /api/v1/groups/{group_id}/media_attachments | List Media Objects
[**media_objects_index_for_courses**](MediaObjectsApi.md#media_objects_index_for_courses) | **GET** /api/v1/courses/{course_id}/media_objects | List Media Objects
[**media_objects_index_for_groups**](MediaObjectsApi.md#media_objects_index_for_groups) | **GET** /api/v1/groups/{group_id}/media_objects | List Media Objects
[**media_objects_index_for_other**](MediaObjectsApi.md#media_objects_index_for_other) | **GET** /api/v1/media_attachments | List Media Objects
[**media_objects_update_media_object**](MediaObjectsApi.md#media_objects_update_media_object) | **PUT** /api/v1/media_objects/{media_object_id} | Update Media Object
[**media_objects_update_media_object_for_other**](MediaObjectsApi.md#media_objects_update_media_object_for_other) | **PUT** /api/v1/media_attachments/{attachment_id} | Update Media Object


# **media_objects_index**
> List[MediaObject] media_objects_index(sort=sort, order=order, exclude=exclude, page=page, per_page=per_page)

List Media Objects

Returns media objects created by the user making the request. When
using the second version, returns media objects associated with
the given course.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.media_object import MediaObject
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
    api_instance = canvas_lms_python_client.MediaObjectsApi(api_client)
    sort = 'sort_example' # str | Field to sort on. Default is \"title\"  title:: sorts on user_entered_title if available, title if not.  created_at:: sorts on the object's creation time. (optional)
    order = 'order_example' # str | Sort direction. Default is \"asc\" (optional)
    exclude = ['exclude_example'] # List[str] | Array of data to exclude. By excluding \"sources\" and \"tracks\", the api will not need to query kaltura, which greatly speeds up its response.  sources:: Do not query kaltura for media_sources tracks:: Do not query kaltura for media_tracks (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List Media Objects
        api_response = await api_instance.media_objects_index(sort=sort, order=order, exclude=exclude, page=page, per_page=per_page)
        print("The response of MediaObjectsApi->media_objects_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaObjectsApi->media_objects_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| Field to sort on. Default is \&quot;title\&quot;  title:: sorts on user_entered_title if available, title if not.  created_at:: sorts on the object&#39;s creation time. | [optional] 
 **order** | **str**| Sort direction. Default is \&quot;asc\&quot; | [optional] 
 **exclude** | [**List[str]**](str.md)| Array of data to exclude. By excluding \&quot;sources\&quot; and \&quot;tracks\&quot;, the api will not need to query kaltura, which greatly speeds up its response.  sources:: Do not query kaltura for media_sources tracks:: Do not query kaltura for media_tracks | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[MediaObject]**](MediaObject.md)

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

# **media_objects_index_by_media_attachments_for_courses**
> List[MediaObject] media_objects_index_by_media_attachments_for_courses(course_id, sort=sort, order=order, exclude=exclude, page=page, per_page=per_page)

List Media Objects

Returns media objects created by the user making the request. When
using the second version, returns media objects associated with
the given course.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.media_object import MediaObject
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
    api_instance = canvas_lms_python_client.MediaObjectsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    sort = 'sort_example' # str | Field to sort on. Default is \"title\"  title:: sorts on user_entered_title if available, title if not.  created_at:: sorts on the object's creation time. (optional)
    order = 'order_example' # str | Sort direction. Default is \"asc\" (optional)
    exclude = ['exclude_example'] # List[str] | Array of data to exclude. By excluding \"sources\" and \"tracks\", the api will not need to query kaltura, which greatly speeds up its response.  sources:: Do not query kaltura for media_sources tracks:: Do not query kaltura for media_tracks (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List Media Objects
        api_response = await api_instance.media_objects_index_by_media_attachments_for_courses(course_id, sort=sort, order=order, exclude=exclude, page=page, per_page=per_page)
        print("The response of MediaObjectsApi->media_objects_index_by_media_attachments_for_courses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaObjectsApi->media_objects_index_by_media_attachments_for_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **sort** | **str**| Field to sort on. Default is \&quot;title\&quot;  title:: sorts on user_entered_title if available, title if not.  created_at:: sorts on the object&#39;s creation time. | [optional] 
 **order** | **str**| Sort direction. Default is \&quot;asc\&quot; | [optional] 
 **exclude** | [**List[str]**](str.md)| Array of data to exclude. By excluding \&quot;sources\&quot; and \&quot;tracks\&quot;, the api will not need to query kaltura, which greatly speeds up its response.  sources:: Do not query kaltura for media_sources tracks:: Do not query kaltura for media_tracks | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[MediaObject]**](MediaObject.md)

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

# **media_objects_index_by_media_attachments_for_groups**
> List[MediaObject] media_objects_index_by_media_attachments_for_groups(group_id, sort=sort, order=order, exclude=exclude, page=page, per_page=per_page)

List Media Objects

Returns media objects created by the user making the request. When
using the second version, returns media objects associated with
the given course.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.media_object import MediaObject
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
    api_instance = canvas_lms_python_client.MediaObjectsApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    sort = 'sort_example' # str | Field to sort on. Default is \"title\"  title:: sorts on user_entered_title if available, title if not.  created_at:: sorts on the object's creation time. (optional)
    order = 'order_example' # str | Sort direction. Default is \"asc\" (optional)
    exclude = ['exclude_example'] # List[str] | Array of data to exclude. By excluding \"sources\" and \"tracks\", the api will not need to query kaltura, which greatly speeds up its response.  sources:: Do not query kaltura for media_sources tracks:: Do not query kaltura for media_tracks (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List Media Objects
        api_response = await api_instance.media_objects_index_by_media_attachments_for_groups(group_id, sort=sort, order=order, exclude=exclude, page=page, per_page=per_page)
        print("The response of MediaObjectsApi->media_objects_index_by_media_attachments_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaObjectsApi->media_objects_index_by_media_attachments_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **sort** | **str**| Field to sort on. Default is \&quot;title\&quot;  title:: sorts on user_entered_title if available, title if not.  created_at:: sorts on the object&#39;s creation time. | [optional] 
 **order** | **str**| Sort direction. Default is \&quot;asc\&quot; | [optional] 
 **exclude** | [**List[str]**](str.md)| Array of data to exclude. By excluding \&quot;sources\&quot; and \&quot;tracks\&quot;, the api will not need to query kaltura, which greatly speeds up its response.  sources:: Do not query kaltura for media_sources tracks:: Do not query kaltura for media_tracks | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[MediaObject]**](MediaObject.md)

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

# **media_objects_index_for_courses**
> List[MediaObject] media_objects_index_for_courses(course_id, sort=sort, order=order, exclude=exclude, page=page, per_page=per_page)

List Media Objects

Returns media objects created by the user making the request. When
using the second version, returns media objects associated with
the given course.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.media_object import MediaObject
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
    api_instance = canvas_lms_python_client.MediaObjectsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    sort = 'sort_example' # str | Field to sort on. Default is \"title\"  title:: sorts on user_entered_title if available, title if not.  created_at:: sorts on the object's creation time. (optional)
    order = 'order_example' # str | Sort direction. Default is \"asc\" (optional)
    exclude = ['exclude_example'] # List[str] | Array of data to exclude. By excluding \"sources\" and \"tracks\", the api will not need to query kaltura, which greatly speeds up its response.  sources:: Do not query kaltura for media_sources tracks:: Do not query kaltura for media_tracks (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List Media Objects
        api_response = await api_instance.media_objects_index_for_courses(course_id, sort=sort, order=order, exclude=exclude, page=page, per_page=per_page)
        print("The response of MediaObjectsApi->media_objects_index_for_courses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaObjectsApi->media_objects_index_for_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **sort** | **str**| Field to sort on. Default is \&quot;title\&quot;  title:: sorts on user_entered_title if available, title if not.  created_at:: sorts on the object&#39;s creation time. | [optional] 
 **order** | **str**| Sort direction. Default is \&quot;asc\&quot; | [optional] 
 **exclude** | [**List[str]**](str.md)| Array of data to exclude. By excluding \&quot;sources\&quot; and \&quot;tracks\&quot;, the api will not need to query kaltura, which greatly speeds up its response.  sources:: Do not query kaltura for media_sources tracks:: Do not query kaltura for media_tracks | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[MediaObject]**](MediaObject.md)

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

# **media_objects_index_for_groups**
> List[MediaObject] media_objects_index_for_groups(group_id, sort=sort, order=order, exclude=exclude, page=page, per_page=per_page)

List Media Objects

Returns media objects created by the user making the request. When
using the second version, returns media objects associated with
the given course.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.media_object import MediaObject
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
    api_instance = canvas_lms_python_client.MediaObjectsApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    sort = 'sort_example' # str | Field to sort on. Default is \"title\"  title:: sorts on user_entered_title if available, title if not.  created_at:: sorts on the object's creation time. (optional)
    order = 'order_example' # str | Sort direction. Default is \"asc\" (optional)
    exclude = ['exclude_example'] # List[str] | Array of data to exclude. By excluding \"sources\" and \"tracks\", the api will not need to query kaltura, which greatly speeds up its response.  sources:: Do not query kaltura for media_sources tracks:: Do not query kaltura for media_tracks (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List Media Objects
        api_response = await api_instance.media_objects_index_for_groups(group_id, sort=sort, order=order, exclude=exclude, page=page, per_page=per_page)
        print("The response of MediaObjectsApi->media_objects_index_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaObjectsApi->media_objects_index_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **sort** | **str**| Field to sort on. Default is \&quot;title\&quot;  title:: sorts on user_entered_title if available, title if not.  created_at:: sorts on the object&#39;s creation time. | [optional] 
 **order** | **str**| Sort direction. Default is \&quot;asc\&quot; | [optional] 
 **exclude** | [**List[str]**](str.md)| Array of data to exclude. By excluding \&quot;sources\&quot; and \&quot;tracks\&quot;, the api will not need to query kaltura, which greatly speeds up its response.  sources:: Do not query kaltura for media_sources tracks:: Do not query kaltura for media_tracks | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[MediaObject]**](MediaObject.md)

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

# **media_objects_index_for_other**
> List[MediaObject] media_objects_index_for_other(sort=sort, order=order, exclude=exclude, page=page, per_page=per_page)

List Media Objects

Returns media objects created by the user making the request. When
using the second version, returns media objects associated with
the given course.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.media_object import MediaObject
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
    api_instance = canvas_lms_python_client.MediaObjectsApi(api_client)
    sort = 'sort_example' # str | Field to sort on. Default is \"title\"  title:: sorts on user_entered_title if available, title if not.  created_at:: sorts on the object's creation time. (optional)
    order = 'order_example' # str | Sort direction. Default is \"asc\" (optional)
    exclude = ['exclude_example'] # List[str] | Array of data to exclude. By excluding \"sources\" and \"tracks\", the api will not need to query kaltura, which greatly speeds up its response.  sources:: Do not query kaltura for media_sources tracks:: Do not query kaltura for media_tracks (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List Media Objects
        api_response = await api_instance.media_objects_index_for_other(sort=sort, order=order, exclude=exclude, page=page, per_page=per_page)
        print("The response of MediaObjectsApi->media_objects_index_for_other:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaObjectsApi->media_objects_index_for_other: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| Field to sort on. Default is \&quot;title\&quot;  title:: sorts on user_entered_title if available, title if not.  created_at:: sorts on the object&#39;s creation time. | [optional] 
 **order** | **str**| Sort direction. Default is \&quot;asc\&quot; | [optional] 
 **exclude** | [**List[str]**](str.md)| Array of data to exclude. By excluding \&quot;sources\&quot; and \&quot;tracks\&quot;, the api will not need to query kaltura, which greatly speeds up its response.  sources:: Do not query kaltura for media_sources tracks:: Do not query kaltura for media_tracks | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[MediaObject]**](MediaObject.md)

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

# **media_objects_update_media_object**
> MediaObject media_objects_update_media_object(media_object_id, media_objects_update_media_object_request=media_objects_update_media_object_request)

Update Media Object

Updates the title of a media object.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.media_object import MediaObject
from canvas_lms_python_client.models.media_objects_update_media_object_request import MediaObjectsUpdateMediaObjectRequest
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
    api_instance = canvas_lms_python_client.MediaObjectsApi(api_client)
    media_object_id = 'media_object_id_example' # str | Scope response to media_object_id
    media_objects_update_media_object_request = canvas_lms_python_client.MediaObjectsUpdateMediaObjectRequest() # MediaObjectsUpdateMediaObjectRequest | Request body parameters (optional)

    try:
        # Update Media Object
        api_response = await api_instance.media_objects_update_media_object(media_object_id, media_objects_update_media_object_request=media_objects_update_media_object_request)
        print("The response of MediaObjectsApi->media_objects_update_media_object:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaObjectsApi->media_objects_update_media_object: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **media_object_id** | **str**| Scope response to media_object_id | 
 **media_objects_update_media_object_request** | [**MediaObjectsUpdateMediaObjectRequest**](MediaObjectsUpdateMediaObjectRequest.md)| Request body parameters | [optional] 

### Return type

[**MediaObject**](MediaObject.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | MediaObject |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **media_objects_update_media_object_for_other**
> MediaObject media_objects_update_media_object_for_other(attachment_id, media_objects_update_media_object_request=media_objects_update_media_object_request)

Update Media Object

Updates the title of a media object.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.media_object import MediaObject
from canvas_lms_python_client.models.media_objects_update_media_object_request import MediaObjectsUpdateMediaObjectRequest
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
    api_instance = canvas_lms_python_client.MediaObjectsApi(api_client)
    attachment_id = 'attachment_id_example' # str | Scope response to attachment_id
    media_objects_update_media_object_request = canvas_lms_python_client.MediaObjectsUpdateMediaObjectRequest() # MediaObjectsUpdateMediaObjectRequest | Request body parameters (optional)

    try:
        # Update Media Object
        api_response = await api_instance.media_objects_update_media_object_for_other(attachment_id, media_objects_update_media_object_request=media_objects_update_media_object_request)
        print("The response of MediaObjectsApi->media_objects_update_media_object_for_other:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaObjectsApi->media_objects_update_media_object_for_other: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | **str**| Scope response to attachment_id | 
 **media_objects_update_media_object_request** | [**MediaObjectsUpdateMediaObjectRequest**](MediaObjectsUpdateMediaObjectRequest.md)| Request body parameters | [optional] 

### Return type

[**MediaObject**](MediaObject.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | MediaObject |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

