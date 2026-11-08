# Report


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for the report. | [optional] 
**file_url** | **str** | The url to the report download. | [optional] 
**attachment** | [**File**](File.md) |  | [optional] 
**status** | **str** | The status of the report | [optional] 
**created_at** | **datetime** | The date and time the report was created. | [optional] 
**started_at** | **datetime** | The date and time the report started processing. | [optional] 
**ended_at** | **datetime** | The date and time the report finished processing. | [optional] 
**parameters** | [**ReportParameters**](ReportParameters.md) |  | [optional] 
**progress** | **int** | The progress of the report | [optional] 
**current_line** | **object** |  | [optional] 
**message** | **object** |  | [optional] 
**report** | **str** |  | [optional] 
**run_time** | **float** |  | [optional] 
**user** | **object** |  | [optional] 
**course_id** | **int** |  | [optional] 
**report_type** | **str** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.report import Report

# TODO update the JSON string below
json = "{}"
# create an instance of Report from a JSON string
report_instance = Report.from_json(json)
# print the JSON string representation of the object
print(Report.to_json())

# convert the object into a dict
report_dict = report_instance.to_dict()
# create an instance of Report from a dict
report_from_dict = Report.from_dict(report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


