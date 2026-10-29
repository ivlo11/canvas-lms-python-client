# BlackoutDatesBulkUpdateRequestBlackoutDates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blackout_date** | **str** | An object containing the array of BlackoutDates we want to exist after this operation. For array entries, if it has an id it will be updated, if not created, and if an existing BlackoutDate id is missing from the array, it will be deleted. | [optional] 

## Example

```python
from canvas_lms_python_client.models.blackout_dates_bulk_update_request_blackout_dates import BlackoutDatesBulkUpdateRequestBlackoutDates

# TODO update the JSON string below
json = "{}"
# create an instance of BlackoutDatesBulkUpdateRequestBlackoutDates from a JSON string
blackout_dates_bulk_update_request_blackout_dates_instance = BlackoutDatesBulkUpdateRequestBlackoutDates.from_json(json)
# print the JSON string representation of the object
print(BlackoutDatesBulkUpdateRequestBlackoutDates.to_json())

# convert the object into a dict
blackout_dates_bulk_update_request_blackout_dates_dict = blackout_dates_bulk_update_request_blackout_dates_instance.to_dict()
# create an instance of BlackoutDatesBulkUpdateRequestBlackoutDates from a dict
blackout_dates_bulk_update_request_blackout_dates_from_dict = BlackoutDatesBulkUpdateRequestBlackoutDates.from_dict(blackout_dates_bulk_update_request_blackout_dates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


