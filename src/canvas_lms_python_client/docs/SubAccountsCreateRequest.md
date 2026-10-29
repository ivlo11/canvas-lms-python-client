# SubAccountsCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**SubAccountsCreateRequestAccount**](SubAccountsCreateRequestAccount.md) |  | 

## Example

```python
from canvas_lms_python_client.models.sub_accounts_create_request import SubAccountsCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SubAccountsCreateRequest from a JSON string
sub_accounts_create_request_instance = SubAccountsCreateRequest.from_json(json)
# print the JSON string representation of the object
print(SubAccountsCreateRequest.to_json())

# convert the object into a dict
sub_accounts_create_request_dict = sub_accounts_create_request_instance.to_dict()
# create an instance of SubAccountsCreateRequest from a dict
sub_accounts_create_request_from_dict = SubAccountsCreateRequest.from_dict(sub_accounts_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


