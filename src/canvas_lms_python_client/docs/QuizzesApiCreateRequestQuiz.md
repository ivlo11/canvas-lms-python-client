# QuizzesApiCreateRequestQuiz


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | [Required, String] The quiz title. | 
**description** | **str** | [String] A description of the quiz. | [optional] 
**quiz_type** | **str** | [\&quot;practice_quiz\&quot;|\&quot;assignment\&quot;|\&quot;graded_survey\&quot;|\&quot;survey\&quot;] The type of quiz. | [optional] 
**assignment_group_id** | **int** | [Integer] The assignment group id to put the assignment in. Defaults to the top assignment group in the course. Only valid if the quiz is graded, i.e. if quiz_type is \&quot;assignment\&quot; or \&quot;graded_survey\&quot;. | [optional] 
**shuffle_answers** | **bool** | [Boolean] If true, quiz answers for multiple choice questions will be randomized for each student. Defaults to false. | [optional] 
**hide_results** | **str** | [String, \&quot;always\&quot;|\&quot;until_after_last_attempt\&quot;] Dictates whether or not quiz results are hidden from students. If null, students can see their results after any attempt. If \&quot;always\&quot;, students can never see their results. If \&quot;until_after_last_attempt\&quot;, students can only see results after their last attempt. (Only valid if allowed_attempts &gt; 1). Defaults to null. | [optional] 
**show_correct_answers** | **bool** | [Boolean] Only valid if hide_results&#x3D;null If false, hides correct answers from students when quiz results are viewed. Defaults to true. | [optional] 
**show_correct_answers_last_attempt** | **bool** | [Boolean] Only valid if show_correct_answers&#x3D;true and allowed_attempts &gt; 1 If true, hides correct answers from students when quiz results are viewed until they submit the last attempt for the quiz. Defaults to false. | [optional] 
**show_correct_answers_at** | **str** | [DateTime] Only valid if show_correct_answers&#x3D;true If set, the correct answers will be visible by students only after this date, otherwise the correct answers are visible once the student hands in their quiz submission. | [optional] 
**hide_correct_answers_at** | **str** | [DateTime] Only valid if show_correct_answers&#x3D;true If set, the correct answers will stop being visible once this date has passed. Otherwise, the correct answers will be visible indefinitely. | [optional] 
**allowed_attempts** | **int** | [Integer] Number of times a student is allowed to take a quiz. Set to -1 for unlimited attempts. Defaults to 1. | [optional] 
**scoring_policy** | **str** | [String, \&quot;keep_highest\&quot;|\&quot;keep_latest\&quot;] Required and only valid if allowed_attempts &gt; 1. Scoring policy for a quiz that students can take multiple times. Defaults to \&quot;keep_highest\&quot;. | [optional] 
**one_question_at_a_time** | **bool** | [Boolean] If true, shows quiz to student one question at a time. Defaults to false. | [optional] 
**cant_go_back** | **bool** | [Boolean] Only valid if one_question_at_a_time&#x3D;true If true, questions are locked after answering. Defaults to false. | [optional] 
**access_code** | **str** | [String] Restricts access to the quiz with a password. For no access code restriction, set to null. Defaults to null. | [optional] 
**ip_filter** | **str** | [String] Restricts access to the quiz to computers in a specified IP range. Filters can be a comma-separated list of addresses, or an address followed by a mask  Examples:   \&quot;192.168.217.1\&quot;   \&quot;192.168.217.1/24\&quot;   \&quot;192.168.217.1/255.255.255.0\&quot;  For no IP filter restriction, set to null. Defaults to null. | [optional] 
**due_at** | **str** | [DateTime] The day/time the quiz is due. Accepts times in ISO 8601 format, e.g. 2011-10-21T18:48Z. | [optional] 
**lock_at** | **str** | [DateTime] The day/time the quiz is locked for students. Accepts times in ISO 8601 format, e.g. 2011-10-21T18:48Z. | [optional] 
**unlock_at** | **str** | [DateTime] The day/time the quiz is unlocked for students. Accepts times in ISO 8601 format, e.g. 2011-10-21T18:48Z. | [optional] 
**published** | **bool** | [Boolean] Whether the quiz should have a draft state of published or unpublished. NOTE: If students have started taking the quiz, or there are any submissions for the quiz, you may not unpublish a quiz and will recieve an error. | [optional] 
**one_time_results** | **bool** | [Boolean] Whether students should be prevented from viewing their quiz results past the first time (right after they turn the quiz in.) Only valid if \&quot;hide_results\&quot; is not set to \&quot;always\&quot;. Defaults to false. | [optional] 
**only_visible_to_overrides** | **bool** | [Boolean] Whether this quiz is only visible to overrides (Only useful if &#39;differentiated assignments&#39; account setting is on) Defaults to false. | [optional] 

## Example

```python
from canvas_lms_python_client.models.quizzes_api_create_request_quiz import QuizzesApiCreateRequestQuiz

# TODO update the JSON string below
json = "{}"
# create an instance of QuizzesApiCreateRequestQuiz from a JSON string
quizzes_api_create_request_quiz_instance = QuizzesApiCreateRequestQuiz.from_json(json)
# print the JSON string representation of the object
print(QuizzesApiCreateRequestQuiz.to_json())

# convert the object into a dict
quizzes_api_create_request_quiz_dict = quizzes_api_create_request_quiz_instance.to_dict()
# create an instance of QuizzesApiCreateRequestQuiz from a dict
quizzes_api_create_request_quiz_from_dict = QuizzesApiCreateRequestQuiz.from_dict(quizzes_api_create_request_quiz_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


