# LtiSubmissionEulaAgreementTimestamp

UTC timestamp showing when the user agreed to the EULA (if given by the tool provider)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from canvas_lms_python_client.models.lti_submission_eula_agreement_timestamp import LtiSubmissionEulaAgreementTimestamp

# TODO update the JSON string below
json = "{}"
# create an instance of LtiSubmissionEulaAgreementTimestamp from a JSON string
lti_submission_eula_agreement_timestamp_instance = LtiSubmissionEulaAgreementTimestamp.from_json(json)
# print the JSON string representation of the object
print(LtiSubmissionEulaAgreementTimestamp.to_json())

# convert the object into a dict
lti_submission_eula_agreement_timestamp_dict = lti_submission_eula_agreement_timestamp_instance.to_dict()
# create an instance of LtiSubmissionEulaAgreementTimestamp from a dict
lti_submission_eula_agreement_timestamp_from_dict = LtiSubmissionEulaAgreementTimestamp.from_dict(lti_submission_eula_agreement_timestamp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


