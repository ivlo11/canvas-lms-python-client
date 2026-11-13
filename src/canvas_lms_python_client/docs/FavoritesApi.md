# canvas_lms_python_client.FavoritesApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**favorites_add_favorite_course**](FavoritesApi.md#favorites_add_favorite_course) | **POST** /api/v1/users/self/favorites/courses/{id} | Add course to favorites
[**favorites_add_favorite_groups**](FavoritesApi.md#favorites_add_favorite_groups) | **POST** /api/v1/users/self/favorites/groups/{id} | Add group to favorites
[**favorites_list_favorite_courses**](FavoritesApi.md#favorites_list_favorite_courses) | **GET** /api/v1/users/self/favorites/courses | List favorite courses
[**favorites_list_favorite_groups**](FavoritesApi.md#favorites_list_favorite_groups) | **GET** /api/v1/users/self/favorites/groups | List favorite groups
[**favorites_remove_favorite_course**](FavoritesApi.md#favorites_remove_favorite_course) | **DELETE** /api/v1/users/self/favorites/courses/{id} | Remove course from favorites
[**favorites_remove_favorite_groups**](FavoritesApi.md#favorites_remove_favorite_groups) | **DELETE** /api/v1/users/self/favorites/groups/{id} | Remove group from favorites
[**favorites_reset_course_favorites**](FavoritesApi.md#favorites_reset_course_favorites) | **DELETE** /api/v1/users/self/favorites/courses | Reset course favorites
[**favorites_reset_groups_favorites**](FavoritesApi.md#favorites_reset_groups_favorites) | **DELETE** /api/v1/users/self/favorites/groups | Reset group favorites


# **favorites_add_favorite_course**
> Favorite favorites_add_favorite_course(id)

Add course to favorites

Add a course to the current user's favorites.  If the course is already
in the user's favorites, nothing happens. Canvas for Elementary subject
and homeroom courses can be added to favorites, but this has no effect in
the UI.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.favorite import Favorite
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
    api_instance = canvas_lms_python_client.FavoritesApi(api_client)
    id = 'id_example' # str | The ID or SIS ID of the course to add.  The current user must be registered in the course.

    try:
        # Add course to favorites
        api_response = await api_instance.favorites_add_favorite_course(id)
        print("The response of FavoritesApi->favorites_add_favorite_course:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FavoritesApi->favorites_add_favorite_course: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or SIS ID of the course to add.  The current user must be registered in the course. | 

### Return type

[**Favorite**](Favorite.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Favorite |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **favorites_add_favorite_groups**
> Favorite favorites_add_favorite_groups(id)

Add group to favorites

Add a group to the current user's favorites.  If the group is already
in the user's favorites, nothing happens.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.favorite import Favorite
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
    api_instance = canvas_lms_python_client.FavoritesApi(api_client)
    id = 'id_example' # str | The ID or SIS ID of the group to add.  The current user must be a member of the group.

    try:
        # Add group to favorites
        api_response = await api_instance.favorites_add_favorite_groups(id)
        print("The response of FavoritesApi->favorites_add_favorite_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FavoritesApi->favorites_add_favorite_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or SIS ID of the group to add.  The current user must be a member of the group. | 

### Return type

[**Favorite**](Favorite.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Favorite |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **favorites_list_favorite_courses**
> List[Course] favorites_list_favorite_courses(exclude_blueprint_courses=exclude_blueprint_courses)

List favorite courses

Retrieve the paginated list of favorite courses for the current user. If the user has not chosen
any favorites, then a selection of currently enrolled courses will be returned.

See the {api:CoursesController#index List courses API} for details on accepted include[] parameters.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.course import Course
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
    api_instance = canvas_lms_python_client.FavoritesApi(api_client)
    exclude_blueprint_courses = True # bool | When set, only return courses that are not configured as blueprint courses. (optional)

    try:
        # List favorite courses
        api_response = await api_instance.favorites_list_favorite_courses(exclude_blueprint_courses=exclude_blueprint_courses)
        print("The response of FavoritesApi->favorites_list_favorite_courses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FavoritesApi->favorites_list_favorite_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exclude_blueprint_courses** | **bool**| When set, only return courses that are not configured as blueprint courses. | [optional] 

### Return type

[**List[Course]**](Course.md)

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

# **favorites_list_favorite_groups**
> List[Group] favorites_list_favorite_groups()

List favorite groups

Retrieve the paginated list of favorite groups for the current user. If the user has not chosen
any favorites, then a selection of groups that the user is a member of will be returned.

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
    api_instance = canvas_lms_python_client.FavoritesApi(api_client)

    try:
        # List favorite groups
        api_response = await api_instance.favorites_list_favorite_groups()
        print("The response of FavoritesApi->favorites_list_favorite_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FavoritesApi->favorites_list_favorite_groups: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

# **favorites_remove_favorite_course**
> Favorite favorites_remove_favorite_course(id)

Remove course from favorites

Remove a course from the current user's favorites.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.favorite import Favorite
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
    api_instance = canvas_lms_python_client.FavoritesApi(api_client)
    id = 'id_example' # str | the ID or SIS ID of the course to remove

    try:
        # Remove course from favorites
        api_response = await api_instance.favorites_remove_favorite_course(id)
        print("The response of FavoritesApi->favorites_remove_favorite_course:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FavoritesApi->favorites_remove_favorite_course: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| the ID or SIS ID of the course to remove | 

### Return type

[**Favorite**](Favorite.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Favorite |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **favorites_remove_favorite_groups**
> Favorite favorites_remove_favorite_groups(id)

Remove group from favorites

Remove a group from the current user's favorites.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.favorite import Favorite
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
    api_instance = canvas_lms_python_client.FavoritesApi(api_client)
    id = 'id_example' # str | the ID or SIS ID of the group to remove

    try:
        # Remove group from favorites
        api_response = await api_instance.favorites_remove_favorite_groups(id)
        print("The response of FavoritesApi->favorites_remove_favorite_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FavoritesApi->favorites_remove_favorite_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| the ID or SIS ID of the group to remove | 

### Return type

[**Favorite**](Favorite.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Favorite |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **favorites_reset_course_favorites**
> FavoritesResetCourseFavoritesResponse favorites_reset_course_favorites()

Reset course favorites

Reset the current user's course favorites to the default
automatically generated list of enrolled courses

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.favorites_reset_course_favorites_response import FavoritesResetCourseFavoritesResponse
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
    api_instance = canvas_lms_python_client.FavoritesApi(api_client)

    try:
        # Reset course favorites
        api_response = await api_instance.favorites_reset_course_favorites()
        print("The response of FavoritesApi->favorites_reset_course_favorites:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FavoritesApi->favorites_reset_course_favorites: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**FavoritesResetCourseFavoritesResponse**](FavoritesResetCourseFavoritesResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | FavoritesResetCourseFavoritesResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **favorites_reset_groups_favorites**
> FavoritesResetCourseFavoritesResponse favorites_reset_groups_favorites()

Reset group favorites

Reset the current user's group favorites to the default
automatically generated list of enrolled group

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.favorites_reset_course_favorites_response import FavoritesResetCourseFavoritesResponse
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
    api_instance = canvas_lms_python_client.FavoritesApi(api_client)

    try:
        # Reset group favorites
        api_response = await api_instance.favorites_reset_groups_favorites()
        print("The response of FavoritesApi->favorites_reset_groups_favorites:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FavoritesApi->favorites_reset_groups_favorites: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**FavoritesResetCourseFavoritesResponse**](FavoritesResetCourseFavoritesResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | FavoritesResetCourseFavoritesResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

