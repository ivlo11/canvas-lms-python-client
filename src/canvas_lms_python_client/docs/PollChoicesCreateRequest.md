# PollChoicesCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**poll_choices_text** | **str** | The descriptive text of the poll choice. | 
**poll_choices_is_correct** | **bool** | Whether this poll choice is considered correct or not. Defaults to false. | [optional] 
**poll_choices_position** | **int** | The order this poll choice should be returned in the context it&#39;s sibling poll choices. | [optional] 

## Example

```python
from canvas_lms_python_client.models.poll_choices_create_request import PollChoicesCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PollChoicesCreateRequest from a JSON string
poll_choices_create_request_instance = PollChoicesCreateRequest.from_json(json)
# print the JSON string representation of the object
print(PollChoicesCreateRequest.to_json())

# convert the object into a dict
poll_choices_create_request_dict = poll_choices_create_request_instance.to_dict()
# create an instance of PollChoicesCreateRequest from a dict
poll_choices_create_request_from_dict = PollChoicesCreateRequest.from_dict(poll_choices_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


