# QuizGroupsIndexResponse

Paginated `quiz_groups` list response (from the Canvas example response).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quiz_groups** | [**List[QuizGroup]**](QuizGroup.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.quiz_groups_index_response import QuizGroupsIndexResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QuizGroupsIndexResponse from a JSON string
quiz_groups_index_response_instance = QuizGroupsIndexResponse.from_json(json)
# print the JSON string representation of the object
print(QuizGroupsIndexResponse.to_json())

# convert the object into a dict
quiz_groups_index_response_dict = quiz_groups_index_response_instance.to_dict()
# create an instance of QuizGroupsIndexResponse from a dict
quiz_groups_index_response_from_dict = QuizGroupsIndexResponse.from_dict(quiz_groups_index_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


