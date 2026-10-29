# canvas_lms_python_client.AccessibilityCourseStatisticsApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accessibility_course_statistics_index**](AccessibilityCourseStatisticsApi.md#accessibility_course_statistics_index) | **GET** /api/v1/users/{user_id}/educator_accessibility_course_statistics | List accessibility course statistics


# **accessibility_course_statistics_index**
> List[AccessibilityCourseStatistic] accessibility_course_statistics_index(user_id, page=page, per_page=per_page)

List accessibility course statistics

Returns per-course accessibility issue statistics for the current user's
active teacher and designer courses. Only courses where the accessibility
checker is enabled and whose workflow state is neither completed nor deleted
are included. Only statistic records with workflow_state "active" are returned.

Requires the educator_dashboard feature flag to be enabled on the root
account, and a11y_checker_account_statistics on site admin plus a11y_checker
on the account (i.e. a11y_checker_account_statistics? must be true).

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.accessibility_course_statistic import AccessibilityCourseStatistic
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
    api_instance = canvas_lms_python_client.AccessibilityCourseStatisticsApi(api_client)
    user_id = 'user_id_example' # str | The ID of the user, or \"self\" for the current user. The requesting user may only retrieve their own statistics.
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List accessibility course statistics
        api_response = await api_instance.accessibility_course_statistics_index(user_id, page=page, per_page=per_page)
        print("The response of AccessibilityCourseStatisticsApi->accessibility_course_statistics_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessibilityCourseStatisticsApi->accessibility_course_statistics_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the user, or \&quot;self\&quot; for the current user. The requesting user may only retrieve their own statistics. | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[AccessibilityCourseStatistic]**](AccessibilityCourseStatistic.md)

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

