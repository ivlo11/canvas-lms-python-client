# LearningObjectDates



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | the ID of the learning object (not present for checkpoints) | [optional] 
**due_at** | **datetime** | the due date for the learning object. returns null if not present or applicable. never applicable for ungraded discussions, pages, and files | [optional] 
**lock_at** | **datetime** | the lock date (learning object is locked after this date). returns null if not present | [optional] 
**reply_to_topic_due_at** | **datetime** | the reply_to_topic sub_assignment due_date. returns null if not present | [optional] 
**required_replies_due_at** | **datetime** | the reply_to_entry sub_assignment due_date. returns null if not present | [optional] 
**unlock_at** | **datetime** | the unlock date (learning object is unlocked after this date). returns null if not present | [optional] 
**only_visible_to_overrides** | **bool** | whether the learning object is only visible to overrides | [optional] 
**graded** | **bool** | whether the learning object is graded (and thus has a due date) | [optional] 
**blueprint_date_locks** | **List[str]** | [exclusive to blueprint child content only] list of lock types | [optional] 
**visible_to_everyone** | **bool** | whether the learning object is visible to everyone | [optional] 
**overrides** | [**List[AssignmentOverride]**](AssignmentOverride.md) | paginated list of AssignmentOverride objects | [optional] 
**checkpoints** | [**List[LearningObjectDates]**](LearningObjectDates.md) | list of Checkpoint objects, only present if a learning object has subAssignments | [optional] 
**tag** | **str** | the tag identifying the type of checkpoint (only present for checkpoints) | [optional] 
**peer_review_sub_assignment** | **object** | peer review sub assignment details. If a peer review sub assignment exists, it is returned regardless of the Peer Review Allocation and Grading feature state. If no peer review sub assignment exists, the feature must be enabled to receive a null value; otherwise the key is omitted. | [optional] 

## Example

```python
from canvas_lms_python_client.models.learning_object_dates import LearningObjectDates

# TODO update the JSON string below
json = "{}"
# create an instance of LearningObjectDates from a JSON string
learning_object_dates_instance = LearningObjectDates.from_json(json)
# print the JSON string representation of the object
print(LearningObjectDates.to_json())

# convert the object into a dict
learning_object_dates_dict = learning_object_dates_instance.to_dict()
# create an instance of LearningObjectDates from a dict
learning_object_dates_from_dict = LearningObjectDates.from_dict(learning_object_dates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


