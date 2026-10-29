# AssignmentEvent



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A synthetic ID for the assignment | [optional] 
**title** | **str** | The title of the assignment | [optional] 
**start_at** | **datetime** | The due_at timestamp of the assignment | [optional] 
**end_at** | **datetime** | The due_at timestamp of the assignment | [optional] 
**description** | **str** | The HTML description of the assignment | [optional] 
**context_code** | **str** | the context code of the (course) calendar this assignment belongs to | [optional] 
**workflow_state** | **str** | Current state of the assignment (&#39;published&#39; or &#39;deleted&#39;) | [optional] 
**url** | **str** | URL for this assignment (note that updating/deleting should be done via the Assignments API) | [optional] 
**html_url** | **str** | URL for a user to view this assignment | [optional] 
**all_day_date** | **datetime** | The due date of this assignment | [optional] 
**all_day** | **bool** | Boolean indicating whether this is an all-day event (e.g. assignment due at midnight) | [optional] 
**created_at** | **datetime** | When the assignment was created | [optional] 
**updated_at** | **datetime** | When the assignment was last updated | [optional] 
**assignment** | [**Assignment**](Assignment.md) |  | [optional] 
**assignment_overrides** | [**AssignmentOverride**](AssignmentOverride.md) |  | [optional] 
**important_dates** | **bool** | Boolean indicating whether this has important dates. | [optional] 
**rrule** | **str** | An iCalendar RRULE for defining how events in a recurring event series repeat. | [optional] 
**series_head** | **bool** | Trueif this is the first event in the series of recurring events. | [optional] 
**series_natural_language** | **str** | A natural language expression of how events occur in the series. | [optional] 

## Example

```python
from canvas_lms_python_client.models.assignment_event import AssignmentEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AssignmentEvent from a JSON string
assignment_event_instance = AssignmentEvent.from_json(json)
# print the JSON string representation of the object
print(AssignmentEvent.to_json())

# convert the object into a dict
assignment_event_dict = assignment_event_instance.to_dict()
# create an instance of AssignmentEvent from a dict
assignment_event_from_dict = AssignmentEvent.from_dict(assignment_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


