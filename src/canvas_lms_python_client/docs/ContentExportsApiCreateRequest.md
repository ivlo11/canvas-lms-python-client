# ContentExportsApiCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**export_type** | **str** | \&quot;common_cartridge\&quot;:: Export the contents of the course in the Common Cartridge (.imscc) format \&quot;qti\&quot;:: Export quizzes from a course in the QTI format \&quot;zip\&quot;:: Export files from a course, group, or user in a zip file | 
**skip_notifications** | **bool** | Don&#39;t send the notifications about the export to the user. Default: false | [optional] 
**select** | **str** | The select parameter allows exporting specific data. The keys are object types like &#39;files&#39;, &#39;folders&#39;, &#39;pages&#39;, etc. The value for each key is a list of object ids. An id can be an integer or a string.  Multiple object types can be selected in the same call. However, not all object types are valid for every export_type. Common Cartridge supports all object types. Zip and QTI only support the object types as described below.  \&quot;folders\&quot;:: Also supported for zip export_type. \&quot;files\&quot;:: Also supported for zip export_type. \&quot;quizzes\&quot;:: Also supported for qti export_type. | [optional] 

## Example

```python
from canvas_lms_python_client.models.content_exports_api_create_request import ContentExportsApiCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ContentExportsApiCreateRequest from a JSON string
content_exports_api_create_request_instance = ContentExportsApiCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ContentExportsApiCreateRequest.to_json())

# convert the object into a dict
content_exports_api_create_request_dict = content_exports_api_create_request_instance.to_dict()
# create an instance of ContentExportsApiCreateRequest from a dict
content_exports_api_create_request_from_dict = ContentExportsApiCreateRequest.from_dict(content_exports_api_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


