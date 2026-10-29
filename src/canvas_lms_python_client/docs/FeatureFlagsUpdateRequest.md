# FeatureFlagsUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | \&quot;off\&quot;:: The feature is not available for the course, user, or account and sub-accounts. \&quot;allowed\&quot;:: (valid only on accounts) The feature is off in the account, but may be enabled in             sub-accounts and courses by setting a feature flag on the sub-account or course. \&quot;on\&quot;:: The feature is turned on unconditionally for the user, course, or account and sub-accounts. | [optional] 

## Example

```python
from canvas_lms_python_client.models.feature_flags_update_request import FeatureFlagsUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureFlagsUpdateRequest from a JSON string
feature_flags_update_request_instance = FeatureFlagsUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(FeatureFlagsUpdateRequest.to_json())

# convert the object into a dict
feature_flags_update_request_dict = feature_flags_update_request_instance.to_dict()
# create an instance of FeatureFlagsUpdateRequest from a dict
feature_flags_update_request_from_dict = FeatureFlagsUpdateRequest.from_dict(feature_flags_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


