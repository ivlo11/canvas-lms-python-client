# OutcomeLink



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | the URL for fetching/updating the outcome link. should be treated as opaque | [optional] 
**context_id** | **int** | the context owning the outcome link. will match the context owning the outcome group containing the outcome link; included for convenience. may be null for links in global outcome groups. | [optional] 
**context_type** | **str** |  | [optional] 
**outcome_group** | [**OutcomeGroup**](OutcomeGroup.md) |  | [optional] 
**outcome** | [**Outcome**](Outcome.md) |  | [optional] 
**assessed** | **bool** | whether this outcome has been used to assess a student in the context of this outcome link.  In other words, this will be set to true if the context is a course, and a student has been assessed with this outcome in that course. | [optional] 
**can_unlink** | **bool** | whether this outcome link is manageable and is not the last link to an aligned outcome | [optional] 
**quiz_lti** | **bool** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.outcome_link import OutcomeLink

# TODO update the JSON string below
json = "{}"
# create an instance of OutcomeLink from a JSON string
outcome_link_instance = OutcomeLink.from_json(json)
# print the JSON string representation of the object
print(OutcomeLink.to_json())

# convert the object into a dict
outcome_link_dict = outcome_link_instance.to_dict()
# create an instance of OutcomeLink from a dict
outcome_link_from_dict = OutcomeLink.from_dict(outcome_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


