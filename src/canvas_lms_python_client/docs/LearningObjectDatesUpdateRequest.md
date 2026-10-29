# LearningObjectDatesUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**due_at** | **str** | The learning object&#39;s due date. Not applicable for ungraded discussions, pages, and files. | [optional] 
**unlock_at** | **str** | The learning object&#39;s unlock date. Must be before the due date if there is one. | [optional] 
**lock_at** | **str** | The learning object&#39;s lock date. Must be after the due date if there is one. | [optional] 
**only_visible_to_overrides** | **bool** | Whether the learning object is only assigned to students who are targeted by an override. | [optional] 
**assignment_overrides** | **List[List[str]]** | List of overrides to apply to the learning object. Overrides that already exist should include an ID and will be updated if needed. New overrides will be created for overrides in the list without an ID. Overrides not included in the list will be deleted. Providing an empty list will delete all of the object&#39;s overrides. Keys for each override object can include: &#39;id&#39;, &#39;title&#39;, &#39;due_at&#39;, &#39;unlock_at&#39;, &#39;lock_at&#39;, &#39;student_ids&#39;, and &#39;course_section_id&#39;, &#39;course_id&#39;, &#39;noop_id&#39;, and &#39;unassign_item&#39;. | [optional] 
**peer_review** | [**LearningObjectDatesUpdateRequestPeerReview**](LearningObjectDatesUpdateRequestPeerReview.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.learning_object_dates_update_request import LearningObjectDatesUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LearningObjectDatesUpdateRequest from a JSON string
learning_object_dates_update_request_instance = LearningObjectDatesUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(LearningObjectDatesUpdateRequest.to_json())

# convert the object into a dict
learning_object_dates_update_request_dict = learning_object_dates_update_request_instance.to_dict()
# create an instance of LearningObjectDatesUpdateRequest from a dict
learning_object_dates_update_request_from_dict = LearningObjectDatesUpdateRequest.from_dict(learning_object_dates_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


