# AdminsCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | The id of the user to promote. | 
**role** | **str** | [DEPRECATED] The user&#39;s admin relationship with the account will be created with the given role. Defaults to &#39;AccountAdmin&#39;. | [optional] 
**role_id** | **int** | The user&#39;s admin relationship with the account will be created with the given role. Defaults to the built-in role for &#39;AccountAdmin&#39;. | [optional] 
**send_confirmation** | **bool** | Send a notification email to the new admin if true. Default is true. | [optional] 

## Example

```python
from canvas_lms_python_client.models.admins_create_request import AdminsCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AdminsCreateRequest from a JSON string
admins_create_request_instance = AdminsCreateRequest.from_json(json)
# print the JSON string representation of the object
print(AdminsCreateRequest.to_json())

# convert the object into a dict
admins_create_request_dict = admins_create_request_instance.to_dict()
# create an instance of AdminsCreateRequest from a dict
admins_create_request_from_dict = AdminsCreateRequest.from_dict(admins_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


