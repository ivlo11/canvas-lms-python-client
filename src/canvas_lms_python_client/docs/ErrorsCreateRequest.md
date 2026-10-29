# ErrorsCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**ErrorsCreateRequestError**](ErrorsCreateRequestError.md) |  | 

## Example

```python
from canvas_lms_python_client.models.errors_create_request import ErrorsCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorsCreateRequest from a JSON string
errors_create_request_instance = ErrorsCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ErrorsCreateRequest.to_json())

# convert the object into a dict
errors_create_request_dict = errors_create_request_instance.to_dict()
# create an instance of ErrorsCreateRequest from a dict
errors_create_request_from_dict = ErrorsCreateRequest.from_dict(errors_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


