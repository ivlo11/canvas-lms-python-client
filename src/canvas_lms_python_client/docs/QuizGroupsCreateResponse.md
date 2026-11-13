# QuizGroupsCreateResponse

Paginated `quiz_groups` list response (from the Canvas example response).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quiz_groups** | [**List[QuizGroup]**](QuizGroup.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.quiz_groups_create_response import QuizGroupsCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QuizGroupsCreateResponse from a JSON string
quiz_groups_create_response_instance = QuizGroupsCreateResponse.from_json(json)
# print the JSON string representation of the object
print(QuizGroupsCreateResponse.to_json())

# convert the object into a dict
quiz_groups_create_response_dict = quiz_groups_create_response_instance.to_dict()
# create an instance of QuizGroupsCreateResponse from a dict
quiz_groups_create_response_from_dict = QuizGroupsCreateResponse.from_dict(quiz_groups_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


