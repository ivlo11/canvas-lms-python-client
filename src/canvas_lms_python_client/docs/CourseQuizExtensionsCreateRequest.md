# CourseQuizExtensionsCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | The ID of the user we want to add quiz extensions for. | 
**extra_attempts** | **int** | Number of times the student is allowed to re-take the quiz over the multiple-attempt limit. This is limited to 1000 attempts or less. | [optional] 
**extra_time** | **int** | The number of extra minutes to allow for all attempts. This will add to the existing time limit on the submission. This is limited to 10080 minutes (1 week) | [optional] 
**manually_unlocked** | **bool** | Allow the student to take the quiz even if it&#39;s locked for everyone else. | [optional] 
**extend_from_now** | **int** | The number of minutes to extend the quiz from the current time. This is mutually exclusive to extend_from_end_at. This is limited to 1440 minutes (24 hours) | [optional] 
**extend_from_end_at** | **int** | The number of minutes to extend the quiz beyond the quiz&#39;s current ending time. This is mutually exclusive to extend_from_now. This is limited to 1440 minutes (24 hours) | [optional] 

## Example

```python
from canvas_lms_python_client.models.course_quiz_extensions_create_request import CourseQuizExtensionsCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CourseQuizExtensionsCreateRequest from a JSON string
course_quiz_extensions_create_request_instance = CourseQuizExtensionsCreateRequest.from_json(json)
# print the JSON string representation of the object
print(CourseQuizExtensionsCreateRequest.to_json())

# convert the object into a dict
course_quiz_extensions_create_request_dict = course_quiz_extensions_create_request_instance.to_dict()
# create an instance of CourseQuizExtensionsCreateRequest from a dict
course_quiz_extensions_create_request_from_dict = CourseQuizExtensionsCreateRequest.from_dict(course_quiz_extensions_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


