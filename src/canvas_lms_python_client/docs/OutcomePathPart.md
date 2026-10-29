# OutcomePathPart

An outcome or outcome group

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The title of the outcome or outcome group | [optional] 

## Example

```python
from canvas_lms_python_client.models.outcome_path_part import OutcomePathPart

# TODO update the JSON string below
json = "{}"
# create an instance of OutcomePathPart from a JSON string
outcome_path_part_instance = OutcomePathPart.from_json(json)
# print the JSON string representation of the object
print(OutcomePathPart.to_json())

# convert the object into a dict
outcome_path_part_dict = outcome_path_part_instance.to_dict()
# create an instance of OutcomePathPart from a dict
outcome_path_part_from_dict = OutcomePathPart.from_dict(outcome_path_part_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


