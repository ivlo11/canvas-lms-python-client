# BlackoutDatesBulkUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blackout_dates_** | [**BlackoutDatesBulkUpdateRequestBlackoutDates**](BlackoutDatesBulkUpdateRequestBlackoutDates.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.blackout_dates_bulk_update_request import BlackoutDatesBulkUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BlackoutDatesBulkUpdateRequest from a JSON string
blackout_dates_bulk_update_request_instance = BlackoutDatesBulkUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(BlackoutDatesBulkUpdateRequest.to_json())

# convert the object into a dict
blackout_dates_bulk_update_request_dict = blackout_dates_bulk_update_request_instance.to_dict()
# create an instance of BlackoutDatesBulkUpdateRequest from a dict
blackout_dates_bulk_update_request_from_dict = BlackoutDatesBulkUpdateRequest.from_dict(blackout_dates_bulk_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


