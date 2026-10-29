# CourseNickname



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**course_id** | **int** | the ID of the course | [optional] 
**name** | **str** | the actual name of the course | [optional] 
**nickname** | **str** | the calling user&#39;s nickname for the course | [optional] 

## Example

```python
from canvas_lms_python_client.models.course_nickname import CourseNickname

# TODO update the JSON string below
json = "{}"
# create an instance of CourseNickname from a JSON string
course_nickname_instance = CourseNickname.from_json(json)
# print the JSON string representation of the object
print(CourseNickname.to_json())

# convert the object into a dict
course_nickname_dict = course_nickname_instance.to_dict()
# create an instance of CourseNickname from a dict
course_nickname_from_dict = CourseNickname.from_dict(course_nickname_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


