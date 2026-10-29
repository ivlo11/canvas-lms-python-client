# canvas_lms_python_client.ProfileApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**profile_profile_pics**](ProfileApi.md#profile_profile_pics) | **GET** /api/v1/users/{user_id}/avatars | List avatar options
[**profile_settings**](ProfileApi.md#profile_settings) | **GET** /api/v1/users/{user_id}/profile | Get user profile


# **profile_profile_pics**
> List[Avatar] profile_profile_pics(user_id)

List avatar options

A paginated list of the possible user avatar options that can be set with the user update endpoint. The response will be an array of avatar records. If the 'type' field is 'attachment', the record will include all the normal attachment json fields; otherwise it will include only the 'url' and 'display_name' fields. Additionally, all records will include a 'type' field and a 'token' field. The following explains each field in more detail
type:: ["gravatar"|"attachment"|"no_pic"] The type of avatar record, for categorization purposes.
url:: The url of the avatar
token:: A unique representation of the avatar record which can be used to set the avatar with the user update endpoint. Note: this is an internal representation and is subject to change without notice. It should be consumed with this api endpoint and used in the user update endpoint, and should not be constructed by the client.
display_name:: A textual description of the avatar record
id:: ['attachment' type only] the internal id of the attachment
content-type:: ['attachment' type only] the content-type of the attachment
filename:: ['attachment' type only] the filename of the attachment
size:: ['attachment' type only] the size of the attachment

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.avatar import Avatar
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
    api_instance = canvas_lms_python_client.ProfileApi(api_client)
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # List avatar options
        api_response = await api_instance.profile_profile_pics(user_id)
        print("The response of ProfileApi->profile_profile_pics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->profile_profile_pics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Scope response to user_id | 

### Return type

[**List[Avatar]**](Avatar.md)

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

# **profile_settings**
> Profile profile_settings(user_id, include=include)

Get user profile

Returns user profile data, including user id, name, and profile pic.

When requesting the profile for the user accessing the API, the user's
calendar feed URL and LTI user id will be returned as well.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.profile import Profile
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
    api_instance = canvas_lms_python_client.ProfileApi(api_client)
    user_id = 'user_id_example' # str | Scope response to user_id
    include = ['include_example'] # List[str] | Array of additional information to include.  \"links\":: include the user's profile links in the response           as an array of objects with +url+ and +title+ fields \"user_services\":: include names and links for the user's connected services \"uuid\":: include the user's uuid in the response (optional)

    try:
        # Get user profile
        api_response = await api_instance.profile_settings(user_id, include=include)
        print("The response of ProfileApi->profile_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->profile_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Scope response to user_id | 
 **include** | [**List[str]**](str.md)| Array of additional information to include.  \&quot;links\&quot;:: include the user&#39;s profile links in the response           as an array of objects with +url+ and +title+ fields \&quot;user_services\&quot;:: include names and links for the user&#39;s connected services \&quot;uuid\&quot;:: include the user&#39;s uuid in the response | [optional] 

### Return type

[**Profile**](Profile.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Profile |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

