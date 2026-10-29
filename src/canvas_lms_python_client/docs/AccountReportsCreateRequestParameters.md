# AccountReportsCreateRequestParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skip_message** | **bool** | [Boolean] If true, no message will be sent to the user upon completion of the report. | [optional] 
**course_id** | **int** | [Integer] The id of the course to report on. Note: this parameter has been listed to serve as an example and may not be valid for every report. | [optional] 
**users** | **bool** | [Boolean] If true, user data will be included. If false, user data will be omitted. Note: this parameter has been listed to serve as an example and may not be valid for every report. | [optional] 

## Example

```python
from canvas_lms_python_client.models.account_reports_create_request_parameters import AccountReportsCreateRequestParameters

# TODO update the JSON string below
json = "{}"
# create an instance of AccountReportsCreateRequestParameters from a JSON string
account_reports_create_request_parameters_instance = AccountReportsCreateRequestParameters.from_json(json)
# print the JSON string representation of the object
print(AccountReportsCreateRequestParameters.to_json())

# convert the object into a dict
account_reports_create_request_parameters_dict = account_reports_create_request_parameters_instance.to_dict()
# create an instance of AccountReportsCreateRequestParameters from a dict
account_reports_create_request_parameters_from_dict = AccountReportsCreateRequestParameters.from_dict(account_reports_create_request_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


