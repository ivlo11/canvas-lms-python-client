# LtiAssignment

A Canvas assignment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**points_possible** | **float** |  | [optional] 
**due_at** | **datetime** | The due date for the assignment. If a user id is supplied and an assignment override is in place this field will reflect the due date as it applies to the user. | [optional] 
**lti_id** | **str** |  | [optional] 
**course_id** | **int** |  | [optional] 
**lti_course_id** | **str** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.lti_assignment import LtiAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of LtiAssignment from a JSON string
lti_assignment_instance = LtiAssignment.from_json(json)
# print the JSON string representation of the object
print(LtiAssignment.to_json())

# convert the object into a dict
lti_assignment_dict = lti_assignment_instance.to_dict()
# create an instance of LtiAssignment from a dict
lti_assignment_from_dict = LtiAssignment.from_dict(lti_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


