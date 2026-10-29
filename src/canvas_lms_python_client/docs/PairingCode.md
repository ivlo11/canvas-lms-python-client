# PairingCode

A code used for linking a user to a student to observe them.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | The ID of the user. | [optional] 
**code** | **str** | The actual code to be sent to other APIs | [optional] 
**expires_at** | **datetime** | When the code expires | [optional] 
**workflow_state** | **str** | The current status of the code | [optional] 

## Example

```python
from canvas_lms_python_client.models.pairing_code import PairingCode

# TODO update the JSON string below
json = "{}"
# create an instance of PairingCode from a JSON string
pairing_code_instance = PairingCode.from_json(json)
# print the JSON string representation of the object
print(PairingCode.to_json())

# convert the object into a dict
pairing_code_dict = pairing_code_instance.to_dict()
# create an instance of PairingCode from a dict
pairing_code_from_dict = PairingCode.from_dict(pairing_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


