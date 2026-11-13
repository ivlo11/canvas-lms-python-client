# SupportHelpersAssetProcessorSubmissionDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_processors** | **List[object]** |  | [optional] 
**asset_reports** | **List[object]** |  | [optional] 
**assets** | **List[object]** |  | [optional] 
**assignment** | **object** |  | [optional] 
**context_external_tools** | **List[object]** |  | [optional] 
**notice_handlers** | **List[object]** |  | [optional] 
**submission** | **object** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.support_helpers_asset_processor_submission_details_response import SupportHelpersAssetProcessorSubmissionDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SupportHelpersAssetProcessorSubmissionDetailsResponse from a JSON string
support_helpers_asset_processor_submission_details_response_instance = SupportHelpersAssetProcessorSubmissionDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(SupportHelpersAssetProcessorSubmissionDetailsResponse.to_json())

# convert the object into a dict
support_helpers_asset_processor_submission_details_response_dict = support_helpers_asset_processor_submission_details_response_instance.to_dict()
# create an instance of SupportHelpersAssetProcessorSubmissionDetailsResponse from a dict
support_helpers_asset_processor_submission_details_response_from_dict = SupportHelpersAssetProcessorSubmissionDetailsResponse.from_dict(support_helpers_asset_processor_submission_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


