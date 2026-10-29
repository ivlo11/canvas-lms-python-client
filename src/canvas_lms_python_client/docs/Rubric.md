# Rubric



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | the ID of the rubric | [optional] 
**title** | **str** | title of the rubric | [optional] 
**context_id** | **int** | the context owning the rubric | [optional] 
**context_type** | **str** |  | [optional] 
**points_possible** | **int** |  | [optional] 
**reusable** | **bool** |  | [optional] 
**read_only** | **bool** |  | [optional] 
**free_form_criterion_comments** | **bool** | whether or not free-form comments are used | [optional] 
**hide_score_total** | **bool** |  | [optional] 
**data** | [**List[RubricCriterion]**](RubricCriterion.md) | An array with all of this Rubric&#39;s grading Criteria | [optional] 
**assessments** | [**List[RubricAssessment]**](RubricAssessment.md) | If an assessment type is included in the &#39;include&#39; parameter, includes an array of rubric assessment objects for a given rubric, based on the assessment type requested. If the user does not request an assessment type this key will be absent. | [optional] 
**associations** | [**List[RubricAssociation]**](RubricAssociation.md) | If an association type is included in the &#39;include&#39; parameter, includes an array of rubric association objects for a given rubric, based on the association type requested. If the user does not request an association type this key will be absent. | [optional] 

## Example

```python
from canvas_lms_python_client.models.rubric import Rubric

# TODO update the JSON string below
json = "{}"
# create an instance of Rubric from a JSON string
rubric_instance = Rubric.from_json(json)
# print the JSON string representation of the object
print(Rubric.to_json())

# convert the object into a dict
rubric_dict = rubric_instance.to_dict()
# create an instance of Rubric from a dict
rubric_from_dict = Rubric.from_dict(rubric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


