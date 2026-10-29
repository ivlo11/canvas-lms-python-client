# Avatar

Possible avatar for a user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | [&#39;gravatar&#39;|&#39;attachment&#39;|&#39;no_pic&#39;] The type of avatar record, for categorization purposes. | 
**url** | **str** | The url of the avatar | 
**token** | **str** | A unique representation of the avatar record which can be used to set the avatar with the user update endpoint. Note: this is an internal representation and is subject to change without notice. It should be consumed with this api endpoint and used in the user update endpoint, and should not be constructed by the client. | 
**display_name** | **str** | A textual description of the avatar record. | 
**id** | **int** | [&#39;attachment&#39; type only] the internal id of the attachment | [optional] 
**content_type** | **str** | [&#39;attachment&#39; type only] the content-type of the attachment. | [optional] 
**filename** | **str** | [&#39;attachment&#39; type only] the filename of the attachment | [optional] 
**size** | **int** | [&#39;attachment&#39; type only] the size of the attachment | [optional] 

## Example

```python
from canvas_lms_python_client.models.avatar import Avatar

# TODO update the JSON string below
json = "{}"
# create an instance of Avatar from a JSON string
avatar_instance = Avatar.from_json(json)
# print the JSON string representation of the object
print(Avatar.to_json())

# convert the object into a dict
avatar_dict = avatar_instance.to_dict()
# create an instance of Avatar from a dict
avatar_from_dict = Avatar.from_dict(avatar_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


