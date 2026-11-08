# User

A Canvas user, e.g. a student, teacher, administrator, observer, etc.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the user. | 
**name** | **str** | The name of the user. | [optional] 
**sortable_name** | **str** | The name of the user that is should be used for sorting groups of users, such as in the gradebook. | [optional] 
**last_name** | **str** | The last name of the user. | [optional] 
**first_name** | **str** | The first name of the user. | [optional] 
**short_name** | **str** | A short name the user has selected, for use in conversations or other less formal places through the site. | [optional] 
**sis_user_id** | **str** | The SIS ID associated with the user.  This field is only included if the user came from a SIS import and has permissions to view SIS information. | [optional] 
**sis_import_id** | **int** | The id of the SIS import.  This field is only included if the user came from a SIS import and has permissions to manage SIS information. | [optional] 
**integration_id** | **str** | The integration_id associated with the user.  This field is only included if the user came from a SIS import and has permissions to view SIS information. | [optional] 
**login_id** | **str** | The unique login id for the user.  This is what the user uses to log in to Canvas. | [optional] 
**avatar_url** | **str** | If avatars are enabled, this field will be included and contain a url to retrieve the user&#39;s avatar. | [optional] 
**avatar_state** | **str** | Optional: If avatars are enabled and caller is admin, this field can be requested and will contain the current state of the user&#39;s avatar. | [optional] 
**enrollments** | [**List[Enrollment]**](Enrollment.md) | Optional: This field can be requested with certain API calls, and will return a list of the users active enrollments. See the List enrollments API for more details about the format of these records. | [optional] 
**email** | **str** | Optional: This field can be requested with certain API calls, and will return the users primary email address. | [optional] 
**locale** | **str** | Optional: This field can be requested with certain API calls, and will return the users locale in RFC 5646 format. | [optional] 
**last_login** | **datetime** | Optional: This field is only returned in certain API calls, and will return a timestamp representing the last time the user logged in to canvas. | [optional] 
**time_zone** | **str** | Optional: This field is only returned in certain API calls, and will return the IANA time zone name of the user&#39;s preferred timezone. | [optional] 
**bio** | **str** | Optional: The user&#39;s bio. | [optional] 
**pronouns** | **str** | Optional: This field is only returned if pronouns are enabled, and will return the pronouns of the user. | [optional] 
**effective_locale** | **str** | Optional: This field is only returned in certain API calls, and only for the current user. It will return the locale the user sees Canvas in, in RFC 5646 format. | [optional] 
**uuid** | **str** | Optional: This field is only returned in certain API calls (for example with include[]&#x3D;uuid), and will return the user&#39;s Canvas UUID. | [optional] 
**permissions** | [**UserPermissions**](UserPermissions.md) |  | [optional] 
**account_uuid** | **str** |  | [optional] 
**anonymous_id** | **str** |  | [optional] 
**avatar_image_source** | **str** |  | [optional] 
**avatar_image_updated_at** | **str** |  | [optional] 
**avatar_image_url** | **str** |  | [optional] 
**browser_locale** | **str** |  | [optional] 
**confirmation_url** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**crocodoc_id** | **int** |  | [optional] 
**custom_links** | **List[object]** |  | [optional] 
**deleted_at** | **str** |  | [optional] 
**destination** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**group_ids** | **List[int]** |  | [optional] 
**group_submissions** | **List[int]** |  | [optional] 
**has_non_collaborative_groups** | **bool** |  | [optional] 
**html_url** | **str** |  | [optional] 
**initial_enrollment_type** | **str** |  | [optional] 
**instructure_identity_id** | **str** |  | [optional] 
**is_inactive** | **bool** |  | [optional] 
**last_logged_out** | **str** |  | [optional] 
**lti_context_id** | **str** |  | [optional] 
**lti_id** | **str** |  | [optional] 
**merged_into_user_id** | **int** |  | [optional] 
**observation_link_root_account_ids** | **List[int]** |  | [optional] 
**preferences** | **object** |  | [optional] 
**pronunciation** | **str** |  | [optional] 
**public** | **bool** |  | [optional] 
**reminder_time_for_due_dates** | **int** |  | [optional] 
**reminder_time_for_grading** | **int** |  | [optional] 
**root_account_ids** | **List[object]** |  | [optional] 
**school_name** | **str** |  | [optional] 
**school_position** | **str** |  | [optional] 
**sections** | **str** |  | [optional] 
**show_user_services** | **bool** |  | [optional] 
**storage_quota** | **int** |  | [optional] 
**stuck_sis_fields** | **List[str]** |  | [optional] 
**subscribe_to_emails** | **bool** |  | [optional] 
**terms_of_use** | **bool** |  | [optional] 
**title** | **str** |  | [optional] 
**turnitin_id** | **int** |  | [optional] 
**unread_conversations_count** | **int** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**visible_inbox_types** | **str** |  | [optional] 
**workflow_state** | **str** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print(User.to_json())

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_from_dict = User.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


