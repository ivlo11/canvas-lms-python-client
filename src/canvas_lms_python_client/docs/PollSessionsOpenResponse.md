# PollSessionsOpenResponse

Object response with `poll_sessions`, `meta` (from the Canvas `@returns`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**poll_sessions** | [**List[PollSession]**](PollSession.md) |  | [optional] 
**meta** | **object** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.poll_sessions_open_response import PollSessionsOpenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PollSessionsOpenResponse from a JSON string
poll_sessions_open_response_instance = PollSessionsOpenResponse.from_json(json)
# print the JSON string representation of the object
print(PollSessionsOpenResponse.to_json())

# convert the object into a dict
poll_sessions_open_response_dict = poll_sessions_open_response_instance.to_dict()
# create an instance of PollSessionsOpenResponse from a dict
poll_sessions_open_response_from_dict = PollSessionsOpenResponse.from_dict(poll_sessions_open_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


