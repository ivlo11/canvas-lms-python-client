# TermsCreateRequestEnrollmentTerm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | [String] The name of the term. | [optional] 
**start_at** | **str** | [DateTime] The day/time the term starts. Accepts times in ISO 8601 format, e.g. 2015-01-10T18:48:00Z. | [optional] 
**end_at** | **str** | [DateTime] The day/time the term ends. Accepts times in ISO 8601 format, e.g. 2015-01-10T18:48:00Z. | [optional] 
**sis_term_id** | **str** | [String] The unique SIS identifier for the term. | [optional] 
**overrides** | **str** | [enrollment_type][end_at] [DateTime] The day/time the term ends, overridden for the given enrollment type. *enrollment_type* can be one of StudentEnrollment, TeacherEnrollment, TaEnrollment, or DesignerEnrollment | [optional] 

## Example

```python
from canvas_lms_python_client.models.terms_create_request_enrollment_term import TermsCreateRequestEnrollmentTerm

# TODO update the JSON string below
json = "{}"
# create an instance of TermsCreateRequestEnrollmentTerm from a JSON string
terms_create_request_enrollment_term_instance = TermsCreateRequestEnrollmentTerm.from_json(json)
# print the JSON string representation of the object
print(TermsCreateRequestEnrollmentTerm.to_json())

# convert the object into a dict
terms_create_request_enrollment_term_dict = terms_create_request_enrollment_term_instance.to_dict()
# create an instance of TermsCreateRequestEnrollmentTerm from a dict
terms_create_request_enrollment_term_from_dict = TermsCreateRequestEnrollmentTerm.from_dict(terms_create_request_enrollment_term_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


