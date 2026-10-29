# AssetProcessorBulkResubmitDiscussionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discussion_topic_id** | **int** | The ID of the discussion topic we want to resubmit notices for | [optional] 
**course_id** | **int** | The ID of the course containing discussion topics we want to resubmit notices for | [optional] 
**tool_id** | **int** | The ID of the external tool to filter asset processors we want to resend notices | [optional] 

## Example

```python
from canvas_lms_python_client.models.asset_processor_bulk_resubmit_discussion_request import AssetProcessorBulkResubmitDiscussionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssetProcessorBulkResubmitDiscussionRequest from a JSON string
asset_processor_bulk_resubmit_discussion_request_instance = AssetProcessorBulkResubmitDiscussionRequest.from_json(json)
# print the JSON string representation of the object
print(AssetProcessorBulkResubmitDiscussionRequest.to_json())

# convert the object into a dict
asset_processor_bulk_resubmit_discussion_request_dict = asset_processor_bulk_resubmit_discussion_request_instance.to_dict()
# create an instance of AssetProcessorBulkResubmitDiscussionRequest from a dict
asset_processor_bulk_resubmit_discussion_request_from_dict = AssetProcessorBulkResubmitDiscussionRequest.from_dict(asset_processor_bulk_resubmit_discussion_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


