# ContentMigrationPreAttachment

file uploading data, see {file:file.file_uploads.html File Upload Documentation} for file upload workflow This works a little differently in that all the file data is in the pre_attachment hash if there is no upload_url then there was an attachment pre-processing error, the error message will be in the message key This data will only be here after a create or update call

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from canvas_lms_python_client.models.content_migration_pre_attachment import ContentMigrationPreAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of ContentMigrationPreAttachment from a JSON string
content_migration_pre_attachment_instance = ContentMigrationPreAttachment.from_json(json)
# print the JSON string representation of the object
print(ContentMigrationPreAttachment.to_json())

# convert the object into a dict
content_migration_pre_attachment_dict = content_migration_pre_attachment_instance.to_dict()
# create an instance of ContentMigrationPreAttachment from a dict
content_migration_pre_attachment_from_dict = ContentMigrationPreAttachment.from_dict(content_migration_pre_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


