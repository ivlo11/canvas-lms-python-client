# OutcomeGroup



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | the ID of the outcome group | [optional] 
**url** | **str** | the URL for fetching/updating the outcome group. should be treated as opaque | [optional] 
**parent_outcome_group** | [**OutcomeGroup**](OutcomeGroup.md) |  | [optional] 
**context_id** | **int** | the context owning the outcome group. may be null for global outcome groups. omitted in the abbreviated form. | [optional] 
**context_type** | **str** |  | [optional] 
**title** | **str** | title of the outcome group | [optional] 
**description** | **str** | description of the outcome group. omitted in the abbreviated form. | [optional] 
**vendor_guid** | **str** | A custom GUID for the learning standard. | [optional] 
**subgroups_url** | **str** | the URL for listing/creating subgroups under the outcome group. should be treated as opaque | [optional] 
**outcomes_url** | **str** | the URL for listing/creating outcome links under the outcome group. should be treated as opaque | [optional] 
**import_url** | **str** | the URL for importing another group into this outcome group. should be treated as opaque. omitted in the abbreviated form. | [optional] 
**can_edit** | **bool** | whether the current user can update the outcome group | [optional] 

## Example

```python
from canvas_lms_python_client.models.outcome_group import OutcomeGroup

# TODO update the JSON string below
json = "{}"
# create an instance of OutcomeGroup from a JSON string
outcome_group_instance = OutcomeGroup.from_json(json)
# print the JSON string representation of the object
print(OutcomeGroup.to_json())

# convert the object into a dict
outcome_group_dict = outcome_group_instance.to_dict()
# create an instance of OutcomeGroup from a dict
outcome_group_from_dict = OutcomeGroup.from_dict(outcome_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


