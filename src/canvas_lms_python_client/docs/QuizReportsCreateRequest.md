# QuizReportsCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_string** | **str** | Whether the output should include documents for the file and/or progress objects associated with this report. (Note: JSON-API only) | [optional] 
**quiz_report** | [**QuizReportsCreateRequestQuizReport**](QuizReportsCreateRequestQuizReport.md) |  | 

## Example

```python
from canvas_lms_python_client.models.quiz_reports_create_request import QuizReportsCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QuizReportsCreateRequest from a JSON string
quiz_reports_create_request_instance = QuizReportsCreateRequest.from_json(json)
# print the JSON string representation of the object
print(QuizReportsCreateRequest.to_json())

# convert the object into a dict
quiz_reports_create_request_dict = quiz_reports_create_request_instance.to_dict()
# create an instance of QuizReportsCreateRequest from a dict
quiz_reports_create_request_from_dict = QuizReportsCreateRequest.from_dict(quiz_reports_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


