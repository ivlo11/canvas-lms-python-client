# GradingStandardsApiCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The title for the Grading Standard. | 
**points_based** | **bool** | Whether or not a grading scheme is points based. Defaults to false. | [optional] 
**scaling_factor** | **int** | The factor by which to scale a percentage into a points based scheme grade. This is the maximum number of points possible in the grading scheme. Defaults to 1. Not required for percentage based grading schemes. | [optional] 
**grading_scheme_entry_name** | **str** | The name for an entry value within a GradingStandard that describes the range of the value e.g. A- | 
**grading_scheme_entry_value** | **int** | The value for the name of the entry within a GradingStandard. The entry represents the lower bound of the range for the entry. This range includes the value up to the next entry in the GradingStandard, or 100 if there is no upper bound. The lowest value will have a lower bound range of 0. e.g. 93 | 

## Example

```python
from canvas_lms_python_client.models.grading_standards_api_create_request import GradingStandardsApiCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GradingStandardsApiCreateRequest from a JSON string
grading_standards_api_create_request_instance = GradingStandardsApiCreateRequest.from_json(json)
# print the JSON string representation of the object
print(GradingStandardsApiCreateRequest.to_json())

# convert the object into a dict
grading_standards_api_create_request_dict = grading_standards_api_create_request_instance.to_dict()
# create an instance of GradingStandardsApiCreateRequest from a dict
grading_standards_api_create_request_from_dict = GradingStandardsApiCreateRequest.from_dict(grading_standards_api_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


