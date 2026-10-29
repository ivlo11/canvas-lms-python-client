# OutcomePath

The full path to an outcome

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | A unique identifier for this outcome | [optional] 
**parts** | [**OutcomePathPart**](OutcomePathPart.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.outcome_path import OutcomePath

# TODO update the JSON string below
json = "{}"
# create an instance of OutcomePath from a JSON string
outcome_path_instance = OutcomePath.from_json(json)
# print the JSON string representation of the object
print(OutcomePath.to_json())

# convert the object into a dict
outcome_path_dict = outcome_path_instance.to_dict()
# create an instance of OutcomePath from a dict
outcome_path_from_dict = OutcomePath.from_dict(outcome_path_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


