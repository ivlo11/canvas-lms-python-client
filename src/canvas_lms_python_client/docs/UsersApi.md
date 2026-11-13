# canvas_lms_python_client.UsersApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_activity_stream**](UsersApi.md#users_activity_stream) | **GET** /api/v1/users/self/activity_stream | List the activity stream
[**users_activity_stream_for_other**](UsersApi.md#users_activity_stream_for_other) | **GET** /api/v1/users/activity_stream | List the activity stream
[**users_activity_stream_summary**](UsersApi.md#users_activity_stream_summary) | **GET** /api/v1/users/self/activity_stream/summary | Activity stream summary
[**users_api_index**](UsersApi.md#users_api_index) | **GET** /api/v1/accounts/{account_id}/users | List users in account
[**users_api_show**](UsersApi.md#users_api_show) | **GET** /api/v1/users/{id} | Show user details
[**users_create**](UsersApi.md#users_create) | **POST** /api/v1/accounts/{account_id}/users | Create a user
[**users_create_file**](UsersApi.md#users_create_file) | **POST** /api/v1/users/{user_id}/files | Upload a file
[**users_create_self_registered_user**](UsersApi.md#users_create_self_registered_user) | **POST** /api/v1/accounts/{account_id}/self_registration | [DEPRECATED] Self register a user
[**users_expire_mobile_sessions**](UsersApi.md#users_expire_mobile_sessions) | **DELETE** /api/v1/users/mobile_sessions | Log users out of all mobile apps
[**users_expire_mobile_sessions_for_users**](UsersApi.md#users_expire_mobile_sessions_for_users) | **DELETE** /api/v1/users/{id}/mobile_sessions | Log users out of all mobile apps
[**users_get_custom_color**](UsersApi.md#users_get_custom_color) | **GET** /api/v1/users/{id}/colors/{asset_string} | Get custom color
[**users_get_custom_colors**](UsersApi.md#users_get_custom_colors) | **GET** /api/v1/users/{id}/colors | Get custom colors
[**users_get_dashboard_positions**](UsersApi.md#users_get_dashboard_positions) | **GET** /api/v1/users/{id}/dashboard_positions | Get dashboard positions
[**users_ignore_all_stream_items**](UsersApi.md#users_ignore_all_stream_items) | **DELETE** /api/v1/users/self/activity_stream | Hide all stream items
[**users_ignore_stream_item**](UsersApi.md#users_ignore_stream_item) | **DELETE** /api/v1/users/self/activity_stream/{id} | Hide a stream item
[**users_merge_into**](UsersApi.md#users_merge_into) | **PUT** /api/v1/users/{id}/merge_into/{destination_user_id} | Merge user into another user
[**users_merge_into_for_users**](UsersApi.md#users_merge_into_for_users) | **PUT** /api/v1/users/{id}/merge_into/accounts/{destination_account_id}/users/{destination_user_id} | Merge user into another user
[**users_missing_submissions**](UsersApi.md#users_missing_submissions) | **GET** /api/v1/users/{user_id}/missing_submissions | List Missing Submissions
[**users_pandata_events_token**](UsersApi.md#users_pandata_events_token) | **POST** /api/v1/users/self/pandata_events_token | Get a Pandata Events jwt token and its expiration date
[**users_set_custom_color**](UsersApi.md#users_set_custom_color) | **PUT** /api/v1/users/{id}/colors/{asset_string} | Update custom color
[**users_set_dashboard_positions**](UsersApi.md#users_set_dashboard_positions) | **PUT** /api/v1/users/{id}/dashboard_positions | Update dashboard positions
[**users_set_files_ui_version_preference**](UsersApi.md#users_set_files_ui_version_preference) | **PUT** /api/v1/users/{id}/files_ui_version_preference | Update files UI version preference
[**users_set_text_editor_preference**](UsersApi.md#users_set_text_editor_preference) | **PUT** /api/v1/users/{id}/text_editor_preference | Update text editor preference
[**users_settings**](UsersApi.md#users_settings) | **GET** /api/v1/users/{id}/settings | Update user settings.
[**users_settings_for_users**](UsersApi.md#users_settings_for_users) | **PUT** /api/v1/users/{id}/settings | Update user settings.
[**users_split**](UsersApi.md#users_split) | **POST** /api/v1/users/{id}/split | Split merged users into separate users
[**users_terminate_sessions**](UsersApi.md#users_terminate_sessions) | **DELETE** /api/v1/users/{id}/sessions | Terminate all user sessions
[**users_todo_item_count**](UsersApi.md#users_todo_item_count) | **GET** /api/v1/users/self/todo_item_count | List counts for todo items
[**users_todo_items**](UsersApi.md#users_todo_items) | **GET** /api/v1/users/self/todo | List the TODO items
[**users_upcoming_events**](UsersApi.md#users_upcoming_events) | **GET** /api/v1/users/self/upcoming_events | List upcoming assignments, calendar events
[**users_update**](UsersApi.md#users_update) | **PUT** /api/v1/users/{id} | Edit a user
[**users_user_graded_submissions**](UsersApi.md#users_user_graded_submissions) | **GET** /api/v1/users/{id}/graded_submissions | Get a users most recently graded submissions


# **users_activity_stream**
> users_activity_stream(only_active_courses=only_active_courses)

List the activity stream

Returns the current user's global activity stream, paginated.

There are many types of objects that can be returned in the activity
stream. All object types have the same basic set of shared attributes:
  !!!javascript
  {
    'created_at': '2011-07-13T09:12:00Z',
    'updated_at': '2011-07-25T08:52:41Z',
    'id': 1234,
    'title': 'Stream Item Subject',
    'message': 'This is the body text of the activity stream item. It is plain-text, and can be multiple paragraphs.',
    'type': 'DiscussionTopic|Conversation|Message|Submission|Conference|Collaboration|AssessmentRequest...',
    'read_state': false,
    'context_type': 'course', // course|group
    'course_id': 1,
    'group_id': null,
    'html_url': "http://..." // URL to the Canvas web UI for this stream item
  }

In addition, each item type has its own set of attributes available.

DiscussionTopic:

  !!!javascript
  {
    'type': 'DiscussionTopic',
    'discussion_topic_id': 1234,
    'total_root_discussion_entries': 5,
    'require_initial_post': true,
    'user_has_posted': true,
    'root_discussion_entries': {
      ...
    }
  }

For DiscussionTopic, the message is truncated at 4kb.

Announcement:

  !!!javascript
  {
    'type': 'Announcement',
    'announcement_id': 1234,
    'total_root_discussion_entries': 5,
    'require_initial_post': true,
    'user_has_posted': null,
    'root_discussion_entries': {
      ...
    }
  }

For Announcement, the message is truncated at 4kb.

Conversation:

  !!!javascript
  {
    'type': 'Conversation',
    'conversation_id': 1234,
    'private': false,
    'participant_count': 3,
  }

Message:

  !!!javascript
  {
    'type': 'Message',
    'message_id': 1234,
    'notification_category': 'Assignment Graded'
  }

Submission:

Returns an {api:Submissions:Submission Submission} with its Course and Assignment data.

Conference:

  !!!javascript
  {
    'type': 'Conference',
    'web_conference_id': 1234
  }

Collaboration:

  !!!javascript
  {
    'type': 'Collaboration',
    'collaboration_id': 1234
  }

AssessmentRequest:

  !!!javascript
  {
    'type': 'AssessmentRequest',
    'assessment_request_id': 1234
  }

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
    api_instance = canvas_lms_python_client.UsersApi(api_client)
    only_active_courses = True # bool | If true, will only return objects for courses the user is actively participating in (optional)

    try:
        # List the activity stream
        await api_instance.users_activity_stream(only_active_courses=only_active_courses)
    except Exception as e:
        print("Exception when calling UsersApi->users_activity_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **only_active_courses** | **bool**| If true, will only return objects for courses the user is actively participating in | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | List the activity stream |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_activity_stream_for_other**
> users_activity_stream_for_other(only_active_courses=only_active_courses)

List the activity stream

Returns the current user's global activity stream, paginated.

There are many types of objects that can be returned in the activity
stream. All object types have the same basic set of shared attributes:
  !!!javascript
  {
    'created_at': '2011-07-13T09:12:00Z',
    'updated_at': '2011-07-25T08:52:41Z',
    'id': 1234,
    'title': 'Stream Item Subject',
    'message': 'This is the body text of the activity stream item. It is plain-text, and can be multiple paragraphs.',
    'type': 'DiscussionTopic|Conversation|Message|Submission|Conference|Collaboration|AssessmentRequest...',
    'read_state': false,
    'context_type': 'course', // course|group
    'course_id': 1,
    'group_id': null,
    'html_url': "http://..." // URL to the Canvas web UI for this stream item
  }

In addition, each item type has its own set of attributes available.

DiscussionTopic:

  !!!javascript
  {
    'type': 'DiscussionTopic',
    'discussion_topic_id': 1234,
    'total_root_discussion_entries': 5,
    'require_initial_post': true,
    'user_has_posted': true,
    'root_discussion_entries': {
      ...
    }
  }

For DiscussionTopic, the message is truncated at 4kb.

Announcement:

  !!!javascript
  {
    'type': 'Announcement',
    'announcement_id': 1234,
    'total_root_discussion_entries': 5,
    'require_initial_post': true,
    'user_has_posted': null,
    'root_discussion_entries': {
      ...
    }
  }

For Announcement, the message is truncated at 4kb.

Conversation:

  !!!javascript
  {
    'type': 'Conversation',
    'conversation_id': 1234,
    'private': false,
    'participant_count': 3,
  }

Message:

  !!!javascript
  {
    'type': 'Message',
    'message_id': 1234,
    'notification_category': 'Assignment Graded'
  }

Submission:

Returns an {api:Submissions:Submission Submission} with its Course and Assignment data.

Conference:

  !!!javascript
  {
    'type': 'Conference',
    'web_conference_id': 1234
  }

Collaboration:

  !!!javascript
  {
    'type': 'Collaboration',
    'collaboration_id': 1234
  }

AssessmentRequest:

  !!!javascript
  {
    'type': 'AssessmentRequest',
    'assessment_request_id': 1234
  }

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
    api_instance = canvas_lms_python_client.UsersApi(api_client)
    only_active_courses = True # bool | If true, will only return objects for courses the user is actively participating in (optional)

    try:
        # List the activity stream
        await api_instance.users_activity_stream_for_other(only_active_courses=only_active_courses)
    except Exception as e:
        print("Exception when calling UsersApi->users_activity_stream_for_other: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **only_active_courses** | **bool**| If true, will only return objects for courses the user is actively participating in | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | List the activity stream |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_activity_stream_summary**
> users_activity_stream_summary(only_active_courses=only_active_courses)

Activity stream summary

Returns a summary of the current user's global activity stream.

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
    api_instance = canvas_lms_python_client.UsersApi(api_client)
    only_active_courses = True # bool | If true, will only return objects for courses the user is actively participating in (optional)

    try:
        # Activity stream summary
        await api_instance.users_activity_stream_summary(only_active_courses=only_active_courses)
    except Exception as e:
        print("Exception when calling UsersApi->users_activity_stream_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **only_active_courses** | **bool**| If true, will only return objects for courses the user is actively participating in | [optional] 

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
**0** | Activity stream summary |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_api_index**
> List[User] users_api_index(account_id, search_term=search_term, enrollment_type=enrollment_type, sort=sort, order=order, include_deleted_users=include_deleted_users, uuids=uuids, page=page, per_page=per_page)

List users in account

A paginated list of users associated with this account.

 @example_request
   curl https://<canvas>/api/v1/accounts/self/users?search_term=<search value> \
      -X GET \
      -H 'Authorization: Bearer <token>'

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
    api_instance = canvas_lms_python_client.UsersApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    search_term = 'search_term_example' # str | The partial name or full ID of the users to match and return in the results list. Must be at least 3 characters.  Note that the API will prefer matching on canonical user ID if the ID has a numeric form. It will only search against other fields if non-numeric in form, or if the numeric value doesn't yield any matches. Queries by administrative users will search on SIS ID, Integration ID, login ID, name, or email address (optional)
    enrollment_type = 'enrollment_type_example' # str | When set, only return users enrolled with the specified course-level base role. This can be a base role type of 'student', 'teacher', 'ta', 'observer', or 'designer'. (optional)
    sort = 'sort_example' # str | The column to sort results by. For efficiency, use +id+ if you intend to retrieve many pages of results. In the future, other sort options may be rate-limited after 50 pages. (optional)
    order = 'order_example' # str | The order to sort the given column by. (optional)
    include_deleted_users = True # bool | When set to true and used with an account context, returns users who have deleted pseudonyms for the context (optional)
    uuids = ['uuids_example'] # List[str] | When set, only return users with the specified UUIDs. UUIDs after the first 100 are ignored. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List users in account
        api_response = await api_instance.users_api_index(account_id, search_term=search_term, enrollment_type=enrollment_type, sort=sort, order=order, include_deleted_users=include_deleted_users, uuids=uuids, page=page, per_page=per_page)
        print("The response of UsersApi->users_api_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_api_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **search_term** | **str**| The partial name or full ID of the users to match and return in the results list. Must be at least 3 characters.  Note that the API will prefer matching on canonical user ID if the ID has a numeric form. It will only search against other fields if non-numeric in form, or if the numeric value doesn&#39;t yield any matches. Queries by administrative users will search on SIS ID, Integration ID, login ID, name, or email address | [optional] 
 **enrollment_type** | **str**| When set, only return users enrolled with the specified course-level base role. This can be a base role type of &#39;student&#39;, &#39;teacher&#39;, &#39;ta&#39;, &#39;observer&#39;, or &#39;designer&#39;. | [optional] 
 **sort** | **str**| The column to sort results by. For efficiency, use +id+ if you intend to retrieve many pages of results. In the future, other sort options may be rate-limited after 50 pages. | [optional] 
 **order** | **str**| The order to sort the given column by. | [optional] 
 **include_deleted_users** | **bool**| When set to true and used with an account context, returns users who have deleted pseudonyms for the context | [optional] 
 **uuids** | [**List[str]**](str.md)| When set, only return users with the specified UUIDs. UUIDs after the first 100 are ignored. | [optional] 
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

# **users_api_show**
> User users_api_show(id, include=include)

Show user details

Shows details for user.

Also includes an attribute "permissions", a non-comprehensive list of permissions for the user.
Example:
  !!!javascript
  "permissions": {
   "can_update_name": true, // Whether the user can update their name.
   "can_update_avatar": false, // Whether the user can update their avatar.
   "limit_parent_app_web_access": false // Whether the user can interact with Canvas web from the Canvas Parent app.
  }

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
    api_instance = canvas_lms_python_client.UsersApi(api_client)
    id = 'id_example' # str | Scope response to id
    include = ['include_example'] # List[str] | Array of additional information to include on the user record. \"locale\", \"avatar_url\", \"permissions\", \"email\", and \"effective_locale\" will always be returned (optional)

    try:
        # Show user details
        api_response = await api_instance.users_api_show(id, include=include)
        print("The response of UsersApi->users_api_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_api_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **include** | [**List[str]**](str.md)| Array of additional information to include on the user record. \&quot;locale\&quot;, \&quot;avatar_url\&quot;, \&quot;permissions\&quot;, \&quot;email\&quot;, and \&quot;effective_locale\&quot; will always be returned | [optional] 

### Return type

[**User**](User.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Schemas::Docs::User |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_create**
> User users_create(account_id, users_create_request=users_create_request)

Create a user

Create and return a new user and pseudonym for an account.

[DEPRECATED (for self-registration only)] If you don't have the "Modify
login details for users" permission, but self-registration is enabled
on the account, you can still use this endpoint to register new users.
Certain fields will be required, and others will be ignored (see below).

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.user import User
from canvas_lms_python_client.models.users_create_request import UsersCreateRequest
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
    api_instance = canvas_lms_python_client.UsersApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    users_create_request = canvas_lms_python_client.UsersCreateRequest() # UsersCreateRequest | Request body parameters (optional)

    try:
        # Create a user
        api_response = await api_instance.users_create(account_id, users_create_request=users_create_request)
        print("The response of UsersApi->users_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **users_create_request** | [**UsersCreateRequest**](UsersCreateRequest.md)| Request body parameters | [optional] 

### Return type

[**User**](User.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | User |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_create_file**
> users_create_file(user_id)

Upload a file

Upload a file to the user's personal files section.

This API endpoint is the first step in uploading a file to a user's files.
See the {file:file.file_uploads.html File Upload Documentation} for details on
the file upload workflow.

Note that typically users will only be able to upload files to their
own files section. Passing a user_id of +self+ is an easy shortcut
to specify the current user.

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
    api_instance = canvas_lms_python_client.UsersApi(api_client)
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # Upload a file
        await api_instance.users_create_file(user_id)
    except Exception as e:
        print("Exception when calling UsersApi->users_create_file: %s\n" % e)
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
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Upload a file |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_create_self_registered_user**
> User users_create_self_registered_user(account_id, users_create_self_registered_user_request=users_create_self_registered_user_request)

[DEPRECATED] Self register a user

Self register and return a new user and pseudonym for an account.

If self-registration is enabled on the account, you can use this
endpoint to self register new users.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.user import User
from canvas_lms_python_client.models.users_create_self_registered_user_request import UsersCreateSelfRegisteredUserRequest
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
    api_instance = canvas_lms_python_client.UsersApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    users_create_self_registered_user_request = canvas_lms_python_client.UsersCreateSelfRegisteredUserRequest() # UsersCreateSelfRegisteredUserRequest | Request body parameters (optional)

    try:
        # [DEPRECATED] Self register a user
        api_response = await api_instance.users_create_self_registered_user(account_id, users_create_self_registered_user_request=users_create_self_registered_user_request)
        print("The response of UsersApi->users_create_self_registered_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_create_self_registered_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **users_create_self_registered_user_request** | [**UsersCreateSelfRegisteredUserRequest**](UsersCreateSelfRegisteredUserRequest.md)| Request body parameters | [optional] 

### Return type

[**User**](User.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | User |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_expire_mobile_sessions**
> users_expire_mobile_sessions(skip_admins=skip_admins)

Log users out of all mobile apps

Permanently expires any active mobile sessions, forcing them to re-authorize.

The route that takes a user id will expire mobile sessions for that user.
The route that doesn't take a user id will expire mobile sessions for *all* users
in the institution (except for account administrators if +skip_admins+ is given).

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
    api_instance = canvas_lms_python_client.UsersApi(api_client)
    skip_admins = True # bool | If true, will not expire mobile sessions for account administrators. (optional)

    try:
        # Log users out of all mobile apps
        await api_instance.users_expire_mobile_sessions(skip_admins=skip_admins)
    except Exception as e:
        print("Exception when calling UsersApi->users_expire_mobile_sessions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip_admins** | **bool**| If true, will not expire mobile sessions for account administrators. | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Log users out of all mobile apps |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_expire_mobile_sessions_for_users**
> users_expire_mobile_sessions_for_users(id, skip_admins=skip_admins)

Log users out of all mobile apps

Permanently expires any active mobile sessions, forcing them to re-authorize.

The route that takes a user id will expire mobile sessions for that user.
The route that doesn't take a user id will expire mobile sessions for *all* users
in the institution (except for account administrators if +skip_admins+ is given).

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
    api_instance = canvas_lms_python_client.UsersApi(api_client)
    id = 'id_example' # str | Scope response to id
    skip_admins = True # bool | If true, will not expire mobile sessions for account administrators. (optional)

    try:
        # Log users out of all mobile apps
        await api_instance.users_expire_mobile_sessions_for_users(id, skip_admins=skip_admins)
    except Exception as e:
        print("Exception when calling UsersApi->users_expire_mobile_sessions_for_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **skip_admins** | **bool**| If true, will not expire mobile sessions for account administrators. | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Log users out of all mobile apps |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_get_custom_color**
> users_get_custom_color(asset_string, id)

Get custom color

Returns the custom colors that have been saved for a user for a given context.

The asset_string parameter should be in the format 'context_id', for example
'course_42'.

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
    api_instance = canvas_lms_python_client.UsersApi(api_client)
    asset_string = 'asset_string_example' # str | Scope response to asset_string
    id = 'id_example' # str | Scope response to id

    try:
        # Get custom color
        await api_instance.users_get_custom_color(asset_string, id)
    except Exception as e:
        print("Exception when calling UsersApi->users_get_custom_color: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_string** | **str**| Scope response to asset_string | 
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
**0** | Get custom color |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_get_custom_colors**
> users_get_custom_colors(id)

Get custom colors

Returns all custom colors that have been saved for a user.

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
    api_instance = canvas_lms_python_client.UsersApi(api_client)
    id = 'id_example' # str | Scope response to id

    try:
        # Get custom colors
        await api_instance.users_get_custom_colors(id)
    except Exception as e:
        print("Exception when calling UsersApi->users_get_custom_colors: %s\n" % e)
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
**0** | Get custom colors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_get_dashboard_positions**
> users_get_dashboard_positions(id)

Get dashboard positions

Returns all dashboard positions that have been saved for a user.

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
    api_instance = canvas_lms_python_client.UsersApi(api_client)
    id = 'id_example' # str | Scope response to id

    try:
        # Get dashboard positions
        await api_instance.users_get_dashboard_positions(id)
    except Exception as e:
        print("Exception when calling UsersApi->users_get_dashboard_positions: %s\n" % e)
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
**0** | Get dashboard positions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_ignore_all_stream_items**
> users_ignore_all_stream_items()

Hide all stream items

Hide all stream items for the user

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
    api_instance = canvas_lms_python_client.UsersApi(api_client)

    try:
        # Hide all stream items
        await api_instance.users_ignore_all_stream_items()
    except Exception as e:
        print("Exception when calling UsersApi->users_ignore_all_stream_items: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**0** | Hide all stream items |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_ignore_stream_item**
> users_ignore_stream_item(id)

Hide a stream item

Hide the given stream item.

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
    api_instance = canvas_lms_python_client.UsersApi(api_client)
    id = 'id_example' # str | Scope response to id

    try:
        # Hide a stream item
        await api_instance.users_ignore_stream_item(id)
    except Exception as e:
        print("Exception when calling UsersApi->users_ignore_stream_item: %s\n" % e)
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
**0** | Hide a stream item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_merge_into**
> User users_merge_into(destination_user_id, id)

Merge user into another user

Merge a user into another user.
To merge users, the caller must have permissions to manage both users. This
should be considered irreversible. This will delete the user and move all
the data into the destination user.

User merge details and caveats:
The from_user is the user that was deleted in the user_merge process.
The destination_user is the user that remains, that is being split.

Avatars:
When both users have avatars, only the destination_users avatar will remain.
When one user has an avatar, it will end up on the destination_user.

Terms of Use:
If either user has accepted terms of use, it will be be left as accepted.

Communication Channels:
All unique communication channels moved to the destination_user.
All notification preferences are moved to the destination_user.

Enrollments:
All unique enrollments are moved to the destination_user.
When there is an enrollment that would end up making it so that a user would
be observing themselves, the enrollment is not moved over.
Everything that is tied to the from_user at the course level relating to the
enrollment is also moved to the destination_user.

Submissions:
All submissions are moved to the destination_user. If there are enrollments
for both users in the same course, we prefer submissions that have grades
then submissions that have work in them, and if there are no grades or no
work, they are not moved.

Other notes:
Access Tokens are moved on merge.
Conversations are moved on merge.
Favorites are moved on merge.
Courses will commonly use LTI tools. LTI tools reference the user with IDs
that are stored on a user object. Merging users deletes one user and moves
all records from the deleted user to the destination_user. These IDs are
kept for all enrollments, group_membership, and account_users for the
from_user at the time of the merge. When the destination_user launches an
LTI tool from a course that used to be the from_user's, it doesn't appear as
a new user to the tool provider. Instead it will send the stored ids. The
destination_user's LTI IDs remain as they were for the courses that they
originally had. Future enrollments for the destination_user will use the IDs
that are on the destination_user object. LTI IDs that are kept and tracked
per context include lti_context_id, lti_id and uuid. APIs that return the
LTI ids will return the one for the context that it is called for, except
for the user uuid. The user UUID will display the destination_users uuid,
and when getting the uuid from an api that is in a context that was
recorded from a merge event, an additional attribute is added as past_uuid.

When finding users by SIS ids in different accounts the
destination_account_id is required.

The account can also be identified by passing the domain in destination_account_id.

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
    api_instance = canvas_lms_python_client.UsersApi(api_client)
    destination_user_id = 'destination_user_id_example' # str | Scope response to destination_user_id
    id = 'id_example' # str | Scope response to id

    try:
        # Merge user into another user
        api_response = await api_instance.users_merge_into(destination_user_id, id)
        print("The response of UsersApi->users_merge_into:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_merge_into: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destination_user_id** | **str**| Scope response to destination_user_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**User**](User.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | User |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_merge_into_for_users**
> User users_merge_into_for_users(destination_account_id, destination_user_id, id)

Merge user into another user

Merge a user into another user.
To merge users, the caller must have permissions to manage both users. This
should be considered irreversible. This will delete the user and move all
the data into the destination user.

User merge details and caveats:
The from_user is the user that was deleted in the user_merge process.
The destination_user is the user that remains, that is being split.

Avatars:
When both users have avatars, only the destination_users avatar will remain.
When one user has an avatar, it will end up on the destination_user.

Terms of Use:
If either user has accepted terms of use, it will be be left as accepted.

Communication Channels:
All unique communication channels moved to the destination_user.
All notification preferences are moved to the destination_user.

Enrollments:
All unique enrollments are moved to the destination_user.
When there is an enrollment that would end up making it so that a user would
be observing themselves, the enrollment is not moved over.
Everything that is tied to the from_user at the course level relating to the
enrollment is also moved to the destination_user.

Submissions:
All submissions are moved to the destination_user. If there are enrollments
for both users in the same course, we prefer submissions that have grades
then submissions that have work in them, and if there are no grades or no
work, they are not moved.

Other notes:
Access Tokens are moved on merge.
Conversations are moved on merge.
Favorites are moved on merge.
Courses will commonly use LTI tools. LTI tools reference the user with IDs
that are stored on a user object. Merging users deletes one user and moves
all records from the deleted user to the destination_user. These IDs are
kept for all enrollments, group_membership, and account_users for the
from_user at the time of the merge. When the destination_user launches an
LTI tool from a course that used to be the from_user's, it doesn't appear as
a new user to the tool provider. Instead it will send the stored ids. The
destination_user's LTI IDs remain as they were for the courses that they
originally had. Future enrollments for the destination_user will use the IDs
that are on the destination_user object. LTI IDs that are kept and tracked
per context include lti_context_id, lti_id and uuid. APIs that return the
LTI ids will return the one for the context that it is called for, except
for the user uuid. The user UUID will display the destination_users uuid,
and when getting the uuid from an api that is in a context that was
recorded from a merge event, an additional attribute is added as past_uuid.

When finding users by SIS ids in different accounts the
destination_account_id is required.

The account can also be identified by passing the domain in destination_account_id.

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
    api_instance = canvas_lms_python_client.UsersApi(api_client)
    destination_account_id = 'destination_account_id_example' # str | Scope response to destination_account_id
    destination_user_id = 'destination_user_id_example' # str | Scope response to destination_user_id
    id = 'id_example' # str | Scope response to id

    try:
        # Merge user into another user
        api_response = await api_instance.users_merge_into_for_users(destination_account_id, destination_user_id, id)
        print("The response of UsersApi->users_merge_into_for_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_merge_into_for_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destination_account_id** | **str**| Scope response to destination_account_id | 
 **destination_user_id** | **str**| Scope response to destination_user_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**User**](User.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | User |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_missing_submissions**
> List[Assignment] users_missing_submissions(user_id, observed_user_id=observed_user_id, include=include, filter=filter, course_ids=course_ids, page=page, per_page=per_page)

List Missing Submissions

A paginated list of past-due assignments for which the student does not have a submission.
The user sending the request must either be the student, an admin or a parent observer using the parent app

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.assignment import Assignment
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
    api_instance = canvas_lms_python_client.UsersApi(api_client)
    user_id = 'user_id_example' # str | the student's ID
    observed_user_id = 'observed_user_id_example' # str | Return missing submissions for the given observed user. Must be accompanied by course_ids[]. The user making the request must be observing the observed user in all the courses specified by course_ids[]. (optional)
    include = ['include_example'] # List[str] | \"planner_overrides\":: Optionally include the assignment's associated planner override, if it exists, for the current user.                       These will be returned under a +planner_override+ key \"course\":: Optionally include the assignments' courses (optional)
    filter = ['filter_example'] # List[str] | \"submittable\":: Only return assignments that the current user can submit (i.e. filter out locked assignments) \"current_grading_period\":: Only return missing assignments that are in the current grading period (optional)
    course_ids = ['course_ids_example'] # List[str] | Optionally restricts the list of past-due assignments to only those associated with the specified course IDs. Required if observed_user_id is passed. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List Missing Submissions
        api_response = await api_instance.users_missing_submissions(user_id, observed_user_id=observed_user_id, include=include, filter=filter, course_ids=course_ids, page=page, per_page=per_page)
        print("The response of UsersApi->users_missing_submissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_missing_submissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| the student&#39;s ID | 
 **observed_user_id** | **str**| Return missing submissions for the given observed user. Must be accompanied by course_ids[]. The user making the request must be observing the observed user in all the courses specified by course_ids[]. | [optional] 
 **include** | [**List[str]**](str.md)| \&quot;planner_overrides\&quot;:: Optionally include the assignment&#39;s associated planner override, if it exists, for the current user.                       These will be returned under a +planner_override+ key \&quot;course\&quot;:: Optionally include the assignments&#39; courses | [optional] 
 **filter** | [**List[str]**](str.md)| \&quot;submittable\&quot;:: Only return assignments that the current user can submit (i.e. filter out locked assignments) \&quot;current_grading_period\&quot;:: Only return missing assignments that are in the current grading period | [optional] 
 **course_ids** | [**List[str]**](str.md)| Optionally restricts the list of past-due assignments to only those associated with the specified course IDs. Required if observed_user_id is passed. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[Assignment]**](Assignment.md)

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

# **users_pandata_events_token**
> users_pandata_events_token(users_pandata_events_token_request=users_pandata_events_token_request)

Get a Pandata Events jwt token and its expiration date

Returns a jwt auth and props token that can be used to send events to
Pandata.

NOTE: This is currently only available to the mobile developer keys.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.users_pandata_events_token_request import UsersPandataEventsTokenRequest
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
    api_instance = canvas_lms_python_client.UsersApi(api_client)
    users_pandata_events_token_request = canvas_lms_python_client.UsersPandataEventsTokenRequest() # UsersPandataEventsTokenRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/users/self/pandata_events_token \\      -X POST \\      -H 'Authorization: Bearer <token>'      -F 'app_key=MOBILE_APPS_KEY' \\ ``` (optional)

    try:
        # Get a Pandata Events jwt token and its expiration date
        await api_instance.users_pandata_events_token(users_pandata_events_token_request=users_pandata_events_token_request)
    except Exception as e:
        print("Exception when calling UsersApi->users_pandata_events_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **users_pandata_events_token_request** | [**UsersPandataEventsTokenRequest**](UsersPandataEventsTokenRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/users/self/pandata_events_token \\      -X POST \\      -H &#39;Authorization: Bearer &lt;token&gt;&#39;      -F &#39;app_key&#x3D;MOBILE_APPS_KEY&#39; \\ &#x60;&#x60;&#x60; | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Get a Pandata Events jwt token and its expiration date |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_set_custom_color**
> users_set_custom_color(asset_string, id, users_set_custom_color_request=users_set_custom_color_request)

Update custom color

Updates a custom color for a user for a given context.  This allows
colors for the calendar and elsewhere to be customized on a user basis.

The asset string parameter should be in the format 'context_id', for example
'course_42'

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.users_set_custom_color_request import UsersSetCustomColorRequest
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
    api_instance = canvas_lms_python_client.UsersApi(api_client)
    asset_string = 'asset_string_example' # str | Scope response to asset_string
    id = 'id_example' # str | Scope response to id
    users_set_custom_color_request = canvas_lms_python_client.UsersSetCustomColorRequest() # UsersSetCustomColorRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/users/<user_id>/colors/<asset_string> \\   -X PUT \\   -F 'hexcode=fffeee'   -H 'Authorization: Bearer <token>' ``` (optional)

    try:
        # Update custom color
        await api_instance.users_set_custom_color(asset_string, id, users_set_custom_color_request=users_set_custom_color_request)
    except Exception as e:
        print("Exception when calling UsersApi->users_set_custom_color: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_string** | **str**| Scope response to asset_string | 
 **id** | **str**| Scope response to id | 
 **users_set_custom_color_request** | [**UsersSetCustomColorRequest**](UsersSetCustomColorRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/users/&lt;user_id&gt;/colors/&lt;asset_string&gt; \\   -X PUT \\   -F &#39;hexcode&#x3D;fffeee&#39;   -H &#39;Authorization: Bearer &lt;token&gt;&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Update custom color |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_set_dashboard_positions**
> users_set_dashboard_positions(id)

Update dashboard positions

Updates the dashboard positions for a user for a given context.  This allows
positions for the dashboard cards and elsewhere to be customized on a per
user basis.

The asset string parameter should be in the format 'context_id', for example
'course_42'

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
    api_instance = canvas_lms_python_client.UsersApi(api_client)
    id = 'id_example' # str | Scope response to id

    try:
        # Update dashboard positions
        await api_instance.users_set_dashboard_positions(id)
    except Exception as e:
        print("Exception when calling UsersApi->users_set_dashboard_positions: %s\n" % e)
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
**0** | Update dashboard positions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_set_files_ui_version_preference**
> users_set_files_ui_version_preference(id, users_set_files_ui_version_preference_request=users_set_files_ui_version_preference_request)

Update files UI version preference

Updates a user's default choice for files UI version. This allows
the files UI to preload the user's preference.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.users_set_files_ui_version_preference_request import UsersSetFilesUiVersionPreferenceRequest
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
    api_instance = canvas_lms_python_client.UsersApi(api_client)
    id = 'id_example' # str | Scope response to id
    users_set_files_ui_version_preference_request = canvas_lms_python_client.UsersSetFilesUiVersionPreferenceRequest() # UsersSetFilesUiVersionPreferenceRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/users/<user_id>/files_ui_version_preference \\   -X PUT \\   -F 'files_ui_version=v2'   -H 'Authorization: Bearer <token>' ``` (optional)

    try:
        # Update files UI version preference
        await api_instance.users_set_files_ui_version_preference(id, users_set_files_ui_version_preference_request=users_set_files_ui_version_preference_request)
    except Exception as e:
        print("Exception when calling UsersApi->users_set_files_ui_version_preference: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **users_set_files_ui_version_preference_request** | [**UsersSetFilesUiVersionPreferenceRequest**](UsersSetFilesUiVersionPreferenceRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/users/&lt;user_id&gt;/files_ui_version_preference \\   -X PUT \\   -F &#39;files_ui_version&#x3D;v2&#39;   -H &#39;Authorization: Bearer &lt;token&gt;&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Update files UI version preference |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_set_text_editor_preference**
> users_set_text_editor_preference(id, users_set_text_editor_preference_request=users_set_text_editor_preference_request)

Update text editor preference

Updates a user's default choice for text editor.  This allows
the Choose an Editor propmts to preload the user's preference.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.users_set_text_editor_preference_request import UsersSetTextEditorPreferenceRequest
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
    api_instance = canvas_lms_python_client.UsersApi(api_client)
    id = 'id_example' # str | Scope response to id
    users_set_text_editor_preference_request = canvas_lms_python_client.UsersSetTextEditorPreferenceRequest() # UsersSetTextEditorPreferenceRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/users/<user_id>/prefered_editor \\   -X PUT \\   -F 'text_editor_preference=rce'   -H 'Authorization: Bearer <token>' ``` (optional)

    try:
        # Update text editor preference
        await api_instance.users_set_text_editor_preference(id, users_set_text_editor_preference_request=users_set_text_editor_preference_request)
    except Exception as e:
        print("Exception when calling UsersApi->users_set_text_editor_preference: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **users_set_text_editor_preference_request** | [**UsersSetTextEditorPreferenceRequest**](UsersSetTextEditorPreferenceRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/users/&lt;user_id&gt;/prefered_editor \\   -X PUT \\   -F &#39;text_editor_preference&#x3D;rce&#39;   -H &#39;Authorization: Bearer &lt;token&gt;&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Update text editor preference |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_settings**
> users_settings(id, manual_mark_as_read=manual_mark_as_read, release_notes_badge_disabled=release_notes_badge_disabled, collapse_global_nav=collapse_global_nav, collapse_course_nav=collapse_course_nav, hide_dashcard_color_overlays=hide_dashcard_color_overlays, comment_library_suggestions_enabled=comment_library_suggestions_enabled, elementary_dashboard_disabled=elementary_dashboard_disabled, widget_dashboard_user_preference=widget_dashboard_user_preference, widget_dashboard_dark_mode=widget_dashboard_dark_mode)

Update user settings.

Update an existing user's settings.

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
    api_instance = canvas_lms_python_client.UsersApi(api_client)
    id = 'id_example' # str | Scope response to id
    manual_mark_as_read = True # bool | If true, require user to manually mark discussion posts as read (don't auto-mark as read). (optional)
    release_notes_badge_disabled = True # bool | If true, hide the badge for new release notes. (optional)
    collapse_global_nav = True # bool | If true, the user's page loads with the global navigation collapsed (optional)
    collapse_course_nav = True # bool | If true, the user's course pages will load with the course navigation collapsed. (optional)
    hide_dashcard_color_overlays = True # bool | If true, images on course cards will be presented without being tinted to match the course color. (optional)
    comment_library_suggestions_enabled = True # bool | If true, suggestions within the comment library will be shown. (optional)
    elementary_dashboard_disabled = True # bool | If true, will display the user's preferred class Canvas dashboard view instead of the canvas for elementary view. (optional)
    widget_dashboard_user_preference = True # bool | If true, enables the widget dashboard for the user. Only applies when the widget_dashboard feature is enabled at the account level. Defaults to true when the feature becomes available. (optional)
    widget_dashboard_dark_mode = True # bool | If true, enables the dark color theme for the widget dashboard. (optional)

    try:
        # Update user settings.
        await api_instance.users_settings(id, manual_mark_as_read=manual_mark_as_read, release_notes_badge_disabled=release_notes_badge_disabled, collapse_global_nav=collapse_global_nav, collapse_course_nav=collapse_course_nav, hide_dashcard_color_overlays=hide_dashcard_color_overlays, comment_library_suggestions_enabled=comment_library_suggestions_enabled, elementary_dashboard_disabled=elementary_dashboard_disabled, widget_dashboard_user_preference=widget_dashboard_user_preference, widget_dashboard_dark_mode=widget_dashboard_dark_mode)
    except Exception as e:
        print("Exception when calling UsersApi->users_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **manual_mark_as_read** | **bool**| If true, require user to manually mark discussion posts as read (don&#39;t auto-mark as read). | [optional] 
 **release_notes_badge_disabled** | **bool**| If true, hide the badge for new release notes. | [optional] 
 **collapse_global_nav** | **bool**| If true, the user&#39;s page loads with the global navigation collapsed | [optional] 
 **collapse_course_nav** | **bool**| If true, the user&#39;s course pages will load with the course navigation collapsed. | [optional] 
 **hide_dashcard_color_overlays** | **bool**| If true, images on course cards will be presented without being tinted to match the course color. | [optional] 
 **comment_library_suggestions_enabled** | **bool**| If true, suggestions within the comment library will be shown. | [optional] 
 **elementary_dashboard_disabled** | **bool**| If true, will display the user&#39;s preferred class Canvas dashboard view instead of the canvas for elementary view. | [optional] 
 **widget_dashboard_user_preference** | **bool**| If true, enables the widget dashboard for the user. Only applies when the widget_dashboard feature is enabled at the account level. Defaults to true when the feature becomes available. | [optional] 
 **widget_dashboard_dark_mode** | **bool**| If true, enables the dark color theme for the widget dashboard. | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Update user settings. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_settings_for_users**
> users_settings_for_users(id, users_settings_for_users_request=users_settings_for_users_request)

Update user settings.

Update an existing user's settings.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.users_settings_for_users_request import UsersSettingsForUsersRequest
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
    api_instance = canvas_lms_python_client.UsersApi(api_client)
    id = 'id_example' # str | Scope response to id
    users_settings_for_users_request = canvas_lms_python_client.UsersSettingsForUsersRequest() # UsersSettingsForUsersRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/users/<user_id>/settings \\   -X PUT \\   -F 'manual_mark_as_read=true'   -H 'Authorization: Bearer <token>' ``` (optional)

    try:
        # Update user settings.
        await api_instance.users_settings_for_users(id, users_settings_for_users_request=users_settings_for_users_request)
    except Exception as e:
        print("Exception when calling UsersApi->users_settings_for_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **users_settings_for_users_request** | [**UsersSettingsForUsersRequest**](UsersSettingsForUsersRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/users/&lt;user_id&gt;/settings \\   -X PUT \\   -F &#39;manual_mark_as_read&#x3D;true&#39;   -H &#39;Authorization: Bearer &lt;token&gt;&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Update user settings. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_split**
> List[User] users_split(id)

Split merged users into separate users

Merged users cannot be fully restored to their previous state, but this will
attempt to split as much as possible to the previous state.
To split a merged user, the caller must have permissions to manage all of
the users logins. If there are multiple users that have been merged into one
user it will split each merge into a separate user.
A split can only happen within 180 days of a user merge. A user merge deletes
the previous user and may be permanently deleted. In this scenario we create
a new user object and proceed to move as much as possible to the new user.
The user object will not have preserved the name or settings from the
previous user. Some items may have been deleted during a user_merge that
cannot be restored, and/or the data has become stale because of other
changes to the objects since the time of the user_merge.

Split users details and caveats:

The from_user is the user that was deleted in the user_merge process.
The destination_user is the user that remains, that is being split.

Avatars:
When both users had avatars, both will be remain.
When from_user had an avatar and destination_user did not have an avatar,
the destination_user's avatar will be deleted if it still matches what was
there are the time of the merge.
If the destination_user's avatar was changed at anytime after the merge, it
will remain on the destination user.
If the from_user had an avatar it will be there after split.

Terms of Use:
If from_user had not accepted terms of use, they will be prompted again
to accept terms of use after the split.
If the destination_user had not accepted terms of use, hey will be prompted
again to accept terms of use after the split.
If neither user had accepted the terms of use, but since the time of the
merge had accepted, both will be prompted to accept terms of use.
If both had accepted terms of use, this will remain.

Communication Channels:
All communication channels are restored to what they were prior to the
merge. If a communication channel was added after the merge, it will remain
on the destination_user.
Notification preferences remain with the communication channels.

Enrollments:
All enrollments from the time of the merge will be moved back to where they
were. Enrollments created since the time of the merge that were created by
sis_import will go to the user that owns that sis_id used for the import.
Other new enrollments will remain on the destination_user.
Everything that is tied to the destination_user at the course level relating
to an enrollment is moved to the from_user. When both users are in the same
course prior to merge this can cause some unexpected items to move.

Submissions:
Unlike other items tied to a course, submissions are explicitly recorded to
avoid problems with grades.
All submissions were moved are restored to the spot prior to merge.
All submission that were created in a course that was moved in enrollments
are moved over to the from_user.

Other notes:
Access Tokens are moved back on split.
Conversations are moved back on split.
Favorites that existing at the time of merge are moved back on split.
LTI ids are restored to how they were prior to merge.

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
    api_instance = canvas_lms_python_client.UsersApi(api_client)
    id = 'id_example' # str | Scope response to id

    try:
        # Split merged users into separate users
        api_response = await api_instance.users_split(id)
        print("The response of UsersApi->users_split:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_split: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 

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

# **users_terminate_sessions**
> users_terminate_sessions(id)

Terminate all user sessions

Terminates all sessions for a user. This includes all browser-based
sessions and all access tokens, including manually generated ones.
The user can immediately re-authenticate to access Canvas again if
they have the current credentials. All integrations will need to
be re-authorized.

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
    api_instance = canvas_lms_python_client.UsersApi(api_client)
    id = 'id_example' # str | Scope response to id

    try:
        # Terminate all user sessions
        await api_instance.users_terminate_sessions(id)
    except Exception as e:
        print("Exception when calling UsersApi->users_terminate_sessions: %s\n" % e)
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
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Terminate all user sessions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_todo_item_count**
> users_todo_item_count(include=include)

List counts for todo items

Counts of different todo items such as the number of assignments needing grading as well as the number of assignments needing submitting.

There is a limit to the number of todo items this endpoint will count.
It will only look at the first 100 todo items for the user. If the user has more than 100 todo items this count may not be reliable.
The largest reliable number for both counts is 100.

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
    api_instance = canvas_lms_python_client.UsersApi(api_client)
    include = ['include_example'] # List[str] | \"ungraded_quizzes\":: Optionally include ungraded quizzes (such as practice quizzes and surveys) in the list.                      These will be returned under a +quiz+ key instead of an +assignment+ key in response elements. (optional)

    try:
        # List counts for todo items
        await api_instance.users_todo_item_count(include=include)
    except Exception as e:
        print("Exception when calling UsersApi->users_todo_item_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | [**List[str]**](str.md)| \&quot;ungraded_quizzes\&quot;:: Optionally include ungraded quizzes (such as practice quizzes and surveys) in the list.                      These will be returned under a +quiz+ key instead of an +assignment+ key in response elements. | [optional] 

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
**0** | List counts for todo items |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_todo_items**
> List[TodoItem] users_todo_items(include=include, course_ids=course_ids, page=page, per_page=per_page)

List the TODO items

A paginated list of the current user's list of todo items.

There is a limit to the number of items returned.

The `ignore` and `ignore_permanently` URLs can be used to update the user's
preferences on what items will be displayed.
Performing a DELETE request against the `ignore` URL will hide that item
from future todo item requests, until the item changes.
Performing a DELETE request against the `ignore_permanently` URL will hide
that item forever.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.todo_item import TodoItem
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
    api_instance = canvas_lms_python_client.UsersApi(api_client)
    include = ['include_example'] # List[str] | \"ungraded_quizzes\":: Optionally include ungraded quizzes (such as practice quizzes and surveys) in the list.                      These will be returned under a +quiz+ key instead of an +assignment+ key in response elements. \"grading_counts\":: Optionally include segmented submission counts on grading-type items:                    +on_time_needs_grading_count+, +late_needs_grading_count+,                    +resubmitted_needs_grading_count+, +submitted_submissions_count+, and                    +total_submissions_count+. Only honored when the account has the                    +educator_dashboard+ feature enabled; otherwise silently ignored. (optional)
    course_ids = ['course_ids_example'] # List[str] | Restrict results to todo items in the given courses. Accepts numeric IDs and SIS IDs of the form +sis_course_id:foo+. Applies to grading, submitting, checkpoint, and ungraded quiz items alike. Courses the user is not enrolled in (or that cannot be resolved) are silently dropped. When the parameter is present but no valid courses resolve, an empty list is returned rather than the unfiltered list. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List the TODO items
        api_response = await api_instance.users_todo_items(include=include, course_ids=course_ids, page=page, per_page=per_page)
        print("The response of UsersApi->users_todo_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_todo_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | [**List[str]**](str.md)| \&quot;ungraded_quizzes\&quot;:: Optionally include ungraded quizzes (such as practice quizzes and surveys) in the list.                      These will be returned under a +quiz+ key instead of an +assignment+ key in response elements. \&quot;grading_counts\&quot;:: Optionally include segmented submission counts on grading-type items:                    +on_time_needs_grading_count+, +late_needs_grading_count+,                    +resubmitted_needs_grading_count+, +submitted_submissions_count+, and                    +total_submissions_count+. Only honored when the account has the                    +educator_dashboard+ feature enabled; otherwise silently ignored. | [optional] 
 **course_ids** | [**List[str]**](str.md)| Restrict results to todo items in the given courses. Accepts numeric IDs and SIS IDs of the form +sis_course_id:foo+. Applies to grading, submitting, checkpoint, and ungraded quiz items alike. Courses the user is not enrolled in (or that cannot be resolved) are silently dropped. When the parameter is present but no valid courses resolve, an empty list is returned rather than the unfiltered list. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[TodoItem]**](TodoItem.md)

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

# **users_upcoming_events**
> users_upcoming_events()

List upcoming assignments, calendar events

A paginated list of the current user's upcoming events.

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
    api_instance = canvas_lms_python_client.UsersApi(api_client)

    try:
        # List upcoming assignments, calendar events
        await api_instance.users_upcoming_events()
    except Exception as e:
        print("Exception when calling UsersApi->users_upcoming_events: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**0** | List upcoming assignments, calendar events |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_update**
> User users_update(id, users_update_request=users_update_request)

Edit a user

Modify an existing user. To modify a user's login, see the documentation for logins.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.user import User
from canvas_lms_python_client.models.users_update_request import UsersUpdateRequest
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
    api_instance = canvas_lms_python_client.UsersApi(api_client)
    id = 'id_example' # str | Scope response to id
    users_update_request = canvas_lms_python_client.UsersUpdateRequest() # UsersUpdateRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/users/133' \\      -X PUT \\      -F 'user[name]=Sheldon Cooper' \\      -F 'user[short_name]=Shelly' \\      -F 'user[time_zone]=Pacific Time (US & Canada)' \\      -F 'user[avatar][token]=<opaque_token>' \\      -H \"Authorization: Bearer <token>\" ``` (optional)

    try:
        # Edit a user
        api_response = await api_instance.users_update(id, users_update_request=users_update_request)
        print("The response of UsersApi->users_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **users_update_request** | [**UsersUpdateRequest**](UsersUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/users/133&#39; \\      -X PUT \\      -F &#39;user[name]&#x3D;Sheldon Cooper&#39; \\      -F &#39;user[short_name]&#x3D;Shelly&#39; \\      -F &#39;user[time_zone]&#x3D;Pacific Time (US &amp; Canada)&#39; \\      -F &#39;user[avatar][token]&#x3D;&lt;opaque_token&gt;&#39; \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**User**](User.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | User |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_graded_submissions**
> List[Submission] users_user_graded_submissions(id, include=include, only_current_enrollments=only_current_enrollments, only_published_assignments=only_published_assignments, page=page, per_page=per_page)

Get a users most recently graded submissions

Returns a list of the user's most recently graded submissions.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.submission import Submission
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
    api_instance = canvas_lms_python_client.UsersApi(api_client)
    id = 'id_example' # str | Scope response to id
    include = ['include_example'] # List[str] | Associations to include with the group (optional)
    only_current_enrollments = True # bool | Returns submissions for only currently active enrollments (optional)
    only_published_assignments = True # bool | Returns submissions for only published assignments (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # Get a users most recently graded submissions
        api_response = await api_instance.users_user_graded_submissions(id, include=include, only_current_enrollments=only_current_enrollments, only_published_assignments=only_published_assignments, page=page, per_page=per_page)
        print("The response of UsersApi->users_user_graded_submissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_user_graded_submissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **include** | [**List[str]**](str.md)| Associations to include with the group | [optional] 
 **only_current_enrollments** | **bool**| Returns submissions for only currently active enrollments | [optional] 
 **only_published_assignments** | **bool**| Returns submissions for only published assignments | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[Submission]**](Submission.md)

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

