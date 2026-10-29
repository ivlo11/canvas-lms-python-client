# QuizzesApiValidateAccessCodeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_code** | **str** | The access code being validated | 

## Example

```python
from canvas_lms_python_client.models.quizzes_api_validate_access_code_request import QuizzesApiValidateAccessCodeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QuizzesApiValidateAccessCodeRequest from a JSON string
quizzes_api_validate_access_code_request_instance = QuizzesApiValidateAccessCodeRequest.from_json(json)
# print the JSON string representation of the object
print(QuizzesApiValidateAccessCodeRequest.to_json())

# convert the object into a dict
quizzes_api_validate_access_code_request_dict = quizzes_api_validate_access_code_request_instance.to_dict()
# create an instance of QuizzesApiValidateAccessCodeRequest from a dict
quizzes_api_validate_access_code_request_from_dict = QuizzesApiValidateAccessCodeRequest.from_dict(quizzes_api_validate_access_code_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


