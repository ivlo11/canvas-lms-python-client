# RubricAssessmentsCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provisional** | **str** | (optional) Indicates whether this assessment is provisional, defaults to false. | [optional] 
**final** | **str** | (optional) Indicates a provisional grade will be marked as final. It only takes effect if the provisional param is passed as true. Defaults to false. | [optional] 
**graded_anonymously** | **bool** | (optional) Defaults to false | [optional] 
**rubric_assessment** | **str** | A Hash of data to complement the rubric assessment: The user id that refers to the person being assessed   rubric_assessment[user_id] Assessment type. There are only three valid types:  &#39;grading&#39;, &#39;peer_review&#39;, or &#39;provisional_grade&#39;   rubric_assessment[assessment_type] The points awarded for this row.   rubric_assessment[criterion_id][points] Comments to add for this row.   rubric_assessment[criterion_id][comments] For each criterion_id, change the id by the criterion number, ex: criterion_123 If the criterion_id is not specified it defaults to false, and nothing is updated. | [optional] 

## Example

```python
from canvas_lms_python_client.models.rubric_assessments_create_request import RubricAssessmentsCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RubricAssessmentsCreateRequest from a JSON string
rubric_assessments_create_request_instance = RubricAssessmentsCreateRequest.from_json(json)
# print the JSON string representation of the object
print(RubricAssessmentsCreateRequest.to_json())

# convert the object into a dict
rubric_assessments_create_request_dict = rubric_assessments_create_request_instance.to_dict()
# create an instance of RubricAssessmentsCreateRequest from a dict
rubric_assessments_create_request_from_dict = RubricAssessmentsCreateRequest.from_dict(rubric_assessments_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


