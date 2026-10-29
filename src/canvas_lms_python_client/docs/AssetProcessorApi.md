# canvas_lms_python_client.AssetProcessorApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**asset_processor_bulk_resubmit**](AssetProcessorApi.md#asset_processor_bulk_resubmit) | **POST** /api/v1/support_helpers/asset_processor/bulk_resubmit | Trigger Asset Processor Notice Resubmission
[**asset_processor_bulk_resubmit_discussion**](AssetProcessorApi.md#asset_processor_bulk_resubmit_discussion) | **POST** /api/v1/support_helpers/asset_processor_discussion/bulk_resubmit | Trigger Discussion Asset Processor Notice Resubmission
[**asset_processor_submission_details**](AssetProcessorApi.md#asset_processor_submission_details) | **GET** /api/v1/support_helpers/asset_processor/submission_details | Get Asset Processor Details


# **asset_processor_bulk_resubmit**
> asset_processor_bulk_resubmit(asset_processor_bulk_resubmit_request=asset_processor_bulk_resubmit_request)

Trigger Asset Processor Notice Resubmission

Go through all the submissions in the context (assignment or course)
and trigger asset processor notices for each submission.
One of assignment_id or course_id is required, and the optional tool_id
can be used to send notices only to a specific tool's Asset Processors.

Example Request:
curl -X POST 'http://canvas-web.inseng.test/api/v1/support_helpers/asset_processor/bulk_resubmit' \
-H "Authorization: Bearer $Canvas-User-Token" \
-H "Content-Type: application/json" \
-d '{"assignment_id":123}'

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.asset_processor_bulk_resubmit_request import AssetProcessorBulkResubmitRequest
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
    api_instance = canvas_lms_python_client.AssetProcessorApi(api_client)
    asset_processor_bulk_resubmit_request = canvas_lms_python_client.AssetProcessorBulkResubmitRequest() # AssetProcessorBulkResubmitRequest | Request body parameters (optional)

    try:
        # Trigger Asset Processor Notice Resubmission
        await api_instance.asset_processor_bulk_resubmit(asset_processor_bulk_resubmit_request=asset_processor_bulk_resubmit_request)
    except Exception as e:
        print("Exception when calling AssetProcessorApi->asset_processor_bulk_resubmit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_processor_bulk_resubmit_request** | [**AssetProcessorBulkResubmitRequest**](AssetProcessorBulkResubmitRequest.md)| Request body parameters | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Trigger Asset Processor Notice Resubmission |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_processor_bulk_resubmit_discussion**
> asset_processor_bulk_resubmit_discussion(asset_processor_bulk_resubmit_discussion_request=asset_processor_bulk_resubmit_discussion_request)

Trigger Discussion Asset Processor Notice Resubmission

Go through all the discussion entries in the context
(discussion topic or course) and trigger asset processor
notices for each discussion entry version.
One of discussion_topic_id or course_id is required, and
the optional tool_id can be used to send notices only to a
specific tool's Asset Processors.

Example Request:
curl -X POST 'http://canvas-web.inseng.test/api/v1/support_helpers/asset_processor_discussion/bulk_resubmit' \
-H "Authorization: Bearer $Canvas-User-Token" \
-H "Content-Type: application/json" \
-d '{"discussion_topic_id":123}'

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.asset_processor_bulk_resubmit_discussion_request import AssetProcessorBulkResubmitDiscussionRequest
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
    api_instance = canvas_lms_python_client.AssetProcessorApi(api_client)
    asset_processor_bulk_resubmit_discussion_request = canvas_lms_python_client.AssetProcessorBulkResubmitDiscussionRequest() # AssetProcessorBulkResubmitDiscussionRequest | Request body parameters (optional)

    try:
        # Trigger Discussion Asset Processor Notice Resubmission
        await api_instance.asset_processor_bulk_resubmit_discussion(asset_processor_bulk_resubmit_discussion_request=asset_processor_bulk_resubmit_discussion_request)
    except Exception as e:
        print("Exception when calling AssetProcessorApi->asset_processor_bulk_resubmit_discussion: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_processor_bulk_resubmit_discussion_request** | [**AssetProcessorBulkResubmitDiscussionRequest**](AssetProcessorBulkResubmitDiscussionRequest.md)| Request body parameters | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Trigger Discussion Asset Processor Notice Resubmission |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_processor_submission_details**
> asset_processor_submission_details(assignment_id, student_id, graph=graph)

Get Asset Processor Details

Get all asset processor information for a specific submission including
Asset Processors, Assets, and Asset Reports. This endpoint is intended
for troubleshooting and support purposes.

Example Request:
http://canvas-web.inseng.test/api/v1/support_helpers/asset_processor/submission_details?
  assignment_id=123&student_id=456

Example Graph Request:
http://canvas-web.inseng.test/api/v1/support_helpers/asset_processor/submission_details?
  assignment_id=123&student_id=456&graph=true

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
    api_instance = canvas_lms_python_client.AssetProcessorApi(api_client)
    assignment_id = 56 # int | The ID of the assignment containing the submission to retrieve asset processor details for
    student_id = 56 # int | The ID of the student (user) who owns the submission
    graph = True # bool | If set to true, it returns a DOT graph representation of the asset processor relationships (optional)

    try:
        # Get Asset Processor Details
        await api_instance.asset_processor_submission_details(assignment_id, student_id, graph=graph)
    except Exception as e:
        print("Exception when calling AssetProcessorApi->asset_processor_submission_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **int**| The ID of the assignment containing the submission to retrieve asset processor details for | 
 **student_id** | **int**| The ID of the student (user) who owns the submission | 
 **graph** | **bool**| If set to true, it returns a DOT graph representation of the asset processor relationships | [optional] 

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
**0** | Get Asset Processor Details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

