# GradingStandard



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | the title of the grading standard | [optional] 
**id** | **int** | the id of the grading standard | [optional] 
**context_type** | **str** | the context this standard is associated with, either &#39;Account&#39; or &#39;Course&#39; | [optional] 
**context_id** | **int** | the id for the context either the Account or Course id | [optional] 
**points_based** | **bool** | whether this is a points-based standard | [optional] 
**scaling_factor** | **float** | the factor by which to scale a score. 1 for percentage based schemss and the max value of points for points based schemes. This number cannot be changed for percentage based schemes. | [optional] 
**grading_scheme** | [**List[GradingSchemeEntry]**](GradingSchemeEntry.md) | A list of GradingSchemeEntry that make up the Grading Standard as an array of values with the scheme name and value | [optional] 

## Example

```python
from canvas_lms_python_client.models.grading_standard import GradingStandard

# TODO update the JSON string below
json = "{}"
# create an instance of GradingStandard from a JSON string
grading_standard_instance = GradingStandard.from_json(json)
# print the JSON string representation of the object
print(GradingStandard.to_json())

# convert the object into a dict
grading_standard_dict = grading_standard_instance.to_dict()
# create an instance of GradingStandard from a dict
grading_standard_from_dict = GradingStandard.from_dict(grading_standard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


