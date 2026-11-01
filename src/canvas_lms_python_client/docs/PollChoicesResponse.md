# PollChoicesResponse

Paginated `poll_choices` list response (from the Canvas example response).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**poll_choices** | [**List[PollChoice]**](PollChoice.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.poll_choices_response import PollChoicesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PollChoicesResponse from a JSON string
poll_choices_response_instance = PollChoicesResponse.from_json(json)
# print the JSON string representation of the object
print(PollChoicesResponse.to_json())

# convert the object into a dict
poll_choices_response_dict = poll_choices_response_instance.to_dict()
# create an instance of PollChoicesResponse from a dict
poll_choices_response_from_dict = PollChoicesResponse.from_dict(poll_choices_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


