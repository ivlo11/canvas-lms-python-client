# SharedBrandConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The shared_brand_config identifier. | [optional] 
**account_id** | **str** | The id of the account it should be shared within. | [optional] 
**brand_config_md5** | **str** | The md5 (since BrandConfigs are identified by MD5 and not numeric id) of the BrandConfig to share. | [optional] 
**name** | **str** | The name to share this theme as | [optional] 
**created_at** | **datetime** | When this was created | [optional] 
**updated_at** | **datetime** | When this was last updated | [optional] 

## Example

```python
from canvas_lms_python_client.models.shared_brand_config import SharedBrandConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SharedBrandConfig from a JSON string
shared_brand_config_instance = SharedBrandConfig.from_json(json)
# print the JSON string representation of the object
print(SharedBrandConfig.to_json())

# convert the object into a dict
shared_brand_config_dict = shared_brand_config_instance.to_dict()
# create an instance of SharedBrandConfig from a dict
shared_brand_config_from_dict = SharedBrandConfig.from_dict(shared_brand_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


