# GradeChangeAuditApiForAssignmentResponse

Object response with `links`, `events`, `linked` (from the Canvas `@returns`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | **object** |  | [optional] 
**events** | [**List[GradeChangeEvent]**](GradeChangeEvent.md) |  | [optional] 
**linked** | [**GradeChangeLinkedRecords**](GradeChangeLinkedRecords.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.grade_change_audit_api_for_assignment_response import GradeChangeAuditApiForAssignmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GradeChangeAuditApiForAssignmentResponse from a JSON string
grade_change_audit_api_for_assignment_response_instance = GradeChangeAuditApiForAssignmentResponse.from_json(json)
# print the JSON string representation of the object
print(GradeChangeAuditApiForAssignmentResponse.to_json())

# convert the object into a dict
grade_change_audit_api_for_assignment_response_dict = grade_change_audit_api_for_assignment_response_instance.to_dict()
# create an instance of GradeChangeAuditApiForAssignmentResponse from a dict
grade_change_audit_api_for_assignment_response_from_dict = GradeChangeAuditApiForAssignmentResponse.from_dict(grade_change_audit_api_for_assignment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


