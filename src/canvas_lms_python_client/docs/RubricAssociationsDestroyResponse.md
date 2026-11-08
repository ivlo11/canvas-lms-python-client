# RubricAssociationsDestroyResponse

Object response with `rubric_association` (from the Canvas `@returns`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rubric_association** | [**RubricAssociation**](RubricAssociation.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.rubric_associations_destroy_response import RubricAssociationsDestroyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RubricAssociationsDestroyResponse from a JSON string
rubric_associations_destroy_response_instance = RubricAssociationsDestroyResponse.from_json(json)
# print the JSON string representation of the object
print(RubricAssociationsDestroyResponse.to_json())

# convert the object into a dict
rubric_associations_destroy_response_dict = rubric_associations_destroy_response_instance.to_dict()
# create an instance of RubricAssociationsDestroyResponse from a dict
rubric_associations_destroy_response_from_dict = RubricAssociationsDestroyResponse.from_dict(rubric_associations_destroy_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


