# OutcomeAlignment



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | the id of the aligned learning outcome. | [optional] 
**assignment_id** | **int** | the id of the aligned assignment (null for live assessments). | [optional] 
**assessment_id** | **int** | the id of the aligned live assessment (null for assignments). | [optional] 
**submission_types** | **str** | a string representing the different submission types of an aligned assignment. | [optional] 
**url** | **str** | the URL for the aligned assignment. | [optional] 
**title** | **str** | the title of the aligned assignment. | [optional] 

## Example

```python
from canvas_lms_python_client.models.outcome_alignment import OutcomeAlignment

# TODO update the JSON string below
json = "{}"
# create an instance of OutcomeAlignment from a JSON string
outcome_alignment_instance = OutcomeAlignment.from_json(json)
# print the JSON string representation of the object
print(OutcomeAlignment.to_json())

# convert the object into a dict
outcome_alignment_dict = outcome_alignment_instance.to_dict()
# create an instance of OutcomeAlignment from a dict
outcome_alignment_from_dict = OutcomeAlignment.from_dict(outcome_alignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


