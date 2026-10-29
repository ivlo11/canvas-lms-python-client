# canvas_lms_python_client.AssignmentOverridesApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assignment_overrides_batch_create**](AssignmentOverridesApi.md#assignment_overrides_batch_create) | **POST** /api/v1/courses/{course_id}/assignments/overrides | Batch create overrides in a course
[**assignment_overrides_batch_retrieve**](AssignmentOverridesApi.md#assignment_overrides_batch_retrieve) | **GET** /api/v1/courses/{course_id}/assignments/overrides | Batch retrieve overrides in a course
[**assignment_overrides_batch_update**](AssignmentOverridesApi.md#assignment_overrides_batch_update) | **PUT** /api/v1/courses/{course_id}/assignments/overrides | Batch update overrides in a course
[**assignment_overrides_create**](AssignmentOverridesApi.md#assignment_overrides_create) | **POST** /api/v1/courses/{course_id}/assignments/{assignment_id}/overrides | Create an assignment override
[**assignment_overrides_destroy**](AssignmentOverridesApi.md#assignment_overrides_destroy) | **DELETE** /api/v1/courses/{course_id}/assignments/{assignment_id}/overrides/{id} | Delete an assignment override
[**assignment_overrides_group_alias**](AssignmentOverridesApi.md#assignment_overrides_group_alias) | **GET** /api/v1/groups/{group_id}/assignments/{assignment_id}/override | Redirect to the assignment override for a group
[**assignment_overrides_index**](AssignmentOverridesApi.md#assignment_overrides_index) | **GET** /api/v1/courses/{course_id}/assignments/{assignment_id}/overrides | List assignment overrides
[**assignment_overrides_section_alias**](AssignmentOverridesApi.md#assignment_overrides_section_alias) | **GET** /api/v1/sections/{course_section_id}/assignments/{assignment_id}/override | Redirect to the assignment override for a section
[**assignment_overrides_show**](AssignmentOverridesApi.md#assignment_overrides_show) | **GET** /api/v1/courses/{course_id}/assignments/{assignment_id}/overrides/{id} | Get a single assignment override
[**assignment_overrides_update**](AssignmentOverridesApi.md#assignment_overrides_update) | **PUT** /api/v1/courses/{course_id}/assignments/{assignment_id}/overrides/{id} | Update an assignment override


# **assignment_overrides_batch_create**
> List[AssignmentOverride] assignment_overrides_batch_create(course_id, assignment_overrides_batch_create_request=assignment_overrides_batch_create_request)

Batch create overrides in a course

Creates the specified overrides for each assignment.  Handles creation in a
transaction, so all records are created or none are.

One of student_ids, group_id, or course_section_id must be present. At most
one should be present; if multiple are present only the most specific
(student_ids first, then group_id, then course_section_id) is used and any
others are ignored.

Errors are reported in an errors attribute, an array of errors corresponding
to inputs.  Global errors will be reported as a single element errors array

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.assignment_override import AssignmentOverride
from canvas_lms_python_client.models.assignment_overrides_batch_create_request import AssignmentOverridesBatchCreateRequest
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
    api_instance = canvas_lms_python_client.AssignmentOverridesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    assignment_overrides_batch_create_request = canvas_lms_python_client.AssignmentOverridesBatchCreateRequest() # AssignmentOverridesBatchCreateRequest | Request body parameters  **Example Request:** ``` curl \"https://<canvas>/api/v1/courses/12/assignments/overrides.json\" \\      -X POST \\      -F \"assignment_overrides[][assignment_id]=109\" \\      -F 'assignment_overrides[][student_ids][]=8' \\      -F \"assignment_overrides[][title]=foo\" \\      -F \"assignment_overrides[][assignment_id]=13\" \\      -F \"assignment_overrides[][course_section_id]=200\" \\      -F \"assignment_overrides[][due_at]=2012-10-08T21:00:00Z\" \\      -H \"Authorization: Bearer <token>\" ``` (optional)

    try:
        # Batch create overrides in a course
        api_response = await api_instance.assignment_overrides_batch_create(course_id, assignment_overrides_batch_create_request=assignment_overrides_batch_create_request)
        print("The response of AssignmentOverridesApi->assignment_overrides_batch_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssignmentOverridesApi->assignment_overrides_batch_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **assignment_overrides_batch_create_request** | [**AssignmentOverridesBatchCreateRequest**](AssignmentOverridesBatchCreateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl \&quot;https://&lt;canvas&gt;/api/v1/courses/12/assignments/overrides.json\&quot; \\      -X POST \\      -F \&quot;assignment_overrides[][assignment_id]&#x3D;109\&quot; \\      -F &#39;assignment_overrides[][student_ids][]&#x3D;8&#39; \\      -F \&quot;assignment_overrides[][title]&#x3D;foo\&quot; \\      -F \&quot;assignment_overrides[][assignment_id]&#x3D;13\&quot; \\      -F \&quot;assignment_overrides[][course_section_id]&#x3D;200\&quot; \\      -F \&quot;assignment_overrides[][due_at]&#x3D;2012-10-08T21:00:00Z\&quot; \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**List[AssignmentOverride]**](AssignmentOverride.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assignment_overrides_batch_retrieve**
> List[AssignmentOverride] assignment_overrides_batch_retrieve(course_id, assignment_overrides_id, assignment_overrides_assignment_id)

Batch retrieve overrides in a course

Returns a list of specified overrides in this course, providing
they target sections/groups/students visible to the current user.
Returns null elements in the list for requests that were not found.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.assignment_override import AssignmentOverride
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
    api_instance = canvas_lms_python_client.AssignmentOverridesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    assignment_overrides_id = 'assignment_overrides_id_example' # str | Ids of overrides to retrieve
    assignment_overrides_assignment_id = 'assignment_overrides_assignment_id_example' # str | Ids of assignments for each override

    try:
        # Batch retrieve overrides in a course
        api_response = await api_instance.assignment_overrides_batch_retrieve(course_id, assignment_overrides_id, assignment_overrides_assignment_id)
        print("The response of AssignmentOverridesApi->assignment_overrides_batch_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssignmentOverridesApi->assignment_overrides_batch_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **assignment_overrides_id** | **str**| Ids of overrides to retrieve | 
 **assignment_overrides_assignment_id** | **str**| Ids of assignments for each override | 

### Return type

[**List[AssignmentOverride]**](AssignmentOverride.md)

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

# **assignment_overrides_batch_update**
> List[AssignmentOverride] assignment_overrides_batch_update(course_id, assignment_overrides_batch_update_request=assignment_overrides_batch_update_request)

Batch update overrides in a course

Updates a list of specified overrides for each assignment.  Handles overrides
in a transaction, so either all updates are applied or none.
See {api:AssignmentOverridesController#update Update an assignment override} for
available attributes.

All current overridden values must be supplied if they are to be retained;
e.g. if due_at was overridden, but this PUT omits a value for due_at,
due_at will no longer be overridden. If the override is adhoc and
student_ids is not supplied, the target override set is unchanged. Target
override sets cannot be changed for group or section overrides.

Errors are reported in an errors attribute, an array of errors corresponding
to inputs.  Global errors will be reported as a single element errors array

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.assignment_override import AssignmentOverride
from canvas_lms_python_client.models.assignment_overrides_batch_update_request import AssignmentOverridesBatchUpdateRequest
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
    api_instance = canvas_lms_python_client.AssignmentOverridesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    assignment_overrides_batch_update_request = canvas_lms_python_client.AssignmentOverridesBatchUpdateRequest() # AssignmentOverridesBatchUpdateRequest | Request body parameters  **Example Request:** ``` curl \"https://<canvas>/api/v1/courses/12/assignments/overrides.json\" \\      -X PUT \\      -F \"assignment_overrides[][id]=122\" \\      -F \"assignment_overrides[][assignment_id]=109\" \\      -F \"assignment_overrides[][title]=foo\" \\      -F \"assignment_overrides[][id]=993\" \\      -F \"assignment_overrides[][assignment_id]=13\" \\      -F \"assignment_overrides[][due_at]=2012-10-08T21:00:00Z\" \\      -H \"Authorization: Bearer <token>\" ``` (optional)

    try:
        # Batch update overrides in a course
        api_response = await api_instance.assignment_overrides_batch_update(course_id, assignment_overrides_batch_update_request=assignment_overrides_batch_update_request)
        print("The response of AssignmentOverridesApi->assignment_overrides_batch_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssignmentOverridesApi->assignment_overrides_batch_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **assignment_overrides_batch_update_request** | [**AssignmentOverridesBatchUpdateRequest**](AssignmentOverridesBatchUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl \&quot;https://&lt;canvas&gt;/api/v1/courses/12/assignments/overrides.json\&quot; \\      -X PUT \\      -F \&quot;assignment_overrides[][id]&#x3D;122\&quot; \\      -F \&quot;assignment_overrides[][assignment_id]&#x3D;109\&quot; \\      -F \&quot;assignment_overrides[][title]&#x3D;foo\&quot; \\      -F \&quot;assignment_overrides[][id]&#x3D;993\&quot; \\      -F \&quot;assignment_overrides[][assignment_id]&#x3D;13\&quot; \\      -F \&quot;assignment_overrides[][due_at]&#x3D;2012-10-08T21:00:00Z\&quot; \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**List[AssignmentOverride]**](AssignmentOverride.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assignment_overrides_create**
> AssignmentOverride assignment_overrides_create(assignment_id, course_id, assignment_overrides_create_request=assignment_overrides_create_request)

Create an assignment override

One of student_ids, group_id, or course_section_id must be present. At most
one should be present; if multiple are present only the most specific
(student_ids first, then group_id, then course_section_id) is used and any
others are ignored.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.assignment_override import AssignmentOverride
from canvas_lms_python_client.models.assignment_overrides_create_request import AssignmentOverridesCreateRequest
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
    api_instance = canvas_lms_python_client.AssignmentOverridesApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    course_id = 'course_id_example' # str | Scope response to course_id
    assignment_overrides_create_request = canvas_lms_python_client.AssignmentOverridesCreateRequest() # AssignmentOverridesCreateRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/courses/1/assignments/2/overrides.json' \\      -X POST \\      -F 'assignment_override[student_ids][]=8' \\      -F 'assignment_override[title]=Fred Flinstone' \\      -F 'assignment_override[due_at]=2012-10-08T21:00:00Z' \\      -H \"Authorization: Bearer <token>\" ``` (optional)

    try:
        # Create an assignment override
        api_response = await api_instance.assignment_overrides_create(assignment_id, course_id, assignment_overrides_create_request=assignment_overrides_create_request)
        print("The response of AssignmentOverridesApi->assignment_overrides_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssignmentOverridesApi->assignment_overrides_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **course_id** | **str**| Scope response to course_id | 
 **assignment_overrides_create_request** | [**AssignmentOverridesCreateRequest**](AssignmentOverridesCreateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/courses/1/assignments/2/overrides.json&#39; \\      -X POST \\      -F &#39;assignment_override[student_ids][]&#x3D;8&#39; \\      -F &#39;assignment_override[title]&#x3D;Fred Flinstone&#39; \\      -F &#39;assignment_override[due_at]&#x3D;2012-10-08T21:00:00Z&#39; \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**AssignmentOverride**](AssignmentOverride.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | AssignmentOverride |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assignment_overrides_destroy**
> AssignmentOverride assignment_overrides_destroy(assignment_id, course_id, id)

Delete an assignment override

Deletes an override and returns its former details.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.assignment_override import AssignmentOverride
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
    api_instance = canvas_lms_python_client.AssignmentOverridesApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id

    try:
        # Delete an assignment override
        api_response = await api_instance.assignment_overrides_destroy(assignment_id, course_id, id)
        print("The response of AssignmentOverridesApi->assignment_overrides_destroy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssignmentOverridesApi->assignment_overrides_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**AssignmentOverride**](AssignmentOverride.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | AssignmentOverride |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assignment_overrides_group_alias**
> assignment_overrides_group_alias(assignment_id, group_id)

Redirect to the assignment override for a group

Responds with a redirect to the override for the given group, if any
(404 otherwise).

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
    api_instance = canvas_lms_python_client.AssignmentOverridesApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    group_id = 'group_id_example' # str | Scope response to group_id

    try:
        # Redirect to the assignment override for a group
        await api_instance.assignment_overrides_group_alias(assignment_id, group_id)
    except Exception as e:
        print("Exception when calling AssignmentOverridesApi->assignment_overrides_group_alias: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **group_id** | **str**| Scope response to group_id | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Redirect to the assignment override for a group |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assignment_overrides_index**
> List[AssignmentOverride] assignment_overrides_index(assignment_id, course_id)

List assignment overrides

Returns the paginated list of overrides for this assignment that target
sections/groups/students visible to the current user.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.assignment_override import AssignmentOverride
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
    api_instance = canvas_lms_python_client.AssignmentOverridesApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    course_id = 'course_id_example' # str | Scope response to course_id

    try:
        # List assignment overrides
        api_response = await api_instance.assignment_overrides_index(assignment_id, course_id)
        print("The response of AssignmentOverridesApi->assignment_overrides_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssignmentOverridesApi->assignment_overrides_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **course_id** | **str**| Scope response to course_id | 

### Return type

[**List[AssignmentOverride]**](AssignmentOverride.md)

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

# **assignment_overrides_section_alias**
> assignment_overrides_section_alias(assignment_id, course_section_id)

Redirect to the assignment override for a section

Responds with a redirect to the override for the given section, if any
(404 otherwise).

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
    api_instance = canvas_lms_python_client.AssignmentOverridesApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    course_section_id = 'course_section_id_example' # str | Scope response to course_section_id

    try:
        # Redirect to the assignment override for a section
        await api_instance.assignment_overrides_section_alias(assignment_id, course_section_id)
    except Exception as e:
        print("Exception when calling AssignmentOverridesApi->assignment_overrides_section_alias: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **course_section_id** | **str**| Scope response to course_section_id | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Redirect to the assignment override for a section |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assignment_overrides_show**
> AssignmentOverride assignment_overrides_show(assignment_id, course_id, id)

Get a single assignment override

Returns details of the the override with the given id.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.assignment_override import AssignmentOverride
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
    api_instance = canvas_lms_python_client.AssignmentOverridesApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id

    try:
        # Get a single assignment override
        api_response = await api_instance.assignment_overrides_show(assignment_id, course_id, id)
        print("The response of AssignmentOverridesApi->assignment_overrides_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssignmentOverridesApi->assignment_overrides_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**AssignmentOverride**](AssignmentOverride.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | AssignmentOverride |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assignment_overrides_update**
> AssignmentOverride assignment_overrides_update(assignment_id, course_id, id, assignment_overrides_update_request=assignment_overrides_update_request)

Update an assignment override

All current overridden values must be supplied if they are to be retained;
e.g. if due_at was overridden, but this PUT omits a value for due_at,
due_at will no longer be overridden. If the override is adhoc and
student_ids is not supplied, the target override set is unchanged. Target
override sets cannot be changed for group or section overrides.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.assignment_override import AssignmentOverride
from canvas_lms_python_client.models.assignment_overrides_update_request import AssignmentOverridesUpdateRequest
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
    api_instance = canvas_lms_python_client.AssignmentOverridesApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    assignment_overrides_update_request = canvas_lms_python_client.AssignmentOverridesUpdateRequest() # AssignmentOverridesUpdateRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/courses/1/assignments/2/overrides/3.json' \\      -X PUT \\      -F 'assignment_override[title]=Fred Flinstone' \\      -F 'assignment_override[due_at]=2012-10-08T21:00:00Z' \\      -H \"Authorization: Bearer <token>\" ``` (optional)

    try:
        # Update an assignment override
        api_response = await api_instance.assignment_overrides_update(assignment_id, course_id, id, assignment_overrides_update_request=assignment_overrides_update_request)
        print("The response of AssignmentOverridesApi->assignment_overrides_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssignmentOverridesApi->assignment_overrides_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **assignment_overrides_update_request** | [**AssignmentOverridesUpdateRequest**](AssignmentOverridesUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/courses/1/assignments/2/overrides/3.json&#39; \\      -X PUT \\      -F &#39;assignment_override[title]&#x3D;Fred Flinstone&#39; \\      -F &#39;assignment_override[due_at]&#x3D;2012-10-08T21:00:00Z&#39; \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**AssignmentOverride**](AssignmentOverride.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | AssignmentOverride |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

