# RubricCriteria



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**points** | **int** |  | [optional] 
**id** | [**RubricCriteriaId**](RubricCriteriaId.md) |  | [optional] 
**learning_outcome_id** | **str** | (Optional) The id of the learning outcome this criteria uses, if any. | [optional] 
**vendor_guid** | **str** | (Optional) The 3rd party vendor&#39;s GUID for the outcome this criteria references, if any. | [optional] 
**description** | **str** |  | [optional] 
**long_description** | **str** |  | [optional] 
**criterion_use_range** | **bool** |  | [optional] 
**ratings** | [**List[RubricRating]**](RubricRating.md) |  | [optional] 
**ignore_for_scoring** | **bool** |  | [optional] 
**outcome_id** | **int** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.rubric_criteria import RubricCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of RubricCriteria from a JSON string
rubric_criteria_instance = RubricCriteria.from_json(json)
# print the JSON string representation of the object
print(RubricCriteria.to_json())

# convert the object into a dict
rubric_criteria_dict = rubric_criteria_instance.to_dict()
# create an instance of RubricCriteria from a dict
rubric_criteria_from_dict = RubricCriteria.from_dict(rubric_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


