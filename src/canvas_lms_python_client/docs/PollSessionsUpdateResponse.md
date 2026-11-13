# PollSessionsUpdateResponse

Object response with `poll_sessions`, `meta` (from the Canvas `@returns`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**poll_sessions** | [**List[PollSession]**](PollSession.md) |  | [optional] 
**meta** | **object** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.poll_sessions_update_response import PollSessionsUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PollSessionsUpdateResponse from a JSON string
poll_sessions_update_response_instance = PollSessionsUpdateResponse.from_json(json)
# print the JSON string representation of the object
print(PollSessionsUpdateResponse.to_json())

# convert the object into a dict
poll_sessions_update_response_dict = poll_sessions_update_response_instance.to_dict()
# create an instance of PollSessionsUpdateResponse from a dict
poll_sessions_update_response_from_dict = PollSessionsUpdateResponse.from_dict(poll_sessions_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


