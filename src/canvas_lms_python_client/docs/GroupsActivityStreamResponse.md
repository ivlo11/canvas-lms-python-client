# GroupsActivityStreamResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context_type** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**discussion_topic_id** | **int** |  | [optional] 
**group_id** | **int** |  | [optional] 
**html_url** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**message** | **str** |  | [optional] 
**read_state** | **bool** |  | [optional] 
**require_initial_post** | **bool** |  | [optional] 
**root_discussion_entries** | **List[object]** |  | [optional] 
**title** | **str** |  | [optional] 
**total_root_discussion_entries** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**user_has_posted** | **object** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.groups_activity_stream_response import GroupsActivityStreamResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GroupsActivityStreamResponse from a JSON string
groups_activity_stream_response_instance = GroupsActivityStreamResponse.from_json(json)
# print the JSON string representation of the object
print(GroupsActivityStreamResponse.to_json())

# convert the object into a dict
groups_activity_stream_response_dict = groups_activity_stream_response_instance.to_dict()
# create an instance of GroupsActivityStreamResponse from a dict
groups_activity_stream_response_from_dict = GroupsActivityStreamResponse.from_dict(groups_activity_stream_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


