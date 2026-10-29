# UpdatedEventData

The updated event data object returns all the fields that have changed in the format of the following example.  If a field does not exist it was not changed.  The value is an array that contains the before and after values for the change as in [:old_value, :new_value].

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **List[str]** |  | [optional] 
**start_at** | **List[datetime]** |  | [optional] 
**conclude_at** | **List[datetime]** |  | [optional] 
**is_public** | **List[bool]** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.updated_event_data import UpdatedEventData

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatedEventData from a JSON string
updated_event_data_instance = UpdatedEventData.from_json(json)
# print the JSON string representation of the object
print(UpdatedEventData.to_json())

# convert the object into a dict
updated_event_data_dict = updated_event_data_instance.to_dict()
# create an instance of UpdatedEventData from a dict
updated_event_data_from_dict = UpdatedEventData.from_dict(updated_event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


