# canvas_lms_python_client.CollaborationsApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**collaborations_api_index**](CollaborationsApi.md#collaborations_api_index) | **GET** /api/v1/courses/{course_id}/collaborations | List collaborations
[**collaborations_api_index_for_groups**](CollaborationsApi.md#collaborations_api_index_for_groups) | **GET** /api/v1/groups/{group_id}/collaborations | List collaborations
[**collaborations_members**](CollaborationsApi.md#collaborations_members) | **GET** /api/v1/collaborations/{id}/members | List members of a collaboration.
[**collaborations_potential_collaborators**](CollaborationsApi.md#collaborations_potential_collaborators) | **GET** /api/v1/courses/{course_id}/potential_collaborators | List potential members
[**collaborations_potential_collaborators_for_groups**](CollaborationsApi.md#collaborations_potential_collaborators_for_groups) | **GET** /api/v1/groups/{group_id}/potential_collaborators | List potential members


# **collaborations_api_index**
> List[Collaboration] collaborations_api_index(course_id, page=page, per_page=per_page)

List collaborations

A paginated list of collaborations the current user has access to in the
context of the course provided in the url. NOTE: this only returns
ExternalToolCollaboration type collaborations.

  curl https://<canvas>/api/v1/courses/1/collaborations/

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.collaboration import Collaboration
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
    api_instance = canvas_lms_python_client.CollaborationsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List collaborations
        api_response = await api_instance.collaborations_api_index(course_id, page=page, per_page=per_page)
        print("The response of CollaborationsApi->collaborations_api_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollaborationsApi->collaborations_api_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[Collaboration]**](Collaboration.md)

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

# **collaborations_api_index_for_groups**
> List[Collaboration] collaborations_api_index_for_groups(group_id, page=page, per_page=per_page)

List collaborations

A paginated list of collaborations the current user has access to in the
context of the course provided in the url. NOTE: this only returns
ExternalToolCollaboration type collaborations.

  curl https://<canvas>/api/v1/courses/1/collaborations/

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.collaboration import Collaboration
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
    api_instance = canvas_lms_python_client.CollaborationsApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List collaborations
        api_response = await api_instance.collaborations_api_index_for_groups(group_id, page=page, per_page=per_page)
        print("The response of CollaborationsApi->collaborations_api_index_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollaborationsApi->collaborations_api_index_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[Collaboration]**](Collaboration.md)

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

# **collaborations_members**
> List[Collaborator] collaborations_members(id, include=include, page=page, per_page=per_page)

List members of a collaboration.

A paginated list of the collaborators of a given collaboration

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.collaborator import Collaborator
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
    api_instance = canvas_lms_python_client.CollaborationsApi(api_client)
    id = 'id_example' # str | Scope response to id
    include = ['include_example'] # List[str] | - \"collaborator_lti_id\": Optional information to include with each member.   Represents an identifier to be used for the member in an LTI context. - \"avatar_image_url\": Optional information to include with each member.   The url for the avatar of a collaborator with type 'user'. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List members of a collaboration.
        api_response = await api_instance.collaborations_members(id, include=include, page=page, per_page=per_page)
        print("The response of CollaborationsApi->collaborations_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollaborationsApi->collaborations_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **include** | [**List[str]**](str.md)| - \&quot;collaborator_lti_id\&quot;: Optional information to include with each member.   Represents an identifier to be used for the member in an LTI context. - \&quot;avatar_image_url\&quot;: Optional information to include with each member.   The url for the avatar of a collaborator with type &#39;user&#39;. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[Collaborator]**](Collaborator.md)

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

# **collaborations_potential_collaborators**
> List[User] collaborations_potential_collaborators(course_id, page=page, per_page=per_page)

List potential members

A paginated list of the users who can potentially be added to a
collaboration in the given context.

For courses, this consists of all enrolled users.  For groups, it is comprised of the
group members plus the admins of the course containing the group.

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
    api_instance = canvas_lms_python_client.CollaborationsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List potential members
        api_response = await api_instance.collaborations_potential_collaborators(course_id, page=page, per_page=per_page)
        print("The response of CollaborationsApi->collaborations_potential_collaborators:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollaborationsApi->collaborations_potential_collaborators: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
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

# **collaborations_potential_collaborators_for_groups**
> List[User] collaborations_potential_collaborators_for_groups(group_id, page=page, per_page=per_page)

List potential members

A paginated list of the users who can potentially be added to a
collaboration in the given context.

For courses, this consists of all enrolled users.  For groups, it is comprised of the
group members plus the admins of the course containing the group.

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
    api_instance = canvas_lms_python_client.CollaborationsApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List potential members
        api_response = await api_instance.collaborations_potential_collaborators_for_groups(group_id, page=page, per_page=per_page)
        print("The response of CollaborationsApi->collaborations_potential_collaborators_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollaborationsApi->collaborations_potential_collaborators_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
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

