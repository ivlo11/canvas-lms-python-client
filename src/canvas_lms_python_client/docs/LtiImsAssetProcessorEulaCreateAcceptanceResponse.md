# LtiImsAssetProcessorEulaCreateAcceptanceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accepted** | **bool** |  | [optional] 
**timestamp** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.lti_ims_asset_processor_eula_create_acceptance_response import LtiImsAssetProcessorEulaCreateAcceptanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LtiImsAssetProcessorEulaCreateAcceptanceResponse from a JSON string
lti_ims_asset_processor_eula_create_acceptance_response_instance = LtiImsAssetProcessorEulaCreateAcceptanceResponse.from_json(json)
# print the JSON string representation of the object
print(LtiImsAssetProcessorEulaCreateAcceptanceResponse.to_json())

# convert the object into a dict
lti_ims_asset_processor_eula_create_acceptance_response_dict = lti_ims_asset_processor_eula_create_acceptance_response_instance.to_dict()
# create an instance of LtiImsAssetProcessorEulaCreateAcceptanceResponse from a dict
lti_ims_asset_processor_eula_create_acceptance_response_from_dict = LtiImsAssetProcessorEulaCreateAcceptanceResponse.from_dict(lti_ims_asset_processor_eula_create_acceptance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


