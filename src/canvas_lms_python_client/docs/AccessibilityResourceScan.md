# AccessibilityResourceScan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_message** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**issue_count** | **int** |  | [optional] 
**issues** | **List[object]** |  | [optional] 
**resource_id** | **object** |  | [optional] 
**resource_name** | **str** |  | [optional] 
**resource_scan_path** | **str** |  | [optional] 
**resource_type** | **object** |  | [optional] 
**resource_updated_at** | **str** |  | [optional] 
**resource_url** | **str** |  | [optional] 
**resource_workflow_state** | **str** |  | [optional] 
**workflow_state** | **str** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.accessibility_resource_scan import AccessibilityResourceScan

# TODO update the JSON string below
json = "{}"
# create an instance of AccessibilityResourceScan from a JSON string
accessibility_resource_scan_instance = AccessibilityResourceScan.from_json(json)
# print the JSON string representation of the object
print(AccessibilityResourceScan.to_json())

# convert the object into a dict
accessibility_resource_scan_dict = accessibility_resource_scan_instance.to_dict()
# create an instance of AccessibilityResourceScan from a dict
accessibility_resource_scan_from_dict = AccessibilityResourceScan.from_dict(accessibility_resource_scan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


