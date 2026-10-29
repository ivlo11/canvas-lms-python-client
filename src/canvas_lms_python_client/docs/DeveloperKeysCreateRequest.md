# DeveloperKeysCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**developer_key** | [**DeveloperKeysCreateRequestDeveloperKey**](DeveloperKeysCreateRequestDeveloperKey.md) |  | 

## Example

```python
from canvas_lms_python_client.models.developer_keys_create_request import DeveloperKeysCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeveloperKeysCreateRequest from a JSON string
developer_keys_create_request_instance = DeveloperKeysCreateRequest.from_json(json)
# print the JSON string representation of the object
print(DeveloperKeysCreateRequest.to_json())

# convert the object into a dict
developer_keys_create_request_dict = developer_keys_create_request_instance.to_dict()
# create an instance of DeveloperKeysCreateRequest from a dict
developer_keys_create_request_from_dict = DeveloperKeysCreateRequest.from_dict(developer_keys_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


