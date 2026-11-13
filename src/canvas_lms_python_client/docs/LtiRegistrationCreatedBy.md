# LtiRegistrationCreatedBy


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

## Example

```python
from canvas_lms_python_client.models.lti_registration_created_by import LtiRegistrationCreatedBy

# TODO update the JSON string below
json = "{}"
# create an instance of LtiRegistrationCreatedBy from a JSON string
lti_registration_created_by_instance = LtiRegistrationCreatedBy.from_json(json)
# print the JSON string representation of the object
print(LtiRegistrationCreatedBy.to_json())

# convert the object into a dict
lti_registration_created_by_dict = lti_registration_created_by_instance.to_dict()
# create an instance of LtiRegistrationCreatedBy from a dict
lti_registration_created_by_from_dict = LtiRegistrationCreatedBy.from_dict(lti_registration_created_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


