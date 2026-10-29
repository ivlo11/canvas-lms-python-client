# canvas_lms_python_client.HistoryApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**history_index**](HistoryApi.md#history_index) | **GET** /api/v1/users/{user_id}/history | List recent history for a user


# **history_index**
> List[HistoryEntry] history_index(user_id, page=page, per_page=per_page)

List recent history for a user

Return a paginated list of the user's recent history. History entries are returned in descending order,
newest to oldest. You may list history entries for yourself (use +self+ as the user_id), for a student you observe,
or for a user you manage as an administrator. Note that the +per_page+ pagination argument is not supported
and the number of history entries returned per page will vary.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.history_entry import HistoryEntry
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
    api_instance = canvas_lms_python_client.HistoryApi(api_client)
    user_id = 'user_id_example' # str | Scope response to user_id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List recent history for a user
        api_response = await api_instance.history_index(user_id, page=page, per_page=per_page)
        print("The response of HistoryApi->history_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HistoryApi->history_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Scope response to user_id | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[HistoryEntry]**](HistoryEntry.md)

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

