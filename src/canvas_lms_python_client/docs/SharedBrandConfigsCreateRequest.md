# SharedBrandConfigsCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shared_brand_config** | [**SharedBrandConfigsCreateRequestSharedBrandConfig**](SharedBrandConfigsCreateRequestSharedBrandConfig.md) |  | 

## Example

```python
from canvas_lms_python_client.models.shared_brand_configs_create_request import SharedBrandConfigsCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SharedBrandConfigsCreateRequest from a JSON string
shared_brand_configs_create_request_instance = SharedBrandConfigsCreateRequest.from_json(json)
# print the JSON string representation of the object
print(SharedBrandConfigsCreateRequest.to_json())

# convert the object into a dict
shared_brand_configs_create_request_dict = shared_brand_configs_create_request_instance.to_dict()
# create an instance of SharedBrandConfigsCreateRequest from a dict
shared_brand_configs_create_request_from_dict = SharedBrandConfigsCreateRequest.from_dict(shared_brand_configs_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


