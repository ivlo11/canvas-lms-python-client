# Admin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for the account role/user assignment. | 
**role** | **str** | The account role assigned. This can be &#39;AccountAdmin&#39; or a user-defined role created by the Roles API. | [optional] 
**user** | [**User**](User.md) |  | [optional] 
**workflow_state** | **str** | The status of the account role/user assignment. | [optional] 

## Example

```python
from canvas_lms_python_client.models.admin import Admin

# TODO update the JSON string below
json = "{}"
# create an instance of Admin from a JSON string
admin_instance = Admin.from_json(json)
# print the JSON string representation of the object
print(Admin.to_json())

# convert the object into a dict
admin_dict = admin_instance.to_dict()
# create an instance of Admin from a dict
admin_from_dict = Admin.from_dict(admin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


