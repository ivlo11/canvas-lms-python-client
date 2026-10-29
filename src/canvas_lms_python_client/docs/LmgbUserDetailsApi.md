# canvas_lms_python_client.LmgbUserDetailsApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lmgb_user_details_show**](LmgbUserDetailsApi.md#lmgb_user_details_show) | **GET** /api/v1/courses/{course_id}/users/{id}/lmgb_user_details | Get LMGB user details


# **lmgb_user_details_show**
> object lmgb_user_details_show(course_id, id)

Get LMGB user details

Returns details about a user in the context of a course for LMGB

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
    api_instance = canvas_lms_python_client.LmgbUserDetailsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | The ID of the user to retrieve details for

    try:
        # Get LMGB user details
        api_response = await api_instance.lmgb_user_details_show(course_id, id)
        print("The response of LmgbUserDetailsApi->lmgb_user_details_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LmgbUserDetailsApi->lmgb_user_details_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| The ID of the user to retrieve details for | 

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
**0** | LmgbUserDetails |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

