# canvas_lms_python_client.AppointmentGroupsApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appointment_groups_create**](AppointmentGroupsApi.md#appointment_groups_create) | **POST** /api/v1/appointment_groups | Create an appointment group
[**appointment_groups_destroy**](AppointmentGroupsApi.md#appointment_groups_destroy) | **DELETE** /api/v1/appointment_groups/{id} | Delete an appointment group
[**appointment_groups_groups**](AppointmentGroupsApi.md#appointment_groups_groups) | **GET** /api/v1/appointment_groups/{id}/groups | List student group participants
[**appointment_groups_index**](AppointmentGroupsApi.md#appointment_groups_index) | **GET** /api/v1/appointment_groups | List appointment groups
[**appointment_groups_next_appointment**](AppointmentGroupsApi.md#appointment_groups_next_appointment) | **GET** /api/v1/appointment_groups/next_appointment | Get next appointment
[**appointment_groups_show**](AppointmentGroupsApi.md#appointment_groups_show) | **GET** /api/v1/appointment_groups/{id} | Get a single appointment group
[**appointment_groups_update**](AppointmentGroupsApi.md#appointment_groups_update) | **PUT** /api/v1/appointment_groups/{id} | Update an appointment group
[**appointment_groups_users**](AppointmentGroupsApi.md#appointment_groups_users) | **GET** /api/v1/appointment_groups/{id}/users | List user participants


# **appointment_groups_create**
> appointment_groups_create(appointment_groups_create_request=appointment_groups_create_request)

Create an appointment group

Create and return a new appointment group. If new_appointments are
specified, the response will return a new_appointments array (same format
as appointments array, see "List appointment groups" action)

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.appointment_groups_create_request import AppointmentGroupsCreateRequest
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
    api_instance = canvas_lms_python_client.AppointmentGroupsApi(api_client)
    appointment_groups_create_request = canvas_lms_python_client.AppointmentGroupsCreateRequest() # AppointmentGroupsCreateRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/appointment_groups.json' \\      -X POST \\      -F 'appointment_group[context_codes][]=course_123' \\      -F 'appointment_group[sub_context_codes][]=course_section_234' \\      -F 'appointment_group[title]=Final Presentation' \\      -F 'appointment_group[participants_per_appointment]=1' \\      -F 'appointment_group[min_appointments_per_participant]=1' \\      -F 'appointment_group[max_appointments_per_participant]=1' \\      -F 'appointment_group[new_appointments][0][]=2012-07-19T21:00:00Z' \\      -F 'appointment_group[new_appointments][0][]=2012-07-19T22:00:00Z' \\      -F 'appointment_group[new_appointments][1][]=2012-07-19T22:00:00Z' \\      -F 'appointment_group[new_appointments][1][]=2012-07-19T23:00:00Z' \\      -H \"Authorization: Bearer <token>\" ``` (optional)

    try:
        # Create an appointment group
        await api_instance.appointment_groups_create(appointment_groups_create_request=appointment_groups_create_request)
    except Exception as e:
        print("Exception when calling AppointmentGroupsApi->appointment_groups_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appointment_groups_create_request** | [**AppointmentGroupsCreateRequest**](AppointmentGroupsCreateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/appointment_groups.json&#39; \\      -X POST \\      -F &#39;appointment_group[context_codes][]&#x3D;course_123&#39; \\      -F &#39;appointment_group[sub_context_codes][]&#x3D;course_section_234&#39; \\      -F &#39;appointment_group[title]&#x3D;Final Presentation&#39; \\      -F &#39;appointment_group[participants_per_appointment]&#x3D;1&#39; \\      -F &#39;appointment_group[min_appointments_per_participant]&#x3D;1&#39; \\      -F &#39;appointment_group[max_appointments_per_participant]&#x3D;1&#39; \\      -F &#39;appointment_group[new_appointments][0][]&#x3D;2012-07-19T21:00:00Z&#39; \\      -F &#39;appointment_group[new_appointments][0][]&#x3D;2012-07-19T22:00:00Z&#39; \\      -F &#39;appointment_group[new_appointments][1][]&#x3D;2012-07-19T22:00:00Z&#39; \\      -F &#39;appointment_group[new_appointments][1][]&#x3D;2012-07-19T23:00:00Z&#39; \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; &#x60;&#x60;&#x60; | [optional] 

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
**0** | Create an appointment group |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **appointment_groups_destroy**
> appointment_groups_destroy(id, cancel_reason=cancel_reason)

Delete an appointment group

Delete an appointment group (and associated time slots and reservations)
and return the deleted group

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
    api_instance = canvas_lms_python_client.AppointmentGroupsApi(api_client)
    id = 'id_example' # str | Scope response to id
    cancel_reason = 'cancel_reason_example' # str | Reason for deleting/canceling the appointment group. (optional)

    try:
        # Delete an appointment group
        await api_instance.appointment_groups_destroy(id, cancel_reason=cancel_reason)
    except Exception as e:
        print("Exception when calling AppointmentGroupsApi->appointment_groups_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **cancel_reason** | **str**| Reason for deleting/canceling the appointment group. | [optional] 

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
**0** | Delete an appointment group |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **appointment_groups_groups**
> appointment_groups_groups(id, registration_status_all_registered_registered=registration_status_all_registered_registered, page=page, per_page=per_page)

List student group participants

A paginated list of student groups that are (or may be) participating in
this appointment group. Refer to the Groups API for the response fields.
Returns no results for appointment groups with the "User" participant_type.

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
    api_instance = canvas_lms_python_client.AppointmentGroupsApi(api_client)
    id = 'id_example' # str | Scope response to id
    registration_status_all_registered_registered = 'registration_status_all_registered_registered_example' # str | Limits results to the a given participation status, defaults to \"all\" (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List student group participants
        await api_instance.appointment_groups_groups(id, registration_status_all_registered_registered=registration_status_all_registered_registered, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling AppointmentGroupsApi->appointment_groups_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **registration_status_all_registered_registered** | **str**| Limits results to the a given participation status, defaults to \&quot;all\&quot; | [optional] 
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
**0** | List student group participants |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **appointment_groups_index**
> appointment_groups_index(scope=scope, context_codes=context_codes, include_past_appointments=include_past_appointments, include_appointments_child_events_participant_count_reserved_times_all_context_codes=include_appointments_child_events_participant_count_reserved_times_all_context_codes, page=page, per_page=per_page)

List appointment groups

Retrieve the paginated list of appointment groups that can be reserved or
managed by the current user.

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
    api_instance = canvas_lms_python_client.AppointmentGroupsApi(api_client)
    scope = 'scope_example' # str | Defaults to \"reservable\" (optional)
    context_codes = ['context_codes_example'] # List[str] | Array of context codes used to limit returned results. (optional)
    include_past_appointments = True # bool | Defaults to false. If true, includes past appointment groups (optional)
    include_appointments_child_events_participant_count_reserved_times_all_context_codes = 'include_appointments_child_events_participant_count_reserved_times_all_context_codes_example' # str | Array of additional information to include.  \"appointments\":: calendar event time slots for this appointment group \"child_events\":: reservations of those time slots \"participant_count\":: number of reservations \"reserved_times\":: the event id, start time and end time of reservations                    the current user has made) \"all_context_codes\":: all context codes associated with this appointment group (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List appointment groups
        await api_instance.appointment_groups_index(scope=scope, context_codes=context_codes, include_past_appointments=include_past_appointments, include_appointments_child_events_participant_count_reserved_times_all_context_codes=include_appointments_child_events_participant_count_reserved_times_all_context_codes, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling AppointmentGroupsApi->appointment_groups_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Defaults to \&quot;reservable\&quot; | [optional] 
 **context_codes** | [**List[str]**](str.md)| Array of context codes used to limit returned results. | [optional] 
 **include_past_appointments** | **bool**| Defaults to false. If true, includes past appointment groups | [optional] 
 **include_appointments_child_events_participant_count_reserved_times_all_context_codes** | **str**| Array of additional information to include.  \&quot;appointments\&quot;:: calendar event time slots for this appointment group \&quot;child_events\&quot;:: reservations of those time slots \&quot;participant_count\&quot;:: number of reservations \&quot;reserved_times\&quot;:: the event id, start time and end time of reservations                    the current user has made) \&quot;all_context_codes\&quot;:: all context codes associated with this appointment group | [optional] 
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
**0** | List appointment groups |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **appointment_groups_next_appointment**
> List[CalendarEvent] appointment_groups_next_appointment(appointment_group_ids=appointment_group_ids)

Get next appointment

Return the next appointment available to sign up for. The appointment
is returned in a one-element array. If no future appointments are
available, an empty array is returned.

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
    api_instance = canvas_lms_python_client.AppointmentGroupsApi(api_client)
    appointment_group_ids = ['appointment_group_ids_example'] # List[str] | List of ids of appointment groups to search. (optional)

    try:
        # Get next appointment
        api_response = await api_instance.appointment_groups_next_appointment(appointment_group_ids=appointment_group_ids)
        print("The response of AppointmentGroupsApi->appointment_groups_next_appointment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppointmentGroupsApi->appointment_groups_next_appointment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appointment_group_ids** | [**List[str]**](str.md)| List of ids of appointment groups to search. | [optional] 

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

# **appointment_groups_show**
> appointment_groups_show(id, include_child_events_appointments_all_context_codes=include_child_events_appointments_all_context_codes)

Get a single appointment group

Returns information for a single appointment group

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
    api_instance = canvas_lms_python_client.AppointmentGroupsApi(api_client)
    id = 'id_example' # str | Scope response to id
    include_child_events_appointments_all_context_codes = 'include_child_events_appointments_all_context_codes_example' # str | Array of additional information to include. See include[] argument of \"List appointment groups\" action.  \"child_events\":: reservations of time slots time slots \"appointments\":: will always be returned \"all_context_codes\":: all context codes associated with this appointment group (optional)

    try:
        # Get a single appointment group
        await api_instance.appointment_groups_show(id, include_child_events_appointments_all_context_codes=include_child_events_appointments_all_context_codes)
    except Exception as e:
        print("Exception when calling AppointmentGroupsApi->appointment_groups_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **include_child_events_appointments_all_context_codes** | **str**| Array of additional information to include. See include[] argument of \&quot;List appointment groups\&quot; action.  \&quot;child_events\&quot;:: reservations of time slots time slots \&quot;appointments\&quot;:: will always be returned \&quot;all_context_codes\&quot;:: all context codes associated with this appointment group | [optional] 

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
**0** | Get a single appointment group |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **appointment_groups_update**
> appointment_groups_update(id, appointment_groups_update_request=appointment_groups_update_request)

Update an appointment group

Update and return an appointment group. If new_appointments are specified,
the response will return a new_appointments array (same format as
appointments array, see "List appointment groups" action).

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.appointment_groups_update_request import AppointmentGroupsUpdateRequest
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
    api_instance = canvas_lms_python_client.AppointmentGroupsApi(api_client)
    id = 'id_example' # str | Scope response to id
    appointment_groups_update_request = canvas_lms_python_client.AppointmentGroupsUpdateRequest() # AppointmentGroupsUpdateRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/appointment_groups/543.json' \\      -X PUT \\      -F 'appointment_group[publish]=1' \\      -H \"Authorization: Bearer <token>\" ``` (optional)

    try:
        # Update an appointment group
        await api_instance.appointment_groups_update(id, appointment_groups_update_request=appointment_groups_update_request)
    except Exception as e:
        print("Exception when calling AppointmentGroupsApi->appointment_groups_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **appointment_groups_update_request** | [**AppointmentGroupsUpdateRequest**](AppointmentGroupsUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/appointment_groups/543.json&#39; \\      -X PUT \\      -F &#39;appointment_group[publish]&#x3D;1&#39; \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; &#x60;&#x60;&#x60; | [optional] 

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
**0** | Update an appointment group |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **appointment_groups_users**
> appointment_groups_users(id, registration_status_all_registered_registered=registration_status_all_registered_registered, page=page, per_page=per_page)

List user participants

A paginated list of users that are (or may be) participating in this
appointment group.  Refer to the Users API for the response fields. Returns
no results for appointment groups with the "Group" participant_type.

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
    api_instance = canvas_lms_python_client.AppointmentGroupsApi(api_client)
    id = 'id_example' # str | Scope response to id
    registration_status_all_registered_registered = 'registration_status_all_registered_registered_example' # str | Limits results to the a given participation status, defaults to \"all\" (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List user participants
        await api_instance.appointment_groups_users(id, registration_status_all_registered_registered=registration_status_all_registered_registered, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling AppointmentGroupsApi->appointment_groups_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **registration_status_all_registered_registered** | **str**| Limits results to the a given participation status, defaults to \&quot;all\&quot; | [optional] 
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
**0** | List user participants |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

