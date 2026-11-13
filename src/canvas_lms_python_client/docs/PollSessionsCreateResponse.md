# PollSessionsCreateResponse

Object response with `poll_sessions`, `meta` (from the Canvas `@returns`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**poll_sessions** | [**List[PollSession]**](PollSession.md) |  | [optional] 
**meta** | **object** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.poll_sessions_create_response import PollSessionsCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PollSessionsCreateResponse from a JSON string
poll_sessions_create_response_instance = PollSessionsCreateResponse.from_json(json)
# print the JSON string representation of the object
print(PollSessionsCreateResponse.to_json())

# convert the object into a dict
poll_sessions_create_response_dict = poll_sessions_create_response_instance.to_dict()
# create an instance of PollSessionsCreateResponse from a dict
poll_sessions_create_response_from_dict = PollSessionsCreateResponse.from_dict(poll_sessions_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


