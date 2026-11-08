# RubricAssessment



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | the ID of the rubric | [optional] 
**rubric_id** | **int** | the rubric the assessment belongs to | [optional] 
**rubric_association_id** | **int** |  | [optional] 
**score** | **int** |  | [optional] 
**artifact_type** | **str** | the object of the assessment | [optional] 
**artifact_id** | **int** | the id of the object of the assessment | [optional] 
**artifact_attempt** | **int** | the current number of attempts made on the object of the assessment | [optional] 
**assessment_type** | **str** | the type of assessment. values will be either &#39;grading&#39;, &#39;peer_review&#39;, or &#39;provisional_grade&#39; | [optional] 
**assessor_id** | **int** | user id of the person who made the assessment | [optional] 
**data** | **List[object]** | (Optional) If &#39;full&#39; is included in the &#39;style&#39; parameter, returned assessments will have their full details contained in their data hash. If the user does not request a style, this key will be absent. | [optional] 
**comments** | **List[str]** | (Optional) If &#39;comments_only&#39; is included in the &#39;style&#39; parameter, returned assessments will include only the comments portion of their data hash. If the user does not request a style, this key will be absent. | [optional] 
**created_at** | **str** |  | [optional] 
**hide_points** | **bool** |  | [optional] 
**root_account_id** | **int** |  | [optional] 
**rubric_assessment_imports_id** | **int** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**user_id** | **int** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.rubric_assessment import RubricAssessment

# TODO update the JSON string below
json = "{}"
# create an instance of RubricAssessment from a JSON string
rubric_assessment_instance = RubricAssessment.from_json(json)
# print the JSON string representation of the object
print(RubricAssessment.to_json())

# convert the object into a dict
rubric_assessment_dict = rubric_assessment_instance.to_dict()
# create an instance of RubricAssessment from a dict
rubric_assessment_from_dict = RubricAssessment.from_dict(rubric_assessment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


