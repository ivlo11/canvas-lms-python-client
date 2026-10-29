# canvas_lms_python_client.MediaTracksApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**media_tracks_index**](MediaTracksApi.md#media_tracks_index) | **GET** /api/v1/media_objects/{media_object_id}/media_tracks | List media tracks for a Media Object or Attachment
[**media_tracks_index_for_other**](MediaTracksApi.md#media_tracks_index_for_other) | **GET** /api/v1/media_attachments/{attachment_id}/media_tracks | List media tracks for a Media Object or Attachment
[**media_tracks_update**](MediaTracksApi.md#media_tracks_update) | **PUT** /api/v1/media_objects/{media_object_id}/media_tracks | Update Media Tracks
[**media_tracks_update_for_other**](MediaTracksApi.md#media_tracks_update_for_other) | **PUT** /api/v1/media_attachments/{attachment_id}/media_tracks | Update Media Tracks


# **media_tracks_index**
> List[object] media_tracks_index(media_object_id, include=include)

List media tracks for a Media Object or Attachment

List the media tracks associated with a media object or attachment

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
    api_instance = canvas_lms_python_client.MediaTracksApi(api_client)
    media_object_id = 'media_object_id_example' # str | Scope response to media_object_id
    include = ['include_example'] # List[str] | By default, index returns id, locale, kind, media_object_id, and user_id for each of the result MediaTracks. Use include[] to add additional fields. For example include[]=content (optional)

    try:
        # List media tracks for a Media Object or Attachment
        api_response = await api_instance.media_tracks_index(media_object_id, include=include)
        print("The response of MediaTracksApi->media_tracks_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaTracksApi->media_tracks_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **media_object_id** | **str**| Scope response to media_object_id | 
 **include** | [**List[str]**](str.md)| By default, index returns id, locale, kind, media_object_id, and user_id for each of the result MediaTracks. Use include[] to add additional fields. For example include[]&#x3D;content | [optional] 

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

# **media_tracks_index_for_other**
> List[object] media_tracks_index_for_other(attachment_id, include=include)

List media tracks for a Media Object or Attachment

List the media tracks associated with a media object or attachment

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
    api_instance = canvas_lms_python_client.MediaTracksApi(api_client)
    attachment_id = 'attachment_id_example' # str | Scope response to attachment_id
    include = ['include_example'] # List[str] | By default, index returns id, locale, kind, media_object_id, and user_id for each of the result MediaTracks. Use include[] to add additional fields. For example include[]=content (optional)

    try:
        # List media tracks for a Media Object or Attachment
        api_response = await api_instance.media_tracks_index_for_other(attachment_id, include=include)
        print("The response of MediaTracksApi->media_tracks_index_for_other:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaTracksApi->media_tracks_index_for_other: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | **str**| Scope response to attachment_id | 
 **include** | [**List[str]**](str.md)| By default, index returns id, locale, kind, media_object_id, and user_id for each of the result MediaTracks. Use include[] to add additional fields. For example include[]&#x3D;content | [optional] 

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

# **media_tracks_update**
> List[object] media_tracks_update(media_object_id, media_tracks_update_request=media_tracks_update_request)

Update Media Tracks

Replace the media tracks associated with a media object or attachment with
the array of tracks provided in the body.
Update will
delete any existing tracks not listed,
leave untouched any tracks with no content field,
and update or create tracks with a content field.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.media_tracks_update_request import MediaTracksUpdateRequest
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
    api_instance = canvas_lms_python_client.MediaTracksApi(api_client)
    media_object_id = 'media_object_id_example' # str | Scope response to media_object_id
    media_tracks_update_request = canvas_lms_python_client.MediaTracksUpdateRequest() # MediaTracksUpdateRequest | Request body parameters  **Example Request:** ``` curl -X PUT https://<canvas>/api/v1/media_objects/<media_object_id>/media_tracks?include[]=content \\   -H 'Authorization: Bearer <token>'   -d '[{\"locale\": \"en\"}, {\"locale\": \"af\",\"content\": \"1\\r\\n00:00:00,000 --> 00:00:01,251\\r\\nThis is the content\\r\\n\"}]' ``` (optional)

    try:
        # Update Media Tracks
        api_response = await api_instance.media_tracks_update(media_object_id, media_tracks_update_request=media_tracks_update_request)
        print("The response of MediaTracksApi->media_tracks_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaTracksApi->media_tracks_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **media_object_id** | **str**| Scope response to media_object_id | 
 **media_tracks_update_request** | [**MediaTracksUpdateRequest**](MediaTracksUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl -X PUT https://&lt;canvas&gt;/api/v1/media_objects/&lt;media_object_id&gt;/media_tracks?include[]&#x3D;content \\   -H &#39;Authorization: Bearer &lt;token&gt;&#39;   -d &#39;[{\&quot;locale\&quot;: \&quot;en\&quot;}, {\&quot;locale\&quot;: \&quot;af\&quot;,\&quot;content\&quot;: \&quot;1\\r\\n00:00:00,000 --&gt; 00:00:01,251\\r\\nThis is the content\\r\\n\&quot;}]&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

**List[object]**

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

# **media_tracks_update_for_other**
> List[object] media_tracks_update_for_other(attachment_id, media_tracks_update_request=media_tracks_update_request)

Update Media Tracks

Replace the media tracks associated with a media object or attachment with
the array of tracks provided in the body.
Update will
delete any existing tracks not listed,
leave untouched any tracks with no content field,
and update or create tracks with a content field.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.media_tracks_update_request import MediaTracksUpdateRequest
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
    api_instance = canvas_lms_python_client.MediaTracksApi(api_client)
    attachment_id = 'attachment_id_example' # str | Scope response to attachment_id
    media_tracks_update_request = canvas_lms_python_client.MediaTracksUpdateRequest() # MediaTracksUpdateRequest | Request body parameters  **Example Request:** ``` curl -X PUT https://<canvas>/api/v1/media_objects/<media_object_id>/media_tracks?include[]=content \\   -H 'Authorization: Bearer <token>'   -d '[{\"locale\": \"en\"}, {\"locale\": \"af\",\"content\": \"1\\r\\n00:00:00,000 --> 00:00:01,251\\r\\nThis is the content\\r\\n\"}]' ``` (optional)

    try:
        # Update Media Tracks
        api_response = await api_instance.media_tracks_update_for_other(attachment_id, media_tracks_update_request=media_tracks_update_request)
        print("The response of MediaTracksApi->media_tracks_update_for_other:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaTracksApi->media_tracks_update_for_other: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | **str**| Scope response to attachment_id | 
 **media_tracks_update_request** | [**MediaTracksUpdateRequest**](MediaTracksUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl -X PUT https://&lt;canvas&gt;/api/v1/media_objects/&lt;media_object_id&gt;/media_tracks?include[]&#x3D;content \\   -H &#39;Authorization: Bearer &lt;token&gt;&#39;   -d &#39;[{\&quot;locale\&quot;: \&quot;en\&quot;}, {\&quot;locale\&quot;: \&quot;af\&quot;,\&quot;content\&quot;: \&quot;1\\r\\n00:00:00,000 --&gt; 00:00:01,251\\r\\nThis is the content\\r\\n\&quot;}]&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

**List[object]**

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

