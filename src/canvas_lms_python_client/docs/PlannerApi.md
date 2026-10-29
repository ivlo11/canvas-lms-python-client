# canvas_lms_python_client.PlannerApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**planner_index**](PlannerApi.md#planner_index) | **GET** /api/v1/planner/items | List planner items
[**planner_index_for_users**](PlannerApi.md#planner_index_for_users) | **GET** /api/v1/users/{user_id}/planner/items | List planner items


# **planner_index**
> planner_index(start_date=start_date, end_date=end_date, context_codes=context_codes, observed_user_id=observed_user_id, filter=filter, page=page, per_page=per_page)

List planner items

Retrieve the paginated list of objects to be shown on the planner for the
current user with the associated planner override to override an item's
visibility if set.

Planner items for a student may also be retrieved by a linked observer. Use
the path that accepts a user_id and supply the student's id.

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
    api_instance = canvas_lms_python_client.PlannerApi(api_client)
    start_date = 'start_date_example' # str | Only return items starting from the given date. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ. (optional)
    end_date = 'end_date_example' # str | Only return items up to the given date. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ. (optional)
    context_codes = ['context_codes_example'] # List[str] | List of context codes of courses and/or groups whose items you want to see. If not specified, defaults to all contexts associated to the current user. Note that concluded courses will be ignored unless specified in the includes[] parameter. The format of this field is the context type, followed by an underscore, followed by the context id. For example: course_42, group_123 (optional)
    observed_user_id = 'observed_user_id_example' # str | Return planner items for the given observed user. Must be accompanied by context_codes[]. The user making the request must be observing the observed user in all the courses specified by context_codes[]. (optional)
    filter = 'filter_example' # str | Only return items that are completed (includes items with planner_override.marked_complete = true or submitted assignments) (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List planner items
        await api_instance.planner_index(start_date=start_date, end_date=end_date, context_codes=context_codes, observed_user_id=observed_user_id, filter=filter, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling PlannerApi->planner_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**| Only return items starting from the given date. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ. | [optional] 
 **end_date** | **str**| Only return items up to the given date. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ. | [optional] 
 **context_codes** | [**List[str]**](str.md)| List of context codes of courses and/or groups whose items you want to see. If not specified, defaults to all contexts associated to the current user. Note that concluded courses will be ignored unless specified in the includes[] parameter. The format of this field is the context type, followed by an underscore, followed by the context id. For example: course_42, group_123 | [optional] 
 **observed_user_id** | **str**| Return planner items for the given observed user. Must be accompanied by context_codes[]. The user making the request must be observing the observed user in all the courses specified by context_codes[]. | [optional] 
 **filter** | **str**| Only return items that are completed (includes items with planner_override.marked_complete &#x3D; true or submitted assignments) | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

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
**0** | List planner items |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **planner_index_for_users**
> planner_index_for_users(user_id, start_date=start_date, end_date=end_date, context_codes=context_codes, observed_user_id=observed_user_id, filter=filter, page=page, per_page=per_page)

List planner items

Retrieve the paginated list of objects to be shown on the planner for the
current user with the associated planner override to override an item's
visibility if set.

Planner items for a student may also be retrieved by a linked observer. Use
the path that accepts a user_id and supply the student's id.

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
    api_instance = canvas_lms_python_client.PlannerApi(api_client)
    user_id = 'user_id_example' # str | Scope response to user_id
    start_date = 'start_date_example' # str | Only return items starting from the given date. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ. (optional)
    end_date = 'end_date_example' # str | Only return items up to the given date. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ. (optional)
    context_codes = ['context_codes_example'] # List[str] | List of context codes of courses and/or groups whose items you want to see. If not specified, defaults to all contexts associated to the current user. Note that concluded courses will be ignored unless specified in the includes[] parameter. The format of this field is the context type, followed by an underscore, followed by the context id. For example: course_42, group_123 (optional)
    observed_user_id = 'observed_user_id_example' # str | Return planner items for the given observed user. Must be accompanied by context_codes[]. The user making the request must be observing the observed user in all the courses specified by context_codes[]. (optional)
    filter = 'filter_example' # str | Only return items that are completed (includes items with planner_override.marked_complete = true or submitted assignments) (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List planner items
        await api_instance.planner_index_for_users(user_id, start_date=start_date, end_date=end_date, context_codes=context_codes, observed_user_id=observed_user_id, filter=filter, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling PlannerApi->planner_index_for_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Scope response to user_id | 
 **start_date** | **str**| Only return items starting from the given date. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ. | [optional] 
 **end_date** | **str**| Only return items up to the given date. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ. | [optional] 
 **context_codes** | [**List[str]**](str.md)| List of context codes of courses and/or groups whose items you want to see. If not specified, defaults to all contexts associated to the current user. Note that concluded courses will be ignored unless specified in the includes[] parameter. The format of this field is the context type, followed by an underscore, followed by the context id. For example: course_42, group_123 | [optional] 
 **observed_user_id** | **str**| Return planner items for the given observed user. Must be accompanied by context_codes[]. The user making the request must be observing the observed user in all the courses specified by context_codes[]. | [optional] 
 **filter** | **str**| Only return items that are completed (includes items with planner_override.marked_complete &#x3D; true or submitted assignments) | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

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
**0** | List planner items |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

