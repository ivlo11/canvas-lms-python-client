# MicrosoftSyncGroup

The membership of a Microsoft group as well as the status of syncing Canvas enrollments to that group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The id of the MicrosoftSync_Group | [optional] 
**course_id** | **int** | The id of the course related to the MicrosoftSync_Group | [optional] 
**workflow_state** | **str** | The current state of the MicrosoftSync_Group | [optional] 
**job_state** | **str** | Internal data about the last step run for a job in the &#39;retrying&#39; state. Only returned for site admins | [optional] 
**last_synced_at** | **datetime** | The time of the last successful sync | [optional] 
**last_error** | **str** | The last error encountered during an attempted sync | [optional] 
**last_error_report_id** | **int** | The ErrorReport ID for the last_error. Only returned for site admins | [optional] 
**root_account_id** | **int** | The root account the MicrosoftSync_Group belongs to | [optional] 
**created_at** | **datetime** | The time the MicrosoftSync_Group was created | [optional] 
**updated_at** | **datetime** | The time the MicrosoftSync_Group was updated | [optional] 
**debug_info** | **List[object]** | List of strings with debugging info (localized). Only returned for site admins. | [optional] 

## Example

```python
from canvas_lms_python_client.models.microsoft_sync_group import MicrosoftSyncGroup

# TODO update the JSON string below
json = "{}"
# create an instance of MicrosoftSyncGroup from a JSON string
microsoft_sync_group_instance = MicrosoftSyncGroup.from_json(json)
# print the JSON string representation of the object
print(MicrosoftSyncGroup.to_json())

# convert the object into a dict
microsoft_sync_group_dict = microsoft_sync_group_instance.to_dict()
# create an instance of MicrosoftSyncGroup from a dict
microsoft_sync_group_from_dict = MicrosoftSyncGroup.from_dict(microsoft_sync_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


