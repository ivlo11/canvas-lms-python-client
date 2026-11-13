# BlueprintMigration



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the migration. | [optional] 
**template_id** | **int** | The ID of the template the migration belongs to. Only present when querying a blueprint course. | [optional] 
**subscription_id** | **int** | The ID of the associated course&#39;s blueprint subscription. Only present when querying a course associated with a blueprint. | [optional] 
**user_id** | **int** | The ID of the user who queued the migration. | [optional] 
**workflow_state** | **str** | Current state of the content migration: queued, exporting, imports_queued, completed, exports_failed, imports_failed | [optional] 
**created_at** | **datetime** | Time when the migration was queued | [optional] 
**exports_started_at** | **datetime** | Time when the exports begun | [optional] 
**imports_queued_at** | **datetime** | Time when the exports were completed and imports were queued | [optional] 
**imports_completed_at** | **datetime** | Time when the imports were completed | [optional] 
**comment** | **str** | User-specified comment describing changes made in this operation | [optional] 
**user** | **object** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.blueprint_migration import BlueprintMigration

# TODO update the JSON string below
json = "{}"
# create an instance of BlueprintMigration from a JSON string
blueprint_migration_instance = BlueprintMigration.from_json(json)
# print the JSON string representation of the object
print(BlueprintMigration.to_json())

# convert the object into a dict
blueprint_migration_dict = blueprint_migration_instance.to_dict()
# create an instance of BlueprintMigration from a dict
blueprint_migration_from_dict = BlueprintMigration.from_dict(blueprint_migration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


