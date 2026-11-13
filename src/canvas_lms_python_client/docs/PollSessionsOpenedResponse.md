# PollSessionsOpenedResponse

Paginated `poll_sessions` list response (from the Canvas example response).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**poll_sessions** | [**List[PollSession]**](PollSession.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.poll_sessions_opened_response import PollSessionsOpenedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PollSessionsOpenedResponse from a JSON string
poll_sessions_opened_response_instance = PollSessionsOpenedResponse.from_json(json)
# print the JSON string representation of the object
print(PollSessionsOpenedResponse.to_json())

# convert the object into a dict
poll_sessions_opened_response_dict = poll_sessions_opened_response_instance.to_dict()
# create an instance of PollSessionsOpenedResponse from a dict
poll_sessions_opened_response_from_dict = PollSessionsOpenedResponse.from_dict(poll_sessions_opened_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


