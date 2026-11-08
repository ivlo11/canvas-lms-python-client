# RubricAssociation



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | the ID of the association | [optional] 
**rubric_id** | **int** | the ID of the rubric | [optional] 
**association_id** | **int** | the ID of the object this association links to | [optional] 
**association_type** | **str** | the type of object this association links to | [optional] 
**use_for_grading** | **bool** | Whether or not the associated rubric is used for grade calculation | [optional] 
**summary_data** | **str** |  | [optional] 
**purpose** | **str** | Whether or not the association is for grading (and thus linked to an assignment) or if it&#39;s to indicate the rubric should appear in its context. Values will be grading or bookmark. | [optional] 
**hide_score_total** | **bool** | Whether or not the score total is displayed within the rubric. This option is only available if the rubric is not used for grading. | [optional] 
**hide_points** | **bool** |  | [optional] 
**hide_outcome_results** | **bool** |  | [optional] 
**bookmarked** | **bool** |  | [optional] 
**context_code** | **str** |  | [optional] 
**context_id** | **int** |  | [optional] 
**context_type** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**root_account_id** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**workflow_state** | **str** |  | [optional] 
**assessment_requests** | **List[object]** |  | [optional] 
**association_count** | **int** |  | [optional] 
**permissions** | **object** |  | [optional] 
**rubric_assessments** | **List[object]** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.rubric_association import RubricAssociation

# TODO update the JSON string below
json = "{}"
# create an instance of RubricAssociation from a JSON string
rubric_association_instance = RubricAssociation.from_json(json)
# print the JSON string representation of the object
print(RubricAssociation.to_json())

# convert the object into a dict
rubric_association_dict = rubric_association_instance.to_dict()
# create an instance of RubricAssociation from a dict
rubric_association_from_dict = RubricAssociation.from_dict(rubric_association_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


