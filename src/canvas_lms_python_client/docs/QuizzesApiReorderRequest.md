# QuizzesApiReorderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **int** | The associated item&#39;s unique identifier | 
**order_type_question_group** | **str** | The type of item is either &#39;question&#39; or &#39;group&#39; | [optional] 

## Example

```python
from canvas_lms_python_client.models.quizzes_api_reorder_request import QuizzesApiReorderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QuizzesApiReorderRequest from a JSON string
quizzes_api_reorder_request_instance = QuizzesApiReorderRequest.from_json(json)
# print the JSON string representation of the object
print(QuizzesApiReorderRequest.to_json())

# convert the object into a dict
quizzes_api_reorder_request_dict = quizzes_api_reorder_request_instance.to_dict()
# create an instance of QuizzesApiReorderRequest from a dict
quizzes_api_reorder_request_from_dict = QuizzesApiReorderRequest.from_dict(quizzes_api_reorder_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


