# AuthenticationEvent



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the event. | [optional] 
**created_at** | **datetime** | timestamp of the event | [optional] 
**event_type** | **str** | authentication event type (&#39;login&#39; or &#39;logout&#39;) | [optional] 
**links** | [**AuthenticationEventLinks**](AuthenticationEventLinks.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.authentication_event import AuthenticationEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationEvent from a JSON string
authentication_event_instance = AuthenticationEvent.from_json(json)
# print the JSON string representation of the object
print(AuthenticationEvent.to_json())

# convert the object into a dict
authentication_event_dict = authentication_event_instance.to_dict()
# create an instance of AuthenticationEvent from a dict
authentication_event_from_dict = AuthenticationEvent.from_dict(authentication_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


