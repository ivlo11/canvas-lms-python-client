# TermsCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enrollment_term** | [**TermsCreateRequestEnrollmentTerm**](TermsCreateRequestEnrollmentTerm.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.terms_create_request import TermsCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TermsCreateRequest from a JSON string
terms_create_request_instance = TermsCreateRequest.from_json(json)
# print the JSON string representation of the object
print(TermsCreateRequest.to_json())

# convert the object into a dict
terms_create_request_dict = terms_create_request_instance.to_dict()
# create an instance of TermsCreateRequest from a dict
terms_create_request_from_dict = TermsCreateRequest.from_dict(terms_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


