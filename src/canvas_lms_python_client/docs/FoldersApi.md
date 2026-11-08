# canvas_lms_python_client.FoldersApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**folders_api_destroy**](FoldersApi.md#folders_api_destroy) | **DELETE** /api/v1/folders/{id} | Delete folder
[**folders_api_index**](FoldersApi.md#folders_api_index) | **GET** /api/v1/folders/{folder_id}/folders | List folders
[**folders_copy_file**](FoldersApi.md#folders_copy_file) | **POST** /api/v1/folders/{dest_folder_id}/copy_file | Copy a file
[**folders_copy_folder**](FoldersApi.md#folders_copy_folder) | **POST** /api/v1/folders/{dest_folder_id}/copy_folder | Copy a folder
[**folders_create**](FoldersApi.md#folders_create) | **POST** /api/v1/courses/{course_id}/folders | Create folder
[**folders_create_file**](FoldersApi.md#folders_create_file) | **POST** /api/v1/folders/{folder_id}/files | Upload a file
[**folders_create_for_accounts**](FoldersApi.md#folders_create_for_accounts) | **POST** /api/v1/accounts/{account_id}/folders | Create folder
[**folders_create_for_groups**](FoldersApi.md#folders_create_for_groups) | **POST** /api/v1/groups/{group_id}/folders | Create folder
[**folders_create_for_other**](FoldersApi.md#folders_create_for_other) | **POST** /api/v1/folders/{folder_id}/folders | Create folder
[**folders_create_for_users**](FoldersApi.md#folders_create_for_users) | **POST** /api/v1/users/{user_id}/folders | Create folder
[**folders_list_all_folders**](FoldersApi.md#folders_list_all_folders) | **GET** /api/v1/courses/{course_id}/folders | List all folders
[**folders_list_all_folders_for_groups**](FoldersApi.md#folders_list_all_folders_for_groups) | **GET** /api/v1/groups/{group_id}/folders | List all folders
[**folders_list_all_folders_for_users**](FoldersApi.md#folders_list_all_folders_for_users) | **GET** /api/v1/users/{user_id}/folders | List all folders
[**folders_media_folder**](FoldersApi.md#folders_media_folder) | **GET** /api/v1/courses/{course_id}/folders/media | Get uploaded media folder for user
[**folders_media_folder_for_groups**](FoldersApi.md#folders_media_folder_for_groups) | **GET** /api/v1/groups/{group_id}/folders/media | Get uploaded media folder for user
[**folders_resolve_path**](FoldersApi.md#folders_resolve_path) | **GET** /api/v1/courses/{course_id}/folders/by_path/*full_path | Resolve path
[**folders_resolve_path_by_by_path_for_groups**](FoldersApi.md#folders_resolve_path_by_by_path_for_groups) | **GET** /api/v1/groups/{group_id}/folders/by_path | Resolve path
[**folders_resolve_path_by_by_path_for_users**](FoldersApi.md#folders_resolve_path_by_by_path_for_users) | **GET** /api/v1/users/{user_id}/folders/by_path | Resolve path
[**folders_resolve_path_for_courses**](FoldersApi.md#folders_resolve_path_for_courses) | **GET** /api/v1/courses/{course_id}/folders/by_path | Resolve path
[**folders_resolve_path_for_groups**](FoldersApi.md#folders_resolve_path_for_groups) | **GET** /api/v1/groups/{group_id}/folders/by_path/*full_path | Resolve path
[**folders_resolve_path_for_users**](FoldersApi.md#folders_resolve_path_for_users) | **GET** /api/v1/users/{user_id}/folders/by_path/*full_path | Resolve path
[**folders_show**](FoldersApi.md#folders_show) | **GET** /api/v1/courses/{course_id}/folders/{id} | Get folder
[**folders_show_for_groups**](FoldersApi.md#folders_show_for_groups) | **GET** /api/v1/groups/{group_id}/folders/{id} | Get folder
[**folders_show_for_other**](FoldersApi.md#folders_show_for_other) | **GET** /api/v1/folders/{id} | Get folder
[**folders_show_for_users**](FoldersApi.md#folders_show_for_users) | **GET** /api/v1/users/{user_id}/folders/{id} | Get folder
[**folders_update**](FoldersApi.md#folders_update) | **PUT** /api/v1/folders/{id} | Update folder


# **folders_api_destroy**
> Folder folders_api_destroy(id, force=force)

Delete folder

Remove the specified folder. You can only delete empty folders unless you
set the 'force' flag

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.folder import Folder
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
    api_instance = canvas_lms_python_client.FoldersApi(api_client)
    id = 'id_example' # str | Scope response to id
    force = True # bool | Set to 'true' to allow deleting a non-empty folder (optional)

    try:
        # Delete folder
        api_response = await api_instance.folders_api_destroy(id, force=force)
        print("The response of FoldersApi->folders_api_destroy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->folders_api_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **force** | **bool**| Set to &#39;true&#39; to allow deleting a non-empty folder | [optional] 

### Return type

[**Folder**](Folder.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Folder |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folders_api_index**
> List[Folder] folders_api_index(folder_id, page=page, per_page=per_page)

List folders

Returns the paginated list of folders in the folder.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.folder import Folder
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
    api_instance = canvas_lms_python_client.FoldersApi(api_client)
    folder_id = 'folder_id_example' # str | Scope response to id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List folders
        api_response = await api_instance.folders_api_index(folder_id, page=page, per_page=per_page)
        print("The response of FoldersApi->folders_api_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->folders_api_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**| Scope response to id | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[Folder]**](Folder.md)

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

# **folders_copy_file**
> File folders_copy_file(dest_folder_id, folders_copy_file_request=folders_copy_file_request)

Copy a file

Copy a file from elsewhere in Canvas into a folder.

Copying a file across contexts (between courses and users) is permitted,
but the source and destination must belong to the same institution.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.file import File
from canvas_lms_python_client.models.folders_copy_file_request import FoldersCopyFileRequest
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
    api_instance = canvas_lms_python_client.FoldersApi(api_client)
    dest_folder_id = 'dest_folder_id_example' # str | Scope response to dest_folder_id
    folders_copy_file_request = canvas_lms_python_client.FoldersCopyFileRequest() # FoldersCopyFileRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/folders/123/copy_file' \\      -H 'Authorization: Bearer <token>'      -F 'source_file_id=456' ``` (optional)

    try:
        # Copy a file
        api_response = await api_instance.folders_copy_file(dest_folder_id, folders_copy_file_request=folders_copy_file_request)
        print("The response of FoldersApi->folders_copy_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->folders_copy_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dest_folder_id** | **str**| Scope response to dest_folder_id | 
 **folders_copy_file_request** | [**FoldersCopyFileRequest**](FoldersCopyFileRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/folders/123/copy_file&#39; \\      -H &#39;Authorization: Bearer &lt;token&gt;&#39;      -F &#39;source_file_id&#x3D;456&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**File**](File.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | File |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folders_copy_folder**
> Folder folders_copy_folder(dest_folder_id, folders_copy_folder_request=folders_copy_folder_request)

Copy a folder

Copy a folder (and its contents) from elsewhere in Canvas into a folder.

Copying a folder across contexts (between courses and users) is permitted,
but the source and destination must belong to the same institution.
If the source and destination folders are in the same context, the
source folder may not contain the destination folder. A folder will be
renamed at its destination if another folder with the same name already
exists.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.folder import Folder
from canvas_lms_python_client.models.folders_copy_folder_request import FoldersCopyFolderRequest
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
    api_instance = canvas_lms_python_client.FoldersApi(api_client)
    dest_folder_id = 'dest_folder_id_example' # str | Scope response to dest_folder_id
    folders_copy_folder_request = canvas_lms_python_client.FoldersCopyFolderRequest() # FoldersCopyFolderRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/folders/123/copy_folder' \\      -H 'Authorization: Bearer <token>'      -F 'source_file_id=789' ``` (optional)

    try:
        # Copy a folder
        api_response = await api_instance.folders_copy_folder(dest_folder_id, folders_copy_folder_request=folders_copy_folder_request)
        print("The response of FoldersApi->folders_copy_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->folders_copy_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dest_folder_id** | **str**| Scope response to dest_folder_id | 
 **folders_copy_folder_request** | [**FoldersCopyFolderRequest**](FoldersCopyFolderRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/folders/123/copy_folder&#39; \\      -H &#39;Authorization: Bearer &lt;token&gt;&#39;      -F &#39;source_file_id&#x3D;789&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**Folder**](Folder.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Folder |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folders_create**
> Folder folders_create(course_id, folders_create_request=folders_create_request)

Create folder

Creates a folder in the specified context

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.folder import Folder
from canvas_lms_python_client.models.folders_create_request import FoldersCreateRequest
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
    api_instance = canvas_lms_python_client.FoldersApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    folders_create_request = canvas_lms_python_client.FoldersCreateRequest() # FoldersCreateRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/folders/<folder_id>/folders' \\      -F 'name=<new_name>' \\      -F 'locked=true' \\      -H 'Authorization: Bearer <token>' ``` (optional)

    try:
        # Create folder
        api_response = await api_instance.folders_create(course_id, folders_create_request=folders_create_request)
        print("The response of FoldersApi->folders_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->folders_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **folders_create_request** | [**FoldersCreateRequest**](FoldersCreateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/folders/&lt;folder_id&gt;/folders&#39; \\      -F &#39;name&#x3D;&lt;new_name&gt;&#39; \\      -F &#39;locked&#x3D;true&#39; \\      -H &#39;Authorization: Bearer &lt;token&gt;&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**Folder**](Folder.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Folder |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folders_create_file**
> FoldersCreateFileResponse folders_create_file(folder_id)

Upload a file

Upload a file to a folder.

This API endpoint is the first step in uploading a file.
See the {file:file.file_uploads.html File Upload Documentation} for details on
the file upload workflow.

Only those with the "Manage Files" permission on a course or group can
upload files to a folder in that course or group.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.folders_create_file_response import FoldersCreateFileResponse
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
    api_instance = canvas_lms_python_client.FoldersApi(api_client)
    folder_id = 'folder_id_example' # str | Scope response to folder_id

    try:
        # Upload a file
        api_response = await api_instance.folders_create_file(folder_id)
        print("The response of FoldersApi->folders_create_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->folders_create_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**| Scope response to folder_id | 

### Return type

[**FoldersCreateFileResponse**](FoldersCreateFileResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | FoldersCreateFileResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folders_create_for_accounts**
> Folder folders_create_for_accounts(account_id, folders_create_request=folders_create_request)

Create folder

Creates a folder in the specified context

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.folder import Folder
from canvas_lms_python_client.models.folders_create_request import FoldersCreateRequest
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
    api_instance = canvas_lms_python_client.FoldersApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    folders_create_request = canvas_lms_python_client.FoldersCreateRequest() # FoldersCreateRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/folders/<folder_id>/folders' \\      -F 'name=<new_name>' \\      -F 'locked=true' \\      -H 'Authorization: Bearer <token>' ``` (optional)

    try:
        # Create folder
        api_response = await api_instance.folders_create_for_accounts(account_id, folders_create_request=folders_create_request)
        print("The response of FoldersApi->folders_create_for_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->folders_create_for_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **folders_create_request** | [**FoldersCreateRequest**](FoldersCreateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/folders/&lt;folder_id&gt;/folders&#39; \\      -F &#39;name&#x3D;&lt;new_name&gt;&#39; \\      -F &#39;locked&#x3D;true&#39; \\      -H &#39;Authorization: Bearer &lt;token&gt;&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**Folder**](Folder.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Folder |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folders_create_for_groups**
> Folder folders_create_for_groups(group_id, folders_create_request=folders_create_request)

Create folder

Creates a folder in the specified context

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.folder import Folder
from canvas_lms_python_client.models.folders_create_request import FoldersCreateRequest
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
    api_instance = canvas_lms_python_client.FoldersApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    folders_create_request = canvas_lms_python_client.FoldersCreateRequest() # FoldersCreateRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/folders/<folder_id>/folders' \\      -F 'name=<new_name>' \\      -F 'locked=true' \\      -H 'Authorization: Bearer <token>' ``` (optional)

    try:
        # Create folder
        api_response = await api_instance.folders_create_for_groups(group_id, folders_create_request=folders_create_request)
        print("The response of FoldersApi->folders_create_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->folders_create_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **folders_create_request** | [**FoldersCreateRequest**](FoldersCreateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/folders/&lt;folder_id&gt;/folders&#39; \\      -F &#39;name&#x3D;&lt;new_name&gt;&#39; \\      -F &#39;locked&#x3D;true&#39; \\      -H &#39;Authorization: Bearer &lt;token&gt;&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**Folder**](Folder.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Folder |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folders_create_for_other**
> Folder folders_create_for_other(folder_id, folders_create_request=folders_create_request)

Create folder

Creates a folder in the specified context

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.folder import Folder
from canvas_lms_python_client.models.folders_create_request import FoldersCreateRequest
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
    api_instance = canvas_lms_python_client.FoldersApi(api_client)
    folder_id = 'folder_id_example' # str | Scope response to folder_id
    folders_create_request = canvas_lms_python_client.FoldersCreateRequest() # FoldersCreateRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/folders/<folder_id>/folders' \\      -F 'name=<new_name>' \\      -F 'locked=true' \\      -H 'Authorization: Bearer <token>' ``` (optional)

    try:
        # Create folder
        api_response = await api_instance.folders_create_for_other(folder_id, folders_create_request=folders_create_request)
        print("The response of FoldersApi->folders_create_for_other:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->folders_create_for_other: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**| Scope response to folder_id | 
 **folders_create_request** | [**FoldersCreateRequest**](FoldersCreateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/folders/&lt;folder_id&gt;/folders&#39; \\      -F &#39;name&#x3D;&lt;new_name&gt;&#39; \\      -F &#39;locked&#x3D;true&#39; \\      -H &#39;Authorization: Bearer &lt;token&gt;&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**Folder**](Folder.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Folder |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folders_create_for_users**
> Folder folders_create_for_users(user_id, folders_create_request=folders_create_request)

Create folder

Creates a folder in the specified context

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.folder import Folder
from canvas_lms_python_client.models.folders_create_request import FoldersCreateRequest
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
    api_instance = canvas_lms_python_client.FoldersApi(api_client)
    user_id = 'user_id_example' # str | Scope response to user_id
    folders_create_request = canvas_lms_python_client.FoldersCreateRequest() # FoldersCreateRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/folders/<folder_id>/folders' \\      -F 'name=<new_name>' \\      -F 'locked=true' \\      -H 'Authorization: Bearer <token>' ``` (optional)

    try:
        # Create folder
        api_response = await api_instance.folders_create_for_users(user_id, folders_create_request=folders_create_request)
        print("The response of FoldersApi->folders_create_for_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->folders_create_for_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Scope response to user_id | 
 **folders_create_request** | [**FoldersCreateRequest**](FoldersCreateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/folders/&lt;folder_id&gt;/folders&#39; \\      -F &#39;name&#x3D;&lt;new_name&gt;&#39; \\      -F &#39;locked&#x3D;true&#39; \\      -H &#39;Authorization: Bearer &lt;token&gt;&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**Folder**](Folder.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Folder |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folders_list_all_folders**
> List[Folder] folders_list_all_folders(course_id, page=page, per_page=per_page)

List all folders

Returns the paginated list of all folders for the given context. This will
be returned as a flat list containing all subfolders as well.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.folder import Folder
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
    api_instance = canvas_lms_python_client.FoldersApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List all folders
        api_response = await api_instance.folders_list_all_folders(course_id, page=page, per_page=per_page)
        print("The response of FoldersApi->folders_list_all_folders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->folders_list_all_folders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[Folder]**](Folder.md)

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

# **folders_list_all_folders_for_groups**
> List[Folder] folders_list_all_folders_for_groups(group_id, page=page, per_page=per_page)

List all folders

Returns the paginated list of all folders for the given context. This will
be returned as a flat list containing all subfolders as well.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.folder import Folder
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
    api_instance = canvas_lms_python_client.FoldersApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List all folders
        api_response = await api_instance.folders_list_all_folders_for_groups(group_id, page=page, per_page=per_page)
        print("The response of FoldersApi->folders_list_all_folders_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->folders_list_all_folders_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[Folder]**](Folder.md)

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

# **folders_list_all_folders_for_users**
> List[Folder] folders_list_all_folders_for_users(user_id, page=page, per_page=per_page)

List all folders

Returns the paginated list of all folders for the given context. This will
be returned as a flat list containing all subfolders as well.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.folder import Folder
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
    api_instance = canvas_lms_python_client.FoldersApi(api_client)
    user_id = 'user_id_example' # str | Scope response to user_id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List all folders
        api_response = await api_instance.folders_list_all_folders_for_users(user_id, page=page, per_page=per_page)
        print("The response of FoldersApi->folders_list_all_folders_for_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->folders_list_all_folders_for_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Scope response to user_id | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[Folder]**](Folder.md)

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

# **folders_media_folder**
> Folder folders_media_folder(course_id)

Get uploaded media folder for user

Returns the details for a designated upload folder that the user has rights to
upload to, and creates it if it doesn't exist.

If the current user does not have the permissions to manage files
in the course or group, the folder will belong to the current user directly.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.folder import Folder
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
    api_instance = canvas_lms_python_client.FoldersApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id

    try:
        # Get uploaded media folder for user
        api_response = await api_instance.folders_media_folder(course_id)
        print("The response of FoldersApi->folders_media_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->folders_media_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 

### Return type

[**Folder**](Folder.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Folder |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folders_media_folder_for_groups**
> Folder folders_media_folder_for_groups(group_id)

Get uploaded media folder for user

Returns the details for a designated upload folder that the user has rights to
upload to, and creates it if it doesn't exist.

If the current user does not have the permissions to manage files
in the course or group, the folder will belong to the current user directly.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.folder import Folder
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
    api_instance = canvas_lms_python_client.FoldersApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id

    try:
        # Get uploaded media folder for user
        api_response = await api_instance.folders_media_folder_for_groups(group_id)
        print("The response of FoldersApi->folders_media_folder_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->folders_media_folder_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 

### Return type

[**Folder**](Folder.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Folder |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folders_resolve_path**
> List[Folder] folders_resolve_path(course_id)

Resolve path

Given the full path to a folder, returns a list of all Folders in the path hierarchy,
starting at the root folder, and ending at the requested folder. The given path is
relative to the context's root folder and does not include the root folder's name
(e.g., "course files"). If an empty path is given, the context's root folder alone
is returned. Otherwise, if no folder exists with the given full path, a Not Found
error is returned.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.folder import Folder
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
    api_instance = canvas_lms_python_client.FoldersApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id

    try:
        # Resolve path
        api_response = await api_instance.folders_resolve_path(course_id)
        print("The response of FoldersApi->folders_resolve_path:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->folders_resolve_path: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 

### Return type

[**List[Folder]**](Folder.md)

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

# **folders_resolve_path_by_by_path_for_groups**
> List[Folder] folders_resolve_path_by_by_path_for_groups(group_id)

Resolve path

Given the full path to a folder, returns a list of all Folders in the path hierarchy,
starting at the root folder, and ending at the requested folder. The given path is
relative to the context's root folder and does not include the root folder's name
(e.g., "course files"). If an empty path is given, the context's root folder alone
is returned. Otherwise, if no folder exists with the given full path, a Not Found
error is returned.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.folder import Folder
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
    api_instance = canvas_lms_python_client.FoldersApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id

    try:
        # Resolve path
        api_response = await api_instance.folders_resolve_path_by_by_path_for_groups(group_id)
        print("The response of FoldersApi->folders_resolve_path_by_by_path_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->folders_resolve_path_by_by_path_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 

### Return type

[**List[Folder]**](Folder.md)

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

# **folders_resolve_path_by_by_path_for_users**
> List[Folder] folders_resolve_path_by_by_path_for_users(user_id)

Resolve path

Given the full path to a folder, returns a list of all Folders in the path hierarchy,
starting at the root folder, and ending at the requested folder. The given path is
relative to the context's root folder and does not include the root folder's name
(e.g., "course files"). If an empty path is given, the context's root folder alone
is returned. Otherwise, if no folder exists with the given full path, a Not Found
error is returned.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.folder import Folder
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
    api_instance = canvas_lms_python_client.FoldersApi(api_client)
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # Resolve path
        api_response = await api_instance.folders_resolve_path_by_by_path_for_users(user_id)
        print("The response of FoldersApi->folders_resolve_path_by_by_path_for_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->folders_resolve_path_by_by_path_for_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Scope response to user_id | 

### Return type

[**List[Folder]**](Folder.md)

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

# **folders_resolve_path_for_courses**
> List[Folder] folders_resolve_path_for_courses(course_id)

Resolve path

Given the full path to a folder, returns a list of all Folders in the path hierarchy,
starting at the root folder, and ending at the requested folder. The given path is
relative to the context's root folder and does not include the root folder's name
(e.g., "course files"). If an empty path is given, the context's root folder alone
is returned. Otherwise, if no folder exists with the given full path, a Not Found
error is returned.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.folder import Folder
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
    api_instance = canvas_lms_python_client.FoldersApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id

    try:
        # Resolve path
        api_response = await api_instance.folders_resolve_path_for_courses(course_id)
        print("The response of FoldersApi->folders_resolve_path_for_courses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->folders_resolve_path_for_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 

### Return type

[**List[Folder]**](Folder.md)

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

# **folders_resolve_path_for_groups**
> List[Folder] folders_resolve_path_for_groups(group_id)

Resolve path

Given the full path to a folder, returns a list of all Folders in the path hierarchy,
starting at the root folder, and ending at the requested folder. The given path is
relative to the context's root folder and does not include the root folder's name
(e.g., "course files"). If an empty path is given, the context's root folder alone
is returned. Otherwise, if no folder exists with the given full path, a Not Found
error is returned.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.folder import Folder
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
    api_instance = canvas_lms_python_client.FoldersApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id

    try:
        # Resolve path
        api_response = await api_instance.folders_resolve_path_for_groups(group_id)
        print("The response of FoldersApi->folders_resolve_path_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->folders_resolve_path_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 

### Return type

[**List[Folder]**](Folder.md)

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

# **folders_resolve_path_for_users**
> List[Folder] folders_resolve_path_for_users(user_id)

Resolve path

Given the full path to a folder, returns a list of all Folders in the path hierarchy,
starting at the root folder, and ending at the requested folder. The given path is
relative to the context's root folder and does not include the root folder's name
(e.g., "course files"). If an empty path is given, the context's root folder alone
is returned. Otherwise, if no folder exists with the given full path, a Not Found
error is returned.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.folder import Folder
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
    api_instance = canvas_lms_python_client.FoldersApi(api_client)
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # Resolve path
        api_response = await api_instance.folders_resolve_path_for_users(user_id)
        print("The response of FoldersApi->folders_resolve_path_for_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->folders_resolve_path_for_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Scope response to user_id | 

### Return type

[**List[Folder]**](Folder.md)

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

# **folders_show**
> Folder folders_show(course_id, id)

Get folder

Returns the details for a folder

You can get the root folder from a context by using 'root' as the :id.
For example, you could get the root folder for a course like:

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.folder import Folder
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
    api_instance = canvas_lms_python_client.FoldersApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id

    try:
        # Get folder
        api_response = await api_instance.folders_show(course_id, id)
        print("The response of FoldersApi->folders_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->folders_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**Folder**](Folder.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Folder |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folders_show_for_groups**
> Folder folders_show_for_groups(group_id, id)

Get folder

Returns the details for a folder

You can get the root folder from a context by using 'root' as the :id.
For example, you could get the root folder for a course like:

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.folder import Folder
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
    api_instance = canvas_lms_python_client.FoldersApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    id = 'id_example' # str | Scope response to id

    try:
        # Get folder
        api_response = await api_instance.folders_show_for_groups(group_id, id)
        print("The response of FoldersApi->folders_show_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->folders_show_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**Folder**](Folder.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Folder |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folders_show_for_other**
> Folder folders_show_for_other(id)

Get folder

Returns the details for a folder

You can get the root folder from a context by using 'root' as the :id.
For example, you could get the root folder for a course like:

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.folder import Folder
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
    api_instance = canvas_lms_python_client.FoldersApi(api_client)
    id = 'id_example' # str | Scope response to id

    try:
        # Get folder
        api_response = await api_instance.folders_show_for_other(id)
        print("The response of FoldersApi->folders_show_for_other:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->folders_show_for_other: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 

### Return type

[**Folder**](Folder.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Folder |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folders_show_for_users**
> Folder folders_show_for_users(id, user_id)

Get folder

Returns the details for a folder

You can get the root folder from a context by using 'root' as the :id.
For example, you could get the root folder for a course like:

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.folder import Folder
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
    api_instance = canvas_lms_python_client.FoldersApi(api_client)
    id = 'id_example' # str | Scope response to id
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # Get folder
        api_response = await api_instance.folders_show_for_users(id, user_id)
        print("The response of FoldersApi->folders_show_for_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->folders_show_for_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **user_id** | **str**| Scope response to user_id | 

### Return type

[**Folder**](Folder.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Folder |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folders_update**
> Folder folders_update(id, folders_update_request=folders_update_request)

Update folder

Updates a folder

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.folder import Folder
from canvas_lms_python_client.models.folders_update_request import FoldersUpdateRequest
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
    api_instance = canvas_lms_python_client.FoldersApi(api_client)
    id = 'id_example' # str | Scope response to id
    folders_update_request = canvas_lms_python_client.FoldersUpdateRequest() # FoldersUpdateRequest | Request body parameters  **Example Request:** ``` curl -XPUT 'https://<canvas>/api/v1/folders/<folder_id>' \\      -F 'name=<new_name>' \\      -F 'locked=true' \\      -H 'Authorization: Bearer <token>' ``` (optional)

    try:
        # Update folder
        api_response = await api_instance.folders_update(id, folders_update_request=folders_update_request)
        print("The response of FoldersApi->folders_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->folders_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **folders_update_request** | [**FoldersUpdateRequest**](FoldersUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl -XPUT &#39;https://&lt;canvas&gt;/api/v1/folders/&lt;folder_id&gt;&#39; \\      -F &#39;name&#x3D;&lt;new_name&gt;&#39; \\      -F &#39;locked&#x3D;true&#39; \\      -H &#39;Authorization: Bearer &lt;token&gt;&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**Folder**](Folder.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Folder |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

