# LtiImsAssetProcessorCreateReportResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **str** |  | [optional] 
**priority** | **int** |  | [optional] 
**processing_progress** | **str** |  | [optional] 
**result** | **str** |  | [optional] 
**timestamp** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**visible_to_owner** | **bool** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.lti_ims_asset_processor_create_report_response import LtiImsAssetProcessorCreateReportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LtiImsAssetProcessorCreateReportResponse from a JSON string
lti_ims_asset_processor_create_report_response_instance = LtiImsAssetProcessorCreateReportResponse.from_json(json)
# print the JSON string representation of the object
print(LtiImsAssetProcessorCreateReportResponse.to_json())

# convert the object into a dict
lti_ims_asset_processor_create_report_response_dict = lti_ims_asset_processor_create_report_response_instance.to_dict()
# create an instance of LtiImsAssetProcessorCreateReportResponse from a dict
lti_ims_asset_processor_create_report_response_from_dict = LtiImsAssetProcessorCreateReportResponse.from_dict(lti_ims_asset_processor_create_report_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


