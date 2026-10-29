# OutcomeProficiencyApiCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ratings_description** | **str** | The description of the rating level. | [optional] 
**ratings_points** | **int** | The non-negative number of points of the rating level. Points across ratings should be strictly decreasing in value. | [optional] 
**ratings_mastery** | **int** | Indicates the rating level where mastery is first achieved. Only one rating in a proficiency should be marked for mastery. | [optional] 
**ratings_color** | **int** | The color associated with the rating level. Should be a hex color code like &#39;00FFFF&#39;. | [optional] 

## Example

```python
from canvas_lms_python_client.models.outcome_proficiency_api_create_request import OutcomeProficiencyApiCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OutcomeProficiencyApiCreateRequest from a JSON string
outcome_proficiency_api_create_request_instance = OutcomeProficiencyApiCreateRequest.from_json(json)
# print the JSON string representation of the object
print(OutcomeProficiencyApiCreateRequest.to_json())

# convert the object into a dict
outcome_proficiency_api_create_request_dict = outcome_proficiency_api_create_request_instance.to_dict()
# create an instance of OutcomeProficiencyApiCreateRequest from a dict
outcome_proficiency_api_create_request_from_dict = OutcomeProficiencyApiCreateRequest.from_dict(outcome_proficiency_api_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


