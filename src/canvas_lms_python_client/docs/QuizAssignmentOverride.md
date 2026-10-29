# QuizAssignmentOverride

Set of assignment-overridden dates for a quiz.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the assignment override, unless this is the base construct, in which case the &#39;id&#39; field is omitted. | [optional] 
**due_at** | **datetime** | The date after which any quiz submission is considered late. | [optional] 
**unlock_at** | **datetime** | Date when the quiz becomes available for taking. | [optional] 
**lock_at** | **datetime** | When the quiz will stop being available for taking. A value of null means it can always be taken. | [optional] 
**title** | **str** | Title of the section this assignment override is for, if any. | [optional] 
**base** | **bool** | If this property is present, it means that dates in this structure are not based on an assignment override, but are instead for all students. | [optional] 

## Example

```python
from canvas_lms_python_client.models.quiz_assignment_override import QuizAssignmentOverride

# TODO update the JSON string below
json = "{}"
# create an instance of QuizAssignmentOverride from a JSON string
quiz_assignment_override_instance = QuizAssignmentOverride.from_json(json)
# print the JSON string representation of the object
print(QuizAssignmentOverride.to_json())

# convert the object into a dict
quiz_assignment_override_dict = quiz_assignment_override_instance.to_dict()
# create an instance of QuizAssignmentOverride from a dict
quiz_assignment_override_from_dict = QuizAssignmentOverride.from_dict(quiz_assignment_override_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


