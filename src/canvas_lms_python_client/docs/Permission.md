# Permission

A permission that can be granted to a role

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The API identifier for the permission | [optional] 
**label** | **str** | The human-readable label for the permission | [optional] 
**group** | **str** | The group this permission belongs to, if it is part of a granular permission group | [optional] 
**group_label** | **str** | The human-readable label for the group this permission belongs to | [optional] 
**available_to** | **List[str]** | The base role types this permission can be enabled for | [optional] 
**true_for** | **List[str]** | The base role types this permission is enabled for by default | [optional] 

## Example

```python
from canvas_lms_python_client.models.permission import Permission

# TODO update the JSON string below
json = "{}"
# create an instance of Permission from a JSON string
permission_instance = Permission.from_json(json)
# print the JSON string representation of the object
print(Permission.to_json())

# convert the object into a dict
permission_dict = permission_instance.to_dict()
# create an instance of Permission from a dict
permission_from_dict = Permission.from_dict(permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


