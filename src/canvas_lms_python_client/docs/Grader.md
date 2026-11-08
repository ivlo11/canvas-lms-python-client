# Grader



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | the user_id of the user who graded the contained submissions | [optional] 
**name** | **str** | the name of the user who graded the contained submissions | [optional] 
**assignments** | [**List[AssignmentGroupAssignmentsInner]**](AssignmentGroupAssignmentsInner.md) | the assignment groups for all submissions in this response that were graded by this user.  The details are not nested inside here, but the fact that an assignment is present here means that the grader did grade submissions for this assignment on the contextual date. You can use the id of a grader and of an assignment to make another API call to find all submissions for a grader/assignment combination on a given date. | [optional] 

## Example

```python
from canvas_lms_python_client.models.grader import Grader

# TODO update the JSON string below
json = "{}"
# create an instance of Grader from a JSON string
grader_instance = Grader.from_json(json)
# print the JSON string representation of the object
print(Grader.to_json())

# convert the object into a dict
grader_dict = grader_instance.to_dict()
# create an instance of Grader from a dict
grader_from_dict = Grader.from_dict(grader_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


