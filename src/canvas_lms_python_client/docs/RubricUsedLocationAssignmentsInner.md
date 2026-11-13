# RubricUsedLocationAssignmentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The assignment&#39;s id | [optional] 
**title** | **str** | The assignment&#39;s title | [optional] 

## Example

```python
from canvas_lms_python_client.models.rubric_used_location_assignments_inner import RubricUsedLocationAssignmentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RubricUsedLocationAssignmentsInner from a JSON string
rubric_used_location_assignments_inner_instance = RubricUsedLocationAssignmentsInner.from_json(json)
# print the JSON string representation of the object
print(RubricUsedLocationAssignmentsInner.to_json())

# convert the object into a dict
rubric_used_location_assignments_inner_dict = rubric_used_location_assignments_inner_instance.to_dict()
# create an instance of RubricUsedLocationAssignmentsInner from a dict
rubric_used_location_assignments_inner_from_dict = RubricUsedLocationAssignmentsInner.from_dict(rubric_used_location_assignments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


