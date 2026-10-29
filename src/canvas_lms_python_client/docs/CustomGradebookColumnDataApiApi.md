# canvas_lms_python_client.CustomGradebookColumnDataApiApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**custom_gradebook_column_data_api_bulk_update**](CustomGradebookColumnDataApiApi.md#custom_gradebook_column_data_api_bulk_update) | **PUT** /api/v1/courses/{course_id}/custom_gradebook_column_data | Bulk update column data
[**custom_gradebook_column_data_api_index**](CustomGradebookColumnDataApiApi.md#custom_gradebook_column_data_api_index) | **GET** /api/v1/courses/{course_id}/custom_gradebook_columns/{id}/data | List entries for a column
[**custom_gradebook_column_data_api_update**](CustomGradebookColumnDataApiApi.md#custom_gradebook_column_data_api_update) | **PUT** /api/v1/courses/{course_id}/custom_gradebook_columns/{id}/data/{user_id} | Update column data


# **custom_gradebook_column_data_api_bulk_update**
> Progress custom_gradebook_column_data_api_bulk_update(course_id, custom_gradebook_column_data_api_bulk_update_request=custom_gradebook_column_data_api_bulk_update_request)

Bulk update column data

Set the content of custom columns

{
  "column_data": [
    {
      "column_id": example_column_id,
      "user_id": example_student_id,
      "content": example_content
      },
      {
      "column_id": example_column_id,
      "user_id": example_student_id,
      "content: example_content
    }
  ]
}

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.custom_gradebook_column_data_api_bulk_update_request import CustomGradebookColumnDataApiBulkUpdateRequest
from canvas_lms_python_client.models.progress import Progress
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
    api_instance = canvas_lms_python_client.CustomGradebookColumnDataApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    custom_gradebook_column_data_api_bulk_update_request = canvas_lms_python_client.CustomGradebookColumnDataApiBulkUpdateRequest() # CustomGradebookColumnDataApiBulkUpdateRequest | Request body parameters (optional)

    try:
        # Bulk update column data
        api_response = await api_instance.custom_gradebook_column_data_api_bulk_update(course_id, custom_gradebook_column_data_api_bulk_update_request=custom_gradebook_column_data_api_bulk_update_request)
        print("The response of CustomGradebookColumnDataApiApi->custom_gradebook_column_data_api_bulk_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomGradebookColumnDataApiApi->custom_gradebook_column_data_api_bulk_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **custom_gradebook_column_data_api_bulk_update_request** | [**CustomGradebookColumnDataApiBulkUpdateRequest**](CustomGradebookColumnDataApiBulkUpdateRequest.md)| Request body parameters | [optional] 

### Return type

[**Progress**](Progress.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Progress |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_gradebook_column_data_api_index**
> List[ColumnDatum] custom_gradebook_column_data_api_index(course_id, id, include_hidden=include_hidden, page=page, per_page=per_page)

List entries for a column

This does not list entries for students without associated data.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.column_datum import ColumnDatum
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
    api_instance = canvas_lms_python_client.CustomGradebookColumnDataApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    include_hidden = True # bool | If true, hidden columns will be included in the result. If false or absent, only visible columns will be returned. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List entries for a column
        api_response = await api_instance.custom_gradebook_column_data_api_index(course_id, id, include_hidden=include_hidden, page=page, per_page=per_page)
        print("The response of CustomGradebookColumnDataApiApi->custom_gradebook_column_data_api_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomGradebookColumnDataApiApi->custom_gradebook_column_data_api_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **include_hidden** | **bool**| If true, hidden columns will be included in the result. If false or absent, only visible columns will be returned. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[ColumnDatum]**](ColumnDatum.md)

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

# **custom_gradebook_column_data_api_update**
> ColumnDatum custom_gradebook_column_data_api_update(course_id, id, user_id, custom_gradebook_column_data_api_update_request=custom_gradebook_column_data_api_update_request)

Update column data

Set the content of a custom column

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.column_datum import ColumnDatum
from canvas_lms_python_client.models.custom_gradebook_column_data_api_update_request import CustomGradebookColumnDataApiUpdateRequest
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
    api_instance = canvas_lms_python_client.CustomGradebookColumnDataApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    user_id = 'user_id_example' # str | Scope response to user_id
    custom_gradebook_column_data_api_update_request = canvas_lms_python_client.CustomGradebookColumnDataApiUpdateRequest() # CustomGradebookColumnDataApiUpdateRequest | Request body parameters (optional)

    try:
        # Update column data
        api_response = await api_instance.custom_gradebook_column_data_api_update(course_id, id, user_id, custom_gradebook_column_data_api_update_request=custom_gradebook_column_data_api_update_request)
        print("The response of CustomGradebookColumnDataApiApi->custom_gradebook_column_data_api_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomGradebookColumnDataApiApi->custom_gradebook_column_data_api_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **user_id** | **str**| Scope response to user_id | 
 **custom_gradebook_column_data_api_update_request** | [**CustomGradebookColumnDataApiUpdateRequest**](CustomGradebookColumnDataApiUpdateRequest.md)| Request body parameters | [optional] 

### Return type

[**ColumnDatum**](ColumnDatum.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ColumnDatum |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

