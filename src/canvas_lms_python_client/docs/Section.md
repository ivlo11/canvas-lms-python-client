# Section



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for the section. | [optional] 
**name** | **str** | The name of the section. | [optional] 
**sis_section_id** | **str** | The sis id of the section. This field is only included if the user has permission to view SIS information. | [optional] 
**integration_id** | **str** | Optional: The integration ID of the section. This field is only included if the user has permission to view SIS information. | [optional] 
**sis_import_id** | **int** | The unique identifier for the SIS import if created through SIS. This field is only included if the user has permission to manage SIS information. | [optional] 
**course_id** | **int** | The unique Canvas identifier for the course in which the section belongs | [optional] 
**sis_course_id** | **str** | The unique SIS identifier for the course in which the section belongs. This field is only included if the user has permission to view SIS information. | [optional] 
**start_at** | **datetime** | the start date for the section, if applicable | [optional] 
**end_at** | **datetime** | the end date for the section, if applicable | [optional] 
**restrict_enrollments_to_section_dates** | **bool** | Restrict user enrollments to the start and end dates of the section | [optional] 
**nonxlist_course_id** | **int** | The unique identifier of the original course of a cross-listed section | [optional] 
**total_students** | **int** | optional: the total number of active and invited students in the section | [optional] 
**students** | [**List[User]**](User.md) | optional: A list of students that are included in the section. Returned only if include[]&#x3D;students. WARNING: this collection&#39;s size is capped (if there are an extremely large number of users in the section (thousands) not all of them will be returned). If you need to capture all the users in a section with certainty or experiencing slow response consider using the paginated /api/v1/sections/&lt;section_id&gt;/users endpoint. | [optional] 
**created_at** | **str** |  | [optional] 
**permissions** | **object** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.section import Section

# TODO update the JSON string below
json = "{}"
# create an instance of Section from a JSON string
section_instance = Section.from_json(json)
# print the JSON string representation of the object
print(Section.to_json())

# convert the object into a dict
section_dict = section_instance.to_dict()
# create an instance of Section from a dict
section_from_dict = Section.from_dict(section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


