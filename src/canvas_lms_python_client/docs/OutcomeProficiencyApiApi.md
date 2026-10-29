# canvas_lms_python_client.OutcomeProficiencyApiApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**outcome_proficiency_api_create**](OutcomeProficiencyApiApi.md#outcome_proficiency_api_create) | **POST** /api/v1/accounts/{account_id}/outcome_proficiency | Create/update proficiency ratings
[**outcome_proficiency_api_create_for_courses**](OutcomeProficiencyApiApi.md#outcome_proficiency_api_create_for_courses) | **POST** /api/v1/courses/{course_id}/outcome_proficiency | Create/update proficiency ratings
[**outcome_proficiency_api_show**](OutcomeProficiencyApiApi.md#outcome_proficiency_api_show) | **GET** /api/v1/accounts/{account_id}/outcome_proficiency | Get proficiency ratings
[**outcome_proficiency_api_show_for_courses**](OutcomeProficiencyApiApi.md#outcome_proficiency_api_show_for_courses) | **GET** /api/v1/courses/{course_id}/outcome_proficiency | Get proficiency ratings


# **outcome_proficiency_api_create**
> Proficiency outcome_proficiency_api_create(account_id, outcome_proficiency_api_create_request=outcome_proficiency_api_create_request)

Create/update proficiency ratings

Create or update account-level proficiency ratings. These ratings will apply to all
sub-accounts, unless they have their own account-level proficiency ratings defined.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.outcome_proficiency_api_create_request import OutcomeProficiencyApiCreateRequest
from canvas_lms_python_client.models.proficiency import Proficiency
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
    api_instance = canvas_lms_python_client.OutcomeProficiencyApiApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    outcome_proficiency_api_create_request = canvas_lms_python_client.OutcomeProficiencyApiCreateRequest() # OutcomeProficiencyApiCreateRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/accounts/<account_id>/outcome_proficiency' \\      -X POST \\      -F 'ratings[][description]=Exceeds Mastery' \\      -F 'ratings[][points]=4' \\      -F 'ratings[][color]=02672D' \\      -F 'ratings[][mastery]=false' \\      -F 'ratings[][description]=Mastery' \\      -F 'ratings[][points]=3' \\      -F 'ratings[][color]=03893D' \\      -F 'ratings[][mastery]=true' \\      -F 'ratings[][description]=Near Mastery' \\      -F 'ratings[][points]=2' \\      -F 'ratings[][color]=FAB901' \\      -F 'ratings[][mastery]=false' \\      -F 'ratings[][description]=Below Mastery' \\      -F 'ratings[][points]=1' \\      -F 'ratings[][color]=FD5D10' \\      -F 'ratings[][mastery]=false' \\      -F 'ratings[][description]=Well Below Mastery' \\      -F 'ratings[][points]=0' \\      -F 'ratings[][color]=E62429' \\      -F 'ratings[][mastery]=false' \\      -H \"Authorization: Bearer <token>\" ``` (optional)

    try:
        # Create/update proficiency ratings
        api_response = await api_instance.outcome_proficiency_api_create(account_id, outcome_proficiency_api_create_request=outcome_proficiency_api_create_request)
        print("The response of OutcomeProficiencyApiApi->outcome_proficiency_api_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutcomeProficiencyApiApi->outcome_proficiency_api_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **outcome_proficiency_api_create_request** | [**OutcomeProficiencyApiCreateRequest**](OutcomeProficiencyApiCreateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/accounts/&lt;account_id&gt;/outcome_proficiency&#39; \\      -X POST \\      -F &#39;ratings[][description]&#x3D;Exceeds Mastery&#39; \\      -F &#39;ratings[][points]&#x3D;4&#39; \\      -F &#39;ratings[][color]&#x3D;02672D&#39; \\      -F &#39;ratings[][mastery]&#x3D;false&#39; \\      -F &#39;ratings[][description]&#x3D;Mastery&#39; \\      -F &#39;ratings[][points]&#x3D;3&#39; \\      -F &#39;ratings[][color]&#x3D;03893D&#39; \\      -F &#39;ratings[][mastery]&#x3D;true&#39; \\      -F &#39;ratings[][description]&#x3D;Near Mastery&#39; \\      -F &#39;ratings[][points]&#x3D;2&#39; \\      -F &#39;ratings[][color]&#x3D;FAB901&#39; \\      -F &#39;ratings[][mastery]&#x3D;false&#39; \\      -F &#39;ratings[][description]&#x3D;Below Mastery&#39; \\      -F &#39;ratings[][points]&#x3D;1&#39; \\      -F &#39;ratings[][color]&#x3D;FD5D10&#39; \\      -F &#39;ratings[][mastery]&#x3D;false&#39; \\      -F &#39;ratings[][description]&#x3D;Well Below Mastery&#39; \\      -F &#39;ratings[][points]&#x3D;0&#39; \\      -F &#39;ratings[][color]&#x3D;E62429&#39; \\      -F &#39;ratings[][mastery]&#x3D;false&#39; \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**Proficiency**](Proficiency.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Proficiency |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **outcome_proficiency_api_create_for_courses**
> Proficiency outcome_proficiency_api_create_for_courses(course_id, outcome_proficiency_api_create_request=outcome_proficiency_api_create_request)

Create/update proficiency ratings

Create or update account-level proficiency ratings. These ratings will apply to all
sub-accounts, unless they have their own account-level proficiency ratings defined.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.outcome_proficiency_api_create_request import OutcomeProficiencyApiCreateRequest
from canvas_lms_python_client.models.proficiency import Proficiency
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
    api_instance = canvas_lms_python_client.OutcomeProficiencyApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    outcome_proficiency_api_create_request = canvas_lms_python_client.OutcomeProficiencyApiCreateRequest() # OutcomeProficiencyApiCreateRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/accounts/<account_id>/outcome_proficiency' \\      -X POST \\      -F 'ratings[][description]=Exceeds Mastery' \\      -F 'ratings[][points]=4' \\      -F 'ratings[][color]=02672D' \\      -F 'ratings[][mastery]=false' \\      -F 'ratings[][description]=Mastery' \\      -F 'ratings[][points]=3' \\      -F 'ratings[][color]=03893D' \\      -F 'ratings[][mastery]=true' \\      -F 'ratings[][description]=Near Mastery' \\      -F 'ratings[][points]=2' \\      -F 'ratings[][color]=FAB901' \\      -F 'ratings[][mastery]=false' \\      -F 'ratings[][description]=Below Mastery' \\      -F 'ratings[][points]=1' \\      -F 'ratings[][color]=FD5D10' \\      -F 'ratings[][mastery]=false' \\      -F 'ratings[][description]=Well Below Mastery' \\      -F 'ratings[][points]=0' \\      -F 'ratings[][color]=E62429' \\      -F 'ratings[][mastery]=false' \\      -H \"Authorization: Bearer <token>\" ``` (optional)

    try:
        # Create/update proficiency ratings
        api_response = await api_instance.outcome_proficiency_api_create_for_courses(course_id, outcome_proficiency_api_create_request=outcome_proficiency_api_create_request)
        print("The response of OutcomeProficiencyApiApi->outcome_proficiency_api_create_for_courses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutcomeProficiencyApiApi->outcome_proficiency_api_create_for_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **outcome_proficiency_api_create_request** | [**OutcomeProficiencyApiCreateRequest**](OutcomeProficiencyApiCreateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/accounts/&lt;account_id&gt;/outcome_proficiency&#39; \\      -X POST \\      -F &#39;ratings[][description]&#x3D;Exceeds Mastery&#39; \\      -F &#39;ratings[][points]&#x3D;4&#39; \\      -F &#39;ratings[][color]&#x3D;02672D&#39; \\      -F &#39;ratings[][mastery]&#x3D;false&#39; \\      -F &#39;ratings[][description]&#x3D;Mastery&#39; \\      -F &#39;ratings[][points]&#x3D;3&#39; \\      -F &#39;ratings[][color]&#x3D;03893D&#39; \\      -F &#39;ratings[][mastery]&#x3D;true&#39; \\      -F &#39;ratings[][description]&#x3D;Near Mastery&#39; \\      -F &#39;ratings[][points]&#x3D;2&#39; \\      -F &#39;ratings[][color]&#x3D;FAB901&#39; \\      -F &#39;ratings[][mastery]&#x3D;false&#39; \\      -F &#39;ratings[][description]&#x3D;Below Mastery&#39; \\      -F &#39;ratings[][points]&#x3D;1&#39; \\      -F &#39;ratings[][color]&#x3D;FD5D10&#39; \\      -F &#39;ratings[][mastery]&#x3D;false&#39; \\      -F &#39;ratings[][description]&#x3D;Well Below Mastery&#39; \\      -F &#39;ratings[][points]&#x3D;0&#39; \\      -F &#39;ratings[][color]&#x3D;E62429&#39; \\      -F &#39;ratings[][mastery]&#x3D;false&#39; \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**Proficiency**](Proficiency.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Proficiency |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **outcome_proficiency_api_show**
> Proficiency outcome_proficiency_api_show(account_id)

Get proficiency ratings

Get account-level proficiency ratings. If not defined for this account,
it will return proficiency ratings for the nearest super-account with ratings defined.
Will return 404 if none found.

  Examples:
    curl https://<canvas>/api/v1/accounts/<account_id>/outcome_proficiency \
        -H 'Authorization: Bearer <token>'

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.proficiency import Proficiency
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
    api_instance = canvas_lms_python_client.OutcomeProficiencyApiApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id

    try:
        # Get proficiency ratings
        api_response = await api_instance.outcome_proficiency_api_show(account_id)
        print("The response of OutcomeProficiencyApiApi->outcome_proficiency_api_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutcomeProficiencyApiApi->outcome_proficiency_api_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 

### Return type

[**Proficiency**](Proficiency.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Proficiency |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **outcome_proficiency_api_show_for_courses**
> Proficiency outcome_proficiency_api_show_for_courses(course_id)

Get proficiency ratings

Get account-level proficiency ratings. If not defined for this account,
it will return proficiency ratings for the nearest super-account with ratings defined.
Will return 404 if none found.

  Examples:
    curl https://<canvas>/api/v1/accounts/<account_id>/outcome_proficiency \
        -H 'Authorization: Bearer <token>'

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.proficiency import Proficiency
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
    api_instance = canvas_lms_python_client.OutcomeProficiencyApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id

    try:
        # Get proficiency ratings
        api_response = await api_instance.outcome_proficiency_api_show_for_courses(course_id)
        print("The response of OutcomeProficiencyApiApi->outcome_proficiency_api_show_for_courses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutcomeProficiencyApiApi->outcome_proficiency_api_show_for_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 

### Return type

[**Proficiency**](Proficiency.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Proficiency |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

