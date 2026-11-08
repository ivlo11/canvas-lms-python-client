# ReportParameters

The parameters returned will vary for each report.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enrollment_term_id** | [**ReportParametersEnrollmentTermId**](ReportParametersEnrollmentTermId.md) |  | [optional] 
**error** | **str** |  | [optional] 
**param** | **str** |  | [optional] 
**enrollment_ids** | **List[object]** |  | [optional] 
**section_ids** | **List[object]** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.report_parameters import ReportParameters

# TODO update the JSON string below
json = "{}"
# create an instance of ReportParameters from a JSON string
report_parameters_instance = ReportParameters.from_json(json)
# print the JSON string representation of the object
print(ReportParameters.to_json())

# convert the object into a dict
report_parameters_dict = report_parameters_instance.to_dict()
# create an instance of ReportParameters from a dict
report_parameters_from_dict = ReportParameters.from_dict(report_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


