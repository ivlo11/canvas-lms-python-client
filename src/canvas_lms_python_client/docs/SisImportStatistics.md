# SisImportStatistics



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_state_changes** | **int** | This is the total number of items that were changed in the sis import. There are a few caveats that can cause this number to not add up to the individual counts. There are some state changes that happen that have no impact to the object. An example would be changing a course from &#39;created&#39; to &#39;claimed&#39;. Both of these would be considered an active course, but would increment this counter. In this example the course would not increment the created or restored counters for course statistic. | [optional] 
**account** | [**SisImportStatistic**](SisImportStatistic.md) |  | [optional] 
**enrollment_term** | [**SisImportStatistic**](SisImportStatistic.md) |  | [optional] 
**communication_channel** | [**SisImportStatistic**](SisImportStatistic.md) |  | [optional] 
**abstract_course** | [**SisImportStatistic**](SisImportStatistic.md) |  | [optional] 
**course** | [**SisImportStatistic**](SisImportStatistic.md) |  | [optional] 
**course_section** | [**SisImportStatistic**](SisImportStatistic.md) |  | [optional] 
**enrollment** | [**SisImportStatistic**](SisImportStatistic.md) |  | [optional] 
**group_category** | [**SisImportStatistic**](SisImportStatistic.md) |  | [optional] 
**group** | [**SisImportStatistic**](SisImportStatistic.md) |  | [optional] 
**group_membership** | [**SisImportStatistic**](SisImportStatistic.md) |  | [optional] 
**pseudonym** | [**SisImportStatistic**](SisImportStatistic.md) |  | [optional] 
**user_observer** | [**SisImportStatistic**](SisImportStatistic.md) |  | [optional] 
**account_user** | [**SisImportStatistic**](SisImportStatistic.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.sis_import_statistics import SisImportStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of SisImportStatistics from a JSON string
sis_import_statistics_instance = SisImportStatistics.from_json(json)
# print the JSON string representation of the object
print(SisImportStatistics.to_json())

# convert the object into a dict
sis_import_statistics_dict = sis_import_statistics_instance.to_dict()
# create an instance of SisImportStatistics from a dict
sis_import_statistics_from_dict = SisImportStatistics.from_dict(sis_import_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


