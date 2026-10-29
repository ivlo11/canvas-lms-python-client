# ProvisionalGrade



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provisional_grade_id** | **int** | The identifier for the provisional grade | [optional] 
**score** | **int** | The numeric score | [optional] 
**grade** | **str** | The grade | [optional] 
**grade_matches_current_submission** | **bool** | Whether the grade was applied to the most current submission (false if the student resubmitted after grading) | [optional] 
**graded_at** | **datetime** | When the grade was given | [optional] 
**final** | **bool** | Whether this is the &#39;final&#39; provisional grade created by the moderator | [optional] 
**speedgrader_url** | **str** | A link to view this provisional grade in SpeedGrader | [optional] 

## Example

```python
from canvas_lms_python_client.models.provisional_grade import ProvisionalGrade

# TODO update the JSON string below
json = "{}"
# create an instance of ProvisionalGrade from a JSON string
provisional_grade_instance = ProvisionalGrade.from_json(json)
# print the JSON string representation of the object
print(ProvisionalGrade.to_json())

# convert the object into a dict
provisional_grade_dict = provisional_grade_instance.to_dict()
# create an instance of ProvisionalGrade from a dict
provisional_grade_from_dict = ProvisionalGrade.from_dict(provisional_grade_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


