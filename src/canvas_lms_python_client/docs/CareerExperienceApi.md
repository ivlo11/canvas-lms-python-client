# canvas_lms_python_client.CareerExperienceApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**career_experience_enabled**](CareerExperienceApi.md#career_experience_enabled) | **GET** /api/v1/career/enabled | Check if Canvas Career is enabled
[**career_experience_experience_summary**](CareerExperienceApi.md#career_experience_experience_summary) | **GET** /api/v1/career/experience_summary | Get current and available experiences
[**career_experience_switch_experience**](CareerExperienceApi.md#career_experience_switch_experience) | **POST** /api/v1/career/switch_experience | Switch experience
[**career_experience_switch_role**](CareerExperienceApi.md#career_experience_switch_role) | **POST** /api/v1/career/switch_role | Switch role


# **career_experience_enabled**
> List[object] career_experience_enabled()

Check if Canvas Career is enabled

Returns whether the root account has Canvas Career (Horizon) enabled
in at least one subaccount.

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
    api_instance = canvas_lms_python_client.CareerExperienceApi(api_client)

    try:
        # Check if Canvas Career is enabled
        api_response = await api_instance.career_experience_enabled()
        print("The response of CareerExperienceApi->career_experience_enabled:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CareerExperienceApi->career_experience_enabled: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[object]**

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

# **career_experience_experience_summary**
> ExperienceSummary career_experience_experience_summary()

Get current and available experiences

Returns the current user's active experience and available experiences
they can switch to.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.experience_summary import ExperienceSummary
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
    api_instance = canvas_lms_python_client.CareerExperienceApi(api_client)

    try:
        # Get current and available experiences
        api_response = await api_instance.career_experience_experience_summary()
        print("The response of CareerExperienceApi->career_experience_experience_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CareerExperienceApi->career_experience_experience_summary: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ExperienceSummary**](ExperienceSummary.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ExperienceSummary |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **career_experience_switch_experience**
> List[object] career_experience_switch_experience(career_experience_switch_experience_request=career_experience_switch_experience_request)

Switch experience

Switch the current user's active experience to the specified one.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.career_experience_switch_experience_request import CareerExperienceSwitchExperienceRequest
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
    api_instance = canvas_lms_python_client.CareerExperienceApi(api_client)
    career_experience_switch_experience_request = canvas_lms_python_client.CareerExperienceSwitchExperienceRequest() # CareerExperienceSwitchExperienceRequest | Request body parameters  **Example Request:** ``` curl -X POST https://<canvas>/api/v1/career/switch_experience \\   -H 'Authorization: Bearer <token>' \\   -d 'experience=academic' ``` (optional)

    try:
        # Switch experience
        api_response = await api_instance.career_experience_switch_experience(career_experience_switch_experience_request=career_experience_switch_experience_request)
        print("The response of CareerExperienceApi->career_experience_switch_experience:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CareerExperienceApi->career_experience_switch_experience: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **career_experience_switch_experience_request** | [**CareerExperienceSwitchExperienceRequest**](CareerExperienceSwitchExperienceRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl -X POST https://&lt;canvas&gt;/api/v1/career/switch_experience \\   -H &#39;Authorization: Bearer &lt;token&gt;&#39; \\   -d &#39;experience&#x3D;academic&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

**List[object]**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | The newly set experience |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **career_experience_switch_role**
> List[object] career_experience_switch_role(career_experience_switch_role_request=career_experience_switch_role_request)

Switch role

Switch the current user's role within the current experience.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.career_experience_switch_role_request import CareerExperienceSwitchRoleRequest
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
    api_instance = canvas_lms_python_client.CareerExperienceApi(api_client)
    career_experience_switch_role_request = canvas_lms_python_client.CareerExperienceSwitchRoleRequest() # CareerExperienceSwitchRoleRequest | Request body parameters  **Example Request:** ``` curl -X POST https://<canvas>/api/v1/career/switch_role \\   -H 'Authorization: Bearer <token>' \\   -d 'role=learner' ``` (optional)

    try:
        # Switch role
        api_response = await api_instance.career_experience_switch_role(career_experience_switch_role_request=career_experience_switch_role_request)
        print("The response of CareerExperienceApi->career_experience_switch_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CareerExperienceApi->career_experience_switch_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **career_experience_switch_role_request** | [**CareerExperienceSwitchRoleRequest**](CareerExperienceSwitchRoleRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl -X POST https://&lt;canvas&gt;/api/v1/career/switch_role \\   -H &#39;Authorization: Bearer &lt;token&gt;&#39; \\   -d &#39;role&#x3D;learner&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

**List[object]**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | The newly set role |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

