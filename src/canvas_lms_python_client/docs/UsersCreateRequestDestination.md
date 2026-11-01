# UsersCreateRequestDestination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | If you&#39;re setting the password for the newly created user, you can provide this param with a valid URL pointing into this Canvas installation, and the response will include a destination field that&#39;s a URL that you can redirect a browser to and have the newly created user automatically logged in. The URL is only valid for a short time, and must match the domain this request is directed to, and be for a well-formed path that Canvas can recognize. | [optional] 

## Example

```python
from canvas_lms_python_client.models.users_create_request_destination import UsersCreateRequestDestination

# TODO update the JSON string below
json = "{}"
# create an instance of UsersCreateRequestDestination from a JSON string
users_create_request_destination_instance = UsersCreateRequestDestination.from_json(json)
# print the JSON string representation of the object
print(UsersCreateRequestDestination.to_json())

# convert the object into a dict
users_create_request_destination_dict = users_create_request_destination_instance.to_dict()
# create an instance of UsersCreateRequestDestination from a dict
users_create_request_destination_from_dict = UsersCreateRequestDestination.from_dict(users_create_request_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


