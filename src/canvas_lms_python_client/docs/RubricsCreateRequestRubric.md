# RubricsCreateRequestRubric


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | [String] The title of the rubric | [optional] 
**free_form_criterion_comments** | **bool** | [Boolean] Whether or not you can write custom comments in the ratings field for a rubric | [optional] 
**criteria** | **str** | [Hash] An indexed Hash of RubricCriteria objects where the keys are integer ids and the values are the RubricCriteria objects | [optional] 

## Example

```python
from canvas_lms_python_client.models.rubrics_create_request_rubric import RubricsCreateRequestRubric

# TODO update the JSON string below
json = "{}"
# create an instance of RubricsCreateRequestRubric from a JSON string
rubrics_create_request_rubric_instance = RubricsCreateRequestRubric.from_json(json)
# print the JSON string representation of the object
print(RubricsCreateRequestRubric.to_json())

# convert the object into a dict
rubrics_create_request_rubric_dict = rubrics_create_request_rubric_instance.to_dict()
# create an instance of RubricsCreateRequestRubric from a dict
rubrics_create_request_rubric_from_dict = RubricsCreateRequestRubric.from_dict(rubrics_create_request_rubric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


