# QuizAssignmentOverrideSetContainer

Container for set of assignment-overridden dates for a quiz.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quiz_assignment_overrides** | [**List[QuizAssignmentOverrideSet]**](QuizAssignmentOverrideSet.md) | The QuizAssignmentOverrideSet | [optional] 

## Example

```python
from canvas_lms_python_client.models.quiz_assignment_override_set_container import QuizAssignmentOverrideSetContainer

# TODO update the JSON string below
json = "{}"
# create an instance of QuizAssignmentOverrideSetContainer from a JSON string
quiz_assignment_override_set_container_instance = QuizAssignmentOverrideSetContainer.from_json(json)
# print the JSON string representation of the object
print(QuizAssignmentOverrideSetContainer.to_json())

# convert the object into a dict
quiz_assignment_override_set_container_dict = quiz_assignment_override_set_container_instance.to_dict()
# create an instance of QuizAssignmentOverrideSetContainer from a dict
quiz_assignment_override_set_container_from_dict = QuizAssignmentOverrideSetContainer.from_dict(quiz_assignment_override_set_container_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


