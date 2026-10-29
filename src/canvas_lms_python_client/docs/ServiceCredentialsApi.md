# canvas_lms_python_client.ServiceCredentialsApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**service_credentials_activity_stream**](ServiceCredentialsApi.md#service_credentials_activity_stream) | **GET** /api/v1/users/self/activity_stream | List the activity stream
[**service_credentials_activity_stream_for_other**](ServiceCredentialsApi.md#service_credentials_activity_stream_for_other) | **GET** /api/v1/users/activity_stream | List the activity stream
[**service_credentials_activity_stream_summary**](ServiceCredentialsApi.md#service_credentials_activity_stream_summary) | **GET** /api/v1/users/self/activity_stream/summary | Activity stream summary
[**service_credentials_api_index**](ServiceCredentialsApi.md#service_credentials_api_index) | **GET** /api/v1/accounts/{account_id}/users | List users in account
[**service_credentials_create_file**](ServiceCredentialsApi.md#service_credentials_create_file) | **POST** /api/v1/users/{user_id}/files | Upload a file
[**service_credentials_ignore_all_stream_items**](ServiceCredentialsApi.md#service_credentials_ignore_all_stream_items) | **DELETE** /api/v1/users/self/activity_stream | Hide all stream items
[**service_credentials_ignore_stream_item**](ServiceCredentialsApi.md#service_credentials_ignore_stream_item) | **DELETE** /api/v1/users/self/activity_stream/{id} | Hide a stream item
[**service_credentials_missing_submissions**](ServiceCredentialsApi.md#service_credentials_missing_submissions) | **GET** /api/v1/users/{user_id}/missing_submissions | List Missing Submissions
[**service_credentials_todo_item_count**](ServiceCredentialsApi.md#service_credentials_todo_item_count) | **GET** /api/v1/users/self/todo_item_count | List counts for todo items
[**service_credentials_todo_items**](ServiceCredentialsApi.md#service_credentials_todo_items) | **GET** /api/v1/users/self/todo | List the TODO items
[**service_credentials_upcoming_events**](ServiceCredentialsApi.md#service_credentials_upcoming_events) | **GET** /api/v1/users/self/upcoming_events | List upcoming assignments, calendar events


# **service_credentials_activity_stream**
> service_credentials_activity_stream(only_active_courses=only_active_courses)

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
    api_instance = canvas_lms_python_client.ServiceCredentialsApi(api_client)
    only_active_courses = True # bool | If true, will only return objects for courses the user is actively participating in (optional)

    try:
        # List the activity stream
        await api_instance.service_credentials_activity_stream(only_active_courses=only_active_courses)
    except Exception as e:
        print("Exception when calling ServiceCredentialsApi->service_credentials_activity_stream: %s\n" % e)
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

# **service_credentials_activity_stream_for_other**
> service_credentials_activity_stream_for_other(only_active_courses=only_active_courses)

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
    api_instance = canvas_lms_python_client.ServiceCredentialsApi(api_client)
    only_active_courses = True # bool | If true, will only return objects for courses the user is actively participating in (optional)

    try:
        # List the activity stream
        await api_instance.service_credentials_activity_stream_for_other(only_active_courses=only_active_courses)
    except Exception as e:
        print("Exception when calling ServiceCredentialsApi->service_credentials_activity_stream_for_other: %s\n" % e)
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

# **service_credentials_activity_stream_summary**
> service_credentials_activity_stream_summary(only_active_courses=only_active_courses)

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
    api_instance = canvas_lms_python_client.ServiceCredentialsApi(api_client)
    only_active_courses = True # bool | If true, will only return objects for courses the user is actively participating in (optional)

    try:
        # Activity stream summary
        await api_instance.service_credentials_activity_stream_summary(only_active_courses=only_active_courses)
    except Exception as e:
        print("Exception when calling ServiceCredentialsApi->service_credentials_activity_stream_summary: %s\n" % e)
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
**0** | Activity stream summary |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_credentials_api_index**
> List[object] service_credentials_api_index(account_id, search_term=search_term, enrollment_type=enrollment_type, sort=sort, order=order, include_deleted_users=include_deleted_users, uuids=uuids, page=page, per_page=per_page)

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
    api_instance = canvas_lms_python_client.ServiceCredentialsApi(api_client)
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
        api_response = await api_instance.service_credentials_api_index(account_id, search_term=search_term, enrollment_type=enrollment_type, sort=sort, order=order, include_deleted_users=include_deleted_users, uuids=uuids, page=page, per_page=per_page)
        print("The response of ServiceCredentialsApi->service_credentials_api_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceCredentialsApi->service_credentials_api_index: %s\n" % e)
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

# **service_credentials_create_file**
> service_credentials_create_file(user_id)

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
    api_instance = canvas_lms_python_client.ServiceCredentialsApi(api_client)
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # Upload a file
        await api_instance.service_credentials_create_file(user_id)
    except Exception as e:
        print("Exception when calling ServiceCredentialsApi->service_credentials_create_file: %s\n" % e)
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

# **service_credentials_ignore_all_stream_items**
> service_credentials_ignore_all_stream_items()

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
    api_instance = canvas_lms_python_client.ServiceCredentialsApi(api_client)

    try:
        # Hide all stream items
        await api_instance.service_credentials_ignore_all_stream_items()
    except Exception as e:
        print("Exception when calling ServiceCredentialsApi->service_credentials_ignore_all_stream_items: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**0** | Hide all stream items |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_credentials_ignore_stream_item**
> service_credentials_ignore_stream_item(id)

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
    api_instance = canvas_lms_python_client.ServiceCredentialsApi(api_client)
    id = 'id_example' # str | Scope response to id

    try:
        # Hide a stream item
        await api_instance.service_credentials_ignore_stream_item(id)
    except Exception as e:
        print("Exception when calling ServiceCredentialsApi->service_credentials_ignore_stream_item: %s\n" % e)
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
**0** | Hide a stream item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_credentials_missing_submissions**
> List[object] service_credentials_missing_submissions(user_id, observed_user_id=observed_user_id, include=include, filter=filter, course_ids=course_ids, page=page, per_page=per_page)

List Missing Submissions

A paginated list of past-due assignments for which the student does not have a submission.
The user sending the request must either be the student, an admin or a parent observer using the parent app

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
    api_instance = canvas_lms_python_client.ServiceCredentialsApi(api_client)
    user_id = 'user_id_example' # str | the student's ID
    observed_user_id = 'observed_user_id_example' # str | Return missing submissions for the given observed user. Must be accompanied by course_ids[]. The user making the request must be observing the observed user in all the courses specified by course_ids[]. (optional)
    include = ['include_example'] # List[str] | \"planner_overrides\":: Optionally include the assignment's associated planner override, if it exists, for the current user.                       These will be returned under a +planner_override+ key \"course\":: Optionally include the assignments' courses (optional)
    filter = ['filter_example'] # List[str] | \"submittable\":: Only return assignments that the current user can submit (i.e. filter out locked assignments) \"current_grading_period\":: Only return missing assignments that are in the current grading period (optional)
    course_ids = ['course_ids_example'] # List[str] | Optionally restricts the list of past-due assignments to only those associated with the specified course IDs. Required if observed_user_id is passed. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List Missing Submissions
        api_response = await api_instance.service_credentials_missing_submissions(user_id, observed_user_id=observed_user_id, include=include, filter=filter, course_ids=course_ids, page=page, per_page=per_page)
        print("The response of ServiceCredentialsApi->service_credentials_missing_submissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceCredentialsApi->service_credentials_missing_submissions: %s\n" % e)
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

# **service_credentials_todo_item_count**
> service_credentials_todo_item_count(include=include)

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
    api_instance = canvas_lms_python_client.ServiceCredentialsApi(api_client)
    include = ['include_example'] # List[str] | \"ungraded_quizzes\":: Optionally include ungraded quizzes (such as practice quizzes and surveys) in the list.                      These will be returned under a +quiz+ key instead of an +assignment+ key in response elements. (optional)

    try:
        # List counts for todo items
        await api_instance.service_credentials_todo_item_count(include=include)
    except Exception as e:
        print("Exception when calling ServiceCredentialsApi->service_credentials_todo_item_count: %s\n" % e)
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
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | List counts for todo items |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_credentials_todo_items**
> service_credentials_todo_items(include=include, course_ids=course_ids, page=page, per_page=per_page)

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
    api_instance = canvas_lms_python_client.ServiceCredentialsApi(api_client)
    include = ['include_example'] # List[str] | \"ungraded_quizzes\":: Optionally include ungraded quizzes (such as practice quizzes and surveys) in the list.                      These will be returned under a +quiz+ key instead of an +assignment+ key in response elements. \"grading_counts\":: Optionally include segmented submission counts on grading-type items:                    +on_time_needs_grading_count+, +late_needs_grading_count+,                    +resubmitted_needs_grading_count+, +submitted_submissions_count+, and                    +total_submissions_count+. Only honored when the account has the                    +educator_dashboard+ feature enabled; otherwise silently ignored. (optional)
    course_ids = ['course_ids_example'] # List[str] | Restrict results to todo items in the given courses. Accepts numeric IDs and SIS IDs of the form +sis_course_id:foo+. Applies to grading, submitting, checkpoint, and ungraded quiz items alike. Courses the user is not enrolled in (or that cannot be resolved) are silently dropped. When the parameter is present but no valid courses resolve, an empty list is returned rather than the unfiltered list. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List the TODO items
        await api_instance.service_credentials_todo_items(include=include, course_ids=course_ids, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling ServiceCredentialsApi->service_credentials_todo_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | [**List[str]**](str.md)| \&quot;ungraded_quizzes\&quot;:: Optionally include ungraded quizzes (such as practice quizzes and surveys) in the list.                      These will be returned under a +quiz+ key instead of an +assignment+ key in response elements. \&quot;grading_counts\&quot;:: Optionally include segmented submission counts on grading-type items:                    +on_time_needs_grading_count+, +late_needs_grading_count+,                    +resubmitted_needs_grading_count+, +submitted_submissions_count+, and                    +total_submissions_count+. Only honored when the account has the                    +educator_dashboard+ feature enabled; otherwise silently ignored. | [optional] 
 **course_ids** | [**List[str]**](str.md)| Restrict results to todo items in the given courses. Accepts numeric IDs and SIS IDs of the form +sis_course_id:foo+. Applies to grading, submitting, checkpoint, and ungraded quiz items alike. Courses the user is not enrolled in (or that cannot be resolved) are silently dropped. When the parameter is present but no valid courses resolve, an empty list is returned rather than the unfiltered list. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

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
**0** | List the TODO items |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_credentials_upcoming_events**
> service_credentials_upcoming_events()

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
    api_instance = canvas_lms_python_client.ServiceCredentialsApi(api_client)

    try:
        # List upcoming assignments, calendar events
        await api_instance.service_credentials_upcoming_events()
    except Exception as e:
        print("Exception when calling ServiceCredentialsApi->service_credentials_upcoming_events: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**0** | List upcoming assignments, calendar events |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

