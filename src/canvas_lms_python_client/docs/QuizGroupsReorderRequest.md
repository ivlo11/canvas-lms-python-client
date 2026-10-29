# QuizGroupsReorderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **int** | The associated item&#39;s unique identifier | 
**order_type** | **str** | The type of item is always &#39;question&#39; for a group | [optional] 

## Example

```python
from canvas_lms_python_client.models.quiz_groups_reorder_request import QuizGroupsReorderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QuizGroupsReorderRequest from a JSON string
quiz_groups_reorder_request_instance = QuizGroupsReorderRequest.from_json(json)
# print the JSON string representation of the object
print(QuizGroupsReorderRequest.to_json())

# convert the object into a dict
quiz_groups_reorder_request_dict = quiz_groups_reorder_request_instance.to_dict()
# create an instance of QuizGroupsReorderRequest from a dict
quiz_groups_reorder_request_from_dict = QuizGroupsReorderRequest.from_dict(quiz_groups_reorder_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


