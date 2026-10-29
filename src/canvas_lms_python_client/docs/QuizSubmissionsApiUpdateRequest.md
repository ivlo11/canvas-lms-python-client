# QuizSubmissionsApiUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quiz_submissions_attempt** | **int** | The attempt number of the quiz submission that should be updated. This attempt MUST be already completed. | 
**quiz_submissions_fudge_points** | **float** | Amount of positive or negative points to fudge the total score by. | [optional] 
**quiz_submissions_questions** | **str** | A set of scores and comments for each question answered by the student. The keys are the question IDs, and the values are hashes of &#x60;score&#x60; and &#x60;comment&#x60; entries. See {Appendix: Manual Scoring} for more on this parameter. | [optional] 

## Example

```python
from canvas_lms_python_client.models.quiz_submissions_api_update_request import QuizSubmissionsApiUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QuizSubmissionsApiUpdateRequest from a JSON string
quiz_submissions_api_update_request_instance = QuizSubmissionsApiUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(QuizSubmissionsApiUpdateRequest.to_json())

# convert the object into a dict
quiz_submissions_api_update_request_dict = quiz_submissions_api_update_request_instance.to_dict()
# create an instance of QuizSubmissionsApiUpdateRequest from a dict
quiz_submissions_api_update_request_from_dict = QuizSubmissionsApiUpdateRequest.from_dict(quiz_submissions_api_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


