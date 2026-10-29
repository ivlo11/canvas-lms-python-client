# canvas_lms_python_client.PlannerNotesApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**planner_notes_create**](PlannerNotesApi.md#planner_notes_create) | **POST** /api/v1/planner_notes | Create a planner note
[**planner_notes_destroy**](PlannerNotesApi.md#planner_notes_destroy) | **DELETE** /api/v1/planner_notes/{id} | Delete a planner note
[**planner_notes_index**](PlannerNotesApi.md#planner_notes_index) | **GET** /api/v1/planner_notes | List planner notes
[**planner_notes_show**](PlannerNotesApi.md#planner_notes_show) | **GET** /api/v1/planner_notes/{id} | Show a planner note
[**planner_notes_update**](PlannerNotesApi.md#planner_notes_update) | **PUT** /api/v1/planner_notes/{id} | Update a planner note


# **planner_notes_create**
> PlannerNote planner_notes_create(planner_notes_create_request=planner_notes_create_request)

Create a planner note

Create a planner note for the current user

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.planner_note import PlannerNote
from canvas_lms_python_client.models.planner_notes_create_request import PlannerNotesCreateRequest
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
    api_instance = canvas_lms_python_client.PlannerNotesApi(api_client)
    planner_notes_create_request = canvas_lms_python_client.PlannerNotesCreateRequest() # PlannerNotesCreateRequest | Request body parameters (optional)

    try:
        # Create a planner note
        api_response = await api_instance.planner_notes_create(planner_notes_create_request=planner_notes_create_request)
        print("The response of PlannerNotesApi->planner_notes_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlannerNotesApi->planner_notes_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **planner_notes_create_request** | [**PlannerNotesCreateRequest**](PlannerNotesCreateRequest.md)| Request body parameters | [optional] 

### Return type

[**PlannerNote**](PlannerNote.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | PlannerNote |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **planner_notes_destroy**
> PlannerNote planner_notes_destroy(id)

Delete a planner note

Delete a planner note for the current user

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.planner_note import PlannerNote
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
    api_instance = canvas_lms_python_client.PlannerNotesApi(api_client)
    id = 'id_example' # str | Scope response to id

    try:
        # Delete a planner note
        api_response = await api_instance.planner_notes_destroy(id)
        print("The response of PlannerNotesApi->planner_notes_destroy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlannerNotesApi->planner_notes_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 

### Return type

[**PlannerNote**](PlannerNote.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | PlannerNote |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **planner_notes_index**
> List[PlannerNote] planner_notes_index(start_date=start_date, end_date=end_date, context_codes=context_codes)

List planner notes

Retrieve the paginated list of planner notes

Retrieve planner note for a user

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.planner_note import PlannerNote
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
    api_instance = canvas_lms_python_client.PlannerNotesApi(api_client)
    start_date = 'start_date_example' # str | Only return notes with todo dates since the start_date (inclusive). No default. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ. (optional)
    end_date = 'end_date_example' # str | Only return notes with todo dates before the end_date (inclusive). No default. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ. If end_date and start_date are both specified and equivalent, then only notes with todo dates on that day are returned. (optional)
    context_codes = ['context_codes_example'] # List[str] | List of context codes of courses whose notes you want to see. If not specified, defaults to all contexts that the user belongs to. The format of this field is the context type, followed by an underscore, followed by the context id. For example: course_42 Including a code matching the user's own context code (e.g. user_1) will include notes that are not associated with any particular course. (optional)

    try:
        # List planner notes
        api_response = await api_instance.planner_notes_index(start_date=start_date, end_date=end_date, context_codes=context_codes)
        print("The response of PlannerNotesApi->planner_notes_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlannerNotesApi->planner_notes_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**| Only return notes with todo dates since the start_date (inclusive). No default. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ. | [optional] 
 **end_date** | **str**| Only return notes with todo dates before the end_date (inclusive). No default. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ. If end_date and start_date are both specified and equivalent, then only notes with todo dates on that day are returned. | [optional] 
 **context_codes** | [**List[str]**](str.md)| List of context codes of courses whose notes you want to see. If not specified, defaults to all contexts that the user belongs to. The format of this field is the context type, followed by an underscore, followed by the context id. For example: course_42 Including a code matching the user&#39;s own context code (e.g. user_1) will include notes that are not associated with any particular course. | [optional] 

### Return type

[**List[PlannerNote]**](PlannerNote.md)

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

# **planner_notes_show**
> PlannerNote planner_notes_show(id)

Show a planner note

Retrieve a planner note for the current user

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.planner_note import PlannerNote
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
    api_instance = canvas_lms_python_client.PlannerNotesApi(api_client)
    id = 'id_example' # str | Scope response to id

    try:
        # Show a planner note
        api_response = await api_instance.planner_notes_show(id)
        print("The response of PlannerNotesApi->planner_notes_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlannerNotesApi->planner_notes_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 

### Return type

[**PlannerNote**](PlannerNote.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | PlannerNote |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **planner_notes_update**
> PlannerNote planner_notes_update(id, planner_notes_update_request=planner_notes_update_request)

Update a planner note

Update a planner note for the current user

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.planner_note import PlannerNote
from canvas_lms_python_client.models.planner_notes_update_request import PlannerNotesUpdateRequest
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
    api_instance = canvas_lms_python_client.PlannerNotesApi(api_client)
    id = 'id_example' # str | Scope response to id
    planner_notes_update_request = canvas_lms_python_client.PlannerNotesUpdateRequest() # PlannerNotesUpdateRequest | Request body parameters (optional)

    try:
        # Update a planner note
        api_response = await api_instance.planner_notes_update(id, planner_notes_update_request=planner_notes_update_request)
        print("The response of PlannerNotesApi->planner_notes_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlannerNotesApi->planner_notes_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **planner_notes_update_request** | [**PlannerNotesUpdateRequest**](PlannerNotesUpdateRequest.md)| Request body parameters | [optional] 

### Return type

[**PlannerNote**](PlannerNote.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | PlannerNote |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

