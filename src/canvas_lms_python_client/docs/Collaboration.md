# Collaboration



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for the collaboration | [optional] 
**collaboration_type** | **str** | A name for the type of collaboration | [optional] 
**document_id** | **str** | The collaboration document identifier for the collaboration provider | [optional] 
**user_id** | **int** | The canvas id of the user who created the collaboration | [optional] 
**context_id** | **int** | The canvas id of the course or group to which the collaboration belongs | [optional] 
**context_type** | **str** | The canvas type of the course or group to which the collaboration belongs | [optional] 
**url** | **str** | The LTI launch url to view collaboration. | [optional] 
**created_at** | **datetime** | The timestamp when the collaboration was created | [optional] 
**updated_at** | **datetime** | The timestamp when the collaboration was last modified | [optional] 
**description** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**type** | **str** | Another representation of the collaboration type | [optional] 
**update_url** | **str** | The LTI launch url to edit the collaboration | [optional] 
**user_name** | **str** | The name of the user who owns the collaboration | [optional] 
**permissions** | **object** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.collaboration import Collaboration

# TODO update the JSON string below
json = "{}"
# create an instance of Collaboration from a JSON string
collaboration_instance = Collaboration.from_json(json)
# print the JSON string representation of the object
print(Collaboration.to_json())

# convert the object into a dict
collaboration_dict = collaboration_instance.to_dict()
# create an instance of Collaboration from a dict
collaboration_from_dict = Collaboration.from_dict(collaboration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


