# OutcomeRollupLinks



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**course** | [**OutcomeRollupLinksCourse**](OutcomeRollupLinksCourse.md) |  | [optional] 
**user** | [**OutcomeRollupLinksUser**](OutcomeRollupLinksUser.md) |  | [optional] 
**section** | [**OutcomeRollupLinksSection**](OutcomeRollupLinksSection.md) |  | [optional] 
**status** | **str** |  | [optional] 

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


