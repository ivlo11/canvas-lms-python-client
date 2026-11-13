# OutcomeRollupScore



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score** | **float** | The rollup score for the outcome, based on the student alignment scores related to the outcome. This could be null if the student has no related scores. | [optional] 
**count** | **int** | The number of alignment scores included in this rollup. | [optional] 
**links** | [**OutcomeRollupScoreLinks**](OutcomeRollupScoreLinks.md) |  | [optional] 
**hide_points** | **bool** |  | [optional] 
**submitted_at** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.outcome_rollup_score import OutcomeRollupScore

# TODO update the JSON string below
json = "{}"
# create an instance of OutcomeRollupScore from a JSON string
outcome_rollup_score_instance = OutcomeRollupScore.from_json(json)
# print the JSON string representation of the object
print(OutcomeRollupScore.to_json())

# convert the object into a dict
outcome_rollup_score_dict = outcome_rollup_score_instance.to_dict()
# create an instance of OutcomeRollupScore from a dict
outcome_rollup_score_from_dict = OutcomeRollupScore.from_dict(outcome_rollup_score_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


