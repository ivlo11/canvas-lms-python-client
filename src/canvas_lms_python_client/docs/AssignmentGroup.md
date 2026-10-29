# AssignmentGroup



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | the id of the Assignment Group | [optional] 
**name** | **str** | the name of the Assignment Group | [optional] 
**position** | **int** | the position of the Assignment Group | [optional] 
**group_weight** | **int** | the weight of the Assignment Group | [optional] 
**sis_source_id** | **str** | the sis source id of the Assignment Group | [optional] 
**integration_data** | **object** | the integration data of the Assignment Group | [optional] 
**assignments** | **List[int]** | the assignments in this Assignment Group (see the Assignment API for a detailed list of fields) | [optional] 
**rules** | [**GradingRules**](GradingRules.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.assignment_group import AssignmentGroup

# TODO update the JSON string below
json = "{}"
# create an instance of AssignmentGroup from a JSON string
assignment_group_instance = AssignmentGroup.from_json(json)
# print the JSON string representation of the object
print(AssignmentGroup.to_json())

# convert the object into a dict
assignment_group_dict = assignment_group_instance.to_dict()
# create an instance of AssignmentGroup from a dict
assignment_group_from_dict = AssignmentGroup.from_dict(assignment_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


