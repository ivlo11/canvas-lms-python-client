# PermissionsHelpGroupsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manage_account_calendar** | **object** |  | [optional] 
**manage_assignments_and_quizzes** | **object** |  | [optional] 
**manage_course_content** | **object** |  | [optional] 
**manage_course_designer_enrollments** | **object** |  | [optional] 
**manage_course_observer_enrollments** | **object** |  | [optional] 
**manage_course_student_enrollments** | **object** |  | [optional] 
**manage_course_ta_enrollments** | **object** |  | [optional] 
**manage_course_teacher_enrollments** | **object** |  | [optional] 
**manage_course_templates** | **object** |  | [optional] 
**manage_courses** | **object** |  | [optional] 
**manage_differentiation_tags** | **object** |  | [optional] 
**manage_files** | **object** |  | [optional] 
**manage_groups** | **object** |  | [optional] 
**manage_institutional_tags** | **object** |  | [optional] 
**manage_lti** | **object** |  | [optional] 
**manage_rate_limiting** | **object** |  | [optional] 
**manage_rules** | **object** |  | [optional] 
**manage_sections** | **object** |  | [optional] 
**manage_temporary_enrollments** | **object** |  | [optional] 
**manage_wiki** | **object** |  | [optional] 
**users_manage_access_tokens** | **object** |  | [optional] 
**view_advanced_analytics** | **object** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.permissions_help_groups_response import PermissionsHelpGroupsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionsHelpGroupsResponse from a JSON string
permissions_help_groups_response_instance = PermissionsHelpGroupsResponse.from_json(json)
# print the JSON string representation of the object
print(PermissionsHelpGroupsResponse.to_json())

# convert the object into a dict
permissions_help_groups_response_dict = permissions_help_groups_response_instance.to_dict()
# create an instance of PermissionsHelpGroupsResponse from a dict
permissions_help_groups_response_from_dict = PermissionsHelpGroupsResponse.from_dict(permissions_help_groups_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


