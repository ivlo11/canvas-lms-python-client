# BlackoutDatesCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **str** | The start date of the blackout date. | [optional] 
**end_date** | **str** | The end date of the blackout date. | [optional] 
**event_title** | **str** | The title of the blackout date. | [optional] 

## Example

```python
from canvas_lms_python_client.models.blackout_dates_create_request import BlackoutDatesCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BlackoutDatesCreateRequest from a JSON string
blackout_dates_create_request_instance = BlackoutDatesCreateRequest.from_json(json)
# print the JSON string representation of the object
print(BlackoutDatesCreateRequest.to_json())

# convert the object into a dict
blackout_dates_create_request_dict = blackout_dates_create_request_instance.to_dict()
# create an instance of BlackoutDatesCreateRequest from a dict
blackout_dates_create_request_from_dict = BlackoutDatesCreateRequest.from_dict(blackout_dates_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


