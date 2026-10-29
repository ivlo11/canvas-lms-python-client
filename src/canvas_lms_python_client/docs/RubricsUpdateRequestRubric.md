# RubricsUpdateRequestRubric


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | [String] The title of the rubric | [optional] 
**free_form_criterion_comments** | **bool** | [Boolean] Whether or not you can write custom comments in the ratings field for a rubric | [optional] 
**skip_updating_points_possible** | **bool** | [Boolean] Whether or not to update the points possible | [optional] 
**criteria** | **str** | [Hash] An indexed Hash of RubricCriteria objects where the keys are integer ids and the values are the RubricCriteria objects | [optional] 

## Example

```python
from canvas_lms_python_client.models.rubrics_update_request_rubric import RubricsUpdateRequestRubric

# TODO update the JSON string below
json = "{}"
# create an instance of RubricsUpdateRequestRubric from a JSON string
rubrics_update_request_rubric_instance = RubricsUpdateRequestRubric.from_json(json)
# print the JSON string representation of the object
print(RubricsUpdateRequestRubric.to_json())

# convert the object into a dict
rubrics_update_request_rubric_dict = rubrics_update_request_rubric_instance.to_dict()
# create an instance of RubricsUpdateRequestRubric from a dict
rubrics_update_request_rubric_from_dict = RubricsUpdateRequestRubric.from_dict(rubrics_update_request_rubric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


