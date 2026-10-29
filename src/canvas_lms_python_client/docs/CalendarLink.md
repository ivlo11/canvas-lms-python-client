# CalendarLink



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ics** | **str** | The URL of the calendar in ICS format | [optional] 

## Example

```python
from canvas_lms_python_client.models.calendar_link import CalendarLink

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarLink from a JSON string
calendar_link_instance = CalendarLink.from_json(json)
# print the JSON string representation of the object
print(CalendarLink.to_json())

# convert the object into a dict
calendar_link_dict = calendar_link_instance.to_dict()
# create an instance of CalendarLink from a dict
calendar_link_from_dict = CalendarLink.from_dict(calendar_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


