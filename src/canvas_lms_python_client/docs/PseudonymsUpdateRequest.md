# PseudonymsUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**override_sis_stickiness** | **bool** | Default is true. If false, any fields containing “sticky” changes will not be updated. See SIS CSV Format documentation for information on which fields can have SIS stickiness | [optional] 
**login** | [**PseudonymsUpdateRequestLogin**](PseudonymsUpdateRequestLogin.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.pseudonyms_update_request import PseudonymsUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PseudonymsUpdateRequest from a JSON string
pseudonyms_update_request_instance = PseudonymsUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(PseudonymsUpdateRequest.to_json())

# convert the object into a dict
pseudonyms_update_request_dict = pseudonyms_update_request_instance.to_dict()
# create an instance of PseudonymsUpdateRequest from a dict
pseudonyms_update_request_from_dict = PseudonymsUpdateRequest.from_dict(pseudonyms_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


