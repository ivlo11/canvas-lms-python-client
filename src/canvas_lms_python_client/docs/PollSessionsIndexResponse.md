# PollSessionsIndexResponse

Object response with `poll_sessions`, `meta` (from the Canvas `@returns`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**poll_sessions** | [**List[PollSession]**](PollSession.md) |  | [optional] 
**meta** | **object** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.poll_sessions_index_response import PollSessionsIndexResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PollSessionsIndexResponse from a JSON string
poll_sessions_index_response_instance = PollSessionsIndexResponse.from_json(json)
# print the JSON string representation of the object
print(PollSessionsIndexResponse.to_json())

# convert the object into a dict
poll_sessions_index_response_dict = poll_sessions_index_response_instance.to_dict()
# create an instance of PollSessionsIndexResponse from a dict
poll_sessions_index_response_from_dict = PollSessionsIndexResponse.from_dict(poll_sessions_index_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


