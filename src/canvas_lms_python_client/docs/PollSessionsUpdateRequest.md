# PollSessionsUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**poll_sessions_course_id** | **int** | The id of the course this session is associated with. | [optional] 
**poll_sessions_course_section_id** | **int** | The id of the course section this session is associated with. | [optional] 
**poll_sessions_has_public_results** | **bool** | Whether or not results are viewable by students. | [optional] 

## Example

```python
from canvas_lms_python_client.models.poll_sessions_update_request import PollSessionsUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PollSessionsUpdateRequest from a JSON string
poll_sessions_update_request_instance = PollSessionsUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(PollSessionsUpdateRequest.to_json())

# convert the object into a dict
poll_sessions_update_request_dict = poll_sessions_update_request_instance.to_dict()
# create an instance of PollSessionsUpdateRequest from a dict
poll_sessions_update_request_from_dict = PollSessionsUpdateRequest.from_dict(poll_sessions_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


