# RubricAssociationsCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rubric_association** | [**RubricAssociationsCreateRequestRubricAssociation**](RubricAssociationsCreateRequestRubricAssociation.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.rubric_associations_create_request import RubricAssociationsCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RubricAssociationsCreateRequest from a JSON string
rubric_associations_create_request_instance = RubricAssociationsCreateRequest.from_json(json)
# print the JSON string representation of the object
print(RubricAssociationsCreateRequest.to_json())

# convert the object into a dict
rubric_associations_create_request_dict = rubric_associations_create_request_instance.to_dict()
# create an instance of RubricAssociationsCreateRequest from a dict
rubric_associations_create_request_from_dict = RubricAssociationsCreateRequest.from_dict(rubric_associations_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


