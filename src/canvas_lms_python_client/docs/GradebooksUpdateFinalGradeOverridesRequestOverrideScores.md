# GradebooksUpdateFinalGradeOverridesRequestOverrideScores


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**student_id** | **int** | [Integer] The ID of the student to update. | [optional] 
**override_score** | **float** | [Float] The new score to assign as a percentage. | [optional] 

## Example

```python
from canvas_lms_python_client.models.gradebooks_update_final_grade_overrides_request_override_scores import GradebooksUpdateFinalGradeOverridesRequestOverrideScores

# TODO update the JSON string below
json = "{}"
# create an instance of GradebooksUpdateFinalGradeOverridesRequestOverrideScores from a JSON string
gradebooks_update_final_grade_overrides_request_override_scores_instance = GradebooksUpdateFinalGradeOverridesRequestOverrideScores.from_json(json)
# print the JSON string representation of the object
print(GradebooksUpdateFinalGradeOverridesRequestOverrideScores.to_json())

# convert the object into a dict
gradebooks_update_final_grade_overrides_request_override_scores_dict = gradebooks_update_final_grade_overrides_request_override_scores_instance.to_dict()
# create an instance of GradebooksUpdateFinalGradeOverridesRequestOverrideScores from a dict
gradebooks_update_final_grade_overrides_request_override_scores_from_dict = GradebooksUpdateFinalGradeOverridesRequestOverrideScores.from_dict(gradebooks_update_final_grade_overrides_request_override_scores_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


