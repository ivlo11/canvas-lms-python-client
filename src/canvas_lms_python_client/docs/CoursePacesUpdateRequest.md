# CoursePacesUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**course_pace_id** | **int** | The id of the course pace | 
**end_date** | **str** | End date of the course pace | [optional] 
**exclude_weekends** | **bool** | Course pace dates excludes weekends if true | [optional] 
**selected_days_to_skip** | **List[str]** | Course pace dates excludes weekends if true | [optional] 
**hard_end_dates** | **bool** | Course pace uess hard end dates if true | [optional] 
**workflow_state** | **str** | The state of the course pace | [optional] 
**course_pace_module_item_attributes** | **List[str]** | Module Items attributes | [optional] 

## Example

```python
from canvas_lms_python_client.models.course_paces_update_request import CoursePacesUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CoursePacesUpdateRequest from a JSON string
course_paces_update_request_instance = CoursePacesUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(CoursePacesUpdateRequest.to_json())

# convert the object into a dict
course_paces_update_request_dict = course_paces_update_request_instance.to_dict()
# create an instance of CoursePacesUpdateRequest from a dict
course_paces_update_request_from_dict = CoursePacesUpdateRequest.from_dict(course_paces_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


