# Collaborator



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique user or group identifier for the collaborator. | 
**type** | **str** | The type of collaborator (e.g. &#39;user&#39; or &#39;group&#39;). | [optional] 
**name** | **str** | The name of the collaborator. | [optional] 

## Example

```python
from canvas_lms_python_client.models.collaborator import Collaborator

# TODO update the JSON string below
json = "{}"
# create an instance of Collaborator from a JSON string
collaborator_instance = Collaborator.from_json(json)
# print the JSON string representation of the object
print(Collaborator.to_json())

# convert the object into a dict
collaborator_dict = collaborator_instance.to_dict()
# create an instance of Collaborator from a dict
collaborator_from_dict = Collaborator.from_dict(collaborator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


