# AccountReportsCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameters** | [**AccountReportsCreateRequestParameters**](AccountReportsCreateRequestParameters.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.account_reports_create_request import AccountReportsCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AccountReportsCreateRequest from a JSON string
account_reports_create_request_instance = AccountReportsCreateRequest.from_json(json)
# print the JSON string representation of the object
print(AccountReportsCreateRequest.to_json())

# convert the object into a dict
account_reports_create_request_dict = account_reports_create_request_instance.to_dict()
# create an instance of AccountReportsCreateRequest from a dict
account_reports_create_request_from_dict = AccountReportsCreateRequest.from_dict(account_reports_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


