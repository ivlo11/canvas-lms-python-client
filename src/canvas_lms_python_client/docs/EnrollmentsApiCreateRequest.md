# EnrollmentsApiCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**root_account** | **str** | The domain of the account to search for the user. Will be a no-op unless the sis_user_id or integration_id parameter is also included. | [optional] 
**enrollment** | [**EnrollmentsApiCreateRequestEnrollment**](EnrollmentsApiCreateRequestEnrollment.md) |  | 

## Example

```python
from canvas_lms_python_client.models.enrollments_api_create_request import EnrollmentsApiCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentsApiCreateRequest from a JSON string
enrollments_api_create_request_instance = EnrollmentsApiCreateRequest.from_json(json)
# print the JSON string representation of the object
print(EnrollmentsApiCreateRequest.to_json())

# convert the object into a dict
enrollments_api_create_request_dict = enrollments_api_create_request_instance.to_dict()
# create an instance of EnrollmentsApiCreateRequest from a dict
enrollments_api_create_request_from_dict = EnrollmentsApiCreateRequest.from_dict(enrollments_api_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


