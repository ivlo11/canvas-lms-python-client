# GradeGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**submission_id** | [**AssignmentGroupGrade**](AssignmentGroupGrade.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.grade_group import GradeGroup

# TODO update the JSON string below
json = "{}"
# create an instance of GradeGroup from a JSON string
grade_group_instance = GradeGroup.from_json(json)
# print the JSON string representation of the object
print(GradeGroup.to_json())

# convert the object into a dict
grade_group_dict = grade_group_instance.to_dict()
# create an instance of GradeGroup from a dict
grade_group_from_dict = GradeGroup.from_dict(grade_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


