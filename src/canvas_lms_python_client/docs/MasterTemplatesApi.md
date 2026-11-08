# canvas_lms_python_client.MasterTemplatesApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**master_templates_associated_courses**](MasterTemplatesApi.md#master_templates_associated_courses) | **GET** /api/v1/courses/{course_id}/blueprint_templates/{template_id}/associated_courses | Get associated course information
[**master_templates_import_details**](MasterTemplatesApi.md#master_templates_import_details) | **GET** /api/v1/courses/{course_id}/blueprint_subscriptions/{subscription_id}/migrations/{id}/details | Get import details
[**master_templates_imports_index**](MasterTemplatesApi.md#master_templates_imports_index) | **GET** /api/v1/courses/{course_id}/blueprint_subscriptions/{subscription_id}/migrations | List blueprint imports
[**master_templates_imports_show**](MasterTemplatesApi.md#master_templates_imports_show) | **GET** /api/v1/courses/{course_id}/blueprint_subscriptions/{subscription_id}/migrations/{id} | Show a blueprint import
[**master_templates_migration_details**](MasterTemplatesApi.md#master_templates_migration_details) | **GET** /api/v1/courses/{course_id}/blueprint_templates/{template_id}/migrations/{id}/details | Get migration details
[**master_templates_migrations_index**](MasterTemplatesApi.md#master_templates_migrations_index) | **GET** /api/v1/courses/{course_id}/blueprint_templates/{template_id}/migrations | List blueprint migrations
[**master_templates_migrations_show**](MasterTemplatesApi.md#master_templates_migrations_show) | **GET** /api/v1/courses/{course_id}/blueprint_templates/{template_id}/migrations/{id} | Show a blueprint migration
[**master_templates_queue_migration**](MasterTemplatesApi.md#master_templates_queue_migration) | **POST** /api/v1/courses/{course_id}/blueprint_templates/{template_id}/migrations | Begin a migration to push to associated courses
[**master_templates_restrict_item**](MasterTemplatesApi.md#master_templates_restrict_item) | **PUT** /api/v1/courses/{course_id}/blueprint_templates/{template_id}/restrict_item | Set or remove restrictions on a blueprint course object
[**master_templates_show**](MasterTemplatesApi.md#master_templates_show) | **GET** /api/v1/courses/{course_id}/blueprint_templates/{template_id} | Get blueprint information
[**master_templates_subscriptions_index**](MasterTemplatesApi.md#master_templates_subscriptions_index) | **GET** /api/v1/courses/{course_id}/blueprint_subscriptions | List blueprint subscriptions
[**master_templates_unsynced_changes**](MasterTemplatesApi.md#master_templates_unsynced_changes) | **GET** /api/v1/courses/{course_id}/blueprint_templates/{template_id}/unsynced_changes | Get unsynced changes
[**master_templates_update_associations**](MasterTemplatesApi.md#master_templates_update_associations) | **PUT** /api/v1/courses/{course_id}/blueprint_templates/{template_id}/update_associations | Update associated courses


# **master_templates_associated_courses**
> List[Course] master_templates_associated_courses(course_id, template_id, page=page, per_page=per_page)

Get associated course information

Returns a list of courses that are configured to receive updates from this blueprint

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
    api_instance = canvas_lms_python_client.MasterTemplatesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    template_id = 'template_id_example' # str | Scope response to template_id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # Get associated course information
        api_response = await api_instance.master_templates_associated_courses(course_id, template_id, page=page, per_page=per_page)
        print("The response of MasterTemplatesApi->master_templates_associated_courses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MasterTemplatesApi->master_templates_associated_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **template_id** | **str**| Scope response to template_id | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

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

# **master_templates_import_details**
> List[ChangeRecord] master_templates_import_details(course_id, id, subscription_id)

Get import details

Show the changes that were propagated to a course associated with a blueprint.  See also
{api:MasterCourses::MasterTemplatesController#migration_details the blueprint course side}.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.change_record import ChangeRecord
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
    api_instance = canvas_lms_python_client.MasterTemplatesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    subscription_id = 'subscription_id_example' # str | Scope response to subscription_id

    try:
        # Get import details
        api_response = await api_instance.master_templates_import_details(course_id, id, subscription_id)
        print("The response of MasterTemplatesApi->master_templates_import_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MasterTemplatesApi->master_templates_import_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **subscription_id** | **str**| Scope response to subscription_id | 

### Return type

[**List[ChangeRecord]**](ChangeRecord.md)

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

# **master_templates_imports_index**
> List[BlueprintMigration] master_templates_imports_index(course_id, subscription_id, page=page, per_page=per_page)

List blueprint imports

Shows a paginated list of migrations imported into a course associated with a blueprint, starting with the most recent. See also
{api:MasterCourses::MasterTemplatesController#migrations_index the blueprint course side}.

Use 'default' as the subscription_id to use the currently active blueprint subscription.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.blueprint_migration import BlueprintMigration
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
    api_instance = canvas_lms_python_client.MasterTemplatesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    subscription_id = 'subscription_id_example' # str | Scope response to subscription_id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List blueprint imports
        api_response = await api_instance.master_templates_imports_index(course_id, subscription_id, page=page, per_page=per_page)
        print("The response of MasterTemplatesApi->master_templates_imports_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MasterTemplatesApi->master_templates_imports_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **subscription_id** | **str**| Scope response to subscription_id | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[BlueprintMigration]**](BlueprintMigration.md)

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

# **master_templates_imports_show**
> BlueprintMigration master_templates_imports_show(course_id, id, subscription_id)

Show a blueprint import

Shows the status of an import into a course associated with a blueprint. See also
{api:MasterCourses::MasterTemplatesController#migrations_show the blueprint course side}.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.blueprint_migration import BlueprintMigration
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
    api_instance = canvas_lms_python_client.MasterTemplatesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    subscription_id = 'subscription_id_example' # str | Scope response to subscription_id

    try:
        # Show a blueprint import
        api_response = await api_instance.master_templates_imports_show(course_id, id, subscription_id)
        print("The response of MasterTemplatesApi->master_templates_imports_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MasterTemplatesApi->master_templates_imports_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **subscription_id** | **str**| Scope response to subscription_id | 

### Return type

[**BlueprintMigration**](BlueprintMigration.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | BlueprintMigration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **master_templates_migration_details**
> List[ChangeRecord] master_templates_migration_details(course_id, id, template_id)

Get migration details

Show the changes that were propagated in a blueprint migration. This endpoint can be called on a
blueprint course. See also {api:MasterCourses::MasterTemplatesController#import_details the associated course side}.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.change_record import ChangeRecord
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
    api_instance = canvas_lms_python_client.MasterTemplatesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    template_id = 'template_id_example' # str | Scope response to template_id

    try:
        # Get migration details
        api_response = await api_instance.master_templates_migration_details(course_id, id, template_id)
        print("The response of MasterTemplatesApi->master_templates_migration_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MasterTemplatesApi->master_templates_migration_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **template_id** | **str**| Scope response to template_id | 

### Return type

[**List[ChangeRecord]**](ChangeRecord.md)

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

# **master_templates_migrations_index**
> List[BlueprintMigration] master_templates_migrations_index(course_id, template_id, page=page, per_page=per_page)

List blueprint migrations

Shows a paginated list of migrations for the template, starting with the most recent. This endpoint can be called on a
blueprint course. See also {api:MasterCourses::MasterTemplatesController#imports_index the associated course side}.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.blueprint_migration import BlueprintMigration
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
    api_instance = canvas_lms_python_client.MasterTemplatesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    template_id = 'template_id_example' # str | Scope response to template_id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List blueprint migrations
        api_response = await api_instance.master_templates_migrations_index(course_id, template_id, page=page, per_page=per_page)
        print("The response of MasterTemplatesApi->master_templates_migrations_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MasterTemplatesApi->master_templates_migrations_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **template_id** | **str**| Scope response to template_id | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[BlueprintMigration]**](BlueprintMigration.md)

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

# **master_templates_migrations_show**
> BlueprintMigration master_templates_migrations_show(course_id, id, template_id)

Show a blueprint migration

Shows the status of a migration. This endpoint can be called on a blueprint course. See also
{api:MasterCourses::MasterTemplatesController#imports_show the associated course side}.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.blueprint_migration import BlueprintMigration
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
    api_instance = canvas_lms_python_client.MasterTemplatesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    template_id = 'template_id_example' # str | Scope response to template_id

    try:
        # Show a blueprint migration
        api_response = await api_instance.master_templates_migrations_show(course_id, id, template_id)
        print("The response of MasterTemplatesApi->master_templates_migrations_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MasterTemplatesApi->master_templates_migrations_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **template_id** | **str**| Scope response to template_id | 

### Return type

[**BlueprintMigration**](BlueprintMigration.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | BlueprintMigration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **master_templates_queue_migration**
> BlueprintMigration master_templates_queue_migration(course_id, template_id, master_templates_queue_migration_request=master_templates_queue_migration_request)

Begin a migration to push to associated courses

Begins a migration to push recently updated content to all associated courses.
Only one migration can be running at a time.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.blueprint_migration import BlueprintMigration
from canvas_lms_python_client.models.master_templates_queue_migration_request import MasterTemplatesQueueMigrationRequest
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
    api_instance = canvas_lms_python_client.MasterTemplatesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    template_id = 'template_id_example' # str | Scope response to template_id
    master_templates_queue_migration_request = canvas_lms_python_client.MasterTemplatesQueueMigrationRequest() # MasterTemplatesQueueMigrationRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/courses/1/blueprint_templates/default/migrations \\ -X POST \\ -F 'comment=Fixed spelling in question 3 of midterm exam' \\ -F 'send_notification=true' \\ -H 'Authorization: Bearer <token>' ``` (optional)

    try:
        # Begin a migration to push to associated courses
        api_response = await api_instance.master_templates_queue_migration(course_id, template_id, master_templates_queue_migration_request=master_templates_queue_migration_request)
        print("The response of MasterTemplatesApi->master_templates_queue_migration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MasterTemplatesApi->master_templates_queue_migration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **template_id** | **str**| Scope response to template_id | 
 **master_templates_queue_migration_request** | [**MasterTemplatesQueueMigrationRequest**](MasterTemplatesQueueMigrationRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/courses/1/blueprint_templates/default/migrations \\ -X POST \\ -F &#39;comment&#x3D;Fixed spelling in question 3 of midterm exam&#39; \\ -F &#39;send_notification&#x3D;true&#39; \\ -H &#39;Authorization: Bearer &lt;token&gt;&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**BlueprintMigration**](BlueprintMigration.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | BlueprintMigration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **master_templates_restrict_item**
> MasterCoursesMasterTemplatesUpdateAssociationsResponse master_templates_restrict_item(course_id, template_id, master_templates_restrict_item_request=master_templates_restrict_item_request)

Set or remove restrictions on a blueprint course object

If a blueprint course object is restricted, editing will be limited for copies in associated courses.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.master_courses_master_templates_update_associations_response import MasterCoursesMasterTemplatesUpdateAssociationsResponse
from canvas_lms_python_client.models.master_templates_restrict_item_request import MasterTemplatesRestrictItemRequest
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
    api_instance = canvas_lms_python_client.MasterTemplatesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    template_id = 'template_id_example' # str | Scope response to template_id
    master_templates_restrict_item_request = canvas_lms_python_client.MasterTemplatesRestrictItemRequest() # MasterTemplatesRestrictItemRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/courses/1/blueprint_templates/default/restrict_item \\ -X PUT \\ -H 'Authorization: Bearer <token>' \\ -d 'content_type=assignment' \\ -d 'content_id=2' \\ -d 'restricted=true' ``` (optional)

    try:
        # Set or remove restrictions on a blueprint course object
        api_response = await api_instance.master_templates_restrict_item(course_id, template_id, master_templates_restrict_item_request=master_templates_restrict_item_request)
        print("The response of MasterTemplatesApi->master_templates_restrict_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MasterTemplatesApi->master_templates_restrict_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **template_id** | **str**| Scope response to template_id | 
 **master_templates_restrict_item_request** | [**MasterTemplatesRestrictItemRequest**](MasterTemplatesRestrictItemRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/courses/1/blueprint_templates/default/restrict_item \\ -X PUT \\ -H &#39;Authorization: Bearer &lt;token&gt;&#39; \\ -d &#39;content_type&#x3D;assignment&#39; \\ -d &#39;content_id&#x3D;2&#39; \\ -d &#39;restricted&#x3D;true&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**MasterCoursesMasterTemplatesUpdateAssociationsResponse**](MasterCoursesMasterTemplatesUpdateAssociationsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | MasterCoursesMasterTemplatesUpdateAssociationsResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **master_templates_show**
> BlueprintTemplate master_templates_show(course_id, template_id)

Get blueprint information

Using 'default' as the template_id should suffice for the current implmentation (as there should be only one template per course).
However, using specific template ids may become necessary in the future

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.blueprint_template import BlueprintTemplate
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
    api_instance = canvas_lms_python_client.MasterTemplatesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    template_id = 'template_id_example' # str | Scope response to template_id

    try:
        # Get blueprint information
        api_response = await api_instance.master_templates_show(course_id, template_id)
        print("The response of MasterTemplatesApi->master_templates_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MasterTemplatesApi->master_templates_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **template_id** | **str**| Scope response to template_id | 

### Return type

[**BlueprintTemplate**](BlueprintTemplate.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | BlueprintTemplate |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **master_templates_subscriptions_index**
> List[BlueprintSubscription] master_templates_subscriptions_index(course_id, page=page, per_page=per_page)

List blueprint subscriptions

Returns a list of blueprint subscriptions for the given course. (Currently a course may have no more than one.)

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.blueprint_subscription import BlueprintSubscription
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
    api_instance = canvas_lms_python_client.MasterTemplatesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List blueprint subscriptions
        api_response = await api_instance.master_templates_subscriptions_index(course_id, page=page, per_page=per_page)
        print("The response of MasterTemplatesApi->master_templates_subscriptions_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MasterTemplatesApi->master_templates_subscriptions_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[BlueprintSubscription]**](BlueprintSubscription.md)

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

# **master_templates_unsynced_changes**
> List[ChangeRecord] master_templates_unsynced_changes(course_id, template_id)

Get unsynced changes

Retrieve a list of learning objects that have changed since the last blueprint sync operation.
If no syncs have been completed, a ChangeRecord with a change_type of +initial_sync+ is returned.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.change_record import ChangeRecord
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
    api_instance = canvas_lms_python_client.MasterTemplatesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    template_id = 'template_id_example' # str | Scope response to template_id

    try:
        # Get unsynced changes
        api_response = await api_instance.master_templates_unsynced_changes(course_id, template_id)
        print("The response of MasterTemplatesApi->master_templates_unsynced_changes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MasterTemplatesApi->master_templates_unsynced_changes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **template_id** | **str**| Scope response to template_id | 

### Return type

[**List[ChangeRecord]**](ChangeRecord.md)

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

# **master_templates_update_associations**
> MasterCoursesMasterTemplatesUpdateAssociationsResponse master_templates_update_associations(course_id, template_id, master_templates_update_associations_request=master_templates_update_associations_request)

Update associated courses

Send a list of course ids to add or remove new associations for the template.
Cannot add courses that do not belong to the blueprint course's account. Also cannot add
other blueprint courses or courses that already have an association with another blueprint course.

After associating new courses, {api:MasterCourses::MasterTemplatesController#queue_migration start a sync} to populate their contents from the blueprint.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.master_courses_master_templates_update_associations_response import MasterCoursesMasterTemplatesUpdateAssociationsResponse
from canvas_lms_python_client.models.master_templates_update_associations_request import MasterTemplatesUpdateAssociationsRequest
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
    api_instance = canvas_lms_python_client.MasterTemplatesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    template_id = 'template_id_example' # str | Scope response to template_id
    master_templates_update_associations_request = canvas_lms_python_client.MasterTemplatesUpdateAssociationsRequest() # MasterTemplatesUpdateAssociationsRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/courses/1/blueprint_templates/default/update_associations \\ -X PUT \\ -H 'Authorization: Bearer <token>' \\ -d 'course_ids_to_add[]=1' \\ -d 'course_ids_to_remove[]=2' \\ ``` (optional)

    try:
        # Update associated courses
        api_response = await api_instance.master_templates_update_associations(course_id, template_id, master_templates_update_associations_request=master_templates_update_associations_request)
        print("The response of MasterTemplatesApi->master_templates_update_associations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MasterTemplatesApi->master_templates_update_associations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **template_id** | **str**| Scope response to template_id | 
 **master_templates_update_associations_request** | [**MasterTemplatesUpdateAssociationsRequest**](MasterTemplatesUpdateAssociationsRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/courses/1/blueprint_templates/default/update_associations \\ -X PUT \\ -H &#39;Authorization: Bearer &lt;token&gt;&#39; \\ -d &#39;course_ids_to_add[]&#x3D;1&#39; \\ -d &#39;course_ids_to_remove[]&#x3D;2&#39; \\ &#x60;&#x60;&#x60; | [optional] 

### Return type

[**MasterCoursesMasterTemplatesUpdateAssociationsResponse**](MasterCoursesMasterTemplatesUpdateAssociationsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | MasterCoursesMasterTemplatesUpdateAssociationsResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

