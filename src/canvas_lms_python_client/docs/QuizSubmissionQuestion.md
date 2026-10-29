# QuizSubmissionQuestion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the QuizQuestion this answer is for. | 
**flagged** | **bool** | Whether this question is flagged. | [optional] 
**answer** | **str** | The provided answer (if any) for this question. The format of this parameter depends on the type of the question, see the Appendix for more information. | [optional] 
**answers** | **List[str]** | The possible answers for this question when those possible answers are necessary.  The presence of this parameter is dependent on permissions. | [optional] 

## Example

```python
from canvas_lms_python_client.models.quiz_submission_question import QuizSubmissionQuestion

# TODO update the JSON string below
json = "{}"
# create an instance of QuizSubmissionQuestion from a JSON string
quiz_submission_question_instance = QuizSubmissionQuestion.from_json(json)
# print the JSON string representation of the object
print(QuizSubmissionQuestion.to_json())

# convert the object into a dict
quiz_submission_question_dict = quiz_submission_question_instance.to_dict()
# create an instance of QuizSubmissionQuestion from a dict
quiz_submission_question_from_dict = QuizSubmissionQuestion.from_dict(quiz_submission_question_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


