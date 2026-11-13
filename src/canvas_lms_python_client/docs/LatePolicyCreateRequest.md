# LatePolicyCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**late_policy** | [**LatePolicyCreateRequestLatePolicy**](LatePolicyCreateRequestLatePolicy.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.late_policy_create_request import LatePolicyCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LatePolicyCreateRequest from a JSON string
late_policy_create_request_instance = LatePolicyCreateRequest.from_json(json)
# print the JSON string representation of the object
print(LatePolicyCreateRequest.to_json())

# convert the object into a dict
late_policy_create_request_dict = late_policy_create_request_instance.to_dict()
# create an instance of LatePolicyCreateRequest from a dict
late_policy_create_request_from_dict = LatePolicyCreateRequest.from_dict(late_policy_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


