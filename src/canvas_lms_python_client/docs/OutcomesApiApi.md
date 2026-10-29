# canvas_lms_python_client.OutcomesApiApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**outcomes_api_outcome_alignments**](OutcomesApiApi.md#outcomes_api_outcome_alignments) | **GET** /api/v1/courses/{course_id}/outcome_alignments | Get outcome alignments for a student or assignment
[**outcomes_api_show**](OutcomesApiApi.md#outcomes_api_show) | **GET** /api/v1/outcomes/{id} | Show an outcome
[**outcomes_api_update**](OutcomesApiApi.md#outcomes_api_update) | **PUT** /api/v1/outcomes/{id} | Update an outcome


# **outcomes_api_outcome_alignments**
> List[OutcomeAlignment] outcomes_api_outcome_alignments(course_id, student_id=student_id, assignment_id=assignment_id)

Get outcome alignments for a student or assignment

Returns outcome alignments for a student or assignment in a course.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.outcome_alignment import OutcomeAlignment
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
    api_instance = canvas_lms_python_client.OutcomesApiApi(api_client)
    course_id = 'course_id_example' # str | The id of the course
    student_id = 56 # int | The id of the student. Returns alignments filtered by student submissions. Can be combined with assignment_id to filter to a specific assignment. (optional)
    assignment_id = 56 # int | The id of the assignment. When provided without student_id, returns all outcome alignments for the assignment (requires manage_grades or view_all_grades permission). When provided with student_id, filters to that student's submission. (optional)

    try:
        # Get outcome alignments for a student or assignment
        api_response = await api_instance.outcomes_api_outcome_alignments(course_id, student_id=student_id, assignment_id=assignment_id)
        print("The response of OutcomesApiApi->outcomes_api_outcome_alignments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutcomesApiApi->outcomes_api_outcome_alignments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| The id of the course | 
 **student_id** | **int**| The id of the student. Returns alignments filtered by student submissions. Can be combined with assignment_id to filter to a specific assignment. | [optional] 
 **assignment_id** | **int**| The id of the assignment. When provided without student_id, returns all outcome alignments for the assignment (requires manage_grades or view_all_grades permission). When provided with student_id, filters to that student&#39;s submission. | [optional] 

### Return type

[**List[OutcomeAlignment]**](OutcomeAlignment.md)

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

# **outcomes_api_show**
> Outcome outcomes_api_show(id, add_defaults=add_defaults)

Show an outcome

Returns the details of the outcome with the given id.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.outcome import Outcome
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
    api_instance = canvas_lms_python_client.OutcomesApiApi(api_client)
    id = 'id_example' # str | Scope response to id
    add_defaults = True # bool | If defaults are requested, then color and mastery level defaults will be added to outcome ratings in the result. This will only take effect if the Account Level Mastery Scales FF is DISABLED (optional)

    try:
        # Show an outcome
        api_response = await api_instance.outcomes_api_show(id, add_defaults=add_defaults)
        print("The response of OutcomesApiApi->outcomes_api_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutcomesApiApi->outcomes_api_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **add_defaults** | **bool**| If defaults are requested, then color and mastery level defaults will be added to outcome ratings in the result. This will only take effect if the Account Level Mastery Scales FF is DISABLED | [optional] 

### Return type

[**Outcome**](Outcome.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **outcomes_api_update**
> Outcome outcomes_api_update(id, outcomes_api_update_request=outcomes_api_update_request)

Update an outcome

Modify an existing outcome. Fields not provided are left as is;
unrecognized fields are ignored.

If any new ratings are provided, the combination of all new ratings
provided completely replace any existing embedded rubric criterion; it is
not possible to tweak the ratings of the embedded rubric criterion.

A new embedded rubric criterion's mastery_points default to the maximum
points in the highest rating if not specified in the mastery_points
parameter. Any new ratings lacking a description are given a default of "No
description". Any new ratings lacking a point value are given a default of
0.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.outcome import Outcome
from canvas_lms_python_client.models.outcomes_api_update_request import OutcomesApiUpdateRequest
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
    api_instance = canvas_lms_python_client.OutcomesApiApi(api_client)
    id = 'id_example' # str | Scope response to id
    outcomes_api_update_request = canvas_lms_python_client.OutcomesApiUpdateRequest() # OutcomesApiUpdateRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/outcomes/1.json' \\      -X PUT \\      -F 'title=Outcome Title' \\      -F 'display_name=Title for reporting' \\      -F 'description=Outcome description' \\      -F 'vendor_guid=customid9001' \\      -F 'mastery_points=3' \\      -F 'calculation_method=decaying_average' \\      -F 'calculation_int=65' \\      -F 'ratings[][description]=Exceeds Expectations' \\      -F 'ratings[][points]=5' \\      -F 'ratings[][description]=Meets Expectations' \\      -F 'ratings[][points]=3' \\      -F 'ratings[][description]=Does Not Meet Expectations' \\      -F 'ratings[][points]=0' \\      -F 'ratings[][points]=0' \\      -H \"Authorization: Bearer <token>\" ``` (optional)

    try:
        # Update an outcome
        api_response = await api_instance.outcomes_api_update(id, outcomes_api_update_request=outcomes_api_update_request)
        print("The response of OutcomesApiApi->outcomes_api_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutcomesApiApi->outcomes_api_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **outcomes_api_update_request** | [**OutcomesApiUpdateRequest**](OutcomesApiUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/outcomes/1.json&#39; \\      -X PUT \\      -F &#39;title&#x3D;Outcome Title&#39; \\      -F &#39;display_name&#x3D;Title for reporting&#39; \\      -F &#39;description&#x3D;Outcome description&#39; \\      -F &#39;vendor_guid&#x3D;customid9001&#39; \\      -F &#39;mastery_points&#x3D;3&#39; \\      -F &#39;calculation_method&#x3D;decaying_average&#39; \\      -F &#39;calculation_int&#x3D;65&#39; \\      -F &#39;ratings[][description]&#x3D;Exceeds Expectations&#39; \\      -F &#39;ratings[][points]&#x3D;5&#39; \\      -F &#39;ratings[][description]&#x3D;Meets Expectations&#39; \\      -F &#39;ratings[][points]&#x3D;3&#39; \\      -F &#39;ratings[][description]&#x3D;Does Not Meet Expectations&#39; \\      -F &#39;ratings[][points]&#x3D;0&#39; \\      -F &#39;ratings[][points]&#x3D;0&#39; \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**Outcome**](Outcome.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

