# OutcomesApiUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The new outcome title. | [optional] 
**display_name** | **str** | A friendly name shown in reports for outcomes with cryptic titles, such as common core standards names. | [optional] 
**description** | **str** | The new outcome description. | [optional] 
**vendor_guid** | **str** | A custom GUID for the learning standard. | [optional] 
**mastery_points** | **int** | The new mastery threshold for the embedded rubric criterion. | [optional] 
**ratings_description** | **str** | The description of a new rating level for the embedded rubric criterion. | [optional] 
**ratings_points** | **int** | The points corresponding to a new rating level for the embedded rubric criterion. | [optional] 
**calculation_method** | **str** | The new calculation method. If the Outcomes New Decaying Average Calculation Method FF is ENABLED then \&quot;weighted_average\&quot; can be used and it is same as previous \&quot;decaying_average\&quot; and new \&quot;decaying_average\&quot; will have improved version of calculation. | [optional] 
**calculation_int** | **int** | The new calculation int.  Only applies if the calculation_method is \&quot;decaying_average\&quot; or \&quot;n_mastery\&quot; | [optional] 
**add_defaults** | **bool** | If defaults are requested, then color and mastery level defaults will be added to outcome ratings in the result. This will only take effect if the Account Level Mastery Scales FF is DISABLED | [optional] 

## Example

```python
from canvas_lms_python_client.models.outcomes_api_update_request import OutcomesApiUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OutcomesApiUpdateRequest from a JSON string
outcomes_api_update_request_instance = OutcomesApiUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(OutcomesApiUpdateRequest.to_json())

# convert the object into a dict
outcomes_api_update_request_dict = outcomes_api_update_request_instance.to_dict()
# create an instance of OutcomesApiUpdateRequest from a dict
outcomes_api_update_request_from_dict = OutcomesApiUpdateRequest.from_dict(outcomes_api_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


