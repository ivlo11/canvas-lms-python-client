# RubricsCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The id of the rubric | [optional] 
**rubric_association_id** | **int** | The id of the rubric association object (not the course/assignment itself, but the join table record id). It can be used in place of +rubric_association[association_id]+ and +rubric_association[association_type]+ if desired. | [optional] 
**rubric** | [**RubricsCreateRequestRubric**](RubricsCreateRequestRubric.md) |  | [optional] 
**rubric_association** | [**RubricsCreateRequestRubricAssociation**](RubricsCreateRequestRubricAssociation.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.rubrics_create_request import RubricsCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RubricsCreateRequest from a JSON string
rubrics_create_request_instance = RubricsCreateRequest.from_json(json)
# print the JSON string representation of the object
print(RubricsCreateRequest.to_json())

# convert the object into a dict
rubrics_create_request_dict = rubrics_create_request_instance.to_dict()
# create an instance of RubricsCreateRequest from a dict
rubrics_create_request_from_dict = RubricsCreateRequest.from_dict(rubrics_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


