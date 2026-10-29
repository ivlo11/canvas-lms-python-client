# FilesApiShowForOtherRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_user** | **str** | Array of additional information to include.  \&quot;user\&quot;:: the user who uploaded the file or last edited its content \&quot;usage_rights\&quot;:: copyright and license information for the file (see UsageRights) | [optional] 
**replacement_chain_context_type** | **str** | When a user replaces a file during upload, Canvas keeps track of the \&quot;replacement chain.\&quot;  Include this parameter if you wish Canvas to follow the replacement chain if the requested file was deleted and replaced by another.  Must be set to &#39;course&#39; or &#39;account&#39;. The \&quot;replacement_chain_context_id\&quot; parameter must also be included. | [optional] 
**replacement_chain_context_id** | **int** | When a user replaces a file during upload, Canvas keeps track of the \&quot;replacement chain.\&quot;  Include this parameter if you wish Canvas to follow the replacement chain if the requested file was deleted and replaced by another.  Indicates the context ID Canvas should use when following the \&quot;replacement chain.\&quot; The \&quot;replacement_chain_context_type\&quot; parameter must also be included. | [optional] 

## Example

```python
from canvas_lms_python_client.models.files_api_show_for_other_request import FilesApiShowForOtherRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FilesApiShowForOtherRequest from a JSON string
files_api_show_for_other_request_instance = FilesApiShowForOtherRequest.from_json(json)
# print the JSON string representation of the object
print(FilesApiShowForOtherRequest.to_json())

# convert the object into a dict
files_api_show_for_other_request_dict = files_api_show_for_other_request_instance.to_dict()
# create an instance of FilesApiShowForOtherRequest from a dict
files_api_show_for_other_request_from_dict = FilesApiShowForOtherRequest.from_dict(files_api_show_for_other_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


