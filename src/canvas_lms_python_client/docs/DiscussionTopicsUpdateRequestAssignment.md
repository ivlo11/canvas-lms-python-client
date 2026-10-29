# DiscussionTopicsUpdateRequestAssignment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignment** | **str** | To create an assignment discussion, pass the assignment parameters as a sub-object. See the {api:AssignmentsApiController#create Create an Assignment API} for the available parameters. The name parameter will be ignored, as it&#39;s taken from the discussion title. If you want to make a discussion that was an assignment NOT an assignment, pass set_assignment &#x3D; false as part of the assignment object | [optional] 

## Example

```python
from canvas_lms_python_client.models.discussion_topics_update_request_assignment import DiscussionTopicsUpdateRequestAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionTopicsUpdateRequestAssignment from a JSON string
discussion_topics_update_request_assignment_instance = DiscussionTopicsUpdateRequestAssignment.from_json(json)
# print the JSON string representation of the object
print(DiscussionTopicsUpdateRequestAssignment.to_json())

# convert the object into a dict
discussion_topics_update_request_assignment_dict = discussion_topics_update_request_assignment_instance.to_dict()
# create an instance of DiscussionTopicsUpdateRequestAssignment from a dict
discussion_topics_update_request_assignment_from_dict = DiscussionTopicsUpdateRequestAssignment.from_dict(discussion_topics_update_request_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


