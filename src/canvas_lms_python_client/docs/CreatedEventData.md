# CreatedEventData

The created event data object returns all the fields that were set in the format of the following example.  If a field does not exist it was not set. The value of each field changed is in the format of [:old_value, :new_value].  The created event type also includes a created_source field to specify what triggered the creation of the course.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **List[str]** |  | [optional] 
**start_at** | **List[datetime]** |  | [optional] 
**conclude_at** | **List[datetime]** |  | [optional] 
**is_public** | **List[bool]** |  | [optional] 
**created_source** | **str** | The type of action that triggered the creation of the course. | [optional] 

## Example

```python
from canvas_lms_python_client.models.created_event_data import CreatedEventData

# TODO update the JSON string below
json = "{}"
# create an instance of CreatedEventData from a JSON string
created_event_data_instance = CreatedEventData.from_json(json)
# print the JSON string representation of the object
print(CreatedEventData.to_json())

# convert the object into a dict
created_event_data_dict = created_event_data_instance.to_dict()
# create an instance of CreatedEventData from a dict
created_event_data_from_dict = CreatedEventData.from_dict(created_event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


