# MasterTemplatesRestrictItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_type** | **str** | The type of the object. | [optional] 
**content_id** | **int** | The ID of the object. | [optional] 
**restricted** | **bool** | Whether to apply restrictions. | [optional] 
**restrictions** | [**MasterTemplatesRestrictItemRequestRestrictions**](MasterTemplatesRestrictItemRequestRestrictions.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.master_templates_restrict_item_request import MasterTemplatesRestrictItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MasterTemplatesRestrictItemRequest from a JSON string
master_templates_restrict_item_request_instance = MasterTemplatesRestrictItemRequest.from_json(json)
# print the JSON string representation of the object
print(MasterTemplatesRestrictItemRequest.to_json())

# convert the object into a dict
master_templates_restrict_item_request_dict = master_templates_restrict_item_request_instance.to_dict()
# create an instance of MasterTemplatesRestrictItemRequest from a dict
master_templates_restrict_item_request_from_dict = MasterTemplatesRestrictItemRequest.from_dict(master_templates_restrict_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


