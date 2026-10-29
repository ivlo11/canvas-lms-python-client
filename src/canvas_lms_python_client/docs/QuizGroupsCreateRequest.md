# QuizGroupsCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quiz_groups_name** | **str** | The name of the question group. | [optional] 
**quiz_groups_pick_count** | **int** | The number of questions to randomly select for this group. | [optional] 
**quiz_groups_question_points** | **int** | The number of points to assign to each question in the group. | [optional] 
**quiz_groups_assessment_question_bank_id** | **int** | The id of the assessment question bank to pull questions from. | [optional] 

## Example

```python
from canvas_lms_python_client.models.quiz_groups_create_request import QuizGroupsCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QuizGroupsCreateRequest from a JSON string
quiz_groups_create_request_instance = QuizGroupsCreateRequest.from_json(json)
# print the JSON string representation of the object
print(QuizGroupsCreateRequest.to_json())

# convert the object into a dict
quiz_groups_create_request_dict = quiz_groups_create_request_instance.to_dict()
# create an instance of QuizGroupsCreateRequest from a dict
quiz_groups_create_request_from_dict = QuizGroupsCreateRequest.from_dict(quiz_groups_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


