# canvas_lms_python_client.BlockEditorTemplatesApiApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**block_editor_templates_api_index**](BlockEditorTemplatesApiApi.md#block_editor_templates_api_index) | **GET** /api/v1/courses/{course_id}/block_editor_templates | List block templates


# **block_editor_templates_api_index**
> List[BlockEditorTemplate] block_editor_templates_api_index(course_id, sort=sort, order=order, drafts=drafts, type=type, include=include)

List block templates

A list of the block templates available to the current user.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.block_editor_template import BlockEditorTemplate
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
    api_instance = canvas_lms_python_client.BlockEditorTemplatesApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    sort = 'sort_example' # str | Sort results by this field. (optional)
    order = 'order_example' # str | The sorting order. Defaults to 'asc'. (optional)
    drafts = True # bool | If true, include draft templates. If false or omitted only published templates will be returned. (optional)
    type = ['type_example'] # List[str] | What type of templates should be returned. (optional)
    include = ['include_example'] # List[str] |  (optional)

    try:
        # List block templates
        api_response = await api_instance.block_editor_templates_api_index(course_id, sort=sort, order=order, drafts=drafts, type=type, include=include)
        print("The response of BlockEditorTemplatesApiApi->block_editor_templates_api_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlockEditorTemplatesApiApi->block_editor_templates_api_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **sort** | **str**| Sort results by this field. | [optional] 
 **order** | **str**| The sorting order. Defaults to &#39;asc&#39;. | [optional] 
 **drafts** | **bool**| If true, include draft templates. If false or omitted only published templates will be returned. | [optional] 
 **type** | [**List[str]**](str.md)| What type of templates should be returned. | [optional] 
 **include** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[BlockEditorTemplate]**](BlockEditorTemplate.md)

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

