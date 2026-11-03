# PaceContext

A course, section or student enrollment that can be paced.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the context. | [optional] 
**type** | **str** | The type of the context: Course, CourseSection or StudentEnrollment. | [optional] 
**item_id** | **int** | The ID of the course, section or enrollment. | [optional] 
**associated_section_count** | **int** | The number of sections in the course. Null for sections and enrollments. | [optional] 
**associated_student_count** | **int** | The number of students in the course or section. Null for enrollments. | [optional] 
**applied_pace** | [**AppliedPace**](AppliedPace.md) |  | [optional] 
**on_pace** | **bool** | Whether the student is on pace. Null for courses and sections. | [optional] 

## Example

```python
from canvas_lms_python_client.models.pace_context import PaceContext

# TODO update the JSON string below
json = "{}"
# create an instance of PaceContext from a JSON string
pace_context_instance = PaceContext.from_json(json)
# print the JSON string representation of the object
print(PaceContext.to_json())

# convert the object into a dict
pace_context_dict = pace_context_instance.to_dict()
# create an instance of PaceContext from a dict
pace_context_from_dict = PaceContext.from_dict(pace_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


