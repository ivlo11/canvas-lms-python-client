# SisImportStatistic



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **int** | This is the number of items that were created. | [optional] 
**concluded** | **int** | This is the number of items that marked as completed. This only applies to courses and enrollments. | [optional] 
**deactivated** | **int** | This is the number of Enrollments that were marked as &#39;inactive&#39;. This only applies to enrollments. | [optional] 
**restored** | **int** | This is the number of items that were set to an active state from a completed, inactive, or deleted state. | [optional] 
**deleted** | **int** | This is the number of items that were deleted. | [optional] 

## Example

```python
from canvas_lms_python_client.models.sis_import_statistic import SisImportStatistic

# TODO update the JSON string below
json = "{}"
# create an instance of SisImportStatistic from a JSON string
sis_import_statistic_instance = SisImportStatistic.from_json(json)
# print the JSON string representation of the object
print(SisImportStatistic.to_json())

# convert the object into a dict
sis_import_statistic_dict = sis_import_statistic_instance.to_dict()
# create an instance of SisImportStatistic from a dict
sis_import_statistic_from_dict = SisImportStatistic.from_dict(sis_import_statistic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


