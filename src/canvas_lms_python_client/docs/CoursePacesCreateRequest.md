# CoursePacesCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_date** | **str** | End date of the course pace | [optional] 
**end_date_context** | **str** | End date context (course, section, hupothetical) | [optional] 
**start_date** | **str** | Start date of the course pace | [optional] 
**start_date_context** | **str** | Start date context (course, section, hupothetical) | [optional] 
**exclude_weekends** | **bool** | Course pace dates excludes weekends if true | [optional] 
**selected_days_to_skip** | **List[str]** | Course pace dates excludes weekends if true | [optional] 
**hard_end_dates** | **bool** | Course pace uess hard end dates if true | [optional] 
**workflow_state** | **str** | The state of the course pace | [optional] 
**course_pace_module_item_attributes** | **List[str]** | Module Items attributes | [optional] 
**context_id** | **int** | Pace Context ID | [optional] 
**context_type** | **str** | Pace Context Type (Course, Section, User) | [optional] 

## Example

```python
from canvas_lms_python_client.models.course_paces_create_request import CoursePacesCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CoursePacesCreateRequest from a JSON string
course_paces_create_request_instance = CoursePacesCreateRequest.from_json(json)
# print the JSON string representation of the object
print(CoursePacesCreateRequest.to_json())

# convert the object into a dict
course_paces_create_request_dict = course_paces_create_request_instance.to_dict()
# create an instance of CoursePacesCreateRequest from a dict
course_paces_create_request_from_dict = CoursePacesCreateRequest.from_dict(course_paces_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


