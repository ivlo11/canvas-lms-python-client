# RubricAssessmentsDestroyResponse

Object response with `rubric_assessment` (from the Canvas `@returns`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rubric_assessment** | [**RubricAssessment**](RubricAssessment.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.rubric_assessments_destroy_response import RubricAssessmentsDestroyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RubricAssessmentsDestroyResponse from a JSON string
rubric_assessments_destroy_response_instance = RubricAssessmentsDestroyResponse.from_json(json)
# print the JSON string representation of the object
print(RubricAssessmentsDestroyResponse.to_json())

# convert the object into a dict
rubric_assessments_destroy_response_dict = rubric_assessments_destroy_response_instance.to_dict()
# create an instance of RubricAssessmentsDestroyResponse from a dict
rubric_assessments_destroy_response_from_dict = RubricAssessmentsDestroyResponse.from_dict(rubric_assessments_destroy_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


