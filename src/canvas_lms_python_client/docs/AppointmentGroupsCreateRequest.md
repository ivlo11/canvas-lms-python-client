# AppointmentGroupsCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appointment_group** | [**AppointmentGroupsCreateRequestAppointmentGroup**](AppointmentGroupsCreateRequestAppointmentGroup.md) |  | 

## Example

```python
from canvas_lms_python_client.models.appointment_groups_create_request import AppointmentGroupsCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppointmentGroupsCreateRequest from a JSON string
appointment_groups_create_request_instance = AppointmentGroupsCreateRequest.from_json(json)
# print the JSON string representation of the object
print(AppointmentGroupsCreateRequest.to_json())

# convert the object into a dict
appointment_groups_create_request_dict = appointment_groups_create_request_instance.to_dict()
# create an instance of AppointmentGroupsCreateRequest from a dict
appointment_groups_create_request_from_dict = AppointmentGroupsCreateRequest.from_dict(appointment_groups_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


