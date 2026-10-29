# RecordAlreadyExistsCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**late_policy** | [**RecordAlreadyExistsCreateRequestLatePolicy**](RecordAlreadyExistsCreateRequestLatePolicy.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.record_already_exists_create_request import RecordAlreadyExistsCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RecordAlreadyExistsCreateRequest from a JSON string
record_already_exists_create_request_instance = RecordAlreadyExistsCreateRequest.from_json(json)
# print the JSON string representation of the object
print(RecordAlreadyExistsCreateRequest.to_json())

# convert the object into a dict
record_already_exists_create_request_dict = record_already_exists_create_request_instance.to_dict()
# create an instance of RecordAlreadyExistsCreateRequest from a dict
record_already_exists_create_request_from_dict = RecordAlreadyExistsCreateRequest.from_dict(record_already_exists_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


