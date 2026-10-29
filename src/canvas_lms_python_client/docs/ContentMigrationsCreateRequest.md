# ContentMigrationsCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**migration_type** | **str** | The type of the migration. Use the {api:ContentMigrationsController#available_migrators Migrator} endpoint to see all available migrators. Default allowed values: canvas_cartridge_importer, common_cartridge_importer, course_copy_importer, zip_file_importer, qti_converter, moodle_converter | 
**selective_import** | **bool** | If set, perform a selective import instead of importing all content. The migration will identify the contents of the package and then stop in the +waiting_for_select+ workflow state. At this point, use the {api:ContentMigrationsController#content_list List items endpoint} to enumerate the contents of the package, identifying the copy parameters for the desired content. Then call the {api:ContentMigrationsController#update Update endpoint} and provide these copy parameters to start the import. | [optional] 
**select** | **str** | For +course_copy_importer+ migrations, this parameter allows you to select the objects to copy without using the +selective_import+ argument and +waiting_for_select+ state as is required for uploaded imports (though that workflow is also supported for course copy migrations). The keys are object types like &#39;files&#39;, &#39;folders&#39;, &#39;pages&#39;, etc. The value for each key is a list of object ids. An id can be an integer or a string. Multiple object types can be selected in the same call. | [optional] 
**pre_attachment** | [**ContentMigrationsCreateRequestPreAttachment**](ContentMigrationsCreateRequestPreAttachment.md) |  | [optional] 
**settings** | [**ContentMigrationsCreateRequestSettings**](ContentMigrationsCreateRequestSettings.md) |  | [optional] 
**date_shift_options** | [**ContentMigrationsCreateRequestDateShiftOptions**](ContentMigrationsCreateRequestDateShiftOptions.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.content_migrations_create_request import ContentMigrationsCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ContentMigrationsCreateRequest from a JSON string
content_migrations_create_request_instance = ContentMigrationsCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ContentMigrationsCreateRequest.to_json())

# convert the object into a dict
content_migrations_create_request_dict = content_migrations_create_request_instance.to_dict()
# create an instance of ContentMigrationsCreateRequest from a dict
content_migrations_create_request_from_dict = ContentMigrationsCreateRequest.from_dict(content_migrations_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


