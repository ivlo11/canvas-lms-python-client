# QuizReportsCreateRequestQuizReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_type** | **str** | [Required, String, \&quot;student_analysis\&quot;|\&quot;item_analysis\&quot;] The type of report to be generated. | 
**includes_all_versions** | **bool** | [Boolean] Whether the report should consider all submissions or only the most recent. Defaults to false, ignored for item_analysis. | [optional] 

## Example

```python
from canvas_lms_python_client.models.quiz_reports_create_request_quiz_report import QuizReportsCreateRequestQuizReport

# TODO update the JSON string below
json = "{}"
# create an instance of QuizReportsCreateRequestQuizReport from a JSON string
quiz_reports_create_request_quiz_report_instance = QuizReportsCreateRequestQuizReport.from_json(json)
# print the JSON string representation of the object
print(QuizReportsCreateRequestQuizReport.to_json())

# convert the object into a dict
quiz_reports_create_request_quiz_report_dict = quiz_reports_create_request_quiz_report_instance.to_dict()
# create an instance of QuizReportsCreateRequestQuizReport from a dict
quiz_reports_create_request_quiz_report_from_dict = QuizReportsCreateRequestQuizReport.from_dict(quiz_reports_create_request_quiz_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


