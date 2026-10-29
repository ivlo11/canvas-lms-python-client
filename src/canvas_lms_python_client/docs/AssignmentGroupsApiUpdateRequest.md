# AssignmentGroupsApiUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The assignment group&#39;s name | [optional] 
**position** | **int** | The position of this assignment group in relation to the other assignment groups | [optional] 
**group_weight** | **float** | The percent of the total grade that this assignment group represents | [optional] 
**sis_source_id** | **str** | The sis source id of the Assignment Group | [optional] 
**integration_data** | **str** | The integration data of the Assignment Group | [optional] 
**rules** | **str** | The grading rules that are applied within this assignment group See the Assignment Group object definition for format | [optional] 

## Example

```python
from canvas_lms_python_client.models.assignment_groups_api_update_request import AssignmentGroupsApiUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssignmentGroupsApiUpdateRequest from a JSON string
assignment_groups_api_update_request_instance = AssignmentGroupsApiUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(AssignmentGroupsApiUpdateRequest.to_json())

# convert the object into a dict
assignment_groups_api_update_request_dict = assignment_groups_api_update_request_instance.to_dict()
# create an instance of AssignmentGroupsApiUpdateRequest from a dict
assignment_groups_api_update_request_from_dict = AssignmentGroupsApiUpdateRequest.from_dict(assignment_groups_api_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


