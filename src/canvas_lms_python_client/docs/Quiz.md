# Quiz



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | the ID of the quiz | [optional] 
**title** | **str** | the title of the quiz | [optional] 
**html_url** | **str** | the HTTP/HTTPS URL to the quiz | [optional] 
**mobile_url** | **str** | a url suitable for loading the quiz in a mobile webview.  it will persiste the headless session and, for quizzes in public courses, will force the user to login | [optional] 
**preview_url** | **str** | A url that can be visited in the browser with a POST request to preview a quiz as the teacher. Only present when the user may grade | [optional] 
**description** | **str** | the description of the quiz | [optional] 
**quiz_type** | **str** | type of quiz possible values: &#39;practice_quiz&#39;, &#39;assignment&#39;, &#39;graded_survey&#39;, &#39;survey&#39; | [optional] 
**assignment_group_id** | **int** | the ID of the quiz&#39;s assignment group: | [optional] 
**time_limit** | **int** | quiz time limit in minutes | [optional] 
**shuffle_answers** | **bool** | shuffle answers for students? | [optional] 
**hide_results** | **str** | let students see their quiz responses? possible values: null, &#39;always&#39;, &#39;until_after_last_attempt&#39; | [optional] 
**show_correct_answers** | **bool** | show which answers were correct when results are shown? only valid if hide_results&#x3D;null | [optional] 
**show_correct_answers_last_attempt** | **bool** | restrict the show_correct_answers option above to apply only to the last submitted attempt of a quiz that allows multiple attempts. only valid if show_correct_answers&#x3D;true and allowed_attempts &gt; 1 | [optional] 
**show_correct_answers_at** | **datetime** | when should the correct answers be visible by students? only valid if show_correct_answers&#x3D;true | [optional] 
**hide_correct_answers_at** | **datetime** | prevent the students from seeing correct answers after the specified date has passed. only valid if show_correct_answers&#x3D;true | [optional] 
**one_time_results** | **bool** | prevent the students from seeing their results more than once (right after they submit the quiz) | [optional] 
**scoring_policy** | **str** | which quiz score to keep (only if allowed_attempts !&#x3D; 1) possible values: &#39;keep_highest&#39;, &#39;keep_latest&#39; | [optional] 
**allowed_attempts** | **int** | how many times a student can take the quiz -1 &#x3D; unlimited attempts | [optional] 
**one_question_at_a_time** | **bool** | show one question at a time? | [optional] 
**question_count** | **int** | the number of questions in the quiz | [optional] 
**points_possible** | **int** | The total point value given to the quiz | [optional] 
**cant_go_back** | **bool** | lock questions after answering? only valid if one_question_at_a_time&#x3D;true | [optional] 
**access_code** | **str** | access code to restrict quiz access | [optional] 
**ip_filter** | **str** | IP address or range that quiz access is limited to | [optional] 
**due_at** | **datetime** | when the quiz is due | [optional] 
**lock_at** | **datetime** | when to lock the quiz | [optional] 
**unlock_at** | **datetime** | when to unlock the quiz | [optional] 
**published** | **bool** | whether the quiz has a published or unpublished draft state. | [optional] 
**unpublishable** | **bool** | Whether the assignment&#39;s &#39;published&#39; state can be changed to false. Will be false if there are student submissions for the quiz. | [optional] 
**locked_for_user** | **bool** | Whether or not this is locked for the user. | [optional] 
**lock_info** | [**LockInfo**](LockInfo.md) |  | [optional] 
**lock_explanation** | **str** | (Optional) An explanation of why this is locked for the user. Present when locked_for_user is true. | [optional] 
**speedgrader_url** | **str** | Link to SpeedGrader for this quiz. Will not be present if quiz is unpublished | [optional] 
**quiz_extensions_url** | **str** | Link to endpoint to send extensions for this quiz. | [optional] 
**permissions** | [**QuizPermissions**](QuizPermissions.md) |  | [optional] 
**all_dates** | [**List[AssignmentDate]**](AssignmentDate.md) | list of due dates for the quiz | [optional] 
**version_number** | **int** | Current version number of the quiz | [optional] 
**question_types** | **List[str]** | List of question types in the quiz | [optional] 
**anonymous_submissions** | **bool** | Whether survey submissions will be kept anonymous (only applicable to &#39;graded_survey&#39;, &#39;survey&#39; quiz types) | [optional] 

## Example

```python
from canvas_lms_python_client.models.quiz import Quiz

# TODO update the JSON string below
json = "{}"
# create an instance of Quiz from a JSON string
quiz_instance = Quiz.from_json(json)
# print the JSON string representation of the object
print(Quiz.to_json())

# convert the object into a dict
quiz_dict = quiz_instance.to_dict()
# create an instance of Quiz from a dict
quiz_from_dict = Quiz.from_dict(quiz_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


