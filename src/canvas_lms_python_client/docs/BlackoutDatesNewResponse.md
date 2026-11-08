# BlackoutDatesNewResponse

Object response with `blackout_date` (from the Canvas `@returns`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blackout_date** | [**BlackoutDate**](BlackoutDate.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.blackout_dates_new_response import BlackoutDatesNewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BlackoutDatesNewResponse from a JSON string
blackout_dates_new_response_instance = BlackoutDatesNewResponse.from_json(json)
# print the JSON string representation of the object
print(BlackoutDatesNewResponse.to_json())

# convert the object into a dict
blackout_dates_new_response_dict = blackout_dates_new_response_instance.to_dict()
# create an instance of BlackoutDatesNewResponse from a dict
blackout_dates_new_response_from_dict = BlackoutDatesNewResponse.from_dict(blackout_dates_new_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


