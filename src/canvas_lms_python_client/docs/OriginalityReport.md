# OriginalityReport



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The id of the OriginalityReport | [optional] 
**file_id** | **int** | The id of the file receiving the originality score | [optional] 
**originality_score** | **float** | A number between 0 and 100 representing the originality score | [optional] 
**originality_report_file_id** | **int** | The ID of the file within Canvas containing the originality report document (if provided) | [optional] 
**originality_report_url** | **str** | A non-LTI launch URL where the originality score of the file may be found. | [optional] 
**tool_setting** | [**ToolSetting**](ToolSetting.md) |  | [optional] 
**error_report** | **str** | A message describing the error. If set, the workflow_state will become &#39;error.&#39; | [optional] 
**submission_time** | **datetime** | The submitted_at date time of the submission. | [optional] 
**root_account_id** | **int** | The id of the root Account associated with the OriginalityReport | [optional] 

## Example

```python
from canvas_lms_python_client.models.originality_report import OriginalityReport

# TODO update the JSON string below
json = "{}"
# create an instance of OriginalityReport from a JSON string
originality_report_instance = OriginalityReport.from_json(json)
# print the JSON string representation of the object
print(OriginalityReport.to_json())

# convert the object into a dict
originality_report_dict = originality_report_instance.to_dict()
# create an instance of OriginalityReport from a dict
originality_report_from_dict = OriginalityReport.from_dict(originality_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


