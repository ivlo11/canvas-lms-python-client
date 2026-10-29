# CoursePacesUpdateRequestSelectedDaysToSkip


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**array_string** | **str** | Course pace dates excludes weekends if true | [optional] 

## Example

```python
from canvas_lms_python_client.models.course_paces_update_request_selected_days_to_skip import CoursePacesUpdateRequestSelectedDaysToSkip

# TODO update the JSON string below
json = "{}"
# create an instance of CoursePacesUpdateRequestSelectedDaysToSkip from a JSON string
course_paces_update_request_selected_days_to_skip_instance = CoursePacesUpdateRequestSelectedDaysToSkip.from_json(json)
# print the JSON string representation of the object
print(CoursePacesUpdateRequestSelectedDaysToSkip.to_json())

# convert the object into a dict
course_paces_update_request_selected_days_to_skip_dict = course_paces_update_request_selected_days_to_skip_instance.to_dict()
# create an instance of CoursePacesUpdateRequestSelectedDaysToSkip from a dict
course_paces_update_request_selected_days_to_skip_from_dict = CoursePacesUpdateRequestSelectedDaysToSkip.from_dict(course_paces_update_request_selected_days_to_skip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


