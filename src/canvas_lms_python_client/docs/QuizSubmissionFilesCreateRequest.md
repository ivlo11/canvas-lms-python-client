# QuizSubmissionFilesCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the quiz submission file | [optional] 
**on_duplicate** | **str** | How to handle duplicate names | [optional] 

## Example

```python
from canvas_lms_python_client.models.quiz_submission_files_create_request import QuizSubmissionFilesCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QuizSubmissionFilesCreateRequest from a JSON string
quiz_submission_files_create_request_instance = QuizSubmissionFilesCreateRequest.from_json(json)
# print the JSON string representation of the object
print(QuizSubmissionFilesCreateRequest.to_json())

# convert the object into a dict
quiz_submission_files_create_request_dict = quiz_submission_files_create_request_instance.to_dict()
# create an instance of QuizSubmissionFilesCreateRequest from a dict
quiz_submission_files_create_request_from_dict = QuizSubmissionFilesCreateRequest.from_dict(quiz_submission_files_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


