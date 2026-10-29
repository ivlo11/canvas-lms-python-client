# Poll


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for the poll. | 
**question** | **str** | The question/title of the poll. | 
**description** | **str** | A short description of the poll. | [optional] 
**created_at** | **datetime** | The time at which the poll was created. | [optional] 
**user_id** | **int** | The unique identifier for the user that created the poll. | [optional] 
**total_results** | **object** | An aggregate of the results of all associated poll sessions, with the poll choice id as the key, and the aggregated submission count as the value. | [optional] 

## Example

```python
from canvas_lms_python_client.models.poll import Poll

# TODO update the JSON string below
json = "{}"
# create an instance of Poll from a JSON string
poll_instance = Poll.from_json(json)
# print the JSON string representation of the object
print(Poll.to_json())

# convert the object into a dict
poll_dict = poll_instance.to_dict()
# create an instance of Poll from a dict
poll_from_dict = Poll.from_dict(poll_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


