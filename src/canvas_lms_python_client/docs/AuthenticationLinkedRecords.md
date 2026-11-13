# AuthenticationLinkedRecords

The records referenced by the events on a page of authentication events

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logins** | [**List[Login]**](Login.md) | The logins associated with the events | [optional] 
**accounts** | [**List[Account]**](Account.md) | The accounts associated with the events | [optional] 
**users** | [**List[User]**](User.md) | The users associated with the events | [optional] 
**page_views** | [**List[PageView]**](PageView.md) | The page views during the events | [optional] 

## Example

```python
from canvas_lms_python_client.models.authentication_linked_records import AuthenticationLinkedRecords

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationLinkedRecords from a JSON string
authentication_linked_records_instance = AuthenticationLinkedRecords.from_json(json)
# print the JSON string representation of the object
print(AuthenticationLinkedRecords.to_json())

# convert the object into a dict
authentication_linked_records_dict = authentication_linked_records_instance.to_dict()
# create an instance of AuthenticationLinkedRecords from a dict
authentication_linked_records_from_dict = AuthenticationLinkedRecords.from_dict(authentication_linked_records_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


