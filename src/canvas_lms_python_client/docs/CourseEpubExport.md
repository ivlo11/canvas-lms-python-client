# CourseEpubExport

Combination of a Course & EpubExport.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | the unique identifier for the course | [optional] 
**name** | **str** | the name for the course | [optional] 
**epub_export** | [**EpubExport**](EpubExport.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.course_epub_export import CourseEpubExport

# TODO update the JSON string below
json = "{}"
# create an instance of CourseEpubExport from a JSON string
course_epub_export_instance = CourseEpubExport.from_json(json)
# print the JSON string representation of the object
print(CourseEpubExport.to_json())

# convert the object into a dict
course_epub_export_dict = course_epub_export_instance.to_dict()
# create an instance of CourseEpubExport from a dict
course_epub_export_from_dict = CourseEpubExport.from_dict(course_epub_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


