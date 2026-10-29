# ModerationSetCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**student_ids** | **List[float]** | user ids for students to select for moderation | [optional] 

## Example

```python
from canvas_lms_python_client.models.moderation_set_create_request import ModerationSetCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ModerationSetCreateRequest from a JSON string
moderation_set_create_request_instance = ModerationSetCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ModerationSetCreateRequest.to_json())

# convert the object into a dict
moderation_set_create_request_dict = moderation_set_create_request_instance.to_dict()
# create an instance of ModerationSetCreateRequest from a dict
moderation_set_create_request_from_dict = ModerationSetCreateRequest.from_dict(moderation_set_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


