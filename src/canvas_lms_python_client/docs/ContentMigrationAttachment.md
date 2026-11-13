# ContentMigrationAttachment

attachment api object for the uploaded file may not be present for all migrations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from canvas_lms_python_client.models.content_migration_attachment import ContentMigrationAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of ContentMigrationAttachment from a JSON string
content_migration_attachment_instance = ContentMigrationAttachment.from_json(json)
# print the JSON string representation of the object
print(ContentMigrationAttachment.to_json())

# convert the object into a dict
content_migration_attachment_dict = content_migration_attachment_instance.to_dict()
# create an instance of ContentMigrationAttachment from a dict
content_migration_attachment_from_dict = ContentMigrationAttachment.from_dict(content_migration_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


