# UsersSetCustomColorRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hexcode** | **str** | The hexcode of the color to set for the context, if you choose to pass the hexcode as a query parameter rather than in the request body you should NOT include the &#39;#&#39; unless you escape it first. | [optional] 

## Example

```python
from canvas_lms_python_client.models.users_set_custom_color_request import UsersSetCustomColorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UsersSetCustomColorRequest from a JSON string
users_set_custom_color_request_instance = UsersSetCustomColorRequest.from_json(json)
# print the JSON string representation of the object
print(UsersSetCustomColorRequest.to_json())

# convert the object into a dict
users_set_custom_color_request_dict = users_set_custom_color_request_instance.to_dict()
# create an instance of UsersSetCustomColorRequest from a dict
users_set_custom_color_request_from_dict = UsersSetCustomColorRequest.from_dict(users_set_custom_color_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


