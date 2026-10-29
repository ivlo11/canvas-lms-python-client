# CspSettingsSetCspLockRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settings_locked** | **bool** | Whether sub-accounts and courses will be prevented from overriding settings inherited from this account. | 

## Example

```python
from canvas_lms_python_client.models.csp_settings_set_csp_lock_request import CspSettingsSetCspLockRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CspSettingsSetCspLockRequest from a JSON string
csp_settings_set_csp_lock_request_instance = CspSettingsSetCspLockRequest.from_json(json)
# print the JSON string representation of the object
print(CspSettingsSetCspLockRequest.to_json())

# convert the object into a dict
csp_settings_set_csp_lock_request_dict = csp_settings_set_csp_lock_request_instance.to_dict()
# create an instance of CspSettingsSetCspLockRequest from a dict
csp_settings_set_csp_lock_request_from_dict = CspSettingsSetCspLockRequest.from_dict(csp_settings_set_csp_lock_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


