# PollChoicesUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**poll_choices_text** | **str** | The descriptive text of the poll choice. | 
**poll_choices_is_correct** | **bool** | Whether this poll choice is considered correct or not.  Defaults to false. | [optional] 
**poll_choices_position** | **int** | The order this poll choice should be returned in the context it&#39;s sibling poll choices. | [optional] 

## Example

```python
from canvas_lms_python_client.models.poll_choices_update_request import PollChoicesUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PollChoicesUpdateRequest from a JSON string
poll_choices_update_request_instance = PollChoicesUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(PollChoicesUpdateRequest.to_json())

# convert the object into a dict
poll_choices_update_request_dict = poll_choices_update_request_instance.to_dict()
# create an instance of PollChoicesUpdateRequest from a dict
poll_choices_update_request_from_dict = PollChoicesUpdateRequest.from_dict(poll_choices_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


