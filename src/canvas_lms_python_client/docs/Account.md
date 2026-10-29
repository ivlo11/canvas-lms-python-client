# Account



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | the ID of the Account object | [optional] 
**name** | **str** | The display name of the account | [optional] 
**uuid** | **str** | The UUID of the account | [optional] 
**parent_account_id** | **int** | The account&#39;s parent ID, or null if this is the root account | [optional] 
**root_account_id** | **int** | The ID of the root account, or null if this is the root account | [optional] 
**workflow_state** | **str** | The state of the account. Can be &#39;active&#39; or &#39;deleted&#39;. | [optional] 

## Example

```python
from canvas_lms_python_client.models.account import Account

# TODO update the JSON string below
json = "{}"
# create an instance of Account from a JSON string
account_instance = Account.from_json(json)
# print the JSON string representation of the object
print(Account.to_json())

# convert the object into a dict
account_dict = account_instance.to_dict()
# create an instance of Account from a dict
account_from_dict = Account.from_dict(account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


