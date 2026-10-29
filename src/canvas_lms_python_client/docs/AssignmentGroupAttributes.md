# AssignmentGroupAttributes

Some of the attributes of an Assignment Group. See Assignments API for more details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | the id of the Assignment Group | [optional] 
**name** | **str** | the name of the Assignment Group | [optional] 
**group_weight** | **int** | the weight of the Assignment Group | [optional] 
**sis_source_id** | **str** | the sis source id of the Assignment Group | [optional] 
**integration_data** | **object** | the integration data of the Assignment Group | [optional] 

## Example

```python
from canvas_lms_python_client.models.assignment_group_attributes import AssignmentGroupAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of AssignmentGroupAttributes from a JSON string
assignment_group_attributes_instance = AssignmentGroupAttributes.from_json(json)
# print the JSON string representation of the object
print(AssignmentGroupAttributes.to_json())

# convert the object into a dict
assignment_group_attributes_dict = assignment_group_attributes_instance.to_dict()
# create an instance of AssignmentGroupAttributes from a dict
assignment_group_attributes_from_dict = AssignmentGroupAttributes.from_dict(assignment_group_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


