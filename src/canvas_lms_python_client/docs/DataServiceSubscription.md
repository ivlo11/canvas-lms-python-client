# DataServiceSubscription

A subscription to a data service live event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context_id** | **str** | The id of the context for the subscription. | [optional] 
**context_type** | **str** | The type of context for the subscription. Must be &#39;assignment&#39;, or &#39;root_account&#39; | [optional] 
**event_types** | **List[str]** | Array of strings representing the event types for the subscription. | [optional] 
**format** | **str** | Format to deliver the live events. Must be &#39;live-event&#39; or &#39;caliper&#39;. | [optional] 
**transport_metadata** | [**DataServiceSubscriptionTransportMetadata**](DataServiceSubscriptionTransportMetadata.md) |  | [optional] 
**transport_type** | **str** | The type of transport for the event. Must be either &#39;sqs&#39; or &#39;https&#39;. | [optional] 
**id** | **str** |  | [optional] 
**owner_id** | **str** |  | [optional] 
**owner_type** | **str** |  | [optional] 
**updated_by** | **str** |  | [optional] 
**updated_by_type** | **str** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.data_service_subscription import DataServiceSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of DataServiceSubscription from a JSON string
data_service_subscription_instance = DataServiceSubscription.from_json(json)
# print the JSON string representation of the object
print(DataServiceSubscription.to_json())

# convert the object into a dict
data_service_subscription_dict = data_service_subscription_instance.to_dict()
# create an instance of DataServiceSubscription from a dict
data_service_subscription_from_dict = DataServiceSubscription.from_dict(data_service_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


