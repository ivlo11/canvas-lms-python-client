# OutcomeRollupLinks



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**course** | **int** | If an aggregate result was requested, the course field will be present. Otherwise, the user and section field will be present (Optional) The id of the course that this rollup applies to | [optional] 
**user** | **int** | (Optional) The id of the user that this rollup applies to | [optional] 
**section** | **int** | (Optional) The id of the section the user is in | [optional] 

## Example

```python
from canvas_lms_python_client.models.outcome_rollup_links import OutcomeRollupLinks

# TODO update the JSON string below
json = "{}"
# create an instance of OutcomeRollupLinks from a JSON string
outcome_rollup_links_instance = OutcomeRollupLinks.from_json(json)
# print the JSON string representation of the object
print(OutcomeRollupLinks.to_json())

# convert the object into a dict
outcome_rollup_links_dict = outcome_rollup_links_instance.to_dict()
# create an instance of OutcomeRollupLinks from a dict
outcome_rollup_links_from_dict = OutcomeRollupLinks.from_dict(outcome_rollup_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


