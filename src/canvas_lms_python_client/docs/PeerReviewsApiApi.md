# canvas_lms_python_client.PeerReviewsApiApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**peer_reviews_api_allocate**](PeerReviewsApiApi.md#peer_reviews_api_allocate) | **POST** /api/v1/courses/{course_id}/assignments/{assignment_id}/allocate | Allocate Peer Review
[**peer_reviews_api_create**](PeerReviewsApiApi.md#peer_reviews_api_create) | **POST** /api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{submission_id}/peer_reviews | Create Peer Review
[**peer_reviews_api_create_for_sections**](PeerReviewsApiApi.md#peer_reviews_api_create_for_sections) | **POST** /api/v1/sections/{section_id}/assignments/{assignment_id}/submissions/{submission_id}/peer_reviews | Create Peer Review
[**peer_reviews_api_destroy**](PeerReviewsApiApi.md#peer_reviews_api_destroy) | **DELETE** /api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{submission_id}/peer_reviews | Delete Peer Review
[**peer_reviews_api_destroy_for_sections**](PeerReviewsApiApi.md#peer_reviews_api_destroy_for_sections) | **DELETE** /api/v1/sections/{section_id}/assignments/{assignment_id}/submissions/{submission_id}/peer_reviews | Delete Peer Review
[**peer_reviews_api_index**](PeerReviewsApiApi.md#peer_reviews_api_index) | **GET** /api/v1/courses/{course_id}/assignments/{assignment_id}/peer_reviews | Get all Peer Reviews
[**peer_reviews_api_index_by_submission_id_for_sections**](PeerReviewsApiApi.md#peer_reviews_api_index_by_submission_id_for_sections) | **GET** /api/v1/sections/{section_id}/assignments/{assignment_id}/submissions/{submission_id}/peer_reviews | Get all Peer Reviews
[**peer_reviews_api_index_for_courses**](PeerReviewsApiApi.md#peer_reviews_api_index_for_courses) | **GET** /api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{submission_id}/peer_reviews | Get all Peer Reviews
[**peer_reviews_api_index_for_sections**](PeerReviewsApiApi.md#peer_reviews_api_index_for_sections) | **GET** /api/v1/sections/{section_id}/assignments/{assignment_id}/peer_reviews | Get all Peer Reviews


# **peer_reviews_api_allocate**
> PeerReview peer_reviews_api_allocate(assignment_id, course_id)

Allocate Peer Review

Allocates a submission for the current user to peer review

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.peer_review import PeerReview
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
    api_instance = canvas_lms_python_client.PeerReviewsApiApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    course_id = 'course_id_example' # str | Scope response to course_id

    try:
        # Allocate Peer Review
        api_response = await api_instance.peer_reviews_api_allocate(assignment_id, course_id)
        print("The response of PeerReviewsApiApi->peer_reviews_api_allocate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PeerReviewsApiApi->peer_reviews_api_allocate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **course_id** | **str**| Scope response to course_id | 

### Return type

[**PeerReview**](PeerReview.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | PeerReview |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **peer_reviews_api_create**
> PeerReview peer_reviews_api_create(assignment_id, course_id, submission_id, peer_reviews_api_create_request=peer_reviews_api_create_request)

Create Peer Review

Create a peer review for the assignment

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.peer_review import PeerReview
from canvas_lms_python_client.models.peer_reviews_api_create_request import PeerReviewsApiCreateRequest
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
    api_instance = canvas_lms_python_client.PeerReviewsApiApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    course_id = 'course_id_example' # str | Scope response to course_id
    submission_id = 'submission_id_example' # str | Scope response to submission_id
    peer_reviews_api_create_request = canvas_lms_python_client.PeerReviewsApiCreateRequest() # PeerReviewsApiCreateRequest | Request body parameters (optional)

    try:
        # Create Peer Review
        api_response = await api_instance.peer_reviews_api_create(assignment_id, course_id, submission_id, peer_reviews_api_create_request=peer_reviews_api_create_request)
        print("The response of PeerReviewsApiApi->peer_reviews_api_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PeerReviewsApiApi->peer_reviews_api_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **course_id** | **str**| Scope response to course_id | 
 **submission_id** | **str**| Scope response to submission_id | 
 **peer_reviews_api_create_request** | [**PeerReviewsApiCreateRequest**](PeerReviewsApiCreateRequest.md)| Request body parameters | [optional] 

### Return type

[**PeerReview**](PeerReview.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | PeerReview |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **peer_reviews_api_create_for_sections**
> PeerReview peer_reviews_api_create_for_sections(assignment_id, section_id, submission_id, peer_reviews_api_create_request=peer_reviews_api_create_request)

Create Peer Review

Create a peer review for the assignment

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.peer_review import PeerReview
from canvas_lms_python_client.models.peer_reviews_api_create_request import PeerReviewsApiCreateRequest
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
    api_instance = canvas_lms_python_client.PeerReviewsApiApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    section_id = 'section_id_example' # str | Scope response to section_id
    submission_id = 'submission_id_example' # str | Scope response to submission_id
    peer_reviews_api_create_request = canvas_lms_python_client.PeerReviewsApiCreateRequest() # PeerReviewsApiCreateRequest | Request body parameters (optional)

    try:
        # Create Peer Review
        api_response = await api_instance.peer_reviews_api_create_for_sections(assignment_id, section_id, submission_id, peer_reviews_api_create_request=peer_reviews_api_create_request)
        print("The response of PeerReviewsApiApi->peer_reviews_api_create_for_sections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PeerReviewsApiApi->peer_reviews_api_create_for_sections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **section_id** | **str**| Scope response to section_id | 
 **submission_id** | **str**| Scope response to submission_id | 
 **peer_reviews_api_create_request** | [**PeerReviewsApiCreateRequest**](PeerReviewsApiCreateRequest.md)| Request body parameters | [optional] 

### Return type

[**PeerReview**](PeerReview.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | PeerReview |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **peer_reviews_api_destroy**
> PeerReview peer_reviews_api_destroy(assignment_id, course_id, submission_id, user_id)

Delete Peer Review

Delete a peer review for the assignment

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.peer_review import PeerReview
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
    api_instance = canvas_lms_python_client.PeerReviewsApiApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    course_id = 'course_id_example' # str | Scope response to course_id
    submission_id = 'submission_id_example' # str | Scope response to submission_id
    user_id = 56 # int | user_id to delete as reviewer on this assignment

    try:
        # Delete Peer Review
        api_response = await api_instance.peer_reviews_api_destroy(assignment_id, course_id, submission_id, user_id)
        print("The response of PeerReviewsApiApi->peer_reviews_api_destroy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PeerReviewsApiApi->peer_reviews_api_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **course_id** | **str**| Scope response to course_id | 
 **submission_id** | **str**| Scope response to submission_id | 
 **user_id** | **int**| user_id to delete as reviewer on this assignment | 

### Return type

[**PeerReview**](PeerReview.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | PeerReview |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **peer_reviews_api_destroy_for_sections**
> PeerReview peer_reviews_api_destroy_for_sections(assignment_id, section_id, submission_id, user_id)

Delete Peer Review

Delete a peer review for the assignment

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.peer_review import PeerReview
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
    api_instance = canvas_lms_python_client.PeerReviewsApiApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    section_id = 'section_id_example' # str | Scope response to section_id
    submission_id = 'submission_id_example' # str | Scope response to submission_id
    user_id = 56 # int | user_id to delete as reviewer on this assignment

    try:
        # Delete Peer Review
        api_response = await api_instance.peer_reviews_api_destroy_for_sections(assignment_id, section_id, submission_id, user_id)
        print("The response of PeerReviewsApiApi->peer_reviews_api_destroy_for_sections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PeerReviewsApiApi->peer_reviews_api_destroy_for_sections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **section_id** | **str**| Scope response to section_id | 
 **submission_id** | **str**| Scope response to submission_id | 
 **user_id** | **int**| user_id to delete as reviewer on this assignment | 

### Return type

[**PeerReview**](PeerReview.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | PeerReview |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **peer_reviews_api_index**
> List[PeerReview] peer_reviews_api_index(assignment_id, course_id, include=include)

Get all Peer Reviews

Get a list of all Peer Reviews for this assignment

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.peer_review import PeerReview
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
    api_instance = canvas_lms_python_client.PeerReviewsApiApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    course_id = 'course_id_example' # str | Scope response to course_id
    include = ['include_example'] # List[str] | Associations to include with the peer review. (optional)

    try:
        # Get all Peer Reviews
        api_response = await api_instance.peer_reviews_api_index(assignment_id, course_id, include=include)
        print("The response of PeerReviewsApiApi->peer_reviews_api_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PeerReviewsApiApi->peer_reviews_api_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **course_id** | **str**| Scope response to course_id | 
 **include** | [**List[str]**](str.md)| Associations to include with the peer review. | [optional] 

### Return type

[**List[PeerReview]**](PeerReview.md)

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

# **peer_reviews_api_index_by_submission_id_for_sections**
> List[PeerReview] peer_reviews_api_index_by_submission_id_for_sections(assignment_id, section_id, submission_id, include=include)

Get all Peer Reviews

Get a list of all Peer Reviews for this assignment

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.peer_review import PeerReview
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
    api_instance = canvas_lms_python_client.PeerReviewsApiApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    section_id = 'section_id_example' # str | Scope response to section_id
    submission_id = 'submission_id_example' # str | Scope response to submission_id
    include = ['include_example'] # List[str] | Associations to include with the peer review. (optional)

    try:
        # Get all Peer Reviews
        api_response = await api_instance.peer_reviews_api_index_by_submission_id_for_sections(assignment_id, section_id, submission_id, include=include)
        print("The response of PeerReviewsApiApi->peer_reviews_api_index_by_submission_id_for_sections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PeerReviewsApiApi->peer_reviews_api_index_by_submission_id_for_sections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **section_id** | **str**| Scope response to section_id | 
 **submission_id** | **str**| Scope response to submission_id | 
 **include** | [**List[str]**](str.md)| Associations to include with the peer review. | [optional] 

### Return type

[**List[PeerReview]**](PeerReview.md)

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

# **peer_reviews_api_index_for_courses**
> List[PeerReview] peer_reviews_api_index_for_courses(assignment_id, course_id, submission_id, include=include)

Get all Peer Reviews

Get a list of all Peer Reviews for this assignment

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.peer_review import PeerReview
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
    api_instance = canvas_lms_python_client.PeerReviewsApiApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    course_id = 'course_id_example' # str | Scope response to course_id
    submission_id = 'submission_id_example' # str | Scope response to submission_id
    include = ['include_example'] # List[str] | Associations to include with the peer review. (optional)

    try:
        # Get all Peer Reviews
        api_response = await api_instance.peer_reviews_api_index_for_courses(assignment_id, course_id, submission_id, include=include)
        print("The response of PeerReviewsApiApi->peer_reviews_api_index_for_courses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PeerReviewsApiApi->peer_reviews_api_index_for_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **course_id** | **str**| Scope response to course_id | 
 **submission_id** | **str**| Scope response to submission_id | 
 **include** | [**List[str]**](str.md)| Associations to include with the peer review. | [optional] 

### Return type

[**List[PeerReview]**](PeerReview.md)

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

# **peer_reviews_api_index_for_sections**
> List[PeerReview] peer_reviews_api_index_for_sections(assignment_id, section_id, include=include)

Get all Peer Reviews

Get a list of all Peer Reviews for this assignment

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.peer_review import PeerReview
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
    api_instance = canvas_lms_python_client.PeerReviewsApiApi(api_client)
    assignment_id = 'assignment_id_example' # str | Scope response to assignment_id
    section_id = 'section_id_example' # str | Scope response to section_id
    include = ['include_example'] # List[str] | Associations to include with the peer review. (optional)

    try:
        # Get all Peer Reviews
        api_response = await api_instance.peer_reviews_api_index_for_sections(assignment_id, section_id, include=include)
        print("The response of PeerReviewsApiApi->peer_reviews_api_index_for_sections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PeerReviewsApiApi->peer_reviews_api_index_for_sections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| Scope response to assignment_id | 
 **section_id** | **str**| Scope response to section_id | 
 **include** | [**List[str]**](str.md)| Associations to include with the peer review. | [optional] 

### Return type

[**List[PeerReview]**](PeerReview.md)

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

