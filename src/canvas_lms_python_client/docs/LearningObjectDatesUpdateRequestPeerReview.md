# LearningObjectDatesUpdateRequestPeerReview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**due_at** | **str** | [DateTime] The peer review due date | [optional] 
**unlock_at** | **str** | [DateTime] The peer review unlock date (when peer reviews become available) | [optional] 
**lock_at** | **str** | [DateTime] The peer review lock date (when peer reviews are no longer available) | [optional] 
**peer_review_overrides** | **str** | [] [Array] List of peer review overrides. Each override can include: &#39;id&#39;, &#39;due_at&#39;, &#39;unlock_at&#39;, &#39;lock_at&#39;, &#39;student_ids&#39;, &#39;course_section_id&#39;, &#39;course_id&#39;, &#39;group_id&#39;, &#39;unassign_item&#39; | [optional] 

## Example

```python
from canvas_lms_python_client.models.learning_object_dates_update_request_peer_review import LearningObjectDatesUpdateRequestPeerReview

# TODO update the JSON string below
json = "{}"
# create an instance of LearningObjectDatesUpdateRequestPeerReview from a JSON string
learning_object_dates_update_request_peer_review_instance = LearningObjectDatesUpdateRequestPeerReview.from_json(json)
# print the JSON string representation of the object
print(LearningObjectDatesUpdateRequestPeerReview.to_json())

# convert the object into a dict
learning_object_dates_update_request_peer_review_dict = learning_object_dates_update_request_peer_review_instance.to_dict()
# create an instance of LearningObjectDatesUpdateRequestPeerReview from a dict
learning_object_dates_update_request_peer_review_from_dict = LearningObjectDatesUpdateRequestPeerReview.from_dict(learning_object_dates_update_request_peer_review_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


