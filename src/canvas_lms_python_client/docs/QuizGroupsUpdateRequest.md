# QuizGroupsUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quiz_groups_name** | **str** | The name of the question group. | [optional] 
**quiz_groups_pick_count** | **int** | The number of questions to randomly select for this group. | [optional] 
**quiz_groups_question_points** | **int** | The number of points to assign to each question in the group. | [optional] 

## Example

```python
from canvas_lms_python_client.models.quiz_groups_update_request import QuizGroupsUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QuizGroupsUpdateRequest from a JSON string
quiz_groups_update_request_instance = QuizGroupsUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(QuizGroupsUpdateRequest.to_json())

# convert the object into a dict
quiz_groups_update_request_dict = quiz_groups_update_request_instance.to_dict()
# create an instance of QuizGroupsUpdateRequest from a dict
quiz_groups_update_request_from_dict = QuizGroupsUpdateRequest.from_dict(quiz_groups_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


