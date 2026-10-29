# AppointmentGroupsUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appointment_group** | [**AppointmentGroupsUpdateRequestAppointmentGroup**](AppointmentGroupsUpdateRequestAppointmentGroup.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.appointment_groups_update_request import AppointmentGroupsUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppointmentGroupsUpdateRequest from a JSON string
appointment_groups_update_request_instance = AppointmentGroupsUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(AppointmentGroupsUpdateRequest.to_json())

# convert the object into a dict
appointment_groups_update_request_dict = appointment_groups_update_request_instance.to_dict()
# create an instance of AppointmentGroupsUpdateRequest from a dict
appointment_groups_update_request_from_dict = AppointmentGroupsUpdateRequest.from_dict(appointment_groups_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


