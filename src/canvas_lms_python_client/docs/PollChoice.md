# PollChoice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for the poll choice. | 
**poll_id** | **int** | The id of the poll this poll choice belongs to. | 
**is_correct** | **bool** | Specifies whether or not this poll choice is a &#39;correct&#39; choice. | [optional] 
**text** | **str** | The text of the poll choice. | 
**position** | **int** | The order of the poll choice in relation to it&#39;s sibling poll choices. | [optional] 

## Example

```python
from canvas_lms_python_client.models.poll_choice import PollChoice

# TODO update the JSON string below
json = "{}"
# create an instance of PollChoice from a JSON string
poll_choice_instance = PollChoice.from_json(json)
# print the JSON string representation of the object
print(PollChoice.to_json())

# convert the object into a dict
poll_choice_dict = poll_choice_instance.to_dict()
# create an instance of PollChoice from a dict
poll_choice_from_dict = PollChoice.from_dict(poll_choice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


