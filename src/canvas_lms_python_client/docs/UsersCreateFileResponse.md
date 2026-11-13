# UsersCreateFileResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_param** | **str** |  | [optional] 
**progress** | **object** |  | [optional] 
**upload_params** | **object** |  | [optional] 
**upload_url** | **str** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.users_create_file_response import UsersCreateFileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UsersCreateFileResponse from a JSON string
users_create_file_response_instance = UsersCreateFileResponse.from_json(json)
# print the JSON string representation of the object
print(UsersCreateFileResponse.to_json())

# convert the object into a dict
users_create_file_response_dict = users_create_file_response_instance.to_dict()
# create an instance of UsersCreateFileResponse from a dict
users_create_file_response_from_dict = UsersCreateFileResponse.from_dict(users_create_file_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


