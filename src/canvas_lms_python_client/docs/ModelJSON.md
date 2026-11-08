# ModelJSON


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted_user_ids** | **List[int]** |  | [optional] 
**message** | **str** |  | [optional] 
**unauthorized_user_ids** | **List[int]** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.model_json import ModelJSON

# TODO update the JSON string below
json = "{}"
# create an instance of ModelJSON from a JSON string
model_json_instance = ModelJSON.from_json(json)
# print the JSON string representation of the object
print(ModelJSON.to_json())

# convert the object into a dict
model_json_dict = model_json_instance.to_dict()
# create an instance of ModelJSON from a dict
model_json_from_dict = ModelJSON.from_dict(model_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


