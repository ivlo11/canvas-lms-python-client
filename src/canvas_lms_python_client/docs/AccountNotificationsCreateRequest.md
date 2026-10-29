# AccountNotificationsCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_notification_roles** | **List[str]** | The role(s) to send global notification to.  Note:  ommitting this field will send to everyone Example:   account_notification_roles: [\&quot;StudentEnrollment\&quot;, \&quot;TeacherEnrollment\&quot;] | [optional] 
**account_notification** | [**AccountNotificationsCreateRequestAccountNotification**](AccountNotificationsCreateRequestAccountNotification.md) |  | 

## Example

```python
from canvas_lms_python_client.models.account_notifications_create_request import AccountNotificationsCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AccountNotificationsCreateRequest from a JSON string
account_notifications_create_request_instance = AccountNotificationsCreateRequest.from_json(json)
# print the JSON string representation of the object
print(AccountNotificationsCreateRequest.to_json())

# convert the object into a dict
account_notifications_create_request_dict = account_notifications_create_request_instance.to_dict()
# create an instance of AccountNotificationsCreateRequest from a dict
account_notifications_create_request_from_dict = AccountNotificationsCreateRequest.from_dict(account_notifications_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


