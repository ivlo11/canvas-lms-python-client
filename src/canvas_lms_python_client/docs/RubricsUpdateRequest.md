# RubricsUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rubric_association_id** | **int** | The id of the rubric association object (not the course/assignment itself, but the join table record id). It can be used in place of +rubric_association[association_id]+ and +rubric_association[association_type]+ if desired. | [optional] 
**rubric** | [**RubricsUpdateRequestRubric**](RubricsUpdateRequestRubric.md) |  | [optional] 
**rubric_association** | [**RubricsUpdateRequestRubricAssociation**](RubricsUpdateRequestRubricAssociation.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.rubrics_update_request import RubricsUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RubricsUpdateRequest from a JSON string
rubrics_update_request_instance = RubricsUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(RubricsUpdateRequest.to_json())

# convert the object into a dict
rubrics_update_request_dict = rubrics_update_request_instance.to_dict()
# create an instance of RubricsUpdateRequest from a dict
rubrics_update_request_from_dict = RubricsUpdateRequest.from_dict(rubrics_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


