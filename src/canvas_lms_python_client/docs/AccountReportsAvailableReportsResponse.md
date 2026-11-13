# AccountReportsAvailableReportsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description_html** | **str** |  | [optional] 
**last_run** | **object** |  | [optional] 
**parameters** | **object** |  | [optional] 
**parameters_html** | **str** |  | [optional] 
**report** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.account_reports_available_reports_response import AccountReportsAvailableReportsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccountReportsAvailableReportsResponse from a JSON string
account_reports_available_reports_response_instance = AccountReportsAvailableReportsResponse.from_json(json)
# print the JSON string representation of the object
print(AccountReportsAvailableReportsResponse.to_json())

# convert the object into a dict
account_reports_available_reports_response_dict = account_reports_available_reports_response_instance.to_dict()
# create an instance of AccountReportsAvailableReportsResponse from a dict
account_reports_available_reports_response_from_dict = AccountReportsAvailableReportsResponse.from_dict(account_reports_available_reports_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


