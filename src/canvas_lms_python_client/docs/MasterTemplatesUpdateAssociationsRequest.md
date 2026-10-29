# MasterTemplatesUpdateAssociationsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**course_ids_to_add** | **List[str]** | Courses to add as associated courses | [optional] 
**course_ids_to_remove** | **List[str]** | Courses to remove as associated courses | [optional] 

## Example

```python
from canvas_lms_python_client.models.master_templates_update_associations_request import MasterTemplatesUpdateAssociationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MasterTemplatesUpdateAssociationsRequest from a JSON string
master_templates_update_associations_request_instance = MasterTemplatesUpdateAssociationsRequest.from_json(json)
# print the JSON string representation of the object
print(MasterTemplatesUpdateAssociationsRequest.to_json())

# convert the object into a dict
master_templates_update_associations_request_dict = master_templates_update_associations_request_instance.to_dict()
# create an instance of MasterTemplatesUpdateAssociationsRequest from a dict
master_templates_update_associations_request_from_dict = MasterTemplatesUpdateAssociationsRequest.from_dict(master_templates_update_associations_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


