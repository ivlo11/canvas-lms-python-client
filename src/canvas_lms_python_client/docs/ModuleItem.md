# ModuleItem



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | the ID of the module item | [optional] 
**duration** | **int** | the duration of the module item | [optional] 
**course_pace_id** | **int** | the course pace id of the module item | [optional] 
**root_account_id** | **int** | the root account id of the module item | [optional] 
**module_item_id** | **int** | the module item id of the module item | [optional] 
**assignment_title** | **str** | The title of the item assignment | [optional] 
**points_possible** | **float** | The points of the item | [optional] 
**assignment_link** | **str** | The link of the item assignment | [optional] 
**position** | **int** | the current position of the module item | [optional] 
**module_item_type** | **str** | The module item type of the item assignment | [optional] 
**published** | **bool** | published boolean value for course pace | [optional] 
**completion_requirement** | **object** |  | [optional] 
**content_details** | **object** |  | [optional] 
**content_id** | **int** |  | [optional] 
**estimated_duration** | **str** |  | [optional] 
**external_url** | **str** |  | [optional] 
**html_url** | **str** |  | [optional] 
**indent** | **int** |  | [optional] 
**mastery_paths** | **object** |  | [optional] 
**module_id** | **int** |  | [optional] 
**new_tab** | **bool** |  | [optional] 
**page_url** | **str** |  | [optional] 
**publish_at** | **object** |  | [optional] 
**quiz_lti** | **bool** |  | [optional] 
**title** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**unpublishable** | **bool** |  | [optional] 
**url** | **str** |  | [optional] 
**created** | **List[object]** |  | [optional] 
**errors** | **List[object]** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.module_item import ModuleItem

# TODO update the JSON string below
json = "{}"
# create an instance of ModuleItem from a JSON string
module_item_instance = ModuleItem.from_json(json)
# print the JSON string representation of the object
print(ModuleItem.to_json())

# convert the object into a dict
module_item_dict = module_item_instance.to_dict()
# create an instance of ModuleItem from a dict
module_item_from_dict = ModuleItem.from_dict(module_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


