# EnrollmentsApiBulkEnrollmentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_ids** | **List[int]** | The user IDs to enroll in the courses. | 
**course_ids** | **List[int]** | The course IDs to enroll each user in. | 
**enrollment_type** | **str** | Enroll each user as a student, teacher, TA, observer, or designer. If no value is given, the type will be &#39;StudentEnrollment&#39;. | [optional] 
**enrollment_role_id** | **int** | Optional custom course-level role id to apply to created enrollments. | [optional] 
**start_at** | **str** | The start time of every created enrollment, in ISO8601 format. e.g. 2012-04-18T23:08:51Z. When provided, applies to all enrollments in the bulk creation. | [optional] 
**end_at** | **str** | The end time of every created enrollment, in ISO8601 format. e.g. 2012-04-18T23:08:51Z. When provided, applies to all enrollments in the bulk creation. | [optional] 

## Example

```python
from canvas_lms_python_client.models.enrollments_api_bulk_enrollment_request import EnrollmentsApiBulkEnrollmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentsApiBulkEnrollmentRequest from a JSON string
enrollments_api_bulk_enrollment_request_instance = EnrollmentsApiBulkEnrollmentRequest.from_json(json)
# print the JSON string representation of the object
print(EnrollmentsApiBulkEnrollmentRequest.to_json())

# convert the object into a dict
enrollments_api_bulk_enrollment_request_dict = enrollments_api_bulk_enrollment_request_instance.to_dict()
# create an instance of EnrollmentsApiBulkEnrollmentRequest from a dict
enrollments_api_bulk_enrollment_request_from_dict = EnrollmentsApiBulkEnrollmentRequest.from_dict(enrollments_api_bulk_enrollment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


