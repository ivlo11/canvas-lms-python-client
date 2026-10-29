# ContentMigration



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | the unique identifier for the migration | [optional] 
**migration_type** | **str** | the type of content migration | [optional] 
**migration_type_title** | **str** | the name of the content migration type | [optional] 
**migration_issues_url** | **str** | API url to the content migration&#39;s issues | [optional] 
**attachment** | **str** | attachment api object for the uploaded file may not be present for all migrations | [optional] 
**progress_url** | **str** | The api endpoint for polling the current progress | [optional] 
**user_id** | **int** | The user who started the migration | [optional] 
**workflow_state** | **str** | Current state of the content migration: pre_processing, pre_processed, running, waiting_for_select, completed, failed | [optional] 
**started_at** | **datetime** | timestamp | [optional] 
**finished_at** | **datetime** | timestamp | [optional] 
**pre_attachment** | **str** | file uploading data, see {file:file.file_uploads.html File Upload Documentation} for file upload workflow This works a little differently in that all the file data is in the pre_attachment hash if there is no upload_url then there was an attachment pre-processing error, the error message will be in the message key This data will only be here after a create or update call | [optional] 

## Example

```python
from canvas_lms_python_client.models.content_migration import ContentMigration

# TODO update the JSON string below
json = "{}"
# create an instance of ContentMigration from a JSON string
content_migration_instance = ContentMigration.from_json(json)
# print the JSON string representation of the object
print(ContentMigration.to_json())

# convert the object into a dict
content_migration_dict = content_migration_instance.to_dict()
# create an instance of ContentMigration from a dict
content_migration_from_dict = ContentMigration.from_dict(content_migration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


