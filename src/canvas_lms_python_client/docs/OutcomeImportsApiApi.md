# canvas_lms_python_client.OutcomeImportsApiApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**outcome_imports_api_create**](OutcomeImportsApiApi.md#outcome_imports_api_create) | **POST** /api/v1/accounts/{account_id}/outcome_imports(/group/{learning_outcome_group_id}) | Import Outcomes
[**outcome_imports_api_create_for_courses**](OutcomeImportsApiApi.md#outcome_imports_api_create_for_courses) | **POST** /api/v1/courses/{course_id}/outcome_imports(/group/{learning_outcome_group_id}) | Import Outcomes
[**outcome_imports_api_created_group_ids**](OutcomeImportsApiApi.md#outcome_imports_api_created_group_ids) | **GET** /api/v1/accounts/{account_id}/outcome_imports/{id}/created_group_ids | Get IDs of outcome groups created after successful import
[**outcome_imports_api_created_group_ids_for_courses**](OutcomeImportsApiApi.md#outcome_imports_api_created_group_ids_for_courses) | **GET** /api/v1/courses/{course_id}/outcome_imports/{id}/created_group_ids | Get IDs of outcome groups created after successful import
[**outcome_imports_api_show**](OutcomeImportsApiApi.md#outcome_imports_api_show) | **GET** /api/v1/accounts/{account_id}/outcome_imports/{id} | Get Outcome import status
[**outcome_imports_api_show_for_courses**](OutcomeImportsApiApi.md#outcome_imports_api_show_for_courses) | **GET** /api/v1/courses/{course_id}/outcome_imports/{id} | Get Outcome import status


# **outcome_imports_api_create**
> OutcomeImport outcome_imports_api_create(account_id, learning_outcome_group_id, outcome_imports_api_create_request=outcome_imports_api_create_request)

Import Outcomes

Import outcomes into Canvas.

For more information on the format that's expected here, please see the
"Outcomes CSV" section in the API docs.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.outcome_import import OutcomeImport
from canvas_lms_python_client.models.outcome_imports_api_create_request import OutcomeImportsApiCreateRequest
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
    api_instance = canvas_lms_python_client.OutcomeImportsApiApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    learning_outcome_group_id = 'learning_outcome_group_id_example' # str | Scope response to learning_outcome_group_id
    outcome_imports_api_create_request = canvas_lms_python_client.OutcomeImportsApiCreateRequest() # OutcomeImportsApiCreateRequest | Request body parameters (optional)

    try:
        # Import Outcomes
        api_response = await api_instance.outcome_imports_api_create(account_id, learning_outcome_group_id, outcome_imports_api_create_request=outcome_imports_api_create_request)
        print("The response of OutcomeImportsApiApi->outcome_imports_api_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutcomeImportsApiApi->outcome_imports_api_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **learning_outcome_group_id** | **str**| Scope response to learning_outcome_group_id | 
 **outcome_imports_api_create_request** | [**OutcomeImportsApiCreateRequest**](OutcomeImportsApiCreateRequest.md)| Request body parameters | [optional] 

### Return type

[**OutcomeImport**](OutcomeImport.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | OutcomeImport |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **outcome_imports_api_create_for_courses**
> OutcomeImport outcome_imports_api_create_for_courses(course_id, learning_outcome_group_id, outcome_imports_api_create_request=outcome_imports_api_create_request)

Import Outcomes

Import outcomes into Canvas.

For more information on the format that's expected here, please see the
"Outcomes CSV" section in the API docs.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.outcome_import import OutcomeImport
from canvas_lms_python_client.models.outcome_imports_api_create_request import OutcomeImportsApiCreateRequest
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
    api_instance = canvas_lms_python_client.OutcomeImportsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    learning_outcome_group_id = 'learning_outcome_group_id_example' # str | Scope response to learning_outcome_group_id
    outcome_imports_api_create_request = canvas_lms_python_client.OutcomeImportsApiCreateRequest() # OutcomeImportsApiCreateRequest | Request body parameters (optional)

    try:
        # Import Outcomes
        api_response = await api_instance.outcome_imports_api_create_for_courses(course_id, learning_outcome_group_id, outcome_imports_api_create_request=outcome_imports_api_create_request)
        print("The response of OutcomeImportsApiApi->outcome_imports_api_create_for_courses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutcomeImportsApiApi->outcome_imports_api_create_for_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **learning_outcome_group_id** | **str**| Scope response to learning_outcome_group_id | 
 **outcome_imports_api_create_request** | [**OutcomeImportsApiCreateRequest**](OutcomeImportsApiCreateRequest.md)| Request body parameters | [optional] 

### Return type

[**OutcomeImport**](OutcomeImport.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | OutcomeImport |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **outcome_imports_api_created_group_ids**
> object outcome_imports_api_created_group_ids(account_id, id)

Get IDs of outcome groups created after successful import

Get the IDs of the outcome groups created after a successful import.
Pass 'latest' for the outcome import id for the latest import.

  Examples:
    curl 'https://<canvas>/api/v1/accounts/<account_id>/outcome_imports/outcomes_group_ids/<outcome_import_id>' \
        -H "Authorization: Bearer <token>"
    curl 'https://<canvas>/api/v1/courses/<course_id>/outcome_imports/outcome_group_ids/<outcome_import_id>' \
        -H "Authorization: Bearer <token>"

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
    api_instance = canvas_lms_python_client.OutcomeImportsApiApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id

    try:
        # Get IDs of outcome groups created after successful import
        api_response = await api_instance.outcome_imports_api_created_group_ids(account_id, id)
        print("The response of OutcomeImportsApiApi->outcome_imports_api_created_group_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutcomeImportsApiApi->outcome_imports_api_created_group_ids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 

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
**0** | array of outcome ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **outcome_imports_api_created_group_ids_for_courses**
> object outcome_imports_api_created_group_ids_for_courses(course_id, id)

Get IDs of outcome groups created after successful import

Get the IDs of the outcome groups created after a successful import.
Pass 'latest' for the outcome import id for the latest import.

  Examples:
    curl 'https://<canvas>/api/v1/accounts/<account_id>/outcome_imports/outcomes_group_ids/<outcome_import_id>' \
        -H "Authorization: Bearer <token>"
    curl 'https://<canvas>/api/v1/courses/<course_id>/outcome_imports/outcome_group_ids/<outcome_import_id>' \
        -H "Authorization: Bearer <token>"

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
    api_instance = canvas_lms_python_client.OutcomeImportsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id

    try:
        # Get IDs of outcome groups created after successful import
        api_response = await api_instance.outcome_imports_api_created_group_ids_for_courses(course_id, id)
        print("The response of OutcomeImportsApiApi->outcome_imports_api_created_group_ids_for_courses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutcomeImportsApiApi->outcome_imports_api_created_group_ids_for_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 

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
**0** | array of outcome ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **outcome_imports_api_show**
> OutcomeImport outcome_imports_api_show(account_id, id)

Get Outcome import status

Get the status of an already created Outcome import. Pass 'latest' for the outcome import id
for the latest import.

  Examples:
    curl 'https://<canvas>/api/v1/accounts/<account_id>/outcome_imports/<outcome_import_id>' \
        -H "Authorization: Bearer <token>"
    curl 'https://<canvas>/api/v1/courses/<course_id>/outcome_imports/<outcome_import_id>' \
        -H "Authorization: Bearer <token>"

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.outcome_import import OutcomeImport
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
    api_instance = canvas_lms_python_client.OutcomeImportsApiApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id

    try:
        # Get Outcome import status
        api_response = await api_instance.outcome_imports_api_show(account_id, id)
        print("The response of OutcomeImportsApiApi->outcome_imports_api_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutcomeImportsApiApi->outcome_imports_api_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**OutcomeImport**](OutcomeImport.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | OutcomeImport |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **outcome_imports_api_show_for_courses**
> OutcomeImport outcome_imports_api_show_for_courses(course_id, id)

Get Outcome import status

Get the status of an already created Outcome import. Pass 'latest' for the outcome import id
for the latest import.

  Examples:
    curl 'https://<canvas>/api/v1/accounts/<account_id>/outcome_imports/<outcome_import_id>' \
        -H "Authorization: Bearer <token>"
    curl 'https://<canvas>/api/v1/courses/<course_id>/outcome_imports/<outcome_import_id>' \
        -H "Authorization: Bearer <token>"

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.outcome_import import OutcomeImport
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
    api_instance = canvas_lms_python_client.OutcomeImportsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id

    try:
        # Get Outcome import status
        api_response = await api_instance.outcome_imports_api_show_for_courses(course_id, id)
        print("The response of OutcomeImportsApiApi->outcome_imports_api_show_for_courses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutcomeImportsApiApi->outcome_imports_api_show_for_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**OutcomeImport**](OutcomeImport.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | OutcomeImport |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

