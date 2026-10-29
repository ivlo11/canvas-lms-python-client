# CourseQuizExtension


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | The ID of the Student that needs the quiz extension. | 
**extra_attempts** | **int** | Number of times the student is allowed to re-take the quiz over the multiple-attempt limit. | [optional] 
**extra_time** | **int** | Amount of extra time allowed for the quiz submission, in minutes. | [optional] 
**manually_unlocked** | **bool** | The student can take the quiz even if it&#39;s locked for everyone else | [optional] 
**end_at** | **datetime** | The time at which the quiz submission will be overdue, and be flagged as a late submission. | [optional] 

## Example

```python
from canvas_lms_python_client.models.course_quiz_extension import CourseQuizExtension

# TODO update the JSON string below
json = "{}"
# create an instance of CourseQuizExtension from a JSON string
course_quiz_extension_instance = CourseQuizExtension.from_json(json)
# print the JSON string representation of the object
print(CourseQuizExtension.to_json())

# convert the object into a dict
course_quiz_extension_dict = course_quiz_extension_instance.to_dict()
# create an instance of CourseQuizExtension from a dict
course_quiz_extension_from_dict = CourseQuizExtension.from_dict(course_quiz_extension_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


