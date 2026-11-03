# GradeChangeAuditApiForGraderResponse

Object response with `links`, `events`, `linked` (from the Canvas `@returns`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | **object** |  | [optional] 
**events** | [**List[GradeChangeEvent]**](GradeChangeEvent.md) |  | [optional] 
**linked** | **object** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.grade_change_audit_api_for_grader_response import GradeChangeAuditApiForGraderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GradeChangeAuditApiForGraderResponse from a JSON string
grade_change_audit_api_for_grader_response_instance = GradeChangeAuditApiForGraderResponse.from_json(json)
# print the JSON string representation of the object
print(GradeChangeAuditApiForGraderResponse.to_json())

# convert the object into a dict
grade_change_audit_api_for_grader_response_dict = grade_change_audit_api_for_grader_response_instance.to_dict()
# create an instance of GradeChangeAuditApiForGraderResponse from a dict
grade_change_audit_api_for_grader_response_from_dict = GradeChangeAuditApiForGraderResponse.from_dict(grade_change_audit_api_for_grader_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


