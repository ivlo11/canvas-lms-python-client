# OutcomeGroupsApiLinkForOtherRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**move_from** | **int** | The ID of the old outcome group. Only used if outcome_id is present. | [optional] 
**title** | **str** | The title of the new outcome. Required if outcome_id is absent. | [optional] 
**display_name** | **str** | A friendly name shown in reports for outcomes with cryptic titles, such as common core standards names. | [optional] 
**description** | **str** | The description of the new outcome. | [optional] 
**vendor_guid** | **str** | A custom GUID for the learning standard. | [optional] 
**mastery_points** | **int** | The mastery threshold for the embedded rubric criterion. | [optional] 
**ratings_description** | **str** | The description of a rating level for the embedded rubric criterion. | [optional] 
**ratings_points** | **int** | The points corresponding to a rating level for the embedded rubric criterion. | [optional] 
**calculation_method** | **str** | The new calculation method.  Defaults to \&quot;decaying_average\&quot; if the Outcomes New Decaying Average Calculation Method FF is ENABLED then Defaults to \&quot;weighted_average\&quot; | [optional] 
**calculation_int** | **int** | The new calculation int.  Only applies if the calculation_method is \&quot;weighted_average\&quot;, \&quot;decaying_average\&quot; or \&quot;n_mastery\&quot;. Defaults to 65 | [optional] 

## Example

```python
from canvas_lms_python_client.models.outcome_groups_api_link_for_other_request import OutcomeGroupsApiLinkForOtherRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OutcomeGroupsApiLinkForOtherRequest from a JSON string
outcome_groups_api_link_for_other_request_instance = OutcomeGroupsApiLinkForOtherRequest.from_json(json)
# print the JSON string representation of the object
print(OutcomeGroupsApiLinkForOtherRequest.to_json())

# convert the object into a dict
outcome_groups_api_link_for_other_request_dict = outcome_groups_api_link_for_other_request_instance.to_dict()
# create an instance of OutcomeGroupsApiLinkForOtherRequest from a dict
outcome_groups_api_link_for_other_request_from_dict = OutcomeGroupsApiLinkForOtherRequest.from_dict(outcome_groups_api_link_for_other_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


