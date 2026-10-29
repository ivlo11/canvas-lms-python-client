# PseudonymsCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**PseudonymsCreateRequestUser**](PseudonymsCreateRequestUser.md) |  | 
**login** | [**PseudonymsCreateRequestLogin**](PseudonymsCreateRequestLogin.md) |  | 

## Example

```python
from canvas_lms_python_client.models.pseudonyms_create_request import PseudonymsCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PseudonymsCreateRequest from a JSON string
pseudonyms_create_request_instance = PseudonymsCreateRequest.from_json(json)
# print the JSON string representation of the object
print(PseudonymsCreateRequest.to_json())

# convert the object into a dict
pseudonyms_create_request_dict = pseudonyms_create_request_instance.to_dict()
# create an instance of PseudonymsCreateRequest from a dict
pseudonyms_create_request_from_dict = PseudonymsCreateRequest.from_dict(pseudonyms_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


