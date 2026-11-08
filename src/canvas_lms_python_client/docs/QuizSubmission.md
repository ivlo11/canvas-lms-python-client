# QuizSubmission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the quiz submission. | 
**quiz_id** | **int** | The ID of the Quiz the quiz submission belongs to. | 
**user_id** | **int** | The ID of the Student that made the quiz submission. | [optional] 
**submission_id** | **int** | The ID of the Submission the quiz submission represents. | [optional] 
**started_at** | **datetime** | The time at which the student started the quiz submission. | [optional] 
**finished_at** | **datetime** | The time at which the student submitted the quiz submission. | [optional] 
**end_at** | **datetime** | The time at which the quiz submission will be overdue, and be flagged as a late submission. | [optional] 
**attempt** | **int** | For quizzes that allow multiple attempts, this field specifies the quiz submission attempt number. | [optional] 
**extra_attempts** | **int** | Number of times the student was allowed to re-take the quiz over the multiple-attempt limit. | [optional] 
**extra_time** | **int** | Amount of extra time allowed for the quiz submission, in minutes. | [optional] 
**manually_unlocked** | **bool** | The student can take the quiz even if it&#39;s locked for everyone else | [optional] 
**time_spent** | **int** | Amount of time spent, in seconds. | [optional] 
**score** | **float** | The score of the quiz submission, if graded. | [optional] 
**score_before_regrade** | **float** | The original score of the quiz submission prior to any re-grading. | [optional] 
**kept_score** | **float** | For quizzes that allow multiple attempts, this is the score that will be used, which might be the score of the latest, or the highest, quiz submission. | [optional] 
**fudge_points** | **float** | Number of points the quiz submission&#39;s score was fudged by. | [optional] 
**has_seen_results** | **bool** | Whether the student has viewed their results to the quiz. | [optional] 
**workflow_state** | **str** | The current state of the quiz submission. Possible values: [&#39;untaken&#39;|&#39;pending_review&#39;|&#39;complete&#39;|&#39;settings_only&#39;|&#39;preview&#39;]. | [optional] 
**overdue_and_needs_submission** | **bool** | Indicates whether the quiz submission is overdue and needs submission | [optional] 
**attempts_left** | **int** |  | [optional] 
**html_url** | **str** |  | [optional] 
**quiz_points_possible** | **float** |  | [optional] 
**quiz_version** | **int** |  | [optional] 
**result_url** | **str** |  | [optional] 
**validation_token** | **str** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.quiz_submission import QuizSubmission

# TODO update the JSON string below
json = "{}"
# create an instance of QuizSubmission from a JSON string
quiz_submission_instance = QuizSubmission.from_json(json)
# print the JSON string representation of the object
print(QuizSubmission.to_json())

# convert the object into a dict
quiz_submission_dict = quiz_submission_instance.to_dict()
# create an instance of QuizSubmission from a dict
quiz_submission_from_dict = QuizSubmission.from_dict(quiz_submission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


