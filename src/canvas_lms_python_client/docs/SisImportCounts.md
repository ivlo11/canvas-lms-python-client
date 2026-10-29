# SisImportCounts



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | **int** |  | [optional] 
**terms** | **int** |  | [optional] 
**abstract_courses** | **int** |  | [optional] 
**courses** | **int** |  | [optional] 
**sections** | **int** |  | [optional] 
**xlists** | **int** |  | [optional] 
**users** | **int** |  | [optional] 
**enrollments** | **int** |  | [optional] 
**groups** | **int** |  | [optional] 
**group_memberships** | **int** |  | [optional] 
**grade_publishing_results** | **int** |  | [optional] 
**batch_courses_deleted** | **int** | the number of courses that were removed because they were not included in the batch for batch_mode imports. Only included if courses were deleted | [optional] 
**batch_sections_deleted** | **int** | the number of sections that were removed because they were not included in the batch for batch_mode imports. Only included if sections were deleted | [optional] 
**batch_enrollments_deleted** | **int** | the number of enrollments that were removed because they were not included in the batch for batch_mode imports. Only included if enrollments were deleted | [optional] 
**error_count** | **int** |  | [optional] 
**warning_count** | **int** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.sis_import_counts import SisImportCounts

# TODO update the JSON string below
json = "{}"
# create an instance of SisImportCounts from a JSON string
sis_import_counts_instance = SisImportCounts.from_json(json)
# print the JSON string representation of the object
print(SisImportCounts.to_json())

# convert the object into a dict
sis_import_counts_dict = sis_import_counts_instance.to_dict()
# create an instance of SisImportCounts from a dict
sis_import_counts_from_dict = SisImportCounts.from_dict(sis_import_counts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


