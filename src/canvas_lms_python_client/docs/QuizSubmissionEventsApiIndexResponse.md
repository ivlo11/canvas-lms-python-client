# QuizSubmissionEventsApiIndexResponse

Object response with `quiz_submission_events` (from the Canvas `@returns`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quiz_submission_events** | [**List[QuizSubmissionEvent]**](QuizSubmissionEvent.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.quiz_submission_events_api_index_response import QuizSubmissionEventsApiIndexResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QuizSubmissionEventsApiIndexResponse from a JSON string
quiz_submission_events_api_index_response_instance = QuizSubmissionEventsApiIndexResponse.from_json(json)
# print the JSON string representation of the object
print(QuizSubmissionEventsApiIndexResponse.to_json())

# convert the object into a dict
quiz_submission_events_api_index_response_dict = quiz_submission_events_api_index_response_instance.to_dict()
# create an instance of QuizSubmissionEventsApiIndexResponse from a dict
quiz_submission_events_api_index_response_from_dict = QuizSubmissionEventsApiIndexResponse.from_dict(quiz_submission_events_api_index_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


