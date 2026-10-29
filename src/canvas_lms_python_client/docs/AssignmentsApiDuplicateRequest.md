# AssignmentsApiDuplicateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result_type** | **str** | Optional information: When the root account has the feature &#x60;newquizzes_on_quiz_page&#x60; enabled and this argument is set to \&quot;Quiz\&quot; the response will be serialized into a {file:quizzes.html#Quiz quiz format}; When this argument isn&#39;t specified the response will be serialized into an assignment format; | [optional] 

## Example

```python
from canvas_lms_python_client.models.assignments_api_duplicate_request import AssignmentsApiDuplicateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssignmentsApiDuplicateRequest from a JSON string
assignments_api_duplicate_request_instance = AssignmentsApiDuplicateRequest.from_json(json)
# print the JSON string representation of the object
print(AssignmentsApiDuplicateRequest.to_json())

# convert the object into a dict
assignments_api_duplicate_request_dict = assignments_api_duplicate_request_instance.to_dict()
# create an instance of AssignmentsApiDuplicateRequest from a dict
assignments_api_duplicate_request_from_dict = AssignmentsApiDuplicateRequest.from_dict(assignments_api_duplicate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


