# EnrollmentsShowTemporaryEnrollmentStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_provide** | **bool** |  | [optional] 
**is_provider** | **bool** |  | [optional] 
**is_recipient** | **bool** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.enrollments_show_temporary_enrollment_status_response import EnrollmentsShowTemporaryEnrollmentStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentsShowTemporaryEnrollmentStatusResponse from a JSON string
enrollments_show_temporary_enrollment_status_response_instance = EnrollmentsShowTemporaryEnrollmentStatusResponse.from_json(json)
# print the JSON string representation of the object
print(EnrollmentsShowTemporaryEnrollmentStatusResponse.to_json())

# convert the object into a dict
enrollments_show_temporary_enrollment_status_response_dict = enrollments_show_temporary_enrollment_status_response_instance.to_dict()
# create an instance of EnrollmentsShowTemporaryEnrollmentStatusResponse from a dict
enrollments_show_temporary_enrollment_status_response_from_dict = EnrollmentsShowTemporaryEnrollmentStatusResponse.from_dict(enrollments_show_temporary_enrollment_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


