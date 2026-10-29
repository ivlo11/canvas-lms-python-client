# AssignmentGroupGrade


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the Assignment Group | [optional] 
**global_id** | **int** | The global ID of the Assignment Group | [optional] 
**score** | **float** | The score for the Assignment Group | [optional] 
**possible** | **float** | The total points possible for the Assignment Group | [optional] 
**weight** | **float** | The weight for the Assignment Group | [optional] 
**grade** | **float** | The grade for the Assignment Group | [optional] 
**dropped** | **List[object]** | The dropped grades for the Assignment Group | [optional] 

## Example

```python
from canvas_lms_python_client.models.assignment_group_grade import AssignmentGroupGrade

# TODO update the JSON string below
json = "{}"
# create an instance of AssignmentGroupGrade from a JSON string
assignment_group_grade_instance = AssignmentGroupGrade.from_json(json)
# print the JSON string representation of the object
print(AssignmentGroupGrade.to_json())

# convert the object into a dict
assignment_group_grade_dict = assignment_group_grade_instance.to_dict()
# create an instance of AssignmentGroupGrade from a dict
assignment_group_grade_from_dict = AssignmentGroupGrade.from_dict(assignment_group_grade_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


