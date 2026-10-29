# QuizSubmissionEventsApiCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quiz_submission_events** | **List[List[str]]** | The submission events to be recorded | 

## Example

```python
from canvas_lms_python_client.models.quiz_submission_events_api_create_request import QuizSubmissionEventsApiCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QuizSubmissionEventsApiCreateRequest from a JSON string
quiz_submission_events_api_create_request_instance = QuizSubmissionEventsApiCreateRequest.from_json(json)
# print the JSON string representation of the object
print(QuizSubmissionEventsApiCreateRequest.to_json())

# convert the object into a dict
quiz_submission_events_api_create_request_dict = quiz_submission_events_api_create_request_instance.to_dict()
# create an instance of QuizSubmissionEventsApiCreateRequest from a dict
quiz_submission_events_api_create_request_from_dict = QuizSubmissionEventsApiCreateRequest.from_dict(quiz_submission_events_api_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


