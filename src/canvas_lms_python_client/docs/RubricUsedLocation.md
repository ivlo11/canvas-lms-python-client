# RubricUsedLocation

A course where a rubric is used, with the assignments that use it

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The course&#39;s id | [optional] 
**name** | **str** | The course&#39;s name | [optional] 
**concluded** | **bool** | Whether the course has concluded | [optional] 
**assignments** | [**List[RubricUsedLocationAssignmentsInner]**](RubricUsedLocationAssignmentsInner.md) | The course&#39;s assignments that use the rubric | [optional] 

## Example

```python
from canvas_lms_python_client.models.rubric_used_location import RubricUsedLocation

# TODO update the JSON string below
json = "{}"
# create an instance of RubricUsedLocation from a JSON string
rubric_used_location_instance = RubricUsedLocation.from_json(json)
# print the JSON string representation of the object
print(RubricUsedLocation.to_json())

# convert the object into a dict
rubric_used_location_dict = rubric_used_location_instance.to_dict()
# create an instance of RubricUsedLocation from a dict
rubric_used_location_from_dict = RubricUsedLocation.from_dict(rubric_used_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


