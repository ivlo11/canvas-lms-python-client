# Grades


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current** | [**Grade**](Grade.md) |  | [optional] 
**current_groups** | [**GradeGroup**](GradeGroup.md) |  | [optional] 
**final** | [**Grade**](Grade.md) |  | [optional] 
**final_groups** | [**GradeGroup**](GradeGroup.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.grades import Grades

# TODO update the JSON string below
json = "{}"
# create an instance of Grades from a JSON string
grades_instance = Grades.from_json(json)
# print the JSON string representation of the object
print(Grades.to_json())

# convert the object into a dict
grades_dict = grades_instance.to_dict()
# create an instance of Grades from a dict
grades_from_dict = Grades.from_dict(grades_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


