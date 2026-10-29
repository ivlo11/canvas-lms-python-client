# JwtsRefreshRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jwt** | **str** | An existing JWT token to be refreshed. The new token will have the same context and workflows as the existing token. | 

## Example

```python
from canvas_lms_python_client.models.jwts_refresh_request import JwtsRefreshRequest

# TODO update the JSON string below
json = "{}"
# create an instance of JwtsRefreshRequest from a JSON string
jwts_refresh_request_instance = JwtsRefreshRequest.from_json(json)
# print the JSON string representation of the object
print(JwtsRefreshRequest.to_json())

# convert the object into a dict
jwts_refresh_request_dict = jwts_refresh_request_instance.to_dict()
# create an instance of JwtsRefreshRequest from a dict
jwts_refresh_request_from_dict = JwtsRefreshRequest.from_dict(jwts_refresh_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


