# SearchableCourse

A minimal representation of a Course for Canvas Apps search purposes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The Canvas DB ID | [optional] 
**name** | **str** | The course name | [optional] 
**sis_id** | **str** | The SIS ID of the course, if any. Only present if user can read or manage SIS. | [optional] 
**display_path** | **List[str]** | Names of the accounts in this course&#39;s account hierarchy, excluding the root. | [optional] 
**course_code** | **str** | The course code | [optional] 

## Example

```python
from canvas_lms_python_client.models.searchable_course import SearchableCourse

# TODO update the JSON string below
json = "{}"
# create an instance of SearchableCourse from a JSON string
searchable_course_instance = SearchableCourse.from_json(json)
# print the JSON string representation of the object
print(SearchableCourse.to_json())

# convert the object into a dict
searchable_course_dict = searchable_course_instance.to_dict()
# create an instance of SearchableCourse from a dict
searchable_course_from_dict = SearchableCourse.from_dict(searchable_course_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


