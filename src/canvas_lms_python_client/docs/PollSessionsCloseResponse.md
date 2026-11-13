# PollSessionsCloseResponse

Paginated `poll_sessions` list response (from the Canvas example response).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**poll_sessions** | [**List[PollSession]**](PollSession.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.poll_sessions_close_response import PollSessionsCloseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PollSessionsCloseResponse from a JSON string
poll_sessions_close_response_instance = PollSessionsCloseResponse.from_json(json)
# print the JSON string representation of the object
print(PollSessionsCloseResponse.to_json())

# convert the object into a dict
poll_sessions_close_response_dict = poll_sessions_close_response_instance.to_dict()
# create an instance of PollSessionsCloseResponse from a dict
poll_sessions_close_response_from_dict = PollSessionsCloseResponse.from_dict(poll_sessions_close_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


