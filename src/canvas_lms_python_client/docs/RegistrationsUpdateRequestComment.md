# RegistrationsUpdateRequestComment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**string___nil** | **str** | A comment explaining why this change was made. Cannot exceed 2000 characters. | [optional] 

## Example

```python
from canvas_lms_python_client.models.registrations_update_request_comment import RegistrationsUpdateRequestComment

# TODO update the JSON string below
json = "{}"
# create an instance of RegistrationsUpdateRequestComment from a JSON string
registrations_update_request_comment_instance = RegistrationsUpdateRequestComment.from_json(json)
# print the JSON string representation of the object
print(RegistrationsUpdateRequestComment.to_json())

# convert the object into a dict
registrations_update_request_comment_dict = registrations_update_request_comment_instance.to_dict()
# create an instance of RegistrationsUpdateRequestComment from a dict
registrations_update_request_comment_from_dict = RegistrationsUpdateRequestComment.from_dict(registrations_update_request_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


