# ContentMigration



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | the unique identifier for the migration | [optional] 
**migration_type** | **str** | the type of content migration | [optional] 
**migration_type_title** | **str** | the name of the content migration type | [optional] 
**migration_issues_url** | **str** | API url to the content migration&#39;s issues | [optional] 
**attachment** | [**ContentMigrationAttachment**](ContentMigrationAttachment.md) |  | [optional] 
**progress_url** | **str** | The api endpoint for polling the current progress | [optional] 
**user_id** | **int** | The user who started the migration | [optional] 
**workflow_state** | **str** | Current state of the content migration: pre_processing, pre_processed, running, waiting_for_select, completed, failed | [optional] 
**started_at** | **datetime** | timestamp | [optional] 
**finished_at** | **datetime** | timestamp | [optional] 
**pre_attachment** | [**ContentMigrationPreAttachment**](ContentMigrationPreAttachment.md) |  | [optional] 
**created_at** | **str** |  | [optional] 
**migration_issues_count** | **int** |  | [optional] 
**audit_info** | **object** |  | [optional] 
**settings** | **object** |  | [optional] 

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


