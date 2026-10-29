# BlockEditorTemplate



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | the ID of the page | [optional] 
**name** | **str** | name of the template | [optional] 
**description** | **str** | description of the template | [optional] 
**created_at** | **datetime** | the creation date for the template | [optional] 
**updated_at** | **datetime** | the date the template was last updated | [optional] 
**node_tree** | **str** | The JSON data that is the template | [optional] 
**editor_version** | **str** | The version of the editor that created the template | [optional] 
**template_type** | **str** | The type of template. One of &#39;block&#39;, &#39;section&#39;, or &#39;page&#39; | [optional] 
**workflow_state** | **str** | String indicating what state this assignment is in. | [optional] 

## Example

```python
from canvas_lms_python_client.models.block_editor_template import BlockEditorTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of BlockEditorTemplate from a JSON string
block_editor_template_instance = BlockEditorTemplate.from_json(json)
# print the JSON string representation of the object
print(BlockEditorTemplate.to_json())

# convert the object into a dict
block_editor_template_dict = block_editor_template_instance.to_dict()
# create an instance of BlockEditorTemplate from a dict
block_editor_template_from_dict = BlockEditorTemplate.from_dict(block_editor_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


