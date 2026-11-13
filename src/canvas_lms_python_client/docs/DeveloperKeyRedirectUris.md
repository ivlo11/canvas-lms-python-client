# DeveloperKeyRedirectUris

List of URLs used during OAuth2 flow to validate given redirect URI (API keys), or to redirect to after login (LTI keys)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from canvas_lms_python_client.models.developer_key_redirect_uris import DeveloperKeyRedirectUris

# TODO update the JSON string below
json = "{}"
# create an instance of DeveloperKeyRedirectUris from a JSON string
developer_key_redirect_uris_instance = DeveloperKeyRedirectUris.from_json(json)
# print the JSON string representation of the object
print(DeveloperKeyRedirectUris.to_json())

# convert the object into a dict
developer_key_redirect_uris_dict = developer_key_redirect_uris_instance.to_dict()
# create an instance of DeveloperKeyRedirectUris from a dict
developer_key_redirect_uris_from_dict = DeveloperKeyRedirectUris.from_dict(developer_key_redirect_uris_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


