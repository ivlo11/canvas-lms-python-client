# ContentMigrationsAssetIdMappingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**announcements** | **object** |  | [optional] 
**assignments** | **object** |  | [optional] 
**discussion_topics** | **object** |  | [optional] 
**files** | **object** |  | [optional] 
**module_items** | **object** |  | [optional] 
**modules** | **object** |  | [optional] 
**pages** | **object** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.content_migrations_asset_id_mapping_response import ContentMigrationsAssetIdMappingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContentMigrationsAssetIdMappingResponse from a JSON string
content_migrations_asset_id_mapping_response_instance = ContentMigrationsAssetIdMappingResponse.from_json(json)
# print the JSON string representation of the object
print(ContentMigrationsAssetIdMappingResponse.to_json())

# convert the object into a dict
content_migrations_asset_id_mapping_response_dict = content_migrations_asset_id_mapping_response_instance.to_dict()
# create an instance of ContentMigrationsAssetIdMappingResponse from a dict
content_migrations_asset_id_mapping_response_from_dict = ContentMigrationsAssetIdMappingResponse.from_dict(content_migrations_asset_id_mapping_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


