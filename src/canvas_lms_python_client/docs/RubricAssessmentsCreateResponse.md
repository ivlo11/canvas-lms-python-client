# RubricAssessmentsCreateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifact** | **object** |  | [optional] 
**artifact_attempt** | **int** |  | [optional] 
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
from canvas_lms_python_client.models.rubric_assessments_create_response import RubricAssessmentsCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RubricAssessmentsCreateResponse from a JSON string
rubric_assessments_create_response_instance = RubricAssessmentsCreateResponse.from_json(json)
# print the JSON string representation of the object
print(RubricAssessmentsCreateResponse.to_json())

# convert the object into a dict
rubric_assessments_create_response_dict = rubric_assessments_create_response_instance.to_dict()
# create an instance of RubricAssessmentsCreateResponse from a dict
rubric_assessments_create_response_from_dict = RubricAssessmentsCreateResponse.from_dict(rubric_assessments_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


