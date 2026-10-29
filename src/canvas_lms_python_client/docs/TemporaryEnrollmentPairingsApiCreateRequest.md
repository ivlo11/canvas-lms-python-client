# TemporaryEnrollmentPairingsApiCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_state** | **str** | The workflow state of the temporary enrollment pairing. | [optional] 
**ending_enrollment_state** | **str** | The ending enrollment state to be given to each associated enrollment when the enrollment period has been reached. Defaults to \&quot;deleted\&quot; if no value is given. Accepted values are \&quot;deleted\&quot;, \&quot;completed\&quot;, and \&quot;inactive\&quot;. | [optional] 

## Example

```python
from canvas_lms_python_client.models.temporary_enrollment_pairings_api_create_request import TemporaryEnrollmentPairingsApiCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TemporaryEnrollmentPairingsApiCreateRequest from a JSON string
temporary_enrollment_pairings_api_create_request_instance = TemporaryEnrollmentPairingsApiCreateRequest.from_json(json)
# print the JSON string representation of the object
print(TemporaryEnrollmentPairingsApiCreateRequest.to_json())

# convert the object into a dict
temporary_enrollment_pairings_api_create_request_dict = temporary_enrollment_pairings_api_create_request_instance.to_dict()
# create an instance of TemporaryEnrollmentPairingsApiCreateRequest from a dict
temporary_enrollment_pairings_api_create_request_from_dict = TemporaryEnrollmentPairingsApiCreateRequest.from_dict(temporary_enrollment_pairings_api_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


