# DeveloperKeysLookupUtidsResponse

Object response with `api_registrations` (from the Canvas `@returns`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_registrations** | [**List[ApiRegistration]**](ApiRegistration.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.developer_keys_lookup_utids_response import DeveloperKeysLookupUtidsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeveloperKeysLookupUtidsResponse from a JSON string
developer_keys_lookup_utids_response_instance = DeveloperKeysLookupUtidsResponse.from_json(json)
# print the JSON string representation of the object
print(DeveloperKeysLookupUtidsResponse.to_json())

# convert the object into a dict
developer_keys_lookup_utids_response_dict = developer_keys_lookup_utids_response_instance.to_dict()
# create an instance of DeveloperKeysLookupUtidsResponse from a dict
developer_keys_lookup_utids_response_from_dict = DeveloperKeysLookupUtidsResponse.from_dict(developer_keys_lookup_utids_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


