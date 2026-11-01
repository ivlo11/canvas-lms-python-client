# PollsResponse

Paginated `polls` list response (from the Canvas example response).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**polls** | [**List[Poll]**](Poll.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.polls_response import PollsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PollsResponse from a JSON string
polls_response_instance = PollsResponse.from_json(json)
# print the JSON string representation of the object
print(PollsResponse.to_json())

# convert the object into a dict
polls_response_dict = polls_response_instance.to_dict()
# create an instance of PollsResponse from a dict
polls_response_from_dict = PollsResponse.from_dict(polls_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


