# Profile

Profile details for a Canvas user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the user. | [optional] 
**name** | **str** | Sample User | [optional] 
**short_name** | **str** | Sample User | [optional] 
**sortable_name** | **str** | user, sample | [optional] 
**title** | **str** |  | [optional] 
**bio** | **str** |  | [optional] 
**pronunciation** | **str** | Name pronunciation | [optional] 
**primary_email** | **str** | sample_user@example.com | [optional] 
**login_id** | **str** | sample_user@example.com | [optional] 
**sis_user_id** | **str** | sis1 | [optional] 
**lti_user_id** | **str** |  | [optional] 
**avatar_url** | **str** | The avatar_url can change over time, so we recommend not caching it for more than a few hours | [optional] 
**calendar** | [**CalendarLink**](CalendarLink.md) |  | [optional] 
**time_zone** | **str** | Optional: This field is only returned in certain API calls, and will return the IANA time zone name of the user&#39;s preferred timezone. | [optional] 
**locale** | **str** | The users locale. | [optional] 
**k5_user** | **bool** | Optional: Whether or not the user is a K5 user. This field is nil if the user settings are not for the user making the request. | [optional] 
**use_classic_font_in_k5** | **bool** | Optional: Whether or not the user should see the classic font on the dashboard. Only applies if k5_user is true. This field is nil if the user settings are not for the user making the request. | [optional] 

## Example

```python
from canvas_lms_python_client.models.profile import Profile

# TODO update the JSON string below
json = "{}"
# create an instance of Profile from a JSON string
profile_instance = Profile.from_json(json)
# print the JSON string representation of the object
print(Profile.to_json())

# convert the object into a dict
profile_dict = profile_instance.to_dict()
# create an instance of Profile from a dict
profile_from_dict = Profile.from_dict(profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


