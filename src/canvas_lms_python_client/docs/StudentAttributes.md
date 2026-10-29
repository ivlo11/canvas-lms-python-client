# StudentAttributes

Attributes of student.  See Users API for more details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | The unique Canvas identifier for the user | [optional] 
**sis_user_id** | **str** | The SIS ID associated with the user.  This field is only included if the user came from a SIS import and has permissions to view SIS information. | [optional] 

## Example

```python
from canvas_lms_python_client.models.student_attributes import StudentAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of StudentAttributes from a JSON string
student_attributes_instance = StudentAttributes.from_json(json)
# print the JSON string representation of the object
print(StudentAttributes.to_json())

# convert the object into a dict
student_attributes_dict = student_attributes_instance.to_dict()
# create an instance of StudentAttributes from a dict
student_attributes_from_dict = StudentAttributes.from_dict(student_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


