# CourseAttributes

Attributes of a course object.  See Courses API for more details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique Canvas identifier for the origin course | [optional] 
**name** | **str** | The name of the origin course. | [optional] 
**sis_id** | **str** | The sis id of the origin_course. | [optional] 
**integration_id** | **str** | The integration ID of the origin_course. | [optional] 

## Example

```python
from canvas_lms_python_client.models.course_attributes import CourseAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of CourseAttributes from a JSON string
course_attributes_instance = CourseAttributes.from_json(json)
# print the JSON string representation of the object
print(CourseAttributes.to_json())

# convert the object into a dict
course_attributes_dict = course_attributes_instance.to_dict()
# create an instance of CourseAttributes from a dict
course_attributes_from_dict = CourseAttributes.from_dict(course_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


