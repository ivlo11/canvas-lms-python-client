# LatePolicyCreateResponse

Object response with `late_policy` (from the Canvas `@returns`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**late_policy** | [**LatePolicy**](LatePolicy.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.late_policy_create_response import LatePolicyCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LatePolicyCreateResponse from a JSON string
late_policy_create_response_instance = LatePolicyCreateResponse.from_json(json)
# print the JSON string representation of the object
print(LatePolicyCreateResponse.to_json())

# convert the object into a dict
late_policy_create_response_dict = late_policy_create_response_instance.to_dict()
# create an instance of LatePolicyCreateResponse from a dict
late_policy_create_response_from_dict = LatePolicyCreateResponse.from_dict(late_policy_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


