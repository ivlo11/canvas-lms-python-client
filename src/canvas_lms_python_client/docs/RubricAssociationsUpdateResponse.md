# RubricAssociationsUpdateResponse

Object response with `rubric`, `rubric_association` (from the Canvas `@returns`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rubric** | [**Rubric**](Rubric.md) |  | [optional] 
**rubric_association** | [**RubricAssociation**](RubricAssociation.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.rubric_associations_update_response import RubricAssociationsUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RubricAssociationsUpdateResponse from a JSON string
rubric_associations_update_response_instance = RubricAssociationsUpdateResponse.from_json(json)
# print the JSON string representation of the object
print(RubricAssociationsUpdateResponse.to_json())

# convert the object into a dict
rubric_associations_update_response_dict = rubric_associations_update_response_instance.to_dict()
# create an instance of RubricAssociationsUpdateResponse from a dict
rubric_associations_update_response_from_dict = RubricAssociationsUpdateResponse.from_dict(rubric_associations_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


