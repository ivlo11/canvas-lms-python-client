# GradebooksUpdateFinalGradeOverridesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grading_period_id** | **int** | The grading period to apply the override scores to. If omitted, override scores will be applied to the total grades for the course. | [optional] 
**override_scores** | [**GradebooksUpdateFinalGradeOverridesRequestOverrideScores**](GradebooksUpdateFinalGradeOverridesRequestOverrideScores.md) |  | 

## Example

```python
from canvas_lms_python_client.models.gradebooks_update_final_grade_overrides_request import GradebooksUpdateFinalGradeOverridesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GradebooksUpdateFinalGradeOverridesRequest from a JSON string
gradebooks_update_final_grade_overrides_request_instance = GradebooksUpdateFinalGradeOverridesRequest.from_json(json)
# print the JSON string representation of the object
print(GradebooksUpdateFinalGradeOverridesRequest.to_json())

# convert the object into a dict
gradebooks_update_final_grade_overrides_request_dict = gradebooks_update_final_grade_overrides_request_instance.to_dict()
# create an instance of GradebooksUpdateFinalGradeOverridesRequest from a dict
gradebooks_update_final_grade_overrides_request_from_dict = GradebooksUpdateFinalGradeOverridesRequest.from_dict(gradebooks_update_final_grade_overrides_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


