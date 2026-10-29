# PollSession


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for the poll session. | 
**poll_id** | **int** | The id of the Poll this poll session is associated with | 
**course_id** | **int** | The id of the Course this poll session is associated with | 
**course_section_id** | **int** | The id of the Course Section this poll session is associated with | [optional] 
**is_published** | **bool** | Specifies whether or not this poll session has been published for students to participate in. | [optional] 
**has_public_results** | **bool** | Specifies whether the results are viewable by students. | [optional] 
**created_at** | **datetime** | The time at which the poll session was created. | [optional] 
**results** | **object** | The results of the submissions of the poll. Each key is the poll choice id, and the value is the count of submissions. | [optional] 
**poll_submissions** | [**PollSubmission**](PollSubmission.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.poll_session import PollSession

# TODO update the JSON string below
json = "{}"
# create an instance of PollSession from a JSON string
poll_session_instance = PollSession.from_json(json)
# print the JSON string representation of the object
print(PollSession.to_json())

# convert the object into a dict
poll_session_dict = poll_session_instance.to_dict()
# create an instance of PollSession from a dict
poll_session_from_dict = PollSession.from_dict(poll_session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


