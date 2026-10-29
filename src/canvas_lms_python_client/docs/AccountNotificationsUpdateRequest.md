# AccountNotificationsUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_notification_roles** | **List[str]** | The role(s) to send global notification to.  Note:  ommitting this field will send to everyone Example:   account_notification_roles: [\&quot;StudentEnrollment\&quot;, \&quot;TeacherEnrollment\&quot;] | [optional] 
**account_notification** | [**AccountNotificationsUpdateRequestAccountNotification**](AccountNotificationsUpdateRequestAccountNotification.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.account_notifications_update_request import AccountNotificationsUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AccountNotificationsUpdateRequest from a JSON string
account_notifications_update_request_instance = AccountNotificationsUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(AccountNotificationsUpdateRequest.to_json())

# convert the object into a dict
account_notifications_update_request_dict = account_notifications_update_request_instance.to_dict()
# create an instance of AccountNotificationsUpdateRequest from a dict
account_notifications_update_request_from_dict = AccountNotificationsUpdateRequest.from_dict(account_notifications_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


