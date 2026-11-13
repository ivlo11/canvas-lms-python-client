# PollsShowResponse

Paginated `polls` list response (from the Canvas example response).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**polls** | [**List[Poll]**](Poll.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.polls_show_response import PollsShowResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PollsShowResponse from a JSON string
polls_show_response_instance = PollsShowResponse.from_json(json)
# print the JSON string representation of the object
print(PollsShowResponse.to_json())

# convert the object into a dict
polls_show_response_dict = polls_show_response_instance.to_dict()
# create an instance of PollsShowResponse from a dict
polls_show_response_from_dict = PollsShowResponse.from_dict(polls_show_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


