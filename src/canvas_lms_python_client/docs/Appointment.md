# Appointment

Date and time for an appointment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The appointment identifier. | [optional] 
**start_at** | **datetime** | Start time for the appointment | [optional] 
**end_at** | **datetime** | End time for the appointment | [optional] 

## Example

```python
from canvas_lms_python_client.models.appointment import Appointment

# TODO update the JSON string below
json = "{}"
# create an instance of Appointment from a JSON string
appointment_instance = Appointment.from_json(json)
# print the JSON string representation of the object
print(Appointment.to_json())

# convert the object into a dict
appointment_dict = appointment_instance.to_dict()
# create an instance of Appointment from a dict
appointment_from_dict = Appointment.from_dict(appointment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


