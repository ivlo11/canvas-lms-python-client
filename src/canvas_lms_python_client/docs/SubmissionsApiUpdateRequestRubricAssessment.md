# SubmissionsApiUpdateRequestRubricAssessment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rubric_assessment** | **str** | Assign a rubric assessment to this assignment submission. The sub-parameters here depend on the rubric for the assignment. The general format is, for each row in the rubric:  The points awarded for this row.   rubric_assessment[criterion_id][points]  The rating id for the row.   rubric_assessment[criterion_id][rating_id]  Comments to add for this row.   rubric_assessment[criterion_id][comments]  For example, if the assignment rubric is (in JSON format):   !!!javascript   [     {       &#39;id&#39;: &#39;crit1&#39;,       &#39;points&#39;: 10,       &#39;description&#39;: &#39;Criterion 1&#39;,       &#39;ratings&#39;:       [         { &#39;id&#39;: &#39;rat1&#39;, &#39;description&#39;: &#39;Good&#39;, &#39;points&#39;: 10 },         { &#39;id&#39;: &#39;rat2&#39;, &#39;description&#39;: &#39;Poor&#39;, &#39;points&#39;: 3 }       ]     },     {       &#39;id&#39;: &#39;crit2&#39;,       &#39;points&#39;: 5,       &#39;description&#39;: &#39;Criterion 2&#39;,       &#39;ratings&#39;:       [         { &#39;id&#39;: &#39;rat1&#39;, &#39;description&#39;: &#39;Exemplary&#39;, &#39;points&#39;: 5 },         { &#39;id&#39;: &#39;rat2&#39;, &#39;description&#39;: &#39;Complete&#39;, &#39;points&#39;: 5 },         { &#39;id&#39;: &#39;rat3&#39;, &#39;description&#39;: &#39;Incomplete&#39;, &#39;points&#39;: 0 }       ]     }   ]  Then a possible set of values for rubric_assessment would be:     rubric_assessment[crit1][points]&#x3D;3&amp;rubric_assessment[crit1][rating_id]&#x3D;rat1&amp;rubric_assessment[crit2][points]&#x3D;5&amp;rubric_assessment[crit2][rating_id]&#x3D;rat2&amp;rubric_assessment[crit2][comments]&#x3D;Well%20Done. | [optional] 

## Example

```python
from canvas_lms_python_client.models.submissions_api_update_request_rubric_assessment import SubmissionsApiUpdateRequestRubricAssessment

# TODO update the JSON string below
json = "{}"
# create an instance of SubmissionsApiUpdateRequestRubricAssessment from a JSON string
submissions_api_update_request_rubric_assessment_instance = SubmissionsApiUpdateRequestRubricAssessment.from_json(json)
# print the JSON string representation of the object
print(SubmissionsApiUpdateRequestRubricAssessment.to_json())

# convert the object into a dict
submissions_api_update_request_rubric_assessment_dict = submissions_api_update_request_rubric_assessment_instance.to_dict()
# create an instance of SubmissionsApiUpdateRequestRubricAssessment from a dict
submissions_api_update_request_rubric_assessment_from_dict = SubmissionsApiUpdateRequestRubricAssessment.from_dict(submissions_api_update_request_rubric_assessment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


