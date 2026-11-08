# RubricAssessmentsUpdateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anonymous_assessor_id** | **str** |  | [optional] 
**artifact** | **object** |  | [optional] 
**artifact_attempt** | **object** |  | [optional] 
**artifact_id** | **int** |  | [optional] 
**artifact_type** | **str** |  | [optional] 
**assessment_type** | **str** |  | [optional] 
**assessor_id** | **int** |  | [optional] 
**assessor_name** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**data** | **List[object]** |  | [optional] 
**hide_points** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**ratings** | **List[object]** |  | [optional] 
**related_group_submissions_and_assessments** | **List[object]** |  | [optional] 
**root_account_id** | **int** |  | [optional] 
**rubric_assessment_imports_id** | **object** |  | [optional] 
**rubric_association** | **object** |  | [optional] 
**rubric_association_id** | **int** |  | [optional] 
**rubric_id** | **int** |  | [optional] 
**score** | **object** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**user_id** | **int** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.rubric_assessments_update_response import RubricAssessmentsUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RubricAssessmentsUpdateResponse from a JSON string
rubric_assessments_update_response_instance = RubricAssessmentsUpdateResponse.from_json(json)
# print the JSON string representation of the object
print(RubricAssessmentsUpdateResponse.to_json())

# convert the object into a dict
rubric_assessments_update_response_dict = rubric_assessments_update_response_instance.to_dict()
# create an instance of RubricAssessmentsUpdateResponse from a dict
rubric_assessments_update_response_from_dict = RubricAssessmentsUpdateResponse.from_dict(rubric_assessments_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


