# RubricAssociationsCreateResponse

Object response with `rubric`, `rubric_association` (from the Canvas `@returns`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rubric** | [**Rubric**](Rubric.md) |  | [optional] 
**rubric_association** | [**RubricAssociation**](RubricAssociation.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.rubric_associations_create_response import RubricAssociationsCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RubricAssociationsCreateResponse from a JSON string
rubric_associations_create_response_instance = RubricAssociationsCreateResponse.from_json(json)
# print the JSON string representation of the object
print(RubricAssociationsCreateResponse.to_json())

# convert the object into a dict
rubric_associations_create_response_dict = rubric_associations_create_response_instance.to_dict()
# create an instance of RubricAssociationsCreateResponse from a dict
rubric_associations_create_response_from_dict = RubricAssociationsCreateResponse.from_dict(rubric_associations_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


