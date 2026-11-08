# PollSession


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the poll session. | 
**poll_id** | **str** | The id of the Poll this poll session is associated with | 
**course_id** | **str** | The id of the Course this poll session is associated with | 
**course_section_id** | **str** | The id of the Course Section this poll session is associated with | [optional] 
**is_published** | **bool** | Specifies whether or not this poll session has been published for students to participate in. | [optional] 
**has_public_results** | **bool** | Specifies whether the results are viewable by students. | [optional] 
**created_at** | **datetime** | The time at which the poll session was created. | [optional] 
**results** | **object** | The results of the submissions of the poll. Each key is the poll choice id, and the value is the count of submissions. | [optional] 
**poll_submissions** | [**List[PollSubmission]**](PollSubmission.md) | If the poll session has public results, this will return an array of all submissions, viewable by both students and teachers. If the results are not public, for students it will return their submission only. | [optional] 
**has_submitted** | **bool** |  | [optional] 

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


