# MultipleGradeableStudent

A student's display fields with the requested assignments they can submit.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the user. | [optional] 
**anonymous_id** | **str** | The anonymous ID of the user, for use in anonymous grading. | [optional] 
**display_name** | **str** | The name of the user, as it should be displayed. | [optional] 
**avatar_image_url** | **str** | The URL of the user&#39;s avatar image. | [optional] 
**html_url** | **str** | The URL of the user&#39;s page in the course. | [optional] 
**pronouns** | **str** | The user&#39;s pronouns, if pronouns are enabled. | [optional] 
**fake_student** | **bool** | Optional: true if the user is the course&#39;s test student. Only included for test students. | [optional] 
**assignment_ids** | **List[int]** | The IDs of the requested assignments this student can submit. | [optional] 

## Example

```python
from canvas_lms_python_client.models.multiple_gradeable_student import MultipleGradeableStudent

# TODO update the JSON string below
json = "{}"
# create an instance of MultipleGradeableStudent from a JSON string
multiple_gradeable_student_instance = MultipleGradeableStudent.from_json(json)
# print the JSON string representation of the object
print(MultipleGradeableStudent.to_json())

# convert the object into a dict
multiple_gradeable_student_dict = multiple_gradeable_student_instance.to_dict()
# create an instance of MultipleGradeableStudent from a dict
multiple_gradeable_student_from_dict = MultipleGradeableStudent.from_dict(multiple_gradeable_student_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


