# canvas_lms_python_client.FilesApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**files_api_index**](FilesApi.md#files_api_index) | **GET** /api/v1/courses/{course_id}/files | List files
[**files_api_index_for_groups**](FilesApi.md#files_api_index_for_groups) | **GET** /api/v1/groups/{group_id}/files | List files
[**files_api_index_for_other**](FilesApi.md#files_api_index_for_other) | **GET** /api/v1/folders/{folder_id}/files | List files
[**files_api_index_for_users**](FilesApi.md#files_api_index_for_users) | **GET** /api/v1/users/{user_id}/files | List files
[**files_api_quota**](FilesApi.md#files_api_quota) | **GET** /api/v1/courses/{course_id}/files/quota | Get quota information
[**files_api_quota_for_groups**](FilesApi.md#files_api_quota_for_groups) | **GET** /api/v1/groups/{group_id}/files/quota | Get quota information
[**files_api_quota_for_users**](FilesApi.md#files_api_quota_for_users) | **GET** /api/v1/users/{user_id}/files/quota | Get quota information
[**files_api_show**](FilesApi.md#files_api_show) | **GET** /api/v1/files/{id} | Get file
[**files_api_show_for_courses**](FilesApi.md#files_api_show_for_courses) | **GET** /api/v1/courses/{course_id}/files/{id} | Get file
[**files_api_show_for_groups**](FilesApi.md#files_api_show_for_groups) | **GET** /api/v1/groups/{group_id}/files/{id} | Get file
[**files_api_show_for_other**](FilesApi.md#files_api_show_for_other) | **POST** /api/v1/files/{id} | Get file
[**files_api_show_for_users**](FilesApi.md#files_api_show_for_users) | **GET** /api/v1/users/{user_id}/files/{id} | Get file
[**files_api_update**](FilesApi.md#files_api_update) | **PUT** /api/v1/files/{id} | Update file
[**files_destroy**](FilesApi.md#files_destroy) | **DELETE** /api/v1/files/{id} | Delete file
[**files_file_ref**](FilesApi.md#files_file_ref) | **GET** /api/v1/courses/{course_id}/files/file_ref/{migration_id} | Translate file reference
[**files_icon_metadata**](FilesApi.md#files_icon_metadata) | **GET** /api/v1/files/{id}/icon_metadata | Get icon metadata
[**files_public_url**](FilesApi.md#files_public_url) | **GET** /api/v1/files/{id}/public_url | Get public inline preview url
[**files_reset_verifier**](FilesApi.md#files_reset_verifier) | **POST** /api/v1/files/{id}/reset_verifier | Reset link verifier
[**files_show**](FilesApi.md#files_show) | **GET** /courses/{course_id}/files/{file_id}/download | Download file
[**files_show_by_download_for_other**](FilesApi.md#files_show_by_download_for_other) | **GET** /quizzes/quiz_submissions/{quiz_submission_id}/files/{file_id}/download | Download file
[**files_show_for_accounts**](FilesApi.md#files_show_for_accounts) | **GET** /accounts/{account_id}/files/{file_id}/download | Download file
[**files_show_for_assessment_questions**](FilesApi.md#files_show_for_assessment_questions) | **GET** /assessment_questions/{assessment_question_id}/files/{file_id}/download | Download file
[**files_show_for_assignments**](FilesApi.md#files_show_for_assignments) | **GET** /assignments/{assignment_id}/files/{id}/download | Download file
[**files_show_for_groups**](FilesApi.md#files_show_for_groups) | **GET** /groups/{group_id}/files/{file_id}/download | Download file
[**files_show_for_other**](FilesApi.md#files_show_for_other) | **GET** /files/{file_id}/download | Download file
[**files_show_for_quiz_statistics**](FilesApi.md#files_show_for_quiz_statistics) | **GET** /quiz_statistics/{quiz_statistics_id}/files/{file_id}/download | Download file
[**files_show_for_users**](FilesApi.md#files_show_for_users) | **GET** /users/{user_id}/files/{file_id}/download | Download file


# **files_api_index**
> List[File] files_api_index(course_id, content_types=content_types, exclude_content_types=exclude_content_types, search_term=search_term, include_user=include_user, only=only, sort=sort, order=order, page=page, per_page=per_page)

List files

Returns the paginated list of files for the folder or course.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.file import File
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
    api_instance = canvas_lms_python_client.FilesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    content_types = ['content_types_example'] # List[str] | Filter results by content-type. You can specify type/subtype pairs (e.g., 'image/jpeg'), or simply types (e.g., 'image', which will match 'image/gif', 'image/jpeg', etc.). (optional)
    exclude_content_types = ['exclude_content_types_example'] # List[str] | Exclude given content-types from your results. You can specify type/subtype pairs (e.g., 'image/jpeg'), or simply types (e.g., 'image', which will match 'image/gif', 'image/jpeg', etc.). (optional)
    search_term = 'search_term_example' # str | The partial name of the files to match and return. (optional)
    include_user = 'include_user_example' # str | Array of additional information to include.  \"user\":: the user who uploaded the file or last edited its content \"usage_rights\":: copyright and license information for the file (see UsageRights) (optional)
    only = [canvas_lms_python_client.List[str]()] # List[List[str]] | Array of information to restrict to. Overrides include[]  \"names\":: only returns file name information (optional)
    sort = 'sort_example' # str | Sort results by this field. Defaults to 'name'. Note that `sort=user` implies `include[]=user`. (optional)
    order = 'order_example' # str | The sorting order. Defaults to 'asc'. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List files
        api_response = await api_instance.files_api_index(course_id, content_types=content_types, exclude_content_types=exclude_content_types, search_term=search_term, include_user=include_user, only=only, sort=sort, order=order, page=page, per_page=per_page)
        print("The response of FilesApi->files_api_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->files_api_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **content_types** | [**List[str]**](str.md)| Filter results by content-type. You can specify type/subtype pairs (e.g., &#39;image/jpeg&#39;), or simply types (e.g., &#39;image&#39;, which will match &#39;image/gif&#39;, &#39;image/jpeg&#39;, etc.). | [optional] 
 **exclude_content_types** | [**List[str]**](str.md)| Exclude given content-types from your results. You can specify type/subtype pairs (e.g., &#39;image/jpeg&#39;), or simply types (e.g., &#39;image&#39;, which will match &#39;image/gif&#39;, &#39;image/jpeg&#39;, etc.). | [optional] 
 **search_term** | **str**| The partial name of the files to match and return. | [optional] 
 **include_user** | **str**| Array of additional information to include.  \&quot;user\&quot;:: the user who uploaded the file or last edited its content \&quot;usage_rights\&quot;:: copyright and license information for the file (see UsageRights) | [optional] 
 **only** | [**List[List[str]]**](List[str].md)| Array of information to restrict to. Overrides include[]  \&quot;names\&quot;:: only returns file name information | [optional] 
 **sort** | **str**| Sort results by this field. Defaults to &#39;name&#39;. Note that &#x60;sort&#x3D;user&#x60; implies &#x60;include[]&#x3D;user&#x60;. | [optional] 
 **order** | **str**| The sorting order. Defaults to &#39;asc&#39;. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[File]**](File.md)

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

# **files_api_index_for_groups**
> List[File] files_api_index_for_groups(group_id, content_types=content_types, exclude_content_types=exclude_content_types, search_term=search_term, include_user=include_user, only=only, sort=sort, order=order, page=page, per_page=per_page)

List files

Returns the paginated list of files for the folder or course.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.file import File
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
    api_instance = canvas_lms_python_client.FilesApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    content_types = ['content_types_example'] # List[str] | Filter results by content-type. You can specify type/subtype pairs (e.g., 'image/jpeg'), or simply types (e.g., 'image', which will match 'image/gif', 'image/jpeg', etc.). (optional)
    exclude_content_types = ['exclude_content_types_example'] # List[str] | Exclude given content-types from your results. You can specify type/subtype pairs (e.g., 'image/jpeg'), or simply types (e.g., 'image', which will match 'image/gif', 'image/jpeg', etc.). (optional)
    search_term = 'search_term_example' # str | The partial name of the files to match and return. (optional)
    include_user = 'include_user_example' # str | Array of additional information to include.  \"user\":: the user who uploaded the file or last edited its content \"usage_rights\":: copyright and license information for the file (see UsageRights) (optional)
    only = [canvas_lms_python_client.List[str]()] # List[List[str]] | Array of information to restrict to. Overrides include[]  \"names\":: only returns file name information (optional)
    sort = 'sort_example' # str | Sort results by this field. Defaults to 'name'. Note that `sort=user` implies `include[]=user`. (optional)
    order = 'order_example' # str | The sorting order. Defaults to 'asc'. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List files
        api_response = await api_instance.files_api_index_for_groups(group_id, content_types=content_types, exclude_content_types=exclude_content_types, search_term=search_term, include_user=include_user, only=only, sort=sort, order=order, page=page, per_page=per_page)
        print("The response of FilesApi->files_api_index_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->files_api_index_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **content_types** | [**List[str]**](str.md)| Filter results by content-type. You can specify type/subtype pairs (e.g., &#39;image/jpeg&#39;), or simply types (e.g., &#39;image&#39;, which will match &#39;image/gif&#39;, &#39;image/jpeg&#39;, etc.). | [optional] 
 **exclude_content_types** | [**List[str]**](str.md)| Exclude given content-types from your results. You can specify type/subtype pairs (e.g., &#39;image/jpeg&#39;), or simply types (e.g., &#39;image&#39;, which will match &#39;image/gif&#39;, &#39;image/jpeg&#39;, etc.). | [optional] 
 **search_term** | **str**| The partial name of the files to match and return. | [optional] 
 **include_user** | **str**| Array of additional information to include.  \&quot;user\&quot;:: the user who uploaded the file or last edited its content \&quot;usage_rights\&quot;:: copyright and license information for the file (see UsageRights) | [optional] 
 **only** | [**List[List[str]]**](List[str].md)| Array of information to restrict to. Overrides include[]  \&quot;names\&quot;:: only returns file name information | [optional] 
 **sort** | **str**| Sort results by this field. Defaults to &#39;name&#39;. Note that &#x60;sort&#x3D;user&#x60; implies &#x60;include[]&#x3D;user&#x60;. | [optional] 
 **order** | **str**| The sorting order. Defaults to &#39;asc&#39;. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[File]**](File.md)

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

# **files_api_index_for_other**
> List[File] files_api_index_for_other(folder_id, content_types=content_types, exclude_content_types=exclude_content_types, search_term=search_term, include_user=include_user, only=only, sort=sort, order=order, page=page, per_page=per_page)

List files

Returns the paginated list of files for the folder or course.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.file import File
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
    api_instance = canvas_lms_python_client.FilesApi(api_client)
    folder_id = 'folder_id_example' # str | Scope response to id
    content_types = ['content_types_example'] # List[str] | Filter results by content-type. You can specify type/subtype pairs (e.g., 'image/jpeg'), or simply types (e.g., 'image', which will match 'image/gif', 'image/jpeg', etc.). (optional)
    exclude_content_types = ['exclude_content_types_example'] # List[str] | Exclude given content-types from your results. You can specify type/subtype pairs (e.g., 'image/jpeg'), or simply types (e.g., 'image', which will match 'image/gif', 'image/jpeg', etc.). (optional)
    search_term = 'search_term_example' # str | The partial name of the files to match and return. (optional)
    include_user = 'include_user_example' # str | Array of additional information to include.  \"user\":: the user who uploaded the file or last edited its content \"usage_rights\":: copyright and license information for the file (see UsageRights) (optional)
    only = [canvas_lms_python_client.List[str]()] # List[List[str]] | Array of information to restrict to. Overrides include[]  \"names\":: only returns file name information (optional)
    sort = 'sort_example' # str | Sort results by this field. Defaults to 'name'. Note that `sort=user` implies `include[]=user`. (optional)
    order = 'order_example' # str | The sorting order. Defaults to 'asc'. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List files
        api_response = await api_instance.files_api_index_for_other(folder_id, content_types=content_types, exclude_content_types=exclude_content_types, search_term=search_term, include_user=include_user, only=only, sort=sort, order=order, page=page, per_page=per_page)
        print("The response of FilesApi->files_api_index_for_other:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->files_api_index_for_other: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**| Scope response to id | 
 **content_types** | [**List[str]**](str.md)| Filter results by content-type. You can specify type/subtype pairs (e.g., &#39;image/jpeg&#39;), or simply types (e.g., &#39;image&#39;, which will match &#39;image/gif&#39;, &#39;image/jpeg&#39;, etc.). | [optional] 
 **exclude_content_types** | [**List[str]**](str.md)| Exclude given content-types from your results. You can specify type/subtype pairs (e.g., &#39;image/jpeg&#39;), or simply types (e.g., &#39;image&#39;, which will match &#39;image/gif&#39;, &#39;image/jpeg&#39;, etc.). | [optional] 
 **search_term** | **str**| The partial name of the files to match and return. | [optional] 
 **include_user** | **str**| Array of additional information to include.  \&quot;user\&quot;:: the user who uploaded the file or last edited its content \&quot;usage_rights\&quot;:: copyright and license information for the file (see UsageRights) | [optional] 
 **only** | [**List[List[str]]**](List[str].md)| Array of information to restrict to. Overrides include[]  \&quot;names\&quot;:: only returns file name information | [optional] 
 **sort** | **str**| Sort results by this field. Defaults to &#39;name&#39;. Note that &#x60;sort&#x3D;user&#x60; implies &#x60;include[]&#x3D;user&#x60;. | [optional] 
 **order** | **str**| The sorting order. Defaults to &#39;asc&#39;. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[File]**](File.md)

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

# **files_api_index_for_users**
> List[File] files_api_index_for_users(user_id, content_types=content_types, exclude_content_types=exclude_content_types, search_term=search_term, include_user=include_user, only=only, sort=sort, order=order, page=page, per_page=per_page)

List files

Returns the paginated list of files for the folder or course.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.file import File
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
    api_instance = canvas_lms_python_client.FilesApi(api_client)
    user_id = 'user_id_example' # str | Scope response to user_id
    content_types = ['content_types_example'] # List[str] | Filter results by content-type. You can specify type/subtype pairs (e.g., 'image/jpeg'), or simply types (e.g., 'image', which will match 'image/gif', 'image/jpeg', etc.). (optional)
    exclude_content_types = ['exclude_content_types_example'] # List[str] | Exclude given content-types from your results. You can specify type/subtype pairs (e.g., 'image/jpeg'), or simply types (e.g., 'image', which will match 'image/gif', 'image/jpeg', etc.). (optional)
    search_term = 'search_term_example' # str | The partial name of the files to match and return. (optional)
    include_user = 'include_user_example' # str | Array of additional information to include.  \"user\":: the user who uploaded the file or last edited its content \"usage_rights\":: copyright and license information for the file (see UsageRights) (optional)
    only = [canvas_lms_python_client.List[str]()] # List[List[str]] | Array of information to restrict to. Overrides include[]  \"names\":: only returns file name information (optional)
    sort = 'sort_example' # str | Sort results by this field. Defaults to 'name'. Note that `sort=user` implies `include[]=user`. (optional)
    order = 'order_example' # str | The sorting order. Defaults to 'asc'. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List files
        api_response = await api_instance.files_api_index_for_users(user_id, content_types=content_types, exclude_content_types=exclude_content_types, search_term=search_term, include_user=include_user, only=only, sort=sort, order=order, page=page, per_page=per_page)
        print("The response of FilesApi->files_api_index_for_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->files_api_index_for_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Scope response to user_id | 
 **content_types** | [**List[str]**](str.md)| Filter results by content-type. You can specify type/subtype pairs (e.g., &#39;image/jpeg&#39;), or simply types (e.g., &#39;image&#39;, which will match &#39;image/gif&#39;, &#39;image/jpeg&#39;, etc.). | [optional] 
 **exclude_content_types** | [**List[str]**](str.md)| Exclude given content-types from your results. You can specify type/subtype pairs (e.g., &#39;image/jpeg&#39;), or simply types (e.g., &#39;image&#39;, which will match &#39;image/gif&#39;, &#39;image/jpeg&#39;, etc.). | [optional] 
 **search_term** | **str**| The partial name of the files to match and return. | [optional] 
 **include_user** | **str**| Array of additional information to include.  \&quot;user\&quot;:: the user who uploaded the file or last edited its content \&quot;usage_rights\&quot;:: copyright and license information for the file (see UsageRights) | [optional] 
 **only** | [**List[List[str]]**](List[str].md)| Array of information to restrict to. Overrides include[]  \&quot;names\&quot;:: only returns file name information | [optional] 
 **sort** | **str**| Sort results by this field. Defaults to &#39;name&#39;. Note that &#x60;sort&#x3D;user&#x60; implies &#x60;include[]&#x3D;user&#x60;. | [optional] 
 **order** | **str**| The sorting order. Defaults to &#39;asc&#39;. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[File]**](File.md)

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

# **files_api_quota**
> files_api_quota(course_id)

Get quota information

Returns the total and used storage quota for the course, group, or user.

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
    api_instance = canvas_lms_python_client.FilesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id

    try:
        # Get quota information
        await api_instance.files_api_quota(course_id)
    except Exception as e:
        print("Exception when calling FilesApi->files_api_quota: %s\n" % e)
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
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Get quota information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_api_quota_for_groups**
> files_api_quota_for_groups(group_id)

Get quota information

Returns the total and used storage quota for the course, group, or user.

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
    api_instance = canvas_lms_python_client.FilesApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id

    try:
        # Get quota information
        await api_instance.files_api_quota_for_groups(group_id)
    except Exception as e:
        print("Exception when calling FilesApi->files_api_quota_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Get quota information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_api_quota_for_users**
> files_api_quota_for_users(user_id)

Get quota information

Returns the total and used storage quota for the course, group, or user.

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
    api_instance = canvas_lms_python_client.FilesApi(api_client)
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # Get quota information
        await api_instance.files_api_quota_for_users(user_id)
    except Exception as e:
        print("Exception when calling FilesApi->files_api_quota_for_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Scope response to user_id | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Get quota information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_api_show**
> File files_api_show(id, include_user=include_user, replacement_chain_context_type=replacement_chain_context_type, replacement_chain_context_id=replacement_chain_context_id)

Get file

Returns the standard attachment json object

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.file import File
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
    api_instance = canvas_lms_python_client.FilesApi(api_client)
    id = 'id_example' # str | Scope response to id
    include_user = 'include_user_example' # str | Array of additional information to include.  \"user\":: the user who uploaded the file or last edited its content \"usage_rights\":: copyright and license information for the file (see UsageRights) (optional)
    replacement_chain_context_type = 'replacement_chain_context_type_example' # str | When a user replaces a file during upload, Canvas keeps track of the \"replacement chain.\"  Include this parameter if you wish Canvas to follow the replacement chain if the requested file was deleted and replaced by another.  Must be set to 'course' or 'account'. The \"replacement_chain_context_id\" parameter must also be included. (optional)
    replacement_chain_context_id = 56 # int | When a user replaces a file during upload, Canvas keeps track of the \"replacement chain.\"  Include this parameter if you wish Canvas to follow the replacement chain if the requested file was deleted and replaced by another.  Indicates the context ID Canvas should use when following the \"replacement chain.\" The \"replacement_chain_context_type\" parameter must also be included. (optional)

    try:
        # Get file
        api_response = await api_instance.files_api_show(id, include_user=include_user, replacement_chain_context_type=replacement_chain_context_type, replacement_chain_context_id=replacement_chain_context_id)
        print("The response of FilesApi->files_api_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->files_api_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **include_user** | **str**| Array of additional information to include.  \&quot;user\&quot;:: the user who uploaded the file or last edited its content \&quot;usage_rights\&quot;:: copyright and license information for the file (see UsageRights) | [optional] 
 **replacement_chain_context_type** | **str**| When a user replaces a file during upload, Canvas keeps track of the \&quot;replacement chain.\&quot;  Include this parameter if you wish Canvas to follow the replacement chain if the requested file was deleted and replaced by another.  Must be set to &#39;course&#39; or &#39;account&#39;. The \&quot;replacement_chain_context_id\&quot; parameter must also be included. | [optional] 
 **replacement_chain_context_id** | **int**| When a user replaces a file during upload, Canvas keeps track of the \&quot;replacement chain.\&quot;  Include this parameter if you wish Canvas to follow the replacement chain if the requested file was deleted and replaced by another.  Indicates the context ID Canvas should use when following the \&quot;replacement chain.\&quot; The \&quot;replacement_chain_context_type\&quot; parameter must also be included. | [optional] 

### Return type

[**File**](File.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | File |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_api_show_for_courses**
> File files_api_show_for_courses(course_id, id, include_user=include_user, replacement_chain_context_type=replacement_chain_context_type, replacement_chain_context_id=replacement_chain_context_id)

Get file

Returns the standard attachment json object

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.file import File
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
    api_instance = canvas_lms_python_client.FilesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    include_user = 'include_user_example' # str | Array of additional information to include.  \"user\":: the user who uploaded the file or last edited its content \"usage_rights\":: copyright and license information for the file (see UsageRights) (optional)
    replacement_chain_context_type = 'replacement_chain_context_type_example' # str | When a user replaces a file during upload, Canvas keeps track of the \"replacement chain.\"  Include this parameter if you wish Canvas to follow the replacement chain if the requested file was deleted and replaced by another.  Must be set to 'course' or 'account'. The \"replacement_chain_context_id\" parameter must also be included. (optional)
    replacement_chain_context_id = 56 # int | When a user replaces a file during upload, Canvas keeps track of the \"replacement chain.\"  Include this parameter if you wish Canvas to follow the replacement chain if the requested file was deleted and replaced by another.  Indicates the context ID Canvas should use when following the \"replacement chain.\" The \"replacement_chain_context_type\" parameter must also be included. (optional)

    try:
        # Get file
        api_response = await api_instance.files_api_show_for_courses(course_id, id, include_user=include_user, replacement_chain_context_type=replacement_chain_context_type, replacement_chain_context_id=replacement_chain_context_id)
        print("The response of FilesApi->files_api_show_for_courses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->files_api_show_for_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **include_user** | **str**| Array of additional information to include.  \&quot;user\&quot;:: the user who uploaded the file or last edited its content \&quot;usage_rights\&quot;:: copyright and license information for the file (see UsageRights) | [optional] 
 **replacement_chain_context_type** | **str**| When a user replaces a file during upload, Canvas keeps track of the \&quot;replacement chain.\&quot;  Include this parameter if you wish Canvas to follow the replacement chain if the requested file was deleted and replaced by another.  Must be set to &#39;course&#39; or &#39;account&#39;. The \&quot;replacement_chain_context_id\&quot; parameter must also be included. | [optional] 
 **replacement_chain_context_id** | **int**| When a user replaces a file during upload, Canvas keeps track of the \&quot;replacement chain.\&quot;  Include this parameter if you wish Canvas to follow the replacement chain if the requested file was deleted and replaced by another.  Indicates the context ID Canvas should use when following the \&quot;replacement chain.\&quot; The \&quot;replacement_chain_context_type\&quot; parameter must also be included. | [optional] 

### Return type

[**File**](File.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | File |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_api_show_for_groups**
> File files_api_show_for_groups(group_id, id, include_user=include_user, replacement_chain_context_type=replacement_chain_context_type, replacement_chain_context_id=replacement_chain_context_id)

Get file

Returns the standard attachment json object

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.file import File
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
    api_instance = canvas_lms_python_client.FilesApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    id = 'id_example' # str | Scope response to id
    include_user = 'include_user_example' # str | Array of additional information to include.  \"user\":: the user who uploaded the file or last edited its content \"usage_rights\":: copyright and license information for the file (see UsageRights) (optional)
    replacement_chain_context_type = 'replacement_chain_context_type_example' # str | When a user replaces a file during upload, Canvas keeps track of the \"replacement chain.\"  Include this parameter if you wish Canvas to follow the replacement chain if the requested file was deleted and replaced by another.  Must be set to 'course' or 'account'. The \"replacement_chain_context_id\" parameter must also be included. (optional)
    replacement_chain_context_id = 56 # int | When a user replaces a file during upload, Canvas keeps track of the \"replacement chain.\"  Include this parameter if you wish Canvas to follow the replacement chain if the requested file was deleted and replaced by another.  Indicates the context ID Canvas should use when following the \"replacement chain.\" The \"replacement_chain_context_type\" parameter must also be included. (optional)

    try:
        # Get file
        api_response = await api_instance.files_api_show_for_groups(group_id, id, include_user=include_user, replacement_chain_context_type=replacement_chain_context_type, replacement_chain_context_id=replacement_chain_context_id)
        print("The response of FilesApi->files_api_show_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->files_api_show_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **id** | **str**| Scope response to id | 
 **include_user** | **str**| Array of additional information to include.  \&quot;user\&quot;:: the user who uploaded the file or last edited its content \&quot;usage_rights\&quot;:: copyright and license information for the file (see UsageRights) | [optional] 
 **replacement_chain_context_type** | **str**| When a user replaces a file during upload, Canvas keeps track of the \&quot;replacement chain.\&quot;  Include this parameter if you wish Canvas to follow the replacement chain if the requested file was deleted and replaced by another.  Must be set to &#39;course&#39; or &#39;account&#39;. The \&quot;replacement_chain_context_id\&quot; parameter must also be included. | [optional] 
 **replacement_chain_context_id** | **int**| When a user replaces a file during upload, Canvas keeps track of the \&quot;replacement chain.\&quot;  Include this parameter if you wish Canvas to follow the replacement chain if the requested file was deleted and replaced by another.  Indicates the context ID Canvas should use when following the \&quot;replacement chain.\&quot; The \&quot;replacement_chain_context_type\&quot; parameter must also be included. | [optional] 

### Return type

[**File**](File.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | File |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_api_show_for_other**
> File files_api_show_for_other(id, files_api_show_for_other_request=files_api_show_for_other_request)

Get file

Returns the standard attachment json object

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.file import File
from canvas_lms_python_client.models.files_api_show_for_other_request import FilesApiShowForOtherRequest
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
    api_instance = canvas_lms_python_client.FilesApi(api_client)
    id = 'id_example' # str | Scope response to id
    files_api_show_for_other_request = canvas_lms_python_client.FilesApiShowForOtherRequest() # FilesApiShowForOtherRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/files/<file_id>' \\       -H 'Authorization: Bearer <token>'  curl 'https://<canvas>/api/v1/courses/<course_id>/files/<file_id>' \\       -H 'Authorization: Bearer <token>' ``` (optional)

    try:
        # Get file
        api_response = await api_instance.files_api_show_for_other(id, files_api_show_for_other_request=files_api_show_for_other_request)
        print("The response of FilesApi->files_api_show_for_other:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->files_api_show_for_other: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **files_api_show_for_other_request** | [**FilesApiShowForOtherRequest**](FilesApiShowForOtherRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/files/&lt;file_id&gt;&#39; \\       -H &#39;Authorization: Bearer &lt;token&gt;&#39;  curl &#39;https://&lt;canvas&gt;/api/v1/courses/&lt;course_id&gt;/files/&lt;file_id&gt;&#39; \\       -H &#39;Authorization: Bearer &lt;token&gt;&#39; &#x60;&#x60;&#x60; | [optional] 

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

# **files_api_show_for_users**
> File files_api_show_for_users(id, user_id, include_user=include_user, replacement_chain_context_type=replacement_chain_context_type, replacement_chain_context_id=replacement_chain_context_id)

Get file

Returns the standard attachment json object

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.file import File
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
    api_instance = canvas_lms_python_client.FilesApi(api_client)
    id = 'id_example' # str | Scope response to id
    user_id = 'user_id_example' # str | Scope response to user_id
    include_user = 'include_user_example' # str | Array of additional information to include.  \"user\":: the user who uploaded the file or last edited its content \"usage_rights\":: copyright and license information for the file (see UsageRights) (optional)
    replacement_chain_context_type = 'replacement_chain_context_type_example' # str | When a user replaces a file during upload, Canvas keeps track of the \"replacement chain.\"  Include this parameter if you wish Canvas to follow the replacement chain if the requested file was deleted and replaced by another.  Must be set to 'course' or 'account'. The \"replacement_chain_context_id\" parameter must also be included. (optional)
    replacement_chain_context_id = 56 # int | When a user replaces a file during upload, Canvas keeps track of the \"replacement chain.\"  Include this parameter if you wish Canvas to follow the replacement chain if the requested file was deleted and replaced by another.  Indicates the context ID Canvas should use when following the \"replacement chain.\" The \"replacement_chain_context_type\" parameter must also be included. (optional)

    try:
        # Get file
        api_response = await api_instance.files_api_show_for_users(id, user_id, include_user=include_user, replacement_chain_context_type=replacement_chain_context_type, replacement_chain_context_id=replacement_chain_context_id)
        print("The response of FilesApi->files_api_show_for_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->files_api_show_for_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **user_id** | **str**| Scope response to user_id | 
 **include_user** | **str**| Array of additional information to include.  \&quot;user\&quot;:: the user who uploaded the file or last edited its content \&quot;usage_rights\&quot;:: copyright and license information for the file (see UsageRights) | [optional] 
 **replacement_chain_context_type** | **str**| When a user replaces a file during upload, Canvas keeps track of the \&quot;replacement chain.\&quot;  Include this parameter if you wish Canvas to follow the replacement chain if the requested file was deleted and replaced by another.  Must be set to &#39;course&#39; or &#39;account&#39;. The \&quot;replacement_chain_context_id\&quot; parameter must also be included. | [optional] 
 **replacement_chain_context_id** | **int**| When a user replaces a file during upload, Canvas keeps track of the \&quot;replacement chain.\&quot;  Include this parameter if you wish Canvas to follow the replacement chain if the requested file was deleted and replaced by another.  Indicates the context ID Canvas should use when following the \&quot;replacement chain.\&quot; The \&quot;replacement_chain_context_type\&quot; parameter must also be included. | [optional] 

### Return type

[**File**](File.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | File |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_api_update**
> File files_api_update(id, files_api_update_request=files_api_update_request)

Update file

Update some settings on the specified file

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.file import File
from canvas_lms_python_client.models.files_api_update_request import FilesApiUpdateRequest
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
    api_instance = canvas_lms_python_client.FilesApi(api_client)
    id = 'id_example' # str | Scope response to id
    files_api_update_request = canvas_lms_python_client.FilesApiUpdateRequest() # FilesApiUpdateRequest | Request body parameters  **Example Request:** ``` curl -X PUT 'https://<canvas>/api/v1/files/<file_id>' \\      -F 'name=<new_name>' \\      -F 'locked=true' \\      -H 'Authorization: Bearer <token>' ``` (optional)

    try:
        # Update file
        api_response = await api_instance.files_api_update(id, files_api_update_request=files_api_update_request)
        print("The response of FilesApi->files_api_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->files_api_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **files_api_update_request** | [**FilesApiUpdateRequest**](FilesApiUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl -X PUT &#39;https://&lt;canvas&gt;/api/v1/files/&lt;file_id&gt;&#39; \\      -F &#39;name&#x3D;&lt;new_name&gt;&#39; \\      -F &#39;locked&#x3D;true&#39; \\      -H &#39;Authorization: Bearer &lt;token&gt;&#39; &#x60;&#x60;&#x60; | [optional] 

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

# **files_destroy**
> File files_destroy(id, replace=replace)

Delete file

Remove the specified file. Unlike most other DELETE endpoints, using this
endpoint will result in comprehensive, irretrievable destruction of the file.
It should be used with the `replace` parameter set to true in cases where the
file preview also needs to be destroyed (such as to remove files that violate
privacy laws).

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.file import File
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
    api_instance = canvas_lms_python_client.FilesApi(api_client)
    id = 'id_example' # str | Scope response to id
    replace = True # bool | This action is irreversible. If replace is set to true the file contents will be replaced with a generic \"file has been removed\" file. This also destroys any previews that have been generated for the file. Must have manage files and become other users permissions (optional)

    try:
        # Delete file
        api_response = await api_instance.files_destroy(id, replace=replace)
        print("The response of FilesApi->files_destroy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->files_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **replace** | **bool**| This action is irreversible. If replace is set to true the file contents will be replaced with a generic \&quot;file has been removed\&quot; file. This also destroys any previews that have been generated for the file. Must have manage files and become other users permissions | [optional] 

### Return type

[**File**](File.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | File |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_file_ref**
> File files_file_ref(course_id, migration_id)

Translate file reference

Get information about a file from a course copy file reference

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.file import File
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
    api_instance = canvas_lms_python_client.FilesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    migration_id = 'migration_id_example' # str | Scope response to migration_id

    try:
        # Translate file reference
        api_response = await api_instance.files_file_ref(course_id, migration_id)
        print("The response of FilesApi->files_file_ref:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->files_file_ref: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **migration_id** | **str**| Scope response to migration_id | 

### Return type

[**File**](File.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | File |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_icon_metadata**
> files_icon_metadata(id)

Get icon metadata

Returns the icon maker file attachment metadata

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
    api_instance = canvas_lms_python_client.FilesApi(api_client)
    id = 'id_example' # str | Scope response to id

    try:
        # Get icon metadata
        await api_instance.files_icon_metadata(id)
    except Exception as e:
        print("Exception when calling FilesApi->files_icon_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Get icon metadata |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_public_url**
> files_public_url(id, submission_id=submission_id)

Get public inline preview url

Determine the URL that should be used for inline preview of the file.

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
    api_instance = canvas_lms_python_client.FilesApi(api_client)
    id = 'id_example' # str | Scope response to id
    submission_id = 56 # int | The id of the submission the file is associated with.  Provide this argument to gain access to a file that has been submitted to an assignment (Canvas will verify that the file belongs to the submission and the calling user has rights to view the submission). (optional)

    try:
        # Get public inline preview url
        await api_instance.files_public_url(id, submission_id=submission_id)
    except Exception as e:
        print("Exception when calling FilesApi->files_public_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **submission_id** | **int**| The id of the submission the file is associated with.  Provide this argument to gain access to a file that has been submitted to an assignment (Canvas will verify that the file belongs to the submission and the calling user has rights to view the submission). | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Get public inline preview url |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_reset_verifier**
> File files_reset_verifier(id)

Reset link verifier

Resets the link verifier. Any existing links to the file using
the previous hard-coded "verifier" parameter will no longer
automatically grant access.

Must have manage files and become other users permissions

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.file import File
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
    api_instance = canvas_lms_python_client.FilesApi(api_client)
    id = 'id_example' # str | Scope response to id

    try:
        # Reset link verifier
        api_response = await api_instance.files_reset_verifier(id)
        print("The response of FilesApi->files_reset_verifier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->files_reset_verifier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 

### Return type

[**File**](File.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | File |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_show**
> File files_show(course_id, file_id)

Download file

Downloads the file

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.file import File
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
    api_instance = canvas_lms_python_client.FilesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    file_id = 'file_id_example' # str | Scope response to file_id

    try:
        # Download file
        api_response = await api_instance.files_show(course_id, file_id)
        print("The response of FilesApi->files_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->files_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **file_id** | **str**| Scope response to file_id | 

### Return type

[**File**](File.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | File |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_show_by_download_for_other**
> File files_show_by_download_for_other(file_id, quiz_submission_id)

Download file

Downloads the file

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.file import File
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
    api_instance = canvas_lms_python_client.FilesApi(api_client)
    file_id = 'file_id_example' # str | Scope response to file_id
    quiz_submission_id = 'quiz_submission_id_example' # str | Scope response to quiz_submission_id

    try:
        # Download file
        api_response = await api_instance.files_show_by_download_for_other(file_id, quiz_submission_id)
        print("The response of FilesApi->files_show_by_download_for_other:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->files_show_by_download_for_other: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| Scope response to file_id | 
 **quiz_submission_id** | **str**| Scope response to quiz_submission_id | 

### Return type

[**File**](File.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | File |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_show_for_accounts**
> File files_show_for_accounts(account_id, file_id)

Download file

Downloads the file

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.file import File
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
    api_instance = canvas_lms_python_client.FilesApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    file_id = 'file_id_example' # str | Scope response to file_id

    try:
        # Download file
        api_response = await api_instance.files_show_for_accounts(account_id, file_id)
        print("The response of FilesApi->files_show_for_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->files_show_for_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **file_id** | **str**| Scope response to file_id | 

### Return type

[**File**](File.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | File |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_show_for_assessment_questions**
> File files_show_for_assessment_questions(assessment_question_id, file_id)

Download file

Downloads the file

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.file import File
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
    api_instance = canvas_lms_python_client.FilesApi(api_client)
    assessment_question_id = 'assessment_question_id_example' # str | Scope response to assessment_question_id
    file_id = 'file_id_example' # str | Scope response to file_id

    try:
        # Download file
        api_response = await api_instance.files_show_for_assessment_questions(assessment_question_id, file_id)
        print("The response of FilesApi->files_show_for_assessment_questions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->files_show_for_assessment_questions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assessment_question_id** | **str**| Scope response to assessment_question_id | 
 **file_id** | **str**| Scope response to file_id | 

### Return type

[**File**](File.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | File |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_show_for_assignments**
> File files_show_for_assignments(assignment_id, id)

Download file

Downloads the file

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.file import File
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
    api_instance = canvas_lms_python_client.FilesApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    id = 'id_example' # str | Scope response to id

    try:
        # Download file
        api_response = await api_instance.files_show_for_assignments(assignment_id, id)
        print("The response of FilesApi->files_show_for_assignments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->files_show_for_assignments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**File**](File.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | File |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_show_for_groups**
> File files_show_for_groups(file_id, group_id)

Download file

Downloads the file

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.file import File
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
    api_instance = canvas_lms_python_client.FilesApi(api_client)
    file_id = 'file_id_example' # str | Scope response to file_id
    group_id = 'group_id_example' # str | Scope response to group_id

    try:
        # Download file
        api_response = await api_instance.files_show_for_groups(file_id, group_id)
        print("The response of FilesApi->files_show_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->files_show_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| Scope response to file_id | 
 **group_id** | **str**| Scope response to group_id | 

### Return type

[**File**](File.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | File |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_show_for_other**
> File files_show_for_other(file_id)

Download file

Downloads the file

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.file import File
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
    api_instance = canvas_lms_python_client.FilesApi(api_client)
    file_id = 'file_id_example' # str | Scope response to file_id

    try:
        # Download file
        api_response = await api_instance.files_show_for_other(file_id)
        print("The response of FilesApi->files_show_for_other:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->files_show_for_other: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| Scope response to file_id | 

### Return type

[**File**](File.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | File |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_show_for_quiz_statistics**
> File files_show_for_quiz_statistics(file_id, quiz_statistics_id)

Download file

Downloads the file

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.file import File
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
    api_instance = canvas_lms_python_client.FilesApi(api_client)
    file_id = 'file_id_example' # str | Scope response to file_id
    quiz_statistics_id = 'quiz_statistics_id_example' # str | Scope response to quiz_statistics_id

    try:
        # Download file
        api_response = await api_instance.files_show_for_quiz_statistics(file_id, quiz_statistics_id)
        print("The response of FilesApi->files_show_for_quiz_statistics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->files_show_for_quiz_statistics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| Scope response to file_id | 
 **quiz_statistics_id** | **str**| Scope response to quiz_statistics_id | 

### Return type

[**File**](File.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | File |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_show_for_users**
> File files_show_for_users(file_id, user_id)

Download file

Downloads the file

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.file import File
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
    api_instance = canvas_lms_python_client.FilesApi(api_client)
    file_id = 'file_id_example' # str | Scope response to file_id
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # Download file
        api_response = await api_instance.files_show_for_users(file_id, user_id)
        print("The response of FilesApi->files_show_for_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->files_show_for_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| Scope response to file_id | 
 **user_id** | **str**| Scope response to user_id | 

### Return type

[**File**](File.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | File |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

