# QuizGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the question group. | 
**quiz_id** | **int** | The ID of the Quiz the question group belongs to. | 
**name** | **str** | The name of the question group. | [optional] 
**pick_count** | **int** | The number of questions to pick from the group to display to the student. | [optional] 
**question_points** | **float** | The amount of points allotted to each question in the group. | [optional] 
**assessment_question_bank_id** | **int** | The ID of the Assessment question bank to pull questions from. | [optional] 
**position** | **int** | The order in which the question group will be retrieved and displayed. | [optional] 

## Example

```python
from canvas_lms_python_client.models.quiz_group import QuizGroup

# TODO update the JSON string below
json = "{}"
# create an instance of QuizGroup from a JSON string
quiz_group_instance = QuizGroup.from_json(json)
# print the JSON string representation of the object
print(QuizGroup.to_json())

# convert the object into a dict
quiz_group_dict = quiz_group_instance.to_dict()
# create an instance of QuizGroup from a dict
quiz_group_from_dict = QuizGroup.from_dict(quiz_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


