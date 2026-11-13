# UsersTodoItemCountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignments_needing_submitting** | **int** |  | [optional] 
**needs_grading_count** | **int** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.users_todo_item_count_response import UsersTodoItemCountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UsersTodoItemCountResponse from a JSON string
users_todo_item_count_response_instance = UsersTodoItemCountResponse.from_json(json)
# print the JSON string representation of the object
print(UsersTodoItemCountResponse.to_json())

# convert the object into a dict
users_todo_item_count_response_dict = users_todo_item_count_response_instance.to_dict()
# create an instance of UsersTodoItemCountResponse from a dict
users_todo_item_count_response_from_dict = UsersTodoItemCountResponse.from_dict(users_todo_item_count_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


