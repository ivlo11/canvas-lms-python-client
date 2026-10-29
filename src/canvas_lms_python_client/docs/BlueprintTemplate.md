# BlueprintTemplate



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the template. | [optional] 
**course_id** | **int** | The ID of the Course the template belongs to. | [optional] 
**last_export_completed_at** | **datetime** | Time when the last export was completed | [optional] 
**associated_course_count** | **int** | Number of associated courses for the template | [optional] 
**latest_migration** | [**BlueprintMigration**](BlueprintMigration.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.blueprint_template import BlueprintTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of BlueprintTemplate from a JSON string
blueprint_template_instance = BlueprintTemplate.from_json(json)
# print the JSON string representation of the object
print(BlueprintTemplate.to_json())

# convert the object into a dict
blueprint_template_dict = blueprint_template_instance.to_dict()
# create an instance of BlueprintTemplate from a dict
blueprint_template_from_dict = BlueprintTemplate.from_dict(blueprint_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


