# AssignmentDate

Object representing a due date for an assignment or quiz. If the due date came from an assignment override, it will have an 'id' field.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | (Optional, missing if &#39;base&#39; is present) id of the assignment override this date represents | [optional] 
**base** | **bool** | (Optional, present if &#39;id&#39; is missing) whether this date represents the assignment&#39;s or quiz&#39;s default due date | [optional] 
**title** | **str** |  | [optional] 
**due_at** | **datetime** | The due date for the assignment. Must be between the unlock date and the lock date if there are lock dates | [optional] 
**unlock_at** | **datetime** | The unlock date for the assignment. Must be before the due date if there is a due date. | [optional] 
**lock_at** | **datetime** | The lock date for the assignment. Must be after the due date if there is a due date. | [optional] 

## Example

```python
from canvas_lms_python_client.models.assignment_date import AssignmentDate

# TODO update the JSON string below
json = "{}"
# create an instance of AssignmentDate from a JSON string
assignment_date_instance = AssignmentDate.from_json(json)
# print the JSON string representation of the object
print(AssignmentDate.to_json())

# convert the object into a dict
assignment_date_dict = assignment_date_instance.to_dict()
# create an instance of AssignmentDate from a dict
assignment_date_from_dict = AssignmentDate.from_dict(assignment_date_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


