# AuthenticationEventLinks



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login** | **int** | ID of the login (pseudonym) associated with the event | [optional] 
**account** | **int** | ID of the account associated with the event. will match the account_id in the associated login. | [optional] 
**user** | **int** | ID of the user associated with the event. will match the user_id in the associated login. | [optional] 
**page_view** | **str** | ID of the page view during the event if it exists. | [optional] 

## Example

```python
from canvas_lms_python_client.models.authentication_event_links import AuthenticationEventLinks

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationEventLinks from a JSON string
authentication_event_links_instance = AuthenticationEventLinks.from_json(json)
# print the JSON string representation of the object
print(AuthenticationEventLinks.to_json())

# convert the object into a dict
authentication_event_links_dict = authentication_event_links_instance.to_dict()
# create an instance of AuthenticationEventLinks from a dict
authentication_event_links_from_dict = AuthenticationEventLinks.from_dict(authentication_event_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


