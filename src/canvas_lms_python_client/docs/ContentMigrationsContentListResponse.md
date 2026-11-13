# ContentMigrationsContentListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**migration_id** | **str** |  | [optional] 
**var_property** | **str** |  | [optional] 
**sub_items_url** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.content_migrations_content_list_response import ContentMigrationsContentListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContentMigrationsContentListResponse from a JSON string
content_migrations_content_list_response_instance = ContentMigrationsContentListResponse.from_json(json)
# print the JSON string representation of the object
print(ContentMigrationsContentListResponse.to_json())

# convert the object into a dict
content_migrations_content_list_response_dict = content_migrations_content_list_response_instance.to_dict()
# create an instance of ContentMigrationsContentListResponse from a dict
content_migrations_content_list_response_from_dict = ContentMigrationsContentListResponse.from_dict(content_migrations_content_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


