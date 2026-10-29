# RubricsCreateRequestRubricAssociation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**association_id** | **int** | [Integer] The id of the object with which this rubric is associated | [optional] 
**association_type** | **str** | [\&quot;Assignment\&quot;|\&quot;Course\&quot;|\&quot;Account\&quot;] The type of object this rubric is associated with | [optional] 
**use_for_grading** | **bool** | [Boolean] Whether or not the associated rubric is used for grade calculation | [optional] 
**hide_score_total** | **bool** | [Boolean] Whether or not the score total is displayed within the rubric. This option is only available if the rubric is not used for grading. | [optional] 
**purpose** | **str** | [String] Whether or not the association is for grading (and thus linked to an assignment) or if it&#39;s to indicate the rubric should appear in its context | [optional] 

## Example

```python
from canvas_lms_python_client.models.rubrics_create_request_rubric_association import RubricsCreateRequestRubricAssociation

# TODO update the JSON string below
json = "{}"
# create an instance of RubricsCreateRequestRubricAssociation from a JSON string
rubrics_create_request_rubric_association_instance = RubricsCreateRequestRubricAssociation.from_json(json)
# print the JSON string representation of the object
print(RubricsCreateRequestRubricAssociation.to_json())

# convert the object into a dict
rubrics_create_request_rubric_association_dict = rubrics_create_request_rubric_association_instance.to_dict()
# create an instance of RubricsCreateRequestRubricAssociation from a dict
rubrics_create_request_rubric_association_from_dict = RubricsCreateRequestRubricAssociation.from_dict(rubrics_create_request_rubric_association_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


