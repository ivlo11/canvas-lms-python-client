# canvas_lms_python_client.CalendarEventsApiApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**calendar_events_api_create**](CalendarEventsApiApi.md#calendar_events_api_create) | **POST** /api/v1/calendar_events | Create a calendar event
[**calendar_events_api_destroy**](CalendarEventsApiApi.md#calendar_events_api_destroy) | **DELETE** /api/v1/calendar_events/{id} | Delete a calendar event
[**calendar_events_api_get_course_timetable**](CalendarEventsApiApi.md#calendar_events_api_get_course_timetable) | **GET** /api/v1/courses/{course_id}/calendar_events/timetable | Get course timetable
[**calendar_events_api_index**](CalendarEventsApiApi.md#calendar_events_api_index) | **GET** /api/v1/calendar_events | List calendar events
[**calendar_events_api_reserve**](CalendarEventsApiApi.md#calendar_events_api_reserve) | **POST** /api/v1/calendar_events/{id}/reservations | Reserve a time slot
[**calendar_events_api_reserve_for_other**](CalendarEventsApiApi.md#calendar_events_api_reserve_for_other) | **POST** /api/v1/calendar_events/{id}/reservations/{participant_id} | Reserve a time slot
[**calendar_events_api_save_enabled_account_calendars**](CalendarEventsApiApi.md#calendar_events_api_save_enabled_account_calendars) | **POST** /api/v1/calendar_events/save_enabled_account_calendars | Save enabled account calendars
[**calendar_events_api_set_course_timetable**](CalendarEventsApiApi.md#calendar_events_api_set_course_timetable) | **POST** /api/v1/courses/{course_id}/calendar_events/timetable | Set a course timetable
[**calendar_events_api_set_course_timetable_events**](CalendarEventsApiApi.md#calendar_events_api_set_course_timetable_events) | **POST** /api/v1/courses/{course_id}/calendar_events/timetable_events | Create or update events directly for a course timetable
[**calendar_events_api_show**](CalendarEventsApiApi.md#calendar_events_api_show) | **GET** /api/v1/calendar_events/{id} | Get a single calendar event or assignment
[**calendar_events_api_update**](CalendarEventsApiApi.md#calendar_events_api_update) | **PUT** /api/v1/calendar_events/{id} | Update a calendar event
[**calendar_events_api_user_index**](CalendarEventsApiApi.md#calendar_events_api_user_index) | **GET** /api/v1/users/{user_id}/calendar_events | List calendar events for a user


# **calendar_events_api_create**
> calendar_events_api_create(calendar_events_api_create_request=calendar_events_api_create_request)

Create a calendar event

Create and return a new calendar event

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.calendar_events_api_create_request import CalendarEventsApiCreateRequest
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
    api_instance = canvas_lms_python_client.CalendarEventsApiApi(api_client)
    calendar_events_api_create_request = canvas_lms_python_client.CalendarEventsApiCreateRequest() # CalendarEventsApiCreateRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/calendar_events.json' \\      -X POST \\      -F 'calendar_event[context_code]=course_123' \\      -F 'calendar_event[title]=Paintball Fight!' \\      -F 'calendar_event[start_at]=2012-07-19T21:00:00Z' \\      -F 'calendar_event[end_at]=2012-07-19T22:00:00Z' \\      -H \"Authorization: Bearer <token>\" ``` (optional)

    try:
        # Create a calendar event
        await api_instance.calendar_events_api_create(calendar_events_api_create_request=calendar_events_api_create_request)
    except Exception as e:
        print("Exception when calling CalendarEventsApiApi->calendar_events_api_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **calendar_events_api_create_request** | [**CalendarEventsApiCreateRequest**](CalendarEventsApiCreateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/calendar_events.json&#39; \\      -X POST \\      -F &#39;calendar_event[context_code]&#x3D;course_123&#39; \\      -F &#39;calendar_event[title]&#x3D;Paintball Fight!&#39; \\      -F &#39;calendar_event[start_at]&#x3D;2012-07-19T21:00:00Z&#39; \\      -F &#39;calendar_event[end_at]&#x3D;2012-07-19T22:00:00Z&#39; \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; &#x60;&#x60;&#x60; | [optional] 

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
**0** | Create a calendar event |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calendar_events_api_destroy**
> calendar_events_api_destroy(id, cancel_reason=cancel_reason, which=which)

Delete a calendar event

Delete an event from the calendar and return the deleted event

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
    api_instance = canvas_lms_python_client.CalendarEventsApiApi(api_client)
    id = 'id_example' # str | Scope response to id
    cancel_reason = 'cancel_reason_example' # str | Reason for deleting/canceling the event. (optional)
    which = 'which_example' # str | Valid if the event whose ID is in the URL is part of a series. Delete just the event whose ID is in in the URL, all events in the series, or the given event and all those following. (optional)

    try:
        # Delete a calendar event
        await api_instance.calendar_events_api_destroy(id, cancel_reason=cancel_reason, which=which)
    except Exception as e:
        print("Exception when calling CalendarEventsApiApi->calendar_events_api_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **cancel_reason** | **str**| Reason for deleting/canceling the event. | [optional] 
 **which** | **str**| Valid if the event whose ID is in the URL is part of a series. Delete just the event whose ID is in in the URL, all events in the series, or the given event and all those following. | [optional] 

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
**0** | Delete a calendar event |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calendar_events_api_get_course_timetable**
> calendar_events_api_get_course_timetable(course_id)

Get course timetable

Returns the last timetable set by the
{api:CalendarEventsApiController#set_course_timetable Set a course timetable} endpoint

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
    api_instance = canvas_lms_python_client.CalendarEventsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id

    try:
        # Get course timetable
        await api_instance.calendar_events_api_get_course_timetable(course_id)
    except Exception as e:
        print("Exception when calling CalendarEventsApiApi->calendar_events_api_get_course_timetable: %s\n" % e)
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
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Get course timetable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calendar_events_api_index**
> List[CalendarEvent] calendar_events_api_index(type=type, start_date=start_date, end_date=end_date, undated=undated, all_events=all_events, context_codes=context_codes, excludes=excludes, includes=includes, important_dates=important_dates, blackout_date=blackout_date, page=page, per_page=per_page)

List calendar events

Retrieve the paginated list of calendar events or assignments for the current user

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.calendar_event import CalendarEvent
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
    api_instance = canvas_lms_python_client.CalendarEventsApiApi(api_client)
    type = 'type_example' # str | Defaults to \"event\" (optional)
    start_date = 'start_date_example' # str | Only return events since the start_date (inclusive). Defaults to today. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ. (optional)
    end_date = 'end_date_example' # str | Only return events before the end_date (inclusive). Defaults to start_date. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ. If end_date is the same as start_date, then only events on that day are returned. (optional)
    undated = True # bool | Defaults to false (dated events only). If true, only return undated events and ignore start_date and end_date. (optional)
    all_events = True # bool | Defaults to false (uses start_date, end_date, and undated criteria). If true, all events are returned, ignoring start_date, end_date, and undated criteria. (optional)
    context_codes = ['context_codes_example'] # List[str] | List of context codes of courses, groups, users, or accounts whose events you want to see. If not specified, defaults to the current user (i.e personal calendar, no course/group events). Limited to 10 context codes, additional ones are ignored. The format of this field is the context type, followed by an underscore, followed by the context id. For example: course_42 (optional)
    excludes = [canvas_lms_python_client.List[str]()] # List[List[str]] | Array of attributes to exclude. Possible values are \"description\", \"child_events\" and \"assignment\" (optional)
    includes = [canvas_lms_python_client.List[str]()] # List[List[str]] | Array of optional attributes to include. Possible values are \"web_conference\" and \"series_natural_language\" (optional)
    important_dates = True # bool | Defaults to false. If true, only events with important dates set to true will be returned. (optional)
    blackout_date = True # bool | Defaults to false. If true, only events with blackout date set to true will be returned. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List calendar events
        api_response = await api_instance.calendar_events_api_index(type=type, start_date=start_date, end_date=end_date, undated=undated, all_events=all_events, context_codes=context_codes, excludes=excludes, includes=includes, important_dates=important_dates, blackout_date=blackout_date, page=page, per_page=per_page)
        print("The response of CalendarEventsApiApi->calendar_events_api_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarEventsApiApi->calendar_events_api_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Defaults to \&quot;event\&quot; | [optional] 
 **start_date** | **str**| Only return events since the start_date (inclusive). Defaults to today. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ. | [optional] 
 **end_date** | **str**| Only return events before the end_date (inclusive). Defaults to start_date. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ. If end_date is the same as start_date, then only events on that day are returned. | [optional] 
 **undated** | **bool**| Defaults to false (dated events only). If true, only return undated events and ignore start_date and end_date. | [optional] 
 **all_events** | **bool**| Defaults to false (uses start_date, end_date, and undated criteria). If true, all events are returned, ignoring start_date, end_date, and undated criteria. | [optional] 
 **context_codes** | [**List[str]**](str.md)| List of context codes of courses, groups, users, or accounts whose events you want to see. If not specified, defaults to the current user (i.e personal calendar, no course/group events). Limited to 10 context codes, additional ones are ignored. The format of this field is the context type, followed by an underscore, followed by the context id. For example: course_42 | [optional] 
 **excludes** | [**List[List[str]]**](List[str].md)| Array of attributes to exclude. Possible values are \&quot;description\&quot;, \&quot;child_events\&quot; and \&quot;assignment\&quot; | [optional] 
 **includes** | [**List[List[str]]**](List[str].md)| Array of optional attributes to include. Possible values are \&quot;web_conference\&quot; and \&quot;series_natural_language\&quot; | [optional] 
 **important_dates** | **bool**| Defaults to false. If true, only events with important dates set to true will be returned. | [optional] 
 **blackout_date** | **bool**| Defaults to false. If true, only events with blackout date set to true will be returned. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[CalendarEvent]**](CalendarEvent.md)

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

# **calendar_events_api_reserve**
> calendar_events_api_reserve(id, calendar_events_api_reserve_request=calendar_events_api_reserve_request)

Reserve a time slot

Reserves a particular time slot and return the new reservation

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.calendar_events_api_reserve_request import CalendarEventsApiReserveRequest
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
    api_instance = canvas_lms_python_client.CalendarEventsApiApi(api_client)
    id = 'id_example' # str | Scope response to id
    calendar_events_api_reserve_request = canvas_lms_python_client.CalendarEventsApiReserveRequest() # CalendarEventsApiReserveRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/calendar_events/345/reservations.json' \\      -X POST \\      -F 'cancel_existing=true' \\      -H \"Authorization: Bearer <token>\" ``` (optional)

    try:
        # Reserve a time slot
        await api_instance.calendar_events_api_reserve(id, calendar_events_api_reserve_request=calendar_events_api_reserve_request)
    except Exception as e:
        print("Exception when calling CalendarEventsApiApi->calendar_events_api_reserve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **calendar_events_api_reserve_request** | [**CalendarEventsApiReserveRequest**](CalendarEventsApiReserveRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/calendar_events/345/reservations.json&#39; \\      -X POST \\      -F &#39;cancel_existing&#x3D;true&#39; \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; &#x60;&#x60;&#x60; | [optional] 

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
**0** | Reserve a time slot |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calendar_events_api_reserve_for_other**
> calendar_events_api_reserve_for_other(id, participant_id, calendar_events_api_reserve_for_other_request=calendar_events_api_reserve_for_other_request)

Reserve a time slot

Reserves a particular time slot and return the new reservation

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.calendar_events_api_reserve_for_other_request import CalendarEventsApiReserveForOtherRequest
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
    api_instance = canvas_lms_python_client.CalendarEventsApiApi(api_client)
    id = 'id_example' # str | Scope response to id
    participant_id = 'participant_id_example' # str | User or group id for whom you are making the reservation (depends on the participant type). Defaults to the current user (or user's candidate group).
    calendar_events_api_reserve_for_other_request = canvas_lms_python_client.CalendarEventsApiReserveForOtherRequest() # CalendarEventsApiReserveForOtherRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/calendar_events/345/reservations.json' \\      -X POST \\      -F 'cancel_existing=true' \\      -H \"Authorization: Bearer <token>\" ``` (optional)

    try:
        # Reserve a time slot
        await api_instance.calendar_events_api_reserve_for_other(id, participant_id, calendar_events_api_reserve_for_other_request=calendar_events_api_reserve_for_other_request)
    except Exception as e:
        print("Exception when calling CalendarEventsApiApi->calendar_events_api_reserve_for_other: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **participant_id** | **str**| User or group id for whom you are making the reservation (depends on the participant type). Defaults to the current user (or user&#39;s candidate group). | 
 **calendar_events_api_reserve_for_other_request** | [**CalendarEventsApiReserveForOtherRequest**](CalendarEventsApiReserveForOtherRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/calendar_events/345/reservations.json&#39; \\      -X POST \\      -F &#39;cancel_existing&#x3D;true&#39; \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; &#x60;&#x60;&#x60; | [optional] 

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
**0** | Reserve a time slot |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calendar_events_api_save_enabled_account_calendars**
> calendar_events_api_save_enabled_account_calendars(calendar_events_api_save_enabled_account_calendars_request=calendar_events_api_save_enabled_account_calendars_request)

Save enabled account calendars

Creates and updates the enabled_account_calendars and mark_feature_as_seen user preferences

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.calendar_events_api_save_enabled_account_calendars_request import CalendarEventsApiSaveEnabledAccountCalendarsRequest
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
    api_instance = canvas_lms_python_client.CalendarEventsApiApi(api_client)
    calendar_events_api_save_enabled_account_calendars_request = canvas_lms_python_client.CalendarEventsApiSaveEnabledAccountCalendarsRequest() # CalendarEventsApiSaveEnabledAccountCalendarsRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/calendar_events/save_enabled_account_calendars' \\      -X POST \\      -F 'mark_feature_as_seen=true' \\      -F 'enabled_account_calendars[]=1' \\      -F 'enabled_account_calendars[]=2' \\      -H \"Authorization: Bearer <token>\" ``` (optional)

    try:
        # Save enabled account calendars
        await api_instance.calendar_events_api_save_enabled_account_calendars(calendar_events_api_save_enabled_account_calendars_request=calendar_events_api_save_enabled_account_calendars_request)
    except Exception as e:
        print("Exception when calling CalendarEventsApiApi->calendar_events_api_save_enabled_account_calendars: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **calendar_events_api_save_enabled_account_calendars_request** | [**CalendarEventsApiSaveEnabledAccountCalendarsRequest**](CalendarEventsApiSaveEnabledAccountCalendarsRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/calendar_events/save_enabled_account_calendars&#39; \\      -X POST \\      -F &#39;mark_feature_as_seen&#x3D;true&#39; \\      -F &#39;enabled_account_calendars[]&#x3D;1&#39; \\      -F &#39;enabled_account_calendars[]&#x3D;2&#39; \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; &#x60;&#x60;&#x60; | [optional] 

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
**0** | Save enabled account calendars |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calendar_events_api_set_course_timetable**
> calendar_events_api_set_course_timetable(course_id, calendar_events_api_set_course_timetable_request=calendar_events_api_set_course_timetable_request)

Set a course timetable

Creates and updates "timetable" events for a course.
Can automaticaly generate a series of calendar events based on simple schedules
(e.g. "Monday and Wednesday at 2:00pm" )

Existing timetable events for the course and course sections
will be updated if they still are part of the timetable.
Otherwise, they will be deleted.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.calendar_events_api_set_course_timetable_request import CalendarEventsApiSetCourseTimetableRequest
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
    api_instance = canvas_lms_python_client.CalendarEventsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    calendar_events_api_set_course_timetable_request = canvas_lms_python_client.CalendarEventsApiSetCourseTimetableRequest() # CalendarEventsApiSetCourseTimetableRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/calendar_events/timetable' \\      -X POST \\      -F 'timetables[all][][weekdays]=Mon,Wed,Fri' \\      -F 'timetables[all][][start_time]=11:00 am' \\      -F 'timetables[all][][end_time]=11:50 am' \\      -F 'timetables[all][][location_name]=Room 237' \\      -H \"Authorization: Bearer <token>\" ``` (optional)

    try:
        # Set a course timetable
        await api_instance.calendar_events_api_set_course_timetable(course_id, calendar_events_api_set_course_timetable_request=calendar_events_api_set_course_timetable_request)
    except Exception as e:
        print("Exception when calling CalendarEventsApiApi->calendar_events_api_set_course_timetable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **calendar_events_api_set_course_timetable_request** | [**CalendarEventsApiSetCourseTimetableRequest**](CalendarEventsApiSetCourseTimetableRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/calendar_events/timetable&#39; \\      -X POST \\      -F &#39;timetables[all][][weekdays]&#x3D;Mon,Wed,Fri&#39; \\      -F &#39;timetables[all][][start_time]&#x3D;11:00 am&#39; \\      -F &#39;timetables[all][][end_time]&#x3D;11:50 am&#39; \\      -F &#39;timetables[all][][location_name]&#x3D;Room 237&#39; \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; &#x60;&#x60;&#x60; | [optional] 

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
**0** | Set a course timetable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calendar_events_api_set_course_timetable_events**
> calendar_events_api_set_course_timetable_events(course_id, calendar_events_api_set_course_timetable_events_request=calendar_events_api_set_course_timetable_events_request)

Create or update events directly for a course timetable

Creates and updates "timetable" events for a course or course section.
Similar to {api:CalendarEventsApiController#set_course_timetable setting a course timetable},
but instead of generating a list of events based on a timetable schedule,
this endpoint expects a complete list of events.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.calendar_events_api_set_course_timetable_events_request import CalendarEventsApiSetCourseTimetableEventsRequest
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
    api_instance = canvas_lms_python_client.CalendarEventsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    calendar_events_api_set_course_timetable_events_request = canvas_lms_python_client.CalendarEventsApiSetCourseTimetableEventsRequest() # CalendarEventsApiSetCourseTimetableEventsRequest | Request body parameters (optional)

    try:
        # Create or update events directly for a course timetable
        await api_instance.calendar_events_api_set_course_timetable_events(course_id, calendar_events_api_set_course_timetable_events_request=calendar_events_api_set_course_timetable_events_request)
    except Exception as e:
        print("Exception when calling CalendarEventsApiApi->calendar_events_api_set_course_timetable_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **calendar_events_api_set_course_timetable_events_request** | [**CalendarEventsApiSetCourseTimetableEventsRequest**](CalendarEventsApiSetCourseTimetableEventsRequest.md)| Request body parameters | [optional] 

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
**0** | Create or update events directly for a course timetable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calendar_events_api_show**
> CalendarEvent calendar_events_api_show(id)

Get a single calendar event or assignment

Returns detailed information about a specific calendar event or assignment.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.calendar_event import CalendarEvent
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
    api_instance = canvas_lms_python_client.CalendarEventsApiApi(api_client)
    id = 'id_example' # str | Scope response to id

    try:
        # Get a single calendar event or assignment
        api_response = await api_instance.calendar_events_api_show(id)
        print("The response of CalendarEventsApiApi->calendar_events_api_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarEventsApiApi->calendar_events_api_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 

### Return type

[**CalendarEvent**](CalendarEvent.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | CalendarEvent |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calendar_events_api_update**
> calendar_events_api_update(id, calendar_events_api_update_request=calendar_events_api_update_request)

Update a calendar event

Update and return a calendar event

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.calendar_events_api_update_request import CalendarEventsApiUpdateRequest
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
    api_instance = canvas_lms_python_client.CalendarEventsApiApi(api_client)
    id = 'id_example' # str | Scope response to id
    calendar_events_api_update_request = canvas_lms_python_client.CalendarEventsApiUpdateRequest() # CalendarEventsApiUpdateRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/calendar_events/234' \\      -X PUT \\      -F 'calendar_event[title]=Epic Paintball Fight!' \\      -H \"Authorization: Bearer <token>\" ``` (optional)

    try:
        # Update a calendar event
        await api_instance.calendar_events_api_update(id, calendar_events_api_update_request=calendar_events_api_update_request)
    except Exception as e:
        print("Exception when calling CalendarEventsApiApi->calendar_events_api_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **calendar_events_api_update_request** | [**CalendarEventsApiUpdateRequest**](CalendarEventsApiUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/calendar_events/234&#39; \\      -X PUT \\      -F &#39;calendar_event[title]&#x3D;Epic Paintball Fight!&#39; \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; &#x60;&#x60;&#x60; | [optional] 

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
**0** | Update a calendar event |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calendar_events_api_user_index**
> List[CalendarEvent] calendar_events_api_user_index(user_id, type=type, start_date=start_date, end_date=end_date, undated=undated, all_events=all_events, context_codes=context_codes, excludes=excludes, submission_types=submission_types, exclude_submission_types=exclude_submission_types, includes=includes, important_dates=important_dates, blackout_date=blackout_date, page=page, per_page=per_page)

List calendar events for a user

Retrieve the paginated list of calendar events or assignments for the specified user.
To view calendar events for a user other than yourself,
you must either be an observer of that user or an administrator.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.calendar_event import CalendarEvent
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
    api_instance = canvas_lms_python_client.CalendarEventsApiApi(api_client)
    user_id = 'user_id_example' # str | Scope response to user_id
    type = 'type_example' # str | Defaults to \"event\" (optional)
    start_date = 'start_date_example' # str | Only return events since the start_date (inclusive). Defaults to today. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ. (optional)
    end_date = 'end_date_example' # str | Only return events before the end_date (inclusive). Defaults to start_date. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ. If end_date is the same as start_date, then only events on that day are returned. (optional)
    undated = True # bool | Defaults to false (dated events only). If true, only return undated events and ignore start_date and end_date. (optional)
    all_events = True # bool | Defaults to false (uses start_date, end_date, and undated criteria). If true, all events are returned, ignoring start_date, end_date, and undated criteria. (optional)
    context_codes = ['context_codes_example'] # List[str] | List of context codes of courses, groups, users, or accounts whose events you want to see. If not specified, defaults to the current user (i.e personal calendar, no course/group events). Limited to 10 context codes, additional ones are ignored. The format of this field is the context type, followed by an underscore, followed by the context id. For example: course_42 (optional)
    excludes = [canvas_lms_python_client.List[str]()] # List[List[str]] | Array of attributes to exclude. Possible values are \"description\", \"child_events\" and \"assignment\" (optional)
    submission_types = [canvas_lms_python_client.List[str]()] # List[List[str]] | When type is \"assignment\", specifies the allowable submission types for returned assignments. Ignored if type is not \"assignment\" or if exclude_submission_types is provided. (optional)
    exclude_submission_types = [canvas_lms_python_client.List[str]()] # List[List[str]] | When type is \"assignment\", specifies the submission types to be excluded from the returned assignments. Ignored if type is not \"assignment\". (optional)
    includes = [canvas_lms_python_client.List[str]()] # List[List[str]] | Array of optional attributes to include. Possible values are \"web_conference\" and \"series_natural_language\" (optional)
    important_dates = True # bool | Defaults to false If true, only events with important dates set to true will be returned. (optional)
    blackout_date = True # bool | Defaults to false If true, only events with blackout date set to true will be returned. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List calendar events for a user
        api_response = await api_instance.calendar_events_api_user_index(user_id, type=type, start_date=start_date, end_date=end_date, undated=undated, all_events=all_events, context_codes=context_codes, excludes=excludes, submission_types=submission_types, exclude_submission_types=exclude_submission_types, includes=includes, important_dates=important_dates, blackout_date=blackout_date, page=page, per_page=per_page)
        print("The response of CalendarEventsApiApi->calendar_events_api_user_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarEventsApiApi->calendar_events_api_user_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Scope response to user_id | 
 **type** | **str**| Defaults to \&quot;event\&quot; | [optional] 
 **start_date** | **str**| Only return events since the start_date (inclusive). Defaults to today. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ. | [optional] 
 **end_date** | **str**| Only return events before the end_date (inclusive). Defaults to start_date. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ. If end_date is the same as start_date, then only events on that day are returned. | [optional] 
 **undated** | **bool**| Defaults to false (dated events only). If true, only return undated events and ignore start_date and end_date. | [optional] 
 **all_events** | **bool**| Defaults to false (uses start_date, end_date, and undated criteria). If true, all events are returned, ignoring start_date, end_date, and undated criteria. | [optional] 
 **context_codes** | [**List[str]**](str.md)| List of context codes of courses, groups, users, or accounts whose events you want to see. If not specified, defaults to the current user (i.e personal calendar, no course/group events). Limited to 10 context codes, additional ones are ignored. The format of this field is the context type, followed by an underscore, followed by the context id. For example: course_42 | [optional] 
 **excludes** | [**List[List[str]]**](List[str].md)| Array of attributes to exclude. Possible values are \&quot;description\&quot;, \&quot;child_events\&quot; and \&quot;assignment\&quot; | [optional] 
 **submission_types** | [**List[List[str]]**](List[str].md)| When type is \&quot;assignment\&quot;, specifies the allowable submission types for returned assignments. Ignored if type is not \&quot;assignment\&quot; or if exclude_submission_types is provided. | [optional] 
 **exclude_submission_types** | [**List[List[str]]**](List[str].md)| When type is \&quot;assignment\&quot;, specifies the submission types to be excluded from the returned assignments. Ignored if type is not \&quot;assignment\&quot;. | [optional] 
 **includes** | [**List[List[str]]**](List[str].md)| Array of optional attributes to include. Possible values are \&quot;web_conference\&quot; and \&quot;series_natural_language\&quot; | [optional] 
 **important_dates** | **bool**| Defaults to false If true, only events with important dates set to true will be returned. | [optional] 
 **blackout_date** | **bool**| Defaults to false If true, only events with blackout date set to true will be returned. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[CalendarEvent]**](CalendarEvent.md)

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

