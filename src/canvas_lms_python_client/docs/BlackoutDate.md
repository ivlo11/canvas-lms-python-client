# BlackoutDate

Blackout dates are used to prevent scheduling assignments on a given date in course pacing.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | the ID of the blackout date | [optional] 
**context_id** | **int** | the context owning the blackout date | [optional] 
**context_type** | **str** |  | [optional] 
**start_date** | **datetime** | the start date of the blackout date | [optional] 
**end_date** | **datetime** | the end date of the blackout date | [optional] 
**event_title** | **str** | title of the blackout date | [optional] 
**created_at** | **str** |  | [optional] 
**root_account_id** | **int** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.blackout_date import BlackoutDate

# TODO update the JSON string below
json = "{}"
# create an instance of BlackoutDate from a JSON string
blackout_date_instance = BlackoutDate.from_json(json)
# print the JSON string representation of the object
print(BlackoutDate.to_json())

# convert the object into a dict
blackout_date_dict = blackout_date_instance.to_dict()
# create an instance of BlackoutDate from a dict
blackout_date_from_dict = BlackoutDate.from_dict(blackout_date_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


