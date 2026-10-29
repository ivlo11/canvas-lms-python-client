# RegistrationsBindRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_state** | **str** | The desired state for this registration/account binding. | 

## Example

```python
from canvas_lms_python_client.models.registrations_bind_request import RegistrationsBindRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RegistrationsBindRequest from a JSON string
registrations_bind_request_instance = RegistrationsBindRequest.from_json(json)
# print the JSON string representation of the object
print(RegistrationsBindRequest.to_json())

# convert the object into a dict
registrations_bind_request_dict = registrations_bind_request_instance.to_dict()
# create an instance of RegistrationsBindRequest from a dict
registrations_bind_request_from_dict = RegistrationsBindRequest.from_dict(registrations_bind_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


