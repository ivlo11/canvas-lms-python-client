# PseudonymsForgotPasswordResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requested** | **bool** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.pseudonyms_forgot_password_response import PseudonymsForgotPasswordResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PseudonymsForgotPasswordResponse from a JSON string
pseudonyms_forgot_password_response_instance = PseudonymsForgotPasswordResponse.from_json(json)
# print the JSON string representation of the object
print(PseudonymsForgotPasswordResponse.to_json())

# convert the object into a dict
pseudonyms_forgot_password_response_dict = pseudonyms_forgot_password_response_instance.to_dict()
# create an instance of PseudonymsForgotPasswordResponse from a dict
pseudonyms_forgot_password_response_from_dict = PseudonymsForgotPasswordResponse.from_dict(pseudonyms_forgot_password_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


