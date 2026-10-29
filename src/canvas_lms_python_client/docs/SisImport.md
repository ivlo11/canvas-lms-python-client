# SisImport



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for the SIS import. | [optional] 
**created_at** | **datetime** | The date the SIS import was created. | [optional] 
**ended_at** | **datetime** | The date the SIS import finished. Returns null if not finished. | [optional] 
**updated_at** | **datetime** | The date the SIS import was last updated. | [optional] 
**workflow_state** | **str** | The current state of the SIS import.  - &#39;initializing&#39;: The SIS import is being created, if this gets stuck in initializing, it will not import and will continue on to next import.  - &#39;created&#39;: The SIS import has been created.  - &#39;importing&#39;: The SIS import is currently processing.  - &#39;cleanup_batch&#39;: The SIS import is currently cleaning up courses, sections, and enrollments not included in the batch for batch_mode imports.  - &#39;imported&#39;: The SIS import has completed successfully.  - &#39;imported_with_messages&#39;: The SIS import completed with errors or warnings.  - &#39;aborted&#39;: The SIS import was aborted.  - &#39;failed_with_messages&#39;: The SIS import failed with errors.  - &#39;failed&#39;: The SIS import failed.  - &#39;restoring&#39;: The SIS import is restoring states of imported items.  - &#39;partially_restored&#39;: The SIS import is restored some of the states of imported items. This is generally due to passing a param like undelete only.  - &#39;restored&#39;: The SIS import is restored all of the states of imported items. | [optional] 
**data** | [**SisImportData**](SisImportData.md) |  | [optional] 
**statistics** | [**SisImportStatistics**](SisImportStatistics.md) |  | [optional] 
**progress** | **str** | The progress of the SIS import. The progress will reset when using batch_mode and have a different progress for the cleanup stage | [optional] 
**errors_attachment** | [**File**](File.md) |  | [optional] 
**user** | [**User**](User.md) |  | [optional] 
**processing_warnings** | **List[List[str]]** | Only imports that are complete will get this data. An array of CSV_file/warning_message pairs. | [optional] 
**processing_errors** | **List[List[str]]** | An array of CSV_file/error_message pairs. | [optional] 
**batch_mode** | **bool** | Whether the import was run in batch mode. | [optional] 
**batch_mode_term_id** | **str** | The term the batch was limited to. | [optional] 
**multi_term_batch_mode** | **bool** | Enables batch mode against all terms in term file. Requires change_threshold to be set. | [optional] 
**skip_deletes** | **bool** | When set the import will skip any deletes. | [optional] 
**override_sis_stickiness** | **bool** | Whether UI changes were overridden. | [optional] 
**add_sis_stickiness** | **bool** | Whether stickiness was added to the batch changes. | [optional] 
**clear_sis_stickiness** | **bool** | Whether stickiness was cleared. | [optional] 
**diffing_threshold_exceeded** | **bool** | Whether a diffing job failed because the threshold limit got exceeded. | [optional] 
**diffing_data_set_identifier** | **str** | The identifier of the data set that this SIS batch diffs against | [optional] 
**diffing_remaster** | **bool** | Whether diffing remaster data was enabled. | [optional] 
**diffed_against_import_id** | **int** | The ID of the SIS Import that this import was diffed against | [optional] 
**csv_attachments** | **List[List[File]]** | An array of CSV files for processing | [optional] 

## Example

```python
from canvas_lms_python_client.models.sis_import import SisImport

# TODO update the JSON string below
json = "{}"
# create an instance of SisImport from a JSON string
sis_import_instance = SisImport.from_json(json)
# print the JSON string representation of the object
print(SisImport.to_json())

# convert the object into a dict
sis_import_dict = sis_import_instance.to_dict()
# create an instance of SisImport from a dict
sis_import_from_dict = SisImport.from_dict(sis_import_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


