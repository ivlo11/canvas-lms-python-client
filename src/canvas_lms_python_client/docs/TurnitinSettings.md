# TurnitinSettings



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**originality_report_visibility** | **str** |  | [optional] 
**s_paper_check** | **bool** |  | [optional] 
**internet_check** | **bool** |  | [optional] 
**journal_check** | **bool** |  | [optional] 
**exclude_biblio** | **bool** |  | [optional] 
**exclude_quoted** | **bool** |  | [optional] 
**exclude_small_matches_type** | **str** |  | [optional] 
**exclude_small_matches_value** | **int** |  | [optional] 
**submit_papers_to** | **bool** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.turnitin_settings import TurnitinSettings

# TODO update the JSON string below
json = "{}"
# create an instance of TurnitinSettings from a JSON string
turnitin_settings_instance = TurnitinSettings.from_json(json)
# print the JSON string representation of the object
print(TurnitinSettings.to_json())

# convert the object into a dict
turnitin_settings_dict = turnitin_settings_instance.to_dict()
# create an instance of TurnitinSettings from a dict
turnitin_settings_from_dict = TurnitinSettings.from_dict(turnitin_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


