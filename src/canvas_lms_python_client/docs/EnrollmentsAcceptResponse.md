# EnrollmentsAcceptResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.enrollments_accept_response import EnrollmentsAcceptResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentsAcceptResponse from a JSON string
enrollments_accept_response_instance = EnrollmentsAcceptResponse.from_json(json)
# print the JSON string representation of the object
print(EnrollmentsAcceptResponse.to_json())

# convert the object into a dict
enrollments_accept_response_dict = enrollments_accept_response_instance.to_dict()
# create an instance of EnrollmentsAcceptResponse from a dict
enrollments_accept_response_from_dict = EnrollmentsAcceptResponse.from_dict(enrollments_accept_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


