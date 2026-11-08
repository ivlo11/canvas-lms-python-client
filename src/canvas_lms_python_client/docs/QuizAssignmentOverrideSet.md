# QuizAssignmentOverrideSet

Set of assignment-overridden dates for a quiz.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quiz_id** | [**QuizAssignmentOverrideSetQuizId**](QuizAssignmentOverrideSetQuizId.md) |  | [optional] 
**due_dates** | [**List[QuizAssignmentOverride]**](QuizAssignmentOverride.md) | An array of quiz assignment overrides. For students, this array will always contain a single item which is the set of dates that apply to that student. For teachers and staff, it may contain more. | [optional] 
**all_dates** | [**List[QuizAssignmentOverride]**](QuizAssignmentOverride.md) | An array of all assignment overrides active for the quiz. This is visible only to teachers and staff. | [optional] 

## Example

```python
from canvas_lms_python_client.models.quiz_assignment_override_set import QuizAssignmentOverrideSet

# TODO update the JSON string below
json = "{}"
# create an instance of QuizAssignmentOverrideSet from a JSON string
quiz_assignment_override_set_instance = QuizAssignmentOverrideSet.from_json(json)
# print the JSON string representation of the object
print(QuizAssignmentOverrideSet.to_json())

# convert the object into a dict
quiz_assignment_override_set_dict = quiz_assignment_override_set_instance.to_dict()
# create an instance of QuizAssignmentOverrideSet from a dict
quiz_assignment_override_set_from_dict = QuizAssignmentOverrideSet.from_dict(quiz_assignment_override_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


