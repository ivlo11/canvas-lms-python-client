# QuizExtensionsCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quiz_extensions_user_id** | **int** | The ID of the user we want to add quiz extensions for. | 
**quiz_extensions_extra_attempts** | **int** | Number of times the student is allowed to re-take the quiz over the multiple-attempt limit. This is limited to 1000 attempts or less. | [optional] 
**quiz_extensions_extra_time** | **int** | The number of extra minutes to allow for all attempts. This will add to the existing time limit on the submission. This is limited to 10080 minutes (1 week) | [optional] 
**quiz_extensions_manually_unlocked** | **bool** | Allow the student to take the quiz even if it&#39;s locked for everyone else. | [optional] 
**quiz_extensions_extend_from_now** | **int** | The number of minutes to extend the quiz from the current time. This is mutually exclusive to extend_from_end_at. This is limited to 1440 minutes (24 hours) | [optional] 
**quiz_extensions_extend_from_end_at** | **int** | The number of minutes to extend the quiz beyond the quiz&#39;s current ending time. This is mutually exclusive to extend_from_now. This is limited to 1440 minutes (24 hours) | [optional] 

## Example

```python
from canvas_lms_python_client.models.quiz_extensions_create_request import QuizExtensionsCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QuizExtensionsCreateRequest from a JSON string
quiz_extensions_create_request_instance = QuizExtensionsCreateRequest.from_json(json)
# print the JSON string representation of the object
print(QuizExtensionsCreateRequest.to_json())

# convert the object into a dict
quiz_extensions_create_request_dict = quiz_extensions_create_request_instance.to_dict()
# create an instance of QuizExtensionsCreateRequest from a dict
quiz_extensions_create_request_from_dict = QuizExtensionsCreateRequest.from_dict(quiz_extensions_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


