# RubricCriterion



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the ID of the criterion | [optional] 
**description** | **str** |  | [optional] 
**long_description** | **str** |  | [optional] 
**points** | **int** |  | [optional] 
**criterion_use_range** | **bool** |  | [optional] 
**ratings** | [**List[RubricRating]**](RubricRating.md) | the possible ratings for this Criterion | [optional] 

## Example

```python
from canvas_lms_python_client.models.rubric_criterion import RubricCriterion

# TODO update the JSON string below
json = "{}"
# create an instance of RubricCriterion from a JSON string
rubric_criterion_instance = RubricCriterion.from_json(json)
# print the JSON string representation of the object
print(RubricCriterion.to_json())

# convert the object into a dict
rubric_criterion_dict = rubric_criterion_instance.to_dict()
# create an instance of RubricCriterion from a dict
rubric_criterion_from_dict = RubricCriterion.from_dict(rubric_criterion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


