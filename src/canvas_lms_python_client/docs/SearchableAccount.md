# SearchableAccount

A minimal representation of an Account for Canvas Apps search purposes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The Canvas DB ID | [optional] 
**name** | **str** | The account name | [optional] 
**sis_id** | **str** | The SIS ID of the account, if any. Only present if user can read or manage SIS. | [optional] 
**display_path** | **List[str]** | Names of the accounts in this account&#39;s hierarchy, excluding the root and this account. | [optional] 

## Example

```python
from canvas_lms_python_client.models.searchable_account import SearchableAccount

# TODO update the JSON string below
json = "{}"
# create an instance of SearchableAccount from a JSON string
searchable_account_instance = SearchableAccount.from_json(json)
# print the JSON string representation of the object
print(SearchableAccount.to_json())

# convert the object into a dict
searchable_account_dict = searchable_account_instance.to_dict()
# create an instance of SearchableAccount from a dict
searchable_account_from_dict = SearchableAccount.from_dict(searchable_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


