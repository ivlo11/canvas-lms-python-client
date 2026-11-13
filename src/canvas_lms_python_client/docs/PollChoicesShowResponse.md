# PollChoicesShowResponse

Object response with `poll_choices`, `meta` (from the Canvas `@returns`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**poll_choices** | [**List[PollChoice]**](PollChoice.md) |  | [optional] 
**meta** | **object** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.poll_choices_show_response import PollChoicesShowResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PollChoicesShowResponse from a JSON string
poll_choices_show_response_instance = PollChoicesShowResponse.from_json(json)
# print the JSON string representation of the object
print(PollChoicesShowResponse.to_json())

# convert the object into a dict
poll_choices_show_response_dict = poll_choices_show_response_instance.to_dict()
# create an instance of PollChoicesShowResponse from a dict
poll_choices_show_response_from_dict = PollChoicesShowResponse.from_dict(poll_choices_show_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


