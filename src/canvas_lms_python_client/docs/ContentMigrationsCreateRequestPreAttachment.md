# ContentMigrationsCreateRequestPreAttachment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | [String] Required if uploading a file. This is the first step in uploading a file to the content migration. See the {file:file.file_uploads.html File Upload Documentation} for details on the file upload workflow. | [optional] 

## Example

```python
from canvas_lms_python_client.models.content_migrations_create_request_pre_attachment import ContentMigrationsCreateRequestPreAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of ContentMigrationsCreateRequestPreAttachment from a JSON string
content_migrations_create_request_pre_attachment_instance = ContentMigrationsCreateRequestPreAttachment.from_json(json)
# print the JSON string representation of the object
print(ContentMigrationsCreateRequestPreAttachment.to_json())

# convert the object into a dict
content_migrations_create_request_pre_attachment_dict = content_migrations_create_request_pre_attachment_instance.to_dict()
# create an instance of ContentMigrationsCreateRequestPreAttachment from a dict
content_migrations_create_request_pre_attachment_from_dict = ContentMigrationsCreateRequestPreAttachment.from_dict(content_migrations_create_request_pre_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


