# OutcomeRollup



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scores** | [**OutcomeRollupScore**](OutcomeRollupScore.md) |  | [optional] 
**name** | **str** | The name of the resource for this rollup. For example, the user name. | [optional] 
**links** | [**OutcomeRollupLinks**](OutcomeRollupLinks.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.outcome_rollup import OutcomeRollup

# TODO update the JSON string below
json = "{}"
# create an instance of OutcomeRollup from a JSON string
outcome_rollup_instance = OutcomeRollup.from_json(json)
# print the JSON string representation of the object
print(OutcomeRollup.to_json())

# convert the object into a dict
outcome_rollup_dict = outcome_rollup_instance.to_dict()
# create an instance of OutcomeRollup from a dict
outcome_rollup_from_dict = OutcomeRollup.from_dict(outcome_rollup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


