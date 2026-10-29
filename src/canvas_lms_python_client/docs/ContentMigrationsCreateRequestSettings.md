# ContentMigrationsCreateRequestSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_url** | **str** | [string] A URL to download the file from. Must not require authentication. | [optional] 
**content_export_id** | **str** | [String] The id of a ContentExport to import. This allows you to import content previously exported from Canvas without needing to download and re-upload it. | [optional] 
**source_course_id** | **str** | [String] The course to copy from for a course copy migration. (required if doing course copy) | [optional] 
**folder_id** | **str** | [String] The folder to unzip the .zip file into for a zip_file_import. | [optional] 
**overwrite_quizzes** | **bool** | [Boolean] Whether to overwrite quizzes with the same identifiers between content packages. | [optional] 
**question_bank_id** | **int** | [Integer] The existing question bank ID to import questions into if not specified in the content package. | [optional] 
**question_bank_name** | **str** | [String] The question bank to import questions into if not specified in the content package, if both bank id and name are set, id will take precedence. | [optional] 
**insert_into_module_id** | **int** | [Integer] The id of a module in the target course. This will add all imported items (that can be added to a module) to the given module. | [optional] 
**insert_into_module_type** | **str** | [String,\&quot;assignment\&quot;|\&quot;discussion_topic\&quot;|\&quot;file\&quot;|\&quot;page\&quot;|\&quot;quiz\&quot;] If provided (and +insert_into_module_id+ is supplied), only add objects of the specified type to the module. | [optional] 
**insert_into_module_position** | **int** | [Integer] The (1-based) position to insert the imported items into the course (if +insert_into_module_id+ is supplied). If this parameter is omitted, items will be added to the end of the module. | [optional] 
**move_to_assignment_group_id** | **int** | [Integer] The id of an assignment group in the target course. If provided, all imported assignments will be moved to the given assignment group. | [optional] 
**importer_skips** | **str** | [Optional,Array,\&quot;all_course_settings\&quot;|\&quot;visibility_settings\&quot;] Set of importers to skip, even if otherwise selected by migration settings. | [optional] 
**import_blueprint_settings** | **bool** | [Boolean] Import the \&quot;use as blueprint course\&quot; setting as well as the list of locked items from the source course or package. The destination course must not be associated with an existing blueprint course and cannot have any student or observer enrollments. | [optional] 

## Example

```python
from canvas_lms_python_client.models.content_migrations_create_request_settings import ContentMigrationsCreateRequestSettings

# TODO update the JSON string below
json = "{}"
# create an instance of ContentMigrationsCreateRequestSettings from a JSON string
content_migrations_create_request_settings_instance = ContentMigrationsCreateRequestSettings.from_json(json)
# print the JSON string representation of the object
print(ContentMigrationsCreateRequestSettings.to_json())

# convert the object into a dict
content_migrations_create_request_settings_dict = content_migrations_create_request_settings_instance.to_dict()
# create an instance of ContentMigrationsCreateRequestSettings from a dict
content_migrations_create_request_settings_from_dict = ContentMigrationsCreateRequestSettings.from_dict(content_migrations_create_request_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


