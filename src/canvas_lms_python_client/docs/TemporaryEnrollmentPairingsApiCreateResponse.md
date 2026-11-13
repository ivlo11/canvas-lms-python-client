# TemporaryEnrollmentPairingsApiCreateResponse

Object response with `temporary_enrollment_pairing` (from the Canvas `@returns`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**temporary_enrollment_pairing** | [**TemporaryEnrollmentPairing**](TemporaryEnrollmentPairing.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.temporary_enrollment_pairings_api_create_response import TemporaryEnrollmentPairingsApiCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TemporaryEnrollmentPairingsApiCreateResponse from a JSON string
temporary_enrollment_pairings_api_create_response_instance = TemporaryEnrollmentPairingsApiCreateResponse.from_json(json)
# print the JSON string representation of the object
print(TemporaryEnrollmentPairingsApiCreateResponse.to_json())

# convert the object into a dict
temporary_enrollment_pairings_api_create_response_dict = temporary_enrollment_pairings_api_create_response_instance.to_dict()
# create an instance of TemporaryEnrollmentPairingsApiCreateResponse from a dict
temporary_enrollment_pairings_api_create_response_from_dict = TemporaryEnrollmentPairingsApiCreateResponse.from_dict(temporary_enrollment_pairings_api_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


