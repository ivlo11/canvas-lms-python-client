# Outcome



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | the ID of the outcome | [optional] 
**url** | **str** | the URL for fetching/updating the outcome. should be treated as opaque | [optional] 
**context_id** | **int** | the context owning the outcome. may be null for global outcomes | [optional] 
**context_type** | **str** |  | [optional] 
**title** | **str** | title of the outcome | [optional] 
**display_name** | **str** | Optional friendly name for reporting | [optional] 
**description** | **str** | description of the outcome. omitted in the abbreviated form. | [optional] 
**vendor_guid** | **str** | A custom GUID for the learning standard. | [optional] 
**points_possible** | **float** | maximum points possible. included only if the outcome embeds a rubric criterion. omitted in the abbreviated form. | [optional] 
**mastery_points** | **float** | points necessary to demonstrate mastery outcomes. included only if the outcome embeds a rubric criterion. omitted in the abbreviated form. | [optional] 
**calculation_method** | **str** | the method used to calculate a students score | [optional] 
**calculation_int** | **int** | this defines the variable value used by the calculation_method. included only if calculation_method uses it | [optional] 
**ratings** | [**List[RubricRating]**](RubricRating.md) | possible ratings for this outcome. included only if the outcome embeds a rubric criterion. omitted in the abbreviated form. | [optional] 
**can_edit** | **bool** | whether the current user can update the outcome | [optional] 
**can_unlink** | **bool** | whether the outcome can be unlinked | [optional] 
**assessed** | **bool** | whether this outcome has been used to assess a student | [optional] 
**has_updateable_rubrics** | **bool** | whether updates to this outcome will propagate to unassessed rubrics that have imported it | [optional] 
**friendly_description** | **str** |  | [optional] 
**proficiency_context_id** | **str** |  | [optional] 
**proficiency_context_type** | **str** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.outcome import Outcome

# TODO update the JSON string below
json = "{}"
# create an instance of Outcome from a JSON string
outcome_instance = Outcome.from_json(json)
# print the JSON string representation of the object
print(Outcome.to_json())

# convert the object into a dict
outcome_dict = outcome_instance.to_dict()
# create an instance of Outcome from a dict
outcome_from_dict = Outcome.from_dict(outcome_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


