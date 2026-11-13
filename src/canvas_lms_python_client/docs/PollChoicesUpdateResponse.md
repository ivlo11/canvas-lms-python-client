# PollChoicesUpdateResponse

Object response with `poll_choices`, `meta` (from the Canvas `@returns`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**poll_choices** | [**List[PollChoice]**](PollChoice.md) |  | [optional] 
**meta** | **object** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.poll_choices_update_response import PollChoicesUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PollChoicesUpdateResponse from a JSON string
poll_choices_update_response_instance = PollChoicesUpdateResponse.from_json(json)
# print the JSON string representation of the object
print(PollChoicesUpdateResponse.to_json())

# convert the object into a dict
poll_choices_update_response_dict = poll_choices_update_response_instance.to_dict()
# create an instance of PollChoicesUpdateResponse from a dict
poll_choices_update_response_from_dict = PollChoicesUpdateResponse.from_dict(poll_choices_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


