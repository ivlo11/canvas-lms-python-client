# PollsCreateResponse

Object response with `polls`, `meta` (from the Canvas `@returns`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**polls** | [**List[Poll]**](Poll.md) |  | [optional] 
**meta** | **object** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.polls_create_response import PollsCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PollsCreateResponse from a JSON string
polls_create_response_instance = PollsCreateResponse.from_json(json)
# print the JSON string representation of the object
print(PollsCreateResponse.to_json())

# convert the object into a dict
polls_create_response_dict = polls_create_response_instance.to_dict()
# create an instance of PollsCreateResponse from a dict
polls_create_response_from_dict = PollsCreateResponse.from_dict(polls_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


