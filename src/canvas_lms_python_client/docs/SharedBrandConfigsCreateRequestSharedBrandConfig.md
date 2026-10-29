# SharedBrandConfigsCreateRequestSharedBrandConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | [Required, String] Name to share this BrandConfig (theme) as. | 
**brand_config_md5** | **str** | [Required, String] MD5 of brand_config to share | 

## Example

```python
from canvas_lms_python_client.models.shared_brand_configs_create_request_shared_brand_config import SharedBrandConfigsCreateRequestSharedBrandConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SharedBrandConfigsCreateRequestSharedBrandConfig from a JSON string
shared_brand_configs_create_request_shared_brand_config_instance = SharedBrandConfigsCreateRequestSharedBrandConfig.from_json(json)
# print the JSON string representation of the object
print(SharedBrandConfigsCreateRequestSharedBrandConfig.to_json())

# convert the object into a dict
shared_brand_configs_create_request_shared_brand_config_dict = shared_brand_configs_create_request_shared_brand_config_instance.to_dict()
# create an instance of SharedBrandConfigsCreateRequestSharedBrandConfig from a dict
shared_brand_configs_create_request_shared_brand_config_from_dict = SharedBrandConfigsCreateRequestSharedBrandConfig.from_dict(shared_brand_configs_create_request_shared_brand_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


