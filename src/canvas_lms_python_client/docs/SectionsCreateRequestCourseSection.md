# SectionsCreateRequestCourseSection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | [String] The name of the section | [optional] 
**sis_section_id** | **str** | [String] The sis ID of the section. Must have manage_sis permission to set. This is ignored if caller does not have permission to set. | [optional] 
**integration_id** | **str** | [String] The integration_id of the section. Must have manage_sis permission to set. This is ignored if caller does not have permission to set. | [optional] 
**start_at** | **str** | [DateTime] Section start date in ISO8601 format, e.g. 2011-01-01T01:00Z | [optional] 
**end_at** | **str** | [DateTime] Section end date in ISO8601 format. e.g. 2011-01-01T01:00Z | [optional] 
**restrict_enrollments_to_section_dates** | **bool** | [Boolean] Set to true to restrict user enrollments to the start and end dates of the section. | [optional] 

## Example

```python
from canvas_lms_python_client.models.sections_create_request_course_section import SectionsCreateRequestCourseSection

# TODO update the JSON string below
json = "{}"
# create an instance of SectionsCreateRequestCourseSection from a JSON string
sections_create_request_course_section_instance = SectionsCreateRequestCourseSection.from_json(json)
# print the JSON string representation of the object
print(SectionsCreateRequestCourseSection.to_json())

# convert the object into a dict
sections_create_request_course_section_dict = sections_create_request_course_section_instance.to_dict()
# create an instance of SectionsCreateRequestCourseSection from a dict
sections_create_request_course_section_from_dict = SectionsCreateRequestCourseSection.from_dict(sections_create_request_course_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


