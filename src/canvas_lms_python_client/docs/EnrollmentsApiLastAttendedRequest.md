# EnrollmentsApiLastAttendedRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** | The last attended date of a student enrollment in a course. | [optional] 

## Example

```python
from canvas_lms_python_client.models.enrollments_api_last_attended_request import EnrollmentsApiLastAttendedRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentsApiLastAttendedRequest from a JSON string
enrollments_api_last_attended_request_instance = EnrollmentsApiLastAttendedRequest.from_json(json)
# print the JSON string representation of the object
print(EnrollmentsApiLastAttendedRequest.to_json())

# convert the object into a dict
enrollments_api_last_attended_request_dict = enrollments_api_last_attended_request_instance.to_dict()
# create an instance of EnrollmentsApiLastAttendedRequest from a dict
enrollments_api_last_attended_request_from_dict = EnrollmentsApiLastAttendedRequest.from_dict(enrollments_api_last_attended_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


