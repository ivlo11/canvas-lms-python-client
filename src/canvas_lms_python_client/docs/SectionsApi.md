# canvas_lms_python_client.SectionsApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sections_create**](SectionsApi.md#sections_create) | **POST** /api/v1/courses/{course_id}/sections | Create course section
[**sections_crosslist**](SectionsApi.md#sections_crosslist) | **POST** /api/v1/sections/{id}/crosslist/{new_course_id} | Cross-list a Section
[**sections_destroy**](SectionsApi.md#sections_destroy) | **DELETE** /api/v1/sections/{id} | Delete a section
[**sections_index**](SectionsApi.md#sections_index) | **GET** /api/v1/courses/{course_id}/sections | List course sections
[**sections_show**](SectionsApi.md#sections_show) | **GET** /api/v1/courses/{course_id}/sections/{id} | Get section information
[**sections_show_for_other**](SectionsApi.md#sections_show_for_other) | **GET** /api/v1/sections/{id} | Get section information
[**sections_uncrosslist**](SectionsApi.md#sections_uncrosslist) | **DELETE** /api/v1/sections/{id}/crosslist | De-cross-list a Section
[**sections_update**](SectionsApi.md#sections_update) | **PUT** /api/v1/sections/{id} | Edit a section
[**sections_users**](SectionsApi.md#sections_users) | **GET** /api/v1/sections/{id}/users | List section&#39;s users


# **sections_create**
> Section sections_create(course_id, sections_create_request=sections_create_request)

Create course section

Creates a new section for this course.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.section import Section
from canvas_lms_python_client.models.sections_create_request import SectionsCreateRequest
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
    api_instance = canvas_lms_python_client.SectionsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    sections_create_request = canvas_lms_python_client.SectionsCreateRequest() # SectionsCreateRequest | Request body parameters (optional)

    try:
        # Create course section
        api_response = await api_instance.sections_create(course_id, sections_create_request=sections_create_request)
        print("The response of SectionsApi->sections_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SectionsApi->sections_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **sections_create_request** | [**SectionsCreateRequest**](SectionsCreateRequest.md)| Request body parameters | [optional] 

### Return type

[**Section**](Section.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Section |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sections_crosslist**
> Section sections_crosslist(id, new_course_id, sections_crosslist_request=sections_crosslist_request)

Cross-list a Section

Move the Section to another course.  The new course may be in a different account (department),
but must belong to the same root account (institution).

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.section import Section
from canvas_lms_python_client.models.sections_crosslist_request import SectionsCrosslistRequest
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
    api_instance = canvas_lms_python_client.SectionsApi(api_client)
    id = 'id_example' # str | Scope response to id
    new_course_id = 'new_course_id_example' # str | Scope response to new_course_id
    sections_crosslist_request = canvas_lms_python_client.SectionsCrosslistRequest() # SectionsCrosslistRequest | Request body parameters (optional)

    try:
        # Cross-list a Section
        api_response = await api_instance.sections_crosslist(id, new_course_id, sections_crosslist_request=sections_crosslist_request)
        print("The response of SectionsApi->sections_crosslist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SectionsApi->sections_crosslist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **new_course_id** | **str**| Scope response to new_course_id | 
 **sections_crosslist_request** | [**SectionsCrosslistRequest**](SectionsCrosslistRequest.md)| Request body parameters | [optional] 

### Return type

[**Section**](Section.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Section |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sections_destroy**
> Section sections_destroy(id)

Delete a section

Delete an existing section.  Returns the former Section.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.section import Section
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
    api_instance = canvas_lms_python_client.SectionsApi(api_client)
    id = 'id_example' # str | Scope response to id

    try:
        # Delete a section
        api_response = await api_instance.sections_destroy(id)
        print("The response of SectionsApi->sections_destroy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SectionsApi->sections_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 

### Return type

[**Section**](Section.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Section |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sections_index**
> List[Section] sections_index(course_id, include=include, search_term=search_term, page=page, per_page=per_page)

List course sections

A paginated list of the list of sections for this course.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.section import Section
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
    api_instance = canvas_lms_python_client.SectionsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    include = ['include_example'] # List[str] | - \"students\": Associations to include with the group. Note: this is only   available if you have permission to view users or grades in the course - \"avatar_url\": Include the avatar URLs for students returned. - \"enrollments\": If 'students' is also included, return the section   enrollment for each student - \"total_students\": Returns the total amount of active and invited students   for the course section - \"passback_status\": Include the grade passback status. - \"permissions\": Include whether section grants :manage_calendar permission   to the caller (optional)
    search_term = 'search_term_example' # str | When included, searches course sections for the term. Returns only matching results. Term must be at least 2 characters. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List course sections
        api_response = await api_instance.sections_index(course_id, include=include, search_term=search_term, page=page, per_page=per_page)
        print("The response of SectionsApi->sections_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SectionsApi->sections_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **include** | [**List[str]**](str.md)| - \&quot;students\&quot;: Associations to include with the group. Note: this is only   available if you have permission to view users or grades in the course - \&quot;avatar_url\&quot;: Include the avatar URLs for students returned. - \&quot;enrollments\&quot;: If &#39;students&#39; is also included, return the section   enrollment for each student - \&quot;total_students\&quot;: Returns the total amount of active and invited students   for the course section - \&quot;passback_status\&quot;: Include the grade passback status. - \&quot;permissions\&quot;: Include whether section grants :manage_calendar permission   to the caller | [optional] 
 **search_term** | **str**| When included, searches course sections for the term. Returns only matching results. Term must be at least 2 characters. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[Section]**](Section.md)

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

# **sections_show**
> Section sections_show(course_id, id, include=include)

Get section information

Gets details about a specific section

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.section import Section
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
    api_instance = canvas_lms_python_client.SectionsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    include = ['include_example'] # List[str] | - \"students\": Associations to include with the group. Note: this is only   available if you have permission to view users or grades in the course - \"avatar_url\": Include the avatar URLs for students returned. - \"enrollments\": If 'students' is also included, return the section   enrollment for each student - \"total_students\": Returns the total amount of active and invited students   for the course section - \"passback_status\": Include the grade passback status. - \"permissions\": Include whether section grants :manage_calendar permission   to the caller (optional)

    try:
        # Get section information
        api_response = await api_instance.sections_show(course_id, id, include=include)
        print("The response of SectionsApi->sections_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SectionsApi->sections_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **include** | [**List[str]**](str.md)| - \&quot;students\&quot;: Associations to include with the group. Note: this is only   available if you have permission to view users or grades in the course - \&quot;avatar_url\&quot;: Include the avatar URLs for students returned. - \&quot;enrollments\&quot;: If &#39;students&#39; is also included, return the section   enrollment for each student - \&quot;total_students\&quot;: Returns the total amount of active and invited students   for the course section - \&quot;passback_status\&quot;: Include the grade passback status. - \&quot;permissions\&quot;: Include whether section grants :manage_calendar permission   to the caller | [optional] 

### Return type

[**Section**](Section.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Section |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sections_show_for_other**
> Section sections_show_for_other(id, include=include)

Get section information

Gets details about a specific section

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.section import Section
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
    api_instance = canvas_lms_python_client.SectionsApi(api_client)
    id = 'id_example' # str | Scope response to id
    include = ['include_example'] # List[str] | - \"students\": Associations to include with the group. Note: this is only   available if you have permission to view users or grades in the course - \"avatar_url\": Include the avatar URLs for students returned. - \"enrollments\": If 'students' is also included, return the section   enrollment for each student - \"total_students\": Returns the total amount of active and invited students   for the course section - \"passback_status\": Include the grade passback status. - \"permissions\": Include whether section grants :manage_calendar permission   to the caller (optional)

    try:
        # Get section information
        api_response = await api_instance.sections_show_for_other(id, include=include)
        print("The response of SectionsApi->sections_show_for_other:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SectionsApi->sections_show_for_other: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **include** | [**List[str]**](str.md)| - \&quot;students\&quot;: Associations to include with the group. Note: this is only   available if you have permission to view users or grades in the course - \&quot;avatar_url\&quot;: Include the avatar URLs for students returned. - \&quot;enrollments\&quot;: If &#39;students&#39; is also included, return the section   enrollment for each student - \&quot;total_students\&quot;: Returns the total amount of active and invited students   for the course section - \&quot;passback_status\&quot;: Include the grade passback status. - \&quot;permissions\&quot;: Include whether section grants :manage_calendar permission   to the caller | [optional] 

### Return type

[**Section**](Section.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Section |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sections_uncrosslist**
> Section sections_uncrosslist(id, override_sis_stickiness=override_sis_stickiness)

De-cross-list a Section

Undo cross-listing of a Section, returning it to its original course.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.section import Section
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
    api_instance = canvas_lms_python_client.SectionsApi(api_client)
    id = 'id_example' # str | Scope response to id
    override_sis_stickiness = True # bool | Default is true. If false, any fields containing “sticky” changes will not be updated. See SIS CSV Format documentation for information on which fields can have SIS stickiness (optional)

    try:
        # De-cross-list a Section
        api_response = await api_instance.sections_uncrosslist(id, override_sis_stickiness=override_sis_stickiness)
        print("The response of SectionsApi->sections_uncrosslist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SectionsApi->sections_uncrosslist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **override_sis_stickiness** | **bool**| Default is true. If false, any fields containing “sticky” changes will not be updated. See SIS CSV Format documentation for information on which fields can have SIS stickiness | [optional] 

### Return type

[**Section**](Section.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Section |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sections_update**
> Section sections_update(id, sections_update_request=sections_update_request)

Edit a section

Modify an existing section.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.section import Section
from canvas_lms_python_client.models.sections_update_request import SectionsUpdateRequest
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
    api_instance = canvas_lms_python_client.SectionsApi(api_client)
    id = 'id_example' # str | Scope response to id
    sections_update_request = canvas_lms_python_client.SectionsUpdateRequest() # SectionsUpdateRequest | Request body parameters (optional)

    try:
        # Edit a section
        api_response = await api_instance.sections_update(id, sections_update_request=sections_update_request)
        print("The response of SectionsApi->sections_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SectionsApi->sections_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **sections_update_request** | [**SectionsUpdateRequest**](SectionsUpdateRequest.md)| Request body parameters | [optional] 

### Return type

[**Section**](Section.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Section |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sections_users**
> List[User] sections_users(id, search_term=search_term, include=include, exclude_inactive=exclude_inactive, enrollment_type=enrollment_type, page=page, per_page=per_page)

List section's users

Returns a paginated list of users in the section.

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
    api_instance = canvas_lms_python_client.SectionsApi(api_client)
    id = 'id_example' # str | Scope response to id
    search_term = 'search_term_example' # str | The partial name or full ID of the users to match and return in the results list. Must be at least 2 characters. (optional)
    include = ['include_example'] # List[str] | \"avatar_url\": Include users' avatar_urls. (optional)
    exclude_inactive = True # bool | Whether to filter out inactive users from the results. Defaults to false unless explicitly provided. (optional)
    enrollment_type = 'enrollment_type_example' # str | When set, only return users with the specified enrollment type for the given section. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List section's users
        api_response = await api_instance.sections_users(id, search_term=search_term, include=include, exclude_inactive=exclude_inactive, enrollment_type=enrollment_type, page=page, per_page=per_page)
        print("The response of SectionsApi->sections_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SectionsApi->sections_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **search_term** | **str**| The partial name or full ID of the users to match and return in the results list. Must be at least 2 characters. | [optional] 
 **include** | [**List[str]**](str.md)| \&quot;avatar_url\&quot;: Include users&#39; avatar_urls. | [optional] 
 **exclude_inactive** | **bool**| Whether to filter out inactive users from the results. Defaults to false unless explicitly provided. | [optional] 
 **enrollment_type** | **str**| When set, only return users with the specified enrollment type for the given section. | [optional] 
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

