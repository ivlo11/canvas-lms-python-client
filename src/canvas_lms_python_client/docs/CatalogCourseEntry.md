# CatalogCourseEntry

An item in the course catalog list. Canvas wraps each course in a \"course\" key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**course** | [**CatalogCourse**](CatalogCourse.md) |  | 

## Example

```python
from canvas_lms_python_client.models.catalog_course_entry import CatalogCourseEntry

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogCourseEntry from a JSON string
catalog_course_entry_instance = CatalogCourseEntry.from_json(json)
# print the JSON string representation of the object
print(CatalogCourseEntry.to_json())

# convert the object into a dict
catalog_course_entry_dict = catalog_course_entry_instance.to_dict()
# create an instance of CatalogCourseEntry from a dict
catalog_course_entry_from_dict = CatalogCourseEntry.from_dict(catalog_course_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


