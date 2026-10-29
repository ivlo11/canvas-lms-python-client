# MasterTemplatesQueueMigrationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | An optional comment to be included in the sync history. | [optional] 
**send_notification** | **bool** | Send a notification to the calling user when the sync completes. | [optional] 
**copy_settings** | **bool** | Whether course settings should be copied over to associated courses. Defaults to true for newly associated courses. | [optional] 
**send_item_notifications** | **bool** | By default, new-item notifications are suppressed in blueprint syncs. If this option is set, teachers and students may receive notifications for items such as announcements and assignments that are created in associated courses (subject to the usual notification settings). This option requires the Blueprint Item Notifications feature to be enabled. | [optional] 
**publish_after_initial_sync** | **bool** | If set, newly associated courses will be automatically published after the sync completes | [optional] 

## Example

```python
from canvas_lms_python_client.models.master_templates_queue_migration_request import MasterTemplatesQueueMigrationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MasterTemplatesQueueMigrationRequest from a JSON string
master_templates_queue_migration_request_instance = MasterTemplatesQueueMigrationRequest.from_json(json)
# print the JSON string representation of the object
print(MasterTemplatesQueueMigrationRequest.to_json())

# convert the object into a dict
master_templates_queue_migration_request_dict = master_templates_queue_migration_request_instance.to_dict()
# create an instance of MasterTemplatesQueueMigrationRequest from a dict
master_templates_queue_migration_request_from_dict = MasterTemplatesQueueMigrationRequest.from_dict(master_templates_queue_migration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


