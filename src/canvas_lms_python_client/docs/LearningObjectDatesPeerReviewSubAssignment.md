# LearningObjectDatesPeerReviewSubAssignment

peer review sub assignment details. If a peer review sub assignment exists, it is returned regardless of the Peer Review Allocation and Grading feature state. If no peer review sub assignment exists, the feature must be enabled to receive a null value; otherwise the key is omitted.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**due_at** | **datetime** |  | [optional] 
**unlock_at** | **datetime** |  | [optional] 
**lock_at** | **datetime** |  | [optional] 
**only_visible_to_overrides** | **bool** |  | [optional] 
**visible_to_everyone** | **bool** |  | [optional] 
**overrides** | [**List[AssignmentOverride]**](AssignmentOverride.md) | paginated list of AssignmentOverride objects specific to the peer review sub assignment | [optional] 

## Example

```python
from canvas_lms_python_client.models.learning_object_dates_peer_review_sub_assignment import LearningObjectDatesPeerReviewSubAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of LearningObjectDatesPeerReviewSubAssignment from a JSON string
learning_object_dates_peer_review_sub_assignment_instance = LearningObjectDatesPeerReviewSubAssignment.from_json(json)
# print the JSON string representation of the object
print(LearningObjectDatesPeerReviewSubAssignment.to_json())

# convert the object into a dict
learning_object_dates_peer_review_sub_assignment_dict = learning_object_dates_peer_review_sub_assignment_instance.to_dict()
# create an instance of LearningObjectDatesPeerReviewSubAssignment from a dict
learning_object_dates_peer_review_sub_assignment_from_dict = LearningObjectDatesPeerReviewSubAssignment.from_dict(learning_object_dates_peer_review_sub_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


