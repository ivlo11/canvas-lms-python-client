# SisImportsApiCreateRequestPreAttachment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | [String] The name of the file to be uploaded (in a separate request) via the {file:file.file_uploads.html File Upload} workflow. This is the recommended way to upload larger batches, since the upload itself no longer has to finish within the 1-minute Canvas request timeout period. This argument cannot be combined with the +attachment+ argument; use one or the other.  To use this flow: 1. Perform a POST to this endpoint with file information in +pre_attachment+ 2. {file:file.file_uploads.html Upload the file} using the data in the response&#39;s +pre_attachment+ 3. Once the file has been uploaded, the SIS import will begin. 4. {api:SisImportsApiController#show Check the progress} of the import as usual.  NOTE: this option must be sent as either a query parameter or as a JSON body parameter; +application/x-www-form-urlencoded+ is not supported due to conflicts with raw post body data. | [optional] 

## Example

```python
from canvas_lms_python_client.models.sis_imports_api_create_request_pre_attachment import SisImportsApiCreateRequestPreAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of SisImportsApiCreateRequestPreAttachment from a JSON string
sis_imports_api_create_request_pre_attachment_instance = SisImportsApiCreateRequestPreAttachment.from_json(json)
# print the JSON string representation of the object
print(SisImportsApiCreateRequestPreAttachment.to_json())

# convert the object into a dict
sis_imports_api_create_request_pre_attachment_dict = sis_imports_api_create_request_pre_attachment_instance.to_dict()
# create an instance of SisImportsApiCreateRequestPreAttachment from a dict
sis_imports_api_create_request_pre_attachment_from_dict = SisImportsApiCreateRequestPreAttachment.from_dict(sis_imports_api_create_request_pre_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


