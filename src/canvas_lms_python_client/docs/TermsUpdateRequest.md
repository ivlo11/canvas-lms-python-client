# TermsUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**override_sis_stickiness** | **bool** | Default is true. If false, any fields containing “sticky” changes will not be updated. See SIS CSV Format documentation for information on which fields can have SIS stickiness | [optional] 
**enrollment_term** | [**TermsCreateRequestEnrollmentTerm**](TermsCreateRequestEnrollmentTerm.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.terms_update_request import TermsUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TermsUpdateRequest from a JSON string
terms_update_request_instance = TermsUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(TermsUpdateRequest.to_json())

# convert the object into a dict
terms_update_request_dict = terms_update_request_instance.to_dict()
# create an instance of TermsUpdateRequest from a dict
terms_update_request_from_dict = TermsUpdateRequest.from_dict(terms_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


