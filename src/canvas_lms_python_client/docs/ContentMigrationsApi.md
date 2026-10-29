# canvas_lms_python_client.ContentMigrationsApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**content_migrations_asset_id_mapping**](ContentMigrationsApi.md#content_migrations_asset_id_mapping) | **GET** /api/v1/courses/{course_id}/content_migrations/{id}/asset_id_mapping | Get asset id mapping
[**content_migrations_available_migrators**](ContentMigrationsApi.md#content_migrations_available_migrators) | **GET** /api/v1/accounts/{account_id}/content_migrations/migrators | List Migration Systems
[**content_migrations_available_migrators_for_courses**](ContentMigrationsApi.md#content_migrations_available_migrators_for_courses) | **GET** /api/v1/courses/{course_id}/content_migrations/migrators | List Migration Systems
[**content_migrations_available_migrators_for_groups**](ContentMigrationsApi.md#content_migrations_available_migrators_for_groups) | **GET** /api/v1/groups/{group_id}/content_migrations/migrators | List Migration Systems
[**content_migrations_available_migrators_for_users**](ContentMigrationsApi.md#content_migrations_available_migrators_for_users) | **GET** /api/v1/users/{user_id}/content_migrations/migrators | List Migration Systems
[**content_migrations_content_list**](ContentMigrationsApi.md#content_migrations_content_list) | **GET** /api/v1/accounts/{account_id}/content_migrations/{id}/selective_data | List items for selective import
[**content_migrations_content_list_for_courses**](ContentMigrationsApi.md#content_migrations_content_list_for_courses) | **GET** /api/v1/courses/{course_id}/content_migrations/{id}/selective_data | List items for selective import
[**content_migrations_content_list_for_groups**](ContentMigrationsApi.md#content_migrations_content_list_for_groups) | **GET** /api/v1/groups/{group_id}/content_migrations/{id}/selective_data | List items for selective import
[**content_migrations_content_list_for_users**](ContentMigrationsApi.md#content_migrations_content_list_for_users) | **GET** /api/v1/users/{user_id}/content_migrations/{id}/selective_data | List items for selective import
[**content_migrations_create**](ContentMigrationsApi.md#content_migrations_create) | **POST** /api/v1/accounts/{account_id}/content_migrations | Create a content migration
[**content_migrations_create_for_courses**](ContentMigrationsApi.md#content_migrations_create_for_courses) | **POST** /api/v1/courses/{course_id}/content_migrations | Create a content migration
[**content_migrations_create_for_groups**](ContentMigrationsApi.md#content_migrations_create_for_groups) | **POST** /api/v1/groups/{group_id}/content_migrations | Create a content migration
[**content_migrations_create_for_users**](ContentMigrationsApi.md#content_migrations_create_for_users) | **POST** /api/v1/users/{user_id}/content_migrations | Create a content migration
[**content_migrations_index**](ContentMigrationsApi.md#content_migrations_index) | **GET** /api/v1/accounts/{account_id}/content_migrations | List content migrations
[**content_migrations_index_for_courses**](ContentMigrationsApi.md#content_migrations_index_for_courses) | **GET** /api/v1/courses/{course_id}/content_migrations | List content migrations
[**content_migrations_index_for_groups**](ContentMigrationsApi.md#content_migrations_index_for_groups) | **GET** /api/v1/groups/{group_id}/content_migrations | List content migrations
[**content_migrations_index_for_users**](ContentMigrationsApi.md#content_migrations_index_for_users) | **GET** /api/v1/users/{user_id}/content_migrations | List content migrations
[**content_migrations_show**](ContentMigrationsApi.md#content_migrations_show) | **GET** /api/v1/accounts/{account_id}/content_migrations/{id} | Get a content migration
[**content_migrations_show_for_courses**](ContentMigrationsApi.md#content_migrations_show_for_courses) | **GET** /api/v1/courses/{course_id}/content_migrations/{id} | Get a content migration
[**content_migrations_show_for_groups**](ContentMigrationsApi.md#content_migrations_show_for_groups) | **GET** /api/v1/groups/{group_id}/content_migrations/{id} | Get a content migration
[**content_migrations_show_for_users**](ContentMigrationsApi.md#content_migrations_show_for_users) | **GET** /api/v1/users/{user_id}/content_migrations/{id} | Get a content migration
[**content_migrations_update**](ContentMigrationsApi.md#content_migrations_update) | **PUT** /api/v1/accounts/{account_id}/content_migrations/{id} | Update a content migration
[**content_migrations_update_for_courses**](ContentMigrationsApi.md#content_migrations_update_for_courses) | **PUT** /api/v1/courses/{course_id}/content_migrations/{id} | Update a content migration
[**content_migrations_update_for_groups**](ContentMigrationsApi.md#content_migrations_update_for_groups) | **PUT** /api/v1/groups/{group_id}/content_migrations/{id} | Update a content migration
[**content_migrations_update_for_users**](ContentMigrationsApi.md#content_migrations_update_for_users) | **PUT** /api/v1/users/{user_id}/content_migrations/{id} | Update a content migration


# **content_migrations_asset_id_mapping**
> content_migrations_asset_id_mapping(course_id, id)

Get asset id mapping

Given a complete course copy or blueprint import content migration, return a mapping of asset ids
from the source course to the destination course that were copied in this migration or an earlier one
with the same course pair and migration_type (course copy or blueprint).

The returned object's keys are asset types as they appear in API URLs (+announcements+, +assignments+,
+discussion_topics+, +files+, +module_items+, +modules+, +pages+, and +quizzes+). The values are a mapping
from id in source course to id in destination course for objects of this type.

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
    api_instance = canvas_lms_python_client.ContentMigrationsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id

    try:
        # Get asset id mapping
        await api_instance.content_migrations_asset_id_mapping(course_id, id)
    except Exception as e:
        print("Exception when calling ContentMigrationsApi->content_migrations_asset_id_mapping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
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
**0** | Get asset id mapping |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_migrations_available_migrators**
> List[Migrator] content_migrations_available_migrators(account_id)

List Migration Systems

Lists the currently available migration types. These values may change.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.migrator import Migrator
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
    api_instance = canvas_lms_python_client.ContentMigrationsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id

    try:
        # List Migration Systems
        api_response = await api_instance.content_migrations_available_migrators(account_id)
        print("The response of ContentMigrationsApi->content_migrations_available_migrators:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentMigrationsApi->content_migrations_available_migrators: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 

### Return type

[**List[Migrator]**](Migrator.md)

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

# **content_migrations_available_migrators_for_courses**
> List[Migrator] content_migrations_available_migrators_for_courses(course_id)

List Migration Systems

Lists the currently available migration types. These values may change.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.migrator import Migrator
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
    api_instance = canvas_lms_python_client.ContentMigrationsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id

    try:
        # List Migration Systems
        api_response = await api_instance.content_migrations_available_migrators_for_courses(course_id)
        print("The response of ContentMigrationsApi->content_migrations_available_migrators_for_courses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentMigrationsApi->content_migrations_available_migrators_for_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 

### Return type

[**List[Migrator]**](Migrator.md)

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

# **content_migrations_available_migrators_for_groups**
> List[Migrator] content_migrations_available_migrators_for_groups(group_id)

List Migration Systems

Lists the currently available migration types. These values may change.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.migrator import Migrator
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
    api_instance = canvas_lms_python_client.ContentMigrationsApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id

    try:
        # List Migration Systems
        api_response = await api_instance.content_migrations_available_migrators_for_groups(group_id)
        print("The response of ContentMigrationsApi->content_migrations_available_migrators_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentMigrationsApi->content_migrations_available_migrators_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 

### Return type

[**List[Migrator]**](Migrator.md)

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

# **content_migrations_available_migrators_for_users**
> List[Migrator] content_migrations_available_migrators_for_users(user_id)

List Migration Systems

Lists the currently available migration types. These values may change.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.migrator import Migrator
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
    api_instance = canvas_lms_python_client.ContentMigrationsApi(api_client)
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # List Migration Systems
        api_response = await api_instance.content_migrations_available_migrators_for_users(user_id)
        print("The response of ContentMigrationsApi->content_migrations_available_migrators_for_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentMigrationsApi->content_migrations_available_migrators_for_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Scope response to user_id | 

### Return type

[**List[Migrator]**](Migrator.md)

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

# **content_migrations_content_list**
> object content_migrations_content_list(account_id, id, type_context_modules_assignments_quizzes_assessment_question_banks_discussion_topics_wiki_pages_context_external_tools_tool_profiles_announcements_calendar_events_rubrics_groups_learning_outcomes_attachments=type_context_modules_assignments_quizzes_assessment_question_banks_discussion_topics_wiki_pages_context_external_tools_tool_profiles_announcements_calendar_events_rubrics_groups_learning_outcomes_attachments)

List items for selective import

Enumerates the content available for selective import in a tree structure. Each node provides
a +property+ copy argument that can be supplied to the {api:ContentMigrationsController#update Update endpoint}
to selectively copy the content associated with that tree node and its children. Each node may also
provide a +sub_items_url+ or an array of +sub_items+ which you can use to obtain copy parameters
for a subset of the resources in a given node.

If no +type+ is sent you will get a list of the top-level sections in the content. It will look something like this:

  [{
    "type": "course_settings",
    "property": "copy[all_course_settings]",
    "title": "Course Settings"
  },
  {
    "type": "context_modules",
    "property": "copy[all_context_modules]",
    "title": "Modules",
    "count": 5,
    "sub_items_url": "http://example.com/api/v1/courses/22/content_migrations/77/selective_data?type=context_modules"
  },
  {
    "type": "assignments",
    "property": "copy[all_assignments]",
    "title": "Assignments",
    "count": 2,
    "sub_items_url": "http://localhost:3000/api/v1/courses/22/content_migrations/77/selective_data?type=assignments"
  }]

When a +type+ is provided, nodes may be further divided via +sub_items+. For example, using +type=assignments+
results in a node for each assignment group and a sub_item for each assignment, like this:

  [{
    "type": "assignment_groups",
    "title": "An Assignment Group",
    "property": "copy[assignment_groups][id_i855cf145e5acc7435e1bf1c6e2126e5f]",
    "sub_items": [{
        "type": "assignments",
        "title": "Assignment 1",
        "property": "copy[assignments][id_i2102a7fa93b29226774949298626719d]"
    }, {
        "type": "assignments",
        "title": "Assignment 2",
        "property": "copy[assignments][id_i310cba275dc3f4aa8a3306bbbe380979]"
    }]
  }]


To import the items corresponding to a particular tree node, use the +property+ as a parameter to the
{api:ContentMigrationsController#update Update endpoint} and assign a value of 1, for example:

  copy[assignments][id_i310cba275dc3f4aa8a3306bbbe380979]=1

You can include multiple copy parameters to selectively import multiple items or groups of items.

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
    api_instance = canvas_lms_python_client.ContentMigrationsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id
    type_context_modules_assignments_quizzes_assessment_question_banks_discussion_topics_wiki_pages_context_external_tools_tool_profiles_announcements_calendar_events_rubrics_groups_learning_outcomes_attachments = 'type_context_modules_assignments_quizzes_assessment_question_banks_discussion_topics_wiki_pages_context_external_tools_tool_profiles_announcements_calendar_events_rubrics_groups_learning_outcomes_attachments_example' # str | The type of content to enumerate. (optional)

    try:
        # List items for selective import
        api_response = await api_instance.content_migrations_content_list(account_id, id, type_context_modules_assignments_quizzes_assessment_question_banks_discussion_topics_wiki_pages_context_external_tools_tool_profiles_announcements_calendar_events_rubrics_groups_learning_outcomes_attachments=type_context_modules_assignments_quizzes_assessment_question_banks_discussion_topics_wiki_pages_context_external_tools_tool_profiles_announcements_calendar_events_rubrics_groups_learning_outcomes_attachments)
        print("The response of ContentMigrationsApi->content_migrations_content_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentMigrationsApi->content_migrations_content_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 
 **type_context_modules_assignments_quizzes_assessment_question_banks_discussion_topics_wiki_pages_context_external_tools_tool_profiles_announcements_calendar_events_rubrics_groups_learning_outcomes_attachments** | **str**| The type of content to enumerate. | [optional] 

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
**0** | list of content items |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_migrations_content_list_for_courses**
> object content_migrations_content_list_for_courses(course_id, id, type_context_modules_assignments_quizzes_assessment_question_banks_discussion_topics_wiki_pages_context_external_tools_tool_profiles_announcements_calendar_events_rubrics_groups_learning_outcomes_attachments=type_context_modules_assignments_quizzes_assessment_question_banks_discussion_topics_wiki_pages_context_external_tools_tool_profiles_announcements_calendar_events_rubrics_groups_learning_outcomes_attachments)

List items for selective import

Enumerates the content available for selective import in a tree structure. Each node provides
a +property+ copy argument that can be supplied to the {api:ContentMigrationsController#update Update endpoint}
to selectively copy the content associated with that tree node and its children. Each node may also
provide a +sub_items_url+ or an array of +sub_items+ which you can use to obtain copy parameters
for a subset of the resources in a given node.

If no +type+ is sent you will get a list of the top-level sections in the content. It will look something like this:

  [{
    "type": "course_settings",
    "property": "copy[all_course_settings]",
    "title": "Course Settings"
  },
  {
    "type": "context_modules",
    "property": "copy[all_context_modules]",
    "title": "Modules",
    "count": 5,
    "sub_items_url": "http://example.com/api/v1/courses/22/content_migrations/77/selective_data?type=context_modules"
  },
  {
    "type": "assignments",
    "property": "copy[all_assignments]",
    "title": "Assignments",
    "count": 2,
    "sub_items_url": "http://localhost:3000/api/v1/courses/22/content_migrations/77/selective_data?type=assignments"
  }]

When a +type+ is provided, nodes may be further divided via +sub_items+. For example, using +type=assignments+
results in a node for each assignment group and a sub_item for each assignment, like this:

  [{
    "type": "assignment_groups",
    "title": "An Assignment Group",
    "property": "copy[assignment_groups][id_i855cf145e5acc7435e1bf1c6e2126e5f]",
    "sub_items": [{
        "type": "assignments",
        "title": "Assignment 1",
        "property": "copy[assignments][id_i2102a7fa93b29226774949298626719d]"
    }, {
        "type": "assignments",
        "title": "Assignment 2",
        "property": "copy[assignments][id_i310cba275dc3f4aa8a3306bbbe380979]"
    }]
  }]


To import the items corresponding to a particular tree node, use the +property+ as a parameter to the
{api:ContentMigrationsController#update Update endpoint} and assign a value of 1, for example:

  copy[assignments][id_i310cba275dc3f4aa8a3306bbbe380979]=1

You can include multiple copy parameters to selectively import multiple items or groups of items.

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
    api_instance = canvas_lms_python_client.ContentMigrationsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    type_context_modules_assignments_quizzes_assessment_question_banks_discussion_topics_wiki_pages_context_external_tools_tool_profiles_announcements_calendar_events_rubrics_groups_learning_outcomes_attachments = 'type_context_modules_assignments_quizzes_assessment_question_banks_discussion_topics_wiki_pages_context_external_tools_tool_profiles_announcements_calendar_events_rubrics_groups_learning_outcomes_attachments_example' # str | The type of content to enumerate. (optional)

    try:
        # List items for selective import
        api_response = await api_instance.content_migrations_content_list_for_courses(course_id, id, type_context_modules_assignments_quizzes_assessment_question_banks_discussion_topics_wiki_pages_context_external_tools_tool_profiles_announcements_calendar_events_rubrics_groups_learning_outcomes_attachments=type_context_modules_assignments_quizzes_assessment_question_banks_discussion_topics_wiki_pages_context_external_tools_tool_profiles_announcements_calendar_events_rubrics_groups_learning_outcomes_attachments)
        print("The response of ContentMigrationsApi->content_migrations_content_list_for_courses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentMigrationsApi->content_migrations_content_list_for_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **type_context_modules_assignments_quizzes_assessment_question_banks_discussion_topics_wiki_pages_context_external_tools_tool_profiles_announcements_calendar_events_rubrics_groups_learning_outcomes_attachments** | **str**| The type of content to enumerate. | [optional] 

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
**0** | list of content items |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_migrations_content_list_for_groups**
> object content_migrations_content_list_for_groups(group_id, id, type_context_modules_assignments_quizzes_assessment_question_banks_discussion_topics_wiki_pages_context_external_tools_tool_profiles_announcements_calendar_events_rubrics_groups_learning_outcomes_attachments=type_context_modules_assignments_quizzes_assessment_question_banks_discussion_topics_wiki_pages_context_external_tools_tool_profiles_announcements_calendar_events_rubrics_groups_learning_outcomes_attachments)

List items for selective import

Enumerates the content available for selective import in a tree structure. Each node provides
a +property+ copy argument that can be supplied to the {api:ContentMigrationsController#update Update endpoint}
to selectively copy the content associated with that tree node and its children. Each node may also
provide a +sub_items_url+ or an array of +sub_items+ which you can use to obtain copy parameters
for a subset of the resources in a given node.

If no +type+ is sent you will get a list of the top-level sections in the content. It will look something like this:

  [{
    "type": "course_settings",
    "property": "copy[all_course_settings]",
    "title": "Course Settings"
  },
  {
    "type": "context_modules",
    "property": "copy[all_context_modules]",
    "title": "Modules",
    "count": 5,
    "sub_items_url": "http://example.com/api/v1/courses/22/content_migrations/77/selective_data?type=context_modules"
  },
  {
    "type": "assignments",
    "property": "copy[all_assignments]",
    "title": "Assignments",
    "count": 2,
    "sub_items_url": "http://localhost:3000/api/v1/courses/22/content_migrations/77/selective_data?type=assignments"
  }]

When a +type+ is provided, nodes may be further divided via +sub_items+. For example, using +type=assignments+
results in a node for each assignment group and a sub_item for each assignment, like this:

  [{
    "type": "assignment_groups",
    "title": "An Assignment Group",
    "property": "copy[assignment_groups][id_i855cf145e5acc7435e1bf1c6e2126e5f]",
    "sub_items": [{
        "type": "assignments",
        "title": "Assignment 1",
        "property": "copy[assignments][id_i2102a7fa93b29226774949298626719d]"
    }, {
        "type": "assignments",
        "title": "Assignment 2",
        "property": "copy[assignments][id_i310cba275dc3f4aa8a3306bbbe380979]"
    }]
  }]


To import the items corresponding to a particular tree node, use the +property+ as a parameter to the
{api:ContentMigrationsController#update Update endpoint} and assign a value of 1, for example:

  copy[assignments][id_i310cba275dc3f4aa8a3306bbbe380979]=1

You can include multiple copy parameters to selectively import multiple items or groups of items.

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
    api_instance = canvas_lms_python_client.ContentMigrationsApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    id = 'id_example' # str | Scope response to id
    type_context_modules_assignments_quizzes_assessment_question_banks_discussion_topics_wiki_pages_context_external_tools_tool_profiles_announcements_calendar_events_rubrics_groups_learning_outcomes_attachments = 'type_context_modules_assignments_quizzes_assessment_question_banks_discussion_topics_wiki_pages_context_external_tools_tool_profiles_announcements_calendar_events_rubrics_groups_learning_outcomes_attachments_example' # str | The type of content to enumerate. (optional)

    try:
        # List items for selective import
        api_response = await api_instance.content_migrations_content_list_for_groups(group_id, id, type_context_modules_assignments_quizzes_assessment_question_banks_discussion_topics_wiki_pages_context_external_tools_tool_profiles_announcements_calendar_events_rubrics_groups_learning_outcomes_attachments=type_context_modules_assignments_quizzes_assessment_question_banks_discussion_topics_wiki_pages_context_external_tools_tool_profiles_announcements_calendar_events_rubrics_groups_learning_outcomes_attachments)
        print("The response of ContentMigrationsApi->content_migrations_content_list_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentMigrationsApi->content_migrations_content_list_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **id** | **str**| Scope response to id | 
 **type_context_modules_assignments_quizzes_assessment_question_banks_discussion_topics_wiki_pages_context_external_tools_tool_profiles_announcements_calendar_events_rubrics_groups_learning_outcomes_attachments** | **str**| The type of content to enumerate. | [optional] 

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
**0** | list of content items |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_migrations_content_list_for_users**
> object content_migrations_content_list_for_users(id, user_id, type_context_modules_assignments_quizzes_assessment_question_banks_discussion_topics_wiki_pages_context_external_tools_tool_profiles_announcements_calendar_events_rubrics_groups_learning_outcomes_attachments=type_context_modules_assignments_quizzes_assessment_question_banks_discussion_topics_wiki_pages_context_external_tools_tool_profiles_announcements_calendar_events_rubrics_groups_learning_outcomes_attachments)

List items for selective import

Enumerates the content available for selective import in a tree structure. Each node provides
a +property+ copy argument that can be supplied to the {api:ContentMigrationsController#update Update endpoint}
to selectively copy the content associated with that tree node and its children. Each node may also
provide a +sub_items_url+ or an array of +sub_items+ which you can use to obtain copy parameters
for a subset of the resources in a given node.

If no +type+ is sent you will get a list of the top-level sections in the content. It will look something like this:

  [{
    "type": "course_settings",
    "property": "copy[all_course_settings]",
    "title": "Course Settings"
  },
  {
    "type": "context_modules",
    "property": "copy[all_context_modules]",
    "title": "Modules",
    "count": 5,
    "sub_items_url": "http://example.com/api/v1/courses/22/content_migrations/77/selective_data?type=context_modules"
  },
  {
    "type": "assignments",
    "property": "copy[all_assignments]",
    "title": "Assignments",
    "count": 2,
    "sub_items_url": "http://localhost:3000/api/v1/courses/22/content_migrations/77/selective_data?type=assignments"
  }]

When a +type+ is provided, nodes may be further divided via +sub_items+. For example, using +type=assignments+
results in a node for each assignment group and a sub_item for each assignment, like this:

  [{
    "type": "assignment_groups",
    "title": "An Assignment Group",
    "property": "copy[assignment_groups][id_i855cf145e5acc7435e1bf1c6e2126e5f]",
    "sub_items": [{
        "type": "assignments",
        "title": "Assignment 1",
        "property": "copy[assignments][id_i2102a7fa93b29226774949298626719d]"
    }, {
        "type": "assignments",
        "title": "Assignment 2",
        "property": "copy[assignments][id_i310cba275dc3f4aa8a3306bbbe380979]"
    }]
  }]


To import the items corresponding to a particular tree node, use the +property+ as a parameter to the
{api:ContentMigrationsController#update Update endpoint} and assign a value of 1, for example:

  copy[assignments][id_i310cba275dc3f4aa8a3306bbbe380979]=1

You can include multiple copy parameters to selectively import multiple items or groups of items.

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
    api_instance = canvas_lms_python_client.ContentMigrationsApi(api_client)
    id = 'id_example' # str | Scope response to id
    user_id = 'user_id_example' # str | Scope response to user_id
    type_context_modules_assignments_quizzes_assessment_question_banks_discussion_topics_wiki_pages_context_external_tools_tool_profiles_announcements_calendar_events_rubrics_groups_learning_outcomes_attachments = 'type_context_modules_assignments_quizzes_assessment_question_banks_discussion_topics_wiki_pages_context_external_tools_tool_profiles_announcements_calendar_events_rubrics_groups_learning_outcomes_attachments_example' # str | The type of content to enumerate. (optional)

    try:
        # List items for selective import
        api_response = await api_instance.content_migrations_content_list_for_users(id, user_id, type_context_modules_assignments_quizzes_assessment_question_banks_discussion_topics_wiki_pages_context_external_tools_tool_profiles_announcements_calendar_events_rubrics_groups_learning_outcomes_attachments=type_context_modules_assignments_quizzes_assessment_question_banks_discussion_topics_wiki_pages_context_external_tools_tool_profiles_announcements_calendar_events_rubrics_groups_learning_outcomes_attachments)
        print("The response of ContentMigrationsApi->content_migrations_content_list_for_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentMigrationsApi->content_migrations_content_list_for_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **user_id** | **str**| Scope response to user_id | 
 **type_context_modules_assignments_quizzes_assessment_question_banks_discussion_topics_wiki_pages_context_external_tools_tool_profiles_announcements_calendar_events_rubrics_groups_learning_outcomes_attachments** | **str**| The type of content to enumerate. | [optional] 

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
**0** | list of content items |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_migrations_create**
> ContentMigration content_migrations_create(account_id, content_migrations_create_request=content_migrations_create_request)

Create a content migration

Create a content migration. If the migration requires a file to be uploaded
the actual processing of the file will start once the file upload process is completed.
File uploading works as described in the {file:file.file_uploads.html File Upload Documentation}
except that the values are set on a *pre_attachment* sub-hash.

For migrations that don't require a file to be uploaded, like course copy, the
processing will begin as soon as the migration is created.

You can use the {api:ProgressController#show Progress API} to track the
progress of the migration. The migration's progress is linked to with the
_progress_url_ value.

The two general workflows are:

If no file upload is needed:

1. POST to create
2. Use the {api:ProgressController#show Progress} specified in _progress_url_ to monitor progress

For file uploading:

1. POST to create with file info in *pre_attachment*
2. Do {file:file.file_uploads.html file upload processing} using the data in the *pre_attachment* data
3. {api:ContentMigrationsController#show GET} the ContentMigration
4. Use the {api:ProgressController#show Progress} specified in _progress_url_ to monitor progress

 (required if doing .zip file upload)

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.content_migration import ContentMigration
from canvas_lms_python_client.models.content_migrations_create_request import ContentMigrationsCreateRequest
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
    api_instance = canvas_lms_python_client.ContentMigrationsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    content_migrations_create_request = canvas_lms_python_client.ContentMigrationsCreateRequest() # ContentMigrationsCreateRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/courses/<course_id>/content_migrations' \\      -F 'migration_type=common_cartridge_importer' \\      -F 'settings[question_bank_name]=importquestions' \\      -F 'date_shift_options[old_start_date]=1999-01-01' \\      -F 'date_shift_options[new_start_date]=2013-09-01' \\      -F 'date_shift_options[old_end_date]=1999-04-15' \\      -F 'date_shift_options[new_end_date]=2013-12-15' \\      -F 'date_shift_options[day_substitutions][1]=2' \\      -F 'date_shift_options[day_substitutions][2]=3' \\      -F 'date_shift_options[shift_dates]=true' \\      -F 'pre_attachment[name]=mycourse.imscc' \\      -F 'pre_attachment[size]=12345' \\      -H 'Authorization: Bearer <token>' ``` (optional)

    try:
        # Create a content migration
        api_response = await api_instance.content_migrations_create(account_id, content_migrations_create_request=content_migrations_create_request)
        print("The response of ContentMigrationsApi->content_migrations_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentMigrationsApi->content_migrations_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **content_migrations_create_request** | [**ContentMigrationsCreateRequest**](ContentMigrationsCreateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/courses/&lt;course_id&gt;/content_migrations&#39; \\      -F &#39;migration_type&#x3D;common_cartridge_importer&#39; \\      -F &#39;settings[question_bank_name]&#x3D;importquestions&#39; \\      -F &#39;date_shift_options[old_start_date]&#x3D;1999-01-01&#39; \\      -F &#39;date_shift_options[new_start_date]&#x3D;2013-09-01&#39; \\      -F &#39;date_shift_options[old_end_date]&#x3D;1999-04-15&#39; \\      -F &#39;date_shift_options[new_end_date]&#x3D;2013-12-15&#39; \\      -F &#39;date_shift_options[day_substitutions][1]&#x3D;2&#39; \\      -F &#39;date_shift_options[day_substitutions][2]&#x3D;3&#39; \\      -F &#39;date_shift_options[shift_dates]&#x3D;true&#39; \\      -F &#39;pre_attachment[name]&#x3D;mycourse.imscc&#39; \\      -F &#39;pre_attachment[size]&#x3D;12345&#39; \\      -H &#39;Authorization: Bearer &lt;token&gt;&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**ContentMigration**](ContentMigration.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ContentMigration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_migrations_create_for_courses**
> ContentMigration content_migrations_create_for_courses(course_id, content_migrations_create_request=content_migrations_create_request)

Create a content migration

Create a content migration. If the migration requires a file to be uploaded
the actual processing of the file will start once the file upload process is completed.
File uploading works as described in the {file:file.file_uploads.html File Upload Documentation}
except that the values are set on a *pre_attachment* sub-hash.

For migrations that don't require a file to be uploaded, like course copy, the
processing will begin as soon as the migration is created.

You can use the {api:ProgressController#show Progress API} to track the
progress of the migration. The migration's progress is linked to with the
_progress_url_ value.

The two general workflows are:

If no file upload is needed:

1. POST to create
2. Use the {api:ProgressController#show Progress} specified in _progress_url_ to monitor progress

For file uploading:

1. POST to create with file info in *pre_attachment*
2. Do {file:file.file_uploads.html file upload processing} using the data in the *pre_attachment* data
3. {api:ContentMigrationsController#show GET} the ContentMigration
4. Use the {api:ProgressController#show Progress} specified in _progress_url_ to monitor progress

 (required if doing .zip file upload)

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.content_migration import ContentMigration
from canvas_lms_python_client.models.content_migrations_create_request import ContentMigrationsCreateRequest
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
    api_instance = canvas_lms_python_client.ContentMigrationsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    content_migrations_create_request = canvas_lms_python_client.ContentMigrationsCreateRequest() # ContentMigrationsCreateRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/courses/<course_id>/content_migrations' \\      -F 'migration_type=common_cartridge_importer' \\      -F 'settings[question_bank_name]=importquestions' \\      -F 'date_shift_options[old_start_date]=1999-01-01' \\      -F 'date_shift_options[new_start_date]=2013-09-01' \\      -F 'date_shift_options[old_end_date]=1999-04-15' \\      -F 'date_shift_options[new_end_date]=2013-12-15' \\      -F 'date_shift_options[day_substitutions][1]=2' \\      -F 'date_shift_options[day_substitutions][2]=3' \\      -F 'date_shift_options[shift_dates]=true' \\      -F 'pre_attachment[name]=mycourse.imscc' \\      -F 'pre_attachment[size]=12345' \\      -H 'Authorization: Bearer <token>' ``` (optional)

    try:
        # Create a content migration
        api_response = await api_instance.content_migrations_create_for_courses(course_id, content_migrations_create_request=content_migrations_create_request)
        print("The response of ContentMigrationsApi->content_migrations_create_for_courses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentMigrationsApi->content_migrations_create_for_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **content_migrations_create_request** | [**ContentMigrationsCreateRequest**](ContentMigrationsCreateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/courses/&lt;course_id&gt;/content_migrations&#39; \\      -F &#39;migration_type&#x3D;common_cartridge_importer&#39; \\      -F &#39;settings[question_bank_name]&#x3D;importquestions&#39; \\      -F &#39;date_shift_options[old_start_date]&#x3D;1999-01-01&#39; \\      -F &#39;date_shift_options[new_start_date]&#x3D;2013-09-01&#39; \\      -F &#39;date_shift_options[old_end_date]&#x3D;1999-04-15&#39; \\      -F &#39;date_shift_options[new_end_date]&#x3D;2013-12-15&#39; \\      -F &#39;date_shift_options[day_substitutions][1]&#x3D;2&#39; \\      -F &#39;date_shift_options[day_substitutions][2]&#x3D;3&#39; \\      -F &#39;date_shift_options[shift_dates]&#x3D;true&#39; \\      -F &#39;pre_attachment[name]&#x3D;mycourse.imscc&#39; \\      -F &#39;pre_attachment[size]&#x3D;12345&#39; \\      -H &#39;Authorization: Bearer &lt;token&gt;&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**ContentMigration**](ContentMigration.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ContentMigration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_migrations_create_for_groups**
> ContentMigration content_migrations_create_for_groups(group_id, content_migrations_create_request=content_migrations_create_request)

Create a content migration

Create a content migration. If the migration requires a file to be uploaded
the actual processing of the file will start once the file upload process is completed.
File uploading works as described in the {file:file.file_uploads.html File Upload Documentation}
except that the values are set on a *pre_attachment* sub-hash.

For migrations that don't require a file to be uploaded, like course copy, the
processing will begin as soon as the migration is created.

You can use the {api:ProgressController#show Progress API} to track the
progress of the migration. The migration's progress is linked to with the
_progress_url_ value.

The two general workflows are:

If no file upload is needed:

1. POST to create
2. Use the {api:ProgressController#show Progress} specified in _progress_url_ to monitor progress

For file uploading:

1. POST to create with file info in *pre_attachment*
2. Do {file:file.file_uploads.html file upload processing} using the data in the *pre_attachment* data
3. {api:ContentMigrationsController#show GET} the ContentMigration
4. Use the {api:ProgressController#show Progress} specified in _progress_url_ to monitor progress

 (required if doing .zip file upload)

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.content_migration import ContentMigration
from canvas_lms_python_client.models.content_migrations_create_request import ContentMigrationsCreateRequest
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
    api_instance = canvas_lms_python_client.ContentMigrationsApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    content_migrations_create_request = canvas_lms_python_client.ContentMigrationsCreateRequest() # ContentMigrationsCreateRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/courses/<course_id>/content_migrations' \\      -F 'migration_type=common_cartridge_importer' \\      -F 'settings[question_bank_name]=importquestions' \\      -F 'date_shift_options[old_start_date]=1999-01-01' \\      -F 'date_shift_options[new_start_date]=2013-09-01' \\      -F 'date_shift_options[old_end_date]=1999-04-15' \\      -F 'date_shift_options[new_end_date]=2013-12-15' \\      -F 'date_shift_options[day_substitutions][1]=2' \\      -F 'date_shift_options[day_substitutions][2]=3' \\      -F 'date_shift_options[shift_dates]=true' \\      -F 'pre_attachment[name]=mycourse.imscc' \\      -F 'pre_attachment[size]=12345' \\      -H 'Authorization: Bearer <token>' ``` (optional)

    try:
        # Create a content migration
        api_response = await api_instance.content_migrations_create_for_groups(group_id, content_migrations_create_request=content_migrations_create_request)
        print("The response of ContentMigrationsApi->content_migrations_create_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentMigrationsApi->content_migrations_create_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **content_migrations_create_request** | [**ContentMigrationsCreateRequest**](ContentMigrationsCreateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/courses/&lt;course_id&gt;/content_migrations&#39; \\      -F &#39;migration_type&#x3D;common_cartridge_importer&#39; \\      -F &#39;settings[question_bank_name]&#x3D;importquestions&#39; \\      -F &#39;date_shift_options[old_start_date]&#x3D;1999-01-01&#39; \\      -F &#39;date_shift_options[new_start_date]&#x3D;2013-09-01&#39; \\      -F &#39;date_shift_options[old_end_date]&#x3D;1999-04-15&#39; \\      -F &#39;date_shift_options[new_end_date]&#x3D;2013-12-15&#39; \\      -F &#39;date_shift_options[day_substitutions][1]&#x3D;2&#39; \\      -F &#39;date_shift_options[day_substitutions][2]&#x3D;3&#39; \\      -F &#39;date_shift_options[shift_dates]&#x3D;true&#39; \\      -F &#39;pre_attachment[name]&#x3D;mycourse.imscc&#39; \\      -F &#39;pre_attachment[size]&#x3D;12345&#39; \\      -H &#39;Authorization: Bearer &lt;token&gt;&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**ContentMigration**](ContentMigration.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ContentMigration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_migrations_create_for_users**
> ContentMigration content_migrations_create_for_users(user_id, content_migrations_create_request=content_migrations_create_request)

Create a content migration

Create a content migration. If the migration requires a file to be uploaded
the actual processing of the file will start once the file upload process is completed.
File uploading works as described in the {file:file.file_uploads.html File Upload Documentation}
except that the values are set on a *pre_attachment* sub-hash.

For migrations that don't require a file to be uploaded, like course copy, the
processing will begin as soon as the migration is created.

You can use the {api:ProgressController#show Progress API} to track the
progress of the migration. The migration's progress is linked to with the
_progress_url_ value.

The two general workflows are:

If no file upload is needed:

1. POST to create
2. Use the {api:ProgressController#show Progress} specified in _progress_url_ to monitor progress

For file uploading:

1. POST to create with file info in *pre_attachment*
2. Do {file:file.file_uploads.html file upload processing} using the data in the *pre_attachment* data
3. {api:ContentMigrationsController#show GET} the ContentMigration
4. Use the {api:ProgressController#show Progress} specified in _progress_url_ to monitor progress

 (required if doing .zip file upload)

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.content_migration import ContentMigration
from canvas_lms_python_client.models.content_migrations_create_request import ContentMigrationsCreateRequest
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
    api_instance = canvas_lms_python_client.ContentMigrationsApi(api_client)
    user_id = 'user_id_example' # str | Scope response to user_id
    content_migrations_create_request = canvas_lms_python_client.ContentMigrationsCreateRequest() # ContentMigrationsCreateRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/courses/<course_id>/content_migrations' \\      -F 'migration_type=common_cartridge_importer' \\      -F 'settings[question_bank_name]=importquestions' \\      -F 'date_shift_options[old_start_date]=1999-01-01' \\      -F 'date_shift_options[new_start_date]=2013-09-01' \\      -F 'date_shift_options[old_end_date]=1999-04-15' \\      -F 'date_shift_options[new_end_date]=2013-12-15' \\      -F 'date_shift_options[day_substitutions][1]=2' \\      -F 'date_shift_options[day_substitutions][2]=3' \\      -F 'date_shift_options[shift_dates]=true' \\      -F 'pre_attachment[name]=mycourse.imscc' \\      -F 'pre_attachment[size]=12345' \\      -H 'Authorization: Bearer <token>' ``` (optional)

    try:
        # Create a content migration
        api_response = await api_instance.content_migrations_create_for_users(user_id, content_migrations_create_request=content_migrations_create_request)
        print("The response of ContentMigrationsApi->content_migrations_create_for_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentMigrationsApi->content_migrations_create_for_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Scope response to user_id | 
 **content_migrations_create_request** | [**ContentMigrationsCreateRequest**](ContentMigrationsCreateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/courses/&lt;course_id&gt;/content_migrations&#39; \\      -F &#39;migration_type&#x3D;common_cartridge_importer&#39; \\      -F &#39;settings[question_bank_name]&#x3D;importquestions&#39; \\      -F &#39;date_shift_options[old_start_date]&#x3D;1999-01-01&#39; \\      -F &#39;date_shift_options[new_start_date]&#x3D;2013-09-01&#39; \\      -F &#39;date_shift_options[old_end_date]&#x3D;1999-04-15&#39; \\      -F &#39;date_shift_options[new_end_date]&#x3D;2013-12-15&#39; \\      -F &#39;date_shift_options[day_substitutions][1]&#x3D;2&#39; \\      -F &#39;date_shift_options[day_substitutions][2]&#x3D;3&#39; \\      -F &#39;date_shift_options[shift_dates]&#x3D;true&#39; \\      -F &#39;pre_attachment[name]&#x3D;mycourse.imscc&#39; \\      -F &#39;pre_attachment[size]&#x3D;12345&#39; \\      -H &#39;Authorization: Bearer &lt;token&gt;&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**ContentMigration**](ContentMigration.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ContentMigration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_migrations_index**
> List[ContentMigration] content_migrations_index(account_id, page=page, per_page=per_page)

List content migrations

Returns paginated content migrations

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.content_migration import ContentMigration
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
    api_instance = canvas_lms_python_client.ContentMigrationsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List content migrations
        api_response = await api_instance.content_migrations_index(account_id, page=page, per_page=per_page)
        print("The response of ContentMigrationsApi->content_migrations_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentMigrationsApi->content_migrations_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[ContentMigration]**](ContentMigration.md)

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

# **content_migrations_index_for_courses**
> List[ContentMigration] content_migrations_index_for_courses(course_id, page=page, per_page=per_page)

List content migrations

Returns paginated content migrations

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.content_migration import ContentMigration
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
    api_instance = canvas_lms_python_client.ContentMigrationsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List content migrations
        api_response = await api_instance.content_migrations_index_for_courses(course_id, page=page, per_page=per_page)
        print("The response of ContentMigrationsApi->content_migrations_index_for_courses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentMigrationsApi->content_migrations_index_for_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[ContentMigration]**](ContentMigration.md)

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

# **content_migrations_index_for_groups**
> List[ContentMigration] content_migrations_index_for_groups(group_id, page=page, per_page=per_page)

List content migrations

Returns paginated content migrations

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.content_migration import ContentMigration
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
    api_instance = canvas_lms_python_client.ContentMigrationsApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List content migrations
        api_response = await api_instance.content_migrations_index_for_groups(group_id, page=page, per_page=per_page)
        print("The response of ContentMigrationsApi->content_migrations_index_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentMigrationsApi->content_migrations_index_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[ContentMigration]**](ContentMigration.md)

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

# **content_migrations_index_for_users**
> List[ContentMigration] content_migrations_index_for_users(user_id, page=page, per_page=per_page)

List content migrations

Returns paginated content migrations

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.content_migration import ContentMigration
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
    api_instance = canvas_lms_python_client.ContentMigrationsApi(api_client)
    user_id = 'user_id_example' # str | Scope response to user_id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List content migrations
        api_response = await api_instance.content_migrations_index_for_users(user_id, page=page, per_page=per_page)
        print("The response of ContentMigrationsApi->content_migrations_index_for_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentMigrationsApi->content_migrations_index_for_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Scope response to user_id | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[ContentMigration]**](ContentMigration.md)

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

# **content_migrations_show**
> ContentMigration content_migrations_show(account_id, id)

Get a content migration

Returns data on an individual content migration

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.content_migration import ContentMigration
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
    api_instance = canvas_lms_python_client.ContentMigrationsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id

    try:
        # Get a content migration
        api_response = await api_instance.content_migrations_show(account_id, id)
        print("The response of ContentMigrationsApi->content_migrations_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentMigrationsApi->content_migrations_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**ContentMigration**](ContentMigration.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ContentMigration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_migrations_show_for_courses**
> ContentMigration content_migrations_show_for_courses(course_id, id)

Get a content migration

Returns data on an individual content migration

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.content_migration import ContentMigration
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
    api_instance = canvas_lms_python_client.ContentMigrationsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id

    try:
        # Get a content migration
        api_response = await api_instance.content_migrations_show_for_courses(course_id, id)
        print("The response of ContentMigrationsApi->content_migrations_show_for_courses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentMigrationsApi->content_migrations_show_for_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**ContentMigration**](ContentMigration.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ContentMigration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_migrations_show_for_groups**
> ContentMigration content_migrations_show_for_groups(group_id, id)

Get a content migration

Returns data on an individual content migration

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.content_migration import ContentMigration
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
    api_instance = canvas_lms_python_client.ContentMigrationsApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    id = 'id_example' # str | Scope response to id

    try:
        # Get a content migration
        api_response = await api_instance.content_migrations_show_for_groups(group_id, id)
        print("The response of ContentMigrationsApi->content_migrations_show_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentMigrationsApi->content_migrations_show_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**ContentMigration**](ContentMigration.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ContentMigration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_migrations_show_for_users**
> ContentMigration content_migrations_show_for_users(id, user_id)

Get a content migration

Returns data on an individual content migration

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.content_migration import ContentMigration
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
    api_instance = canvas_lms_python_client.ContentMigrationsApi(api_client)
    id = 'id_example' # str | Scope response to id
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # Get a content migration
        api_response = await api_instance.content_migrations_show_for_users(id, user_id)
        print("The response of ContentMigrationsApi->content_migrations_show_for_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentMigrationsApi->content_migrations_show_for_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **user_id** | **str**| Scope response to user_id | 

### Return type

[**ContentMigration**](ContentMigration.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ContentMigration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_migrations_update**
> ContentMigration content_migrations_update(account_id, id)

Update a content migration

Update a content migration. Takes same arguments as {api:ContentMigrationsController#create create} except that you
can't change the migration type. However, changing most settings after the
migration process has started will not do anything. Generally updating the
content migration will be used when there is a file upload problem, or when
importing content selectively. If the first upload has a problem you can
supply new _pre_attachment_ values to start the process again.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.content_migration import ContentMigration
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
    api_instance = canvas_lms_python_client.ContentMigrationsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id

    try:
        # Update a content migration
        api_response = await api_instance.content_migrations_update(account_id, id)
        print("The response of ContentMigrationsApi->content_migrations_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentMigrationsApi->content_migrations_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**ContentMigration**](ContentMigration.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ContentMigration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_migrations_update_for_courses**
> ContentMigration content_migrations_update_for_courses(course_id, id)

Update a content migration

Update a content migration. Takes same arguments as {api:ContentMigrationsController#create create} except that you
can't change the migration type. However, changing most settings after the
migration process has started will not do anything. Generally updating the
content migration will be used when there is a file upload problem, or when
importing content selectively. If the first upload has a problem you can
supply new _pre_attachment_ values to start the process again.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.content_migration import ContentMigration
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
    api_instance = canvas_lms_python_client.ContentMigrationsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id

    try:
        # Update a content migration
        api_response = await api_instance.content_migrations_update_for_courses(course_id, id)
        print("The response of ContentMigrationsApi->content_migrations_update_for_courses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentMigrationsApi->content_migrations_update_for_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**ContentMigration**](ContentMigration.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ContentMigration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_migrations_update_for_groups**
> ContentMigration content_migrations_update_for_groups(group_id, id)

Update a content migration

Update a content migration. Takes same arguments as {api:ContentMigrationsController#create create} except that you
can't change the migration type. However, changing most settings after the
migration process has started will not do anything. Generally updating the
content migration will be used when there is a file upload problem, or when
importing content selectively. If the first upload has a problem you can
supply new _pre_attachment_ values to start the process again.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.content_migration import ContentMigration
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
    api_instance = canvas_lms_python_client.ContentMigrationsApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    id = 'id_example' # str | Scope response to id

    try:
        # Update a content migration
        api_response = await api_instance.content_migrations_update_for_groups(group_id, id)
        print("The response of ContentMigrationsApi->content_migrations_update_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentMigrationsApi->content_migrations_update_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**ContentMigration**](ContentMigration.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ContentMigration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_migrations_update_for_users**
> ContentMigration content_migrations_update_for_users(id, user_id)

Update a content migration

Update a content migration. Takes same arguments as {api:ContentMigrationsController#create create} except that you
can't change the migration type. However, changing most settings after the
migration process has started will not do anything. Generally updating the
content migration will be used when there is a file upload problem, or when
importing content selectively. If the first upload has a problem you can
supply new _pre_attachment_ values to start the process again.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.content_migration import ContentMigration
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
    api_instance = canvas_lms_python_client.ContentMigrationsApi(api_client)
    id = 'id_example' # str | Scope response to id
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # Update a content migration
        api_response = await api_instance.content_migrations_update_for_users(id, user_id)
        print("The response of ContentMigrationsApi->content_migrations_update_for_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentMigrationsApi->content_migrations_update_for_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **user_id** | **str**| Scope response to user_id | 

### Return type

[**ContentMigration**](ContentMigration.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ContentMigration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

