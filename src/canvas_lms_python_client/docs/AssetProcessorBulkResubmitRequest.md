# AssetProcessorBulkResubmitRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignment_id** | **int** | The ID of the assignment we want to resubmit notices for | [optional] 
**course_id** | **int** | The ID of the course containing assignments we want to resubmit notices for | [optional] 
**tool_id** | **int** | The ID of the external tool to filter asset processors we want to resend notices | [optional] 

## Example

```python
from canvas_lms_python_client.models.asset_processor_bulk_resubmit_request import AssetProcessorBulkResubmitRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssetProcessorBulkResubmitRequest from a JSON string
asset_processor_bulk_resubmit_request_instance = AssetProcessorBulkResubmitRequest.from_json(json)
# print the JSON string representation of the object
print(AssetProcessorBulkResubmitRequest.to_json())

# convert the object into a dict
asset_processor_bulk_resubmit_request_dict = asset_processor_bulk_resubmit_request_instance.to_dict()
# create an instance of AssetProcessorBulkResubmitRequest from a dict
asset_processor_bulk_resubmit_request_from_dict = AssetProcessorBulkResubmitRequest.from_dict(asset_processor_bulk_resubmit_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


