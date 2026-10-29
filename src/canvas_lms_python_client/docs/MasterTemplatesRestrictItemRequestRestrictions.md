# MasterTemplatesRestrictItemRequestRestrictions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blueprint_restriction** | **str** | (Optional) If the object is restricted, this specifies a set of restrictions. If not specified, the course-level restrictions will be used. See {api:CoursesController#update Course API update documentation} | [optional] 

## Example

```python
from canvas_lms_python_client.models.master_templates_restrict_item_request_restrictions import MasterTemplatesRestrictItemRequestRestrictions

# TODO update the JSON string below
json = "{}"
# create an instance of MasterTemplatesRestrictItemRequestRestrictions from a JSON string
master_templates_restrict_item_request_restrictions_instance = MasterTemplatesRestrictItemRequestRestrictions.from_json(json)
# print the JSON string representation of the object
print(MasterTemplatesRestrictItemRequestRestrictions.to_json())

# convert the object into a dict
master_templates_restrict_item_request_restrictions_dict = master_templates_restrict_item_request_restrictions_instance.to_dict()
# create an instance of MasterTemplatesRestrictItemRequestRestrictions from a dict
master_templates_restrict_item_request_restrictions_from_dict = MasterTemplatesRestrictItemRequestRestrictions.from_dict(master_templates_restrict_item_request_restrictions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


