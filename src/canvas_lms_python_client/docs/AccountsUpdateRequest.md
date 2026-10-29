# AccountsUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**override_sis_stickiness** | **bool** | Default is true. If false, any fields containing “sticky” changes will not be updated. See SIS CSV Format documentation for information on which fields can have SIS stickiness | [optional] 
**account** | [**AccountsUpdateRequestAccount**](AccountsUpdateRequestAccount.md) |  | 

## Example

```python
from canvas_lms_python_client.models.accounts_update_request import AccountsUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AccountsUpdateRequest from a JSON string
accounts_update_request_instance = AccountsUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(AccountsUpdateRequest.to_json())

# convert the object into a dict
accounts_update_request_dict = accounts_update_request_instance.to_dict()
# create an instance of AccountsUpdateRequest from a dict
accounts_update_request_from_dict = AccountsUpdateRequest.from_dict(accounts_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


