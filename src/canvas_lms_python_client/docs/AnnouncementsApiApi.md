# canvas_lms_python_client.AnnouncementsApiApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**announcements_api_index**](AnnouncementsApiApi.md#announcements_api_index) | **GET** /api/v1/announcements | List announcements


# **announcements_api_index**
> List[DiscussionTopic] announcements_api_index(context_codes, start_date=start_date, end_date=end_date, available_after=available_after, active_only=active_only, latest_only=latest_only, include=include, page=page, per_page=per_page)

List announcements

Returns the paginated list of announcements for the given courses and date range.  Note that
a +context_code+ field is added to the responses so you can tell which course each announcement
belongs to.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.discussion_topic import DiscussionTopic
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
    api_instance = canvas_lms_python_client.AnnouncementsApiApi(api_client)
    context_codes = ['context_codes_example'] # List[str] | List of context_codes to retrieve announcements for (for example, +course_123+). Only courses are presently supported. The call will fail unless the caller has View Announcements permission in all listed courses.
    start_date = 'start_date_example' # str | Only return announcements posted since the start_date (inclusive). Defaults to 14 days ago. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ. (optional)
    end_date = 'end_date_example' # str | Only return announcements posted before the end_date (inclusive). Defaults to 28 days from start_date. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ. Announcements scheduled for future posting will only be returned to course administrators. (optional)
    available_after = 'available_after_example' # str | Only return announcements having locked_at nil or after available_after (exclusive). The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ. Effective only for students (who don't have moderate forum right). (optional)
    active_only = True # bool | Only return active announcements that have been published. Applies only to requesting users that have permission to view unpublished items. Defaults to false for users with access to view unpublished items, otherwise true and unmodifiable. (optional)
    latest_only = True # bool | Only return the latest announcement for each associated context. The response will include at most one announcement for each specified context in the context_codes[] parameter. Defaults to false. (optional)
    include = ['include_example'] # List[str] | Optional list of resources to include with the response. May include a string of the name of the resource. Possible values are: \"sections\", \"sections_user_count\" if \"sections\" is passed, includes the course sections that are associated with the topic, if the topic is specific to certain sections of the course. If \"sections_user_count\" is passed, then:   (a) If sections were asked for *and* the topic is specific to certain       course sections sections, includes the number of users in each       section. (as part of the section json asked for above)   (b) Else, includes at the root level the total number of users in the       topic's context (group or course) that the topic applies to. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List announcements
        api_response = await api_instance.announcements_api_index(context_codes, start_date=start_date, end_date=end_date, available_after=available_after, active_only=active_only, latest_only=latest_only, include=include, page=page, per_page=per_page)
        print("The response of AnnouncementsApiApi->announcements_api_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnnouncementsApiApi->announcements_api_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context_codes** | [**List[str]**](str.md)| List of context_codes to retrieve announcements for (for example, +course_123+). Only courses are presently supported. The call will fail unless the caller has View Announcements permission in all listed courses. | 
 **start_date** | **str**| Only return announcements posted since the start_date (inclusive). Defaults to 14 days ago. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ. | [optional] 
 **end_date** | **str**| Only return announcements posted before the end_date (inclusive). Defaults to 28 days from start_date. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ. Announcements scheduled for future posting will only be returned to course administrators. | [optional] 
 **available_after** | **str**| Only return announcements having locked_at nil or after available_after (exclusive). The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ. Effective only for students (who don&#39;t have moderate forum right). | [optional] 
 **active_only** | **bool**| Only return active announcements that have been published. Applies only to requesting users that have permission to view unpublished items. Defaults to false for users with access to view unpublished items, otherwise true and unmodifiable. | [optional] 
 **latest_only** | **bool**| Only return the latest announcement for each associated context. The response will include at most one announcement for each specified context in the context_codes[] parameter. Defaults to false. | [optional] 
 **include** | [**List[str]**](str.md)| Optional list of resources to include with the response. May include a string of the name of the resource. Possible values are: \&quot;sections\&quot;, \&quot;sections_user_count\&quot; if \&quot;sections\&quot; is passed, includes the course sections that are associated with the topic, if the topic is specific to certain sections of the course. If \&quot;sections_user_count\&quot; is passed, then:   (a) If sections were asked for *and* the topic is specific to certain       course sections sections, includes the number of users in each       section. (as part of the section json asked for above)   (b) Else, includes at the root level the total number of users in the       topic&#39;s context (group or course) that the topic applies to. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[DiscussionTopic]**](DiscussionTopic.md)

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

