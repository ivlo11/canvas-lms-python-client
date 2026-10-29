# QuizReport



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | the ID of the quiz report | [optional] 
**quiz_id** | **int** | the ID of the quiz | [optional] 
**report_type** | **str** | which type of report this is possible values: &#39;student_analysis&#39;, &#39;item_analysis&#39; | [optional] 
**readable_type** | **str** | a human-readable (and localized) version of the report_type | [optional] 
**includes_all_versions** | **bool** | boolean indicating whether the report represents all submissions or only the most recent ones for each student | [optional] 
**anonymous** | **bool** | boolean indicating whether the report is for an anonymous survey. if true, no student names will be included in the csv | [optional] 
**generatable** | **bool** | boolean indicating whether the report can be generated, which is true unless the quiz is a survey one | [optional] 
**created_at** | **datetime** | when the report was created | [optional] 
**updated_at** | **datetime** | when the report was last updated | [optional] 
**url** | **str** | the API endpoint for this report | [optional] 
**file** | [**File**](File.md) |  | [optional] 
**progress_url** | **str** | if the report has not yet finished generating, a URL where information about its progress can be retrieved. refer to the Progress API for more information (Note: not available in JSON-API format) | [optional] 
**progress** | [**Progress**](Progress.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.quiz_report import QuizReport

# TODO update the JSON string below
json = "{}"
# create an instance of QuizReport from a JSON string
quiz_report_instance = QuizReport.from_json(json)
# print the JSON string representation of the object
print(QuizReport.to_json())

# convert the object into a dict
quiz_report_dict = quiz_report_instance.to_dict()
# create an instance of QuizReport from a dict
quiz_report_from_dict = QuizReport.from_dict(quiz_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


