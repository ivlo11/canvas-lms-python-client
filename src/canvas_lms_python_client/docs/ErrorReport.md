# ErrorReport

A collection of information around a specific notification of a problem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | **str** | The users problem summary, like an email subject line | [optional] 
**comments** | **str** | long form documentation of what was witnessed | [optional] 
**user_perceived_severity** | **str** | categorization of how bad the user thinks the problem is.  Should be one of [just_a_comment, not_urgent, workaround_possible, blocks_what_i_need_to_do, extreme_critical_emergency]. | [optional] 
**email** | **str** | the email address of the reporting user | [optional] 
**url** | **str** | URL of the page on which the error was reported | [optional] 
**context_asset_string** | **str** | string describing the asset being interacted with at the time of error.  Formatted &#39;[type]_[id]&#39; | [optional] 
**user_roles** | **str** | comma seperated list of roles the reporting user holds.  Can be one [student], or many [teacher,admin] | [optional] 

## Example

```python
from canvas_lms_python_client.models.error_report import ErrorReport

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorReport from a JSON string
error_report_instance = ErrorReport.from_json(json)
# print the JSON string representation of the object
print(ErrorReport.to_json())

# convert the object into a dict
error_report_dict = error_report_instance.to_dict()
# create an instance of ErrorReport from a dict
error_report_from_dict = ErrorReport.from_dict(error_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


