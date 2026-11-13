# QuizSubmissionEvent

An event passed from the Quiz Submission take page

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the event. | [optional] 
**created_at** | **datetime** | a timestamp record of creation time | [optional] 
**event_type** | **str** | the type of event being sent | [optional] 
**event_data** | **object** | custom contextual data for the specific event type. Its shape depends on event_type: a list of answers for question_answered, an object for question_flagged and submission_created, and null for page_blurred and page_focused. | [optional] 

## Example

```python
from canvas_lms_python_client.models.quiz_submission_event import QuizSubmissionEvent

# TODO update the JSON string below
json = "{}"
# create an instance of QuizSubmissionEvent from a JSON string
quiz_submission_event_instance = QuizSubmissionEvent.from_json(json)
# print the JSON string representation of the object
print(QuizSubmissionEvent.to_json())

# convert the object into a dict
quiz_submission_event_dict = quiz_submission_event_instance.to_dict()
# create an instance of QuizSubmissionEvent from a dict
quiz_submission_event_from_dict = QuizSubmissionEvent.from_dict(quiz_submission_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


