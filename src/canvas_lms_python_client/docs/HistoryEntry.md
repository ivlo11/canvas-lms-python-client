# HistoryEntry

Information about a recently visited item or page in Canvas

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_code** | **str** | The asset string for the item viewed | 
**asset_name** | **str** | The name of the item | 
**asset_icon** | **str** | The icon type shown for the item. One of &#39;icon-announcement&#39;, &#39;icon-assignment&#39;, &#39;icon-calendar-month&#39;, &#39;icon-discussion&#39;, &#39;icon-document&#39;, &#39;icon-download&#39;, &#39;icon-gradebook&#39;, &#39;icon-home&#39;, &#39;icon-message&#39;, &#39;icon-module&#39;, &#39;icon-outcomes&#39;, &#39;icon-quiz&#39;, &#39;icon-user&#39;, &#39;icon-syllabus&#39; | [optional] 
**asset_readable_category** | **str** | The associated category describing the asset_icon | [optional] 
**context_type** | **str** | The type of context of the item visited. One of &#39;Course&#39;, &#39;Group&#39;, &#39;User&#39;, or &#39;Account&#39; | [optional] 
**context_id** | **int** | The id of the context, if applicable | [optional] 
**context_name** | **str** | The name of the context | [optional] 
**visited_url** | **str** | The URL of the item | 
**visited_at** | **datetime** | When the page was visited | 
**interaction_seconds** | **int** | The estimated time spent on the page in seconds | [optional] 

## Example

```python
from canvas_lms_python_client.models.history_entry import HistoryEntry

# TODO update the JSON string below
json = "{}"
# create an instance of HistoryEntry from a JSON string
history_entry_instance = HistoryEntry.from_json(json)
# print the JSON string representation of the object
print(HistoryEntry.to_json())

# convert the object into a dict
history_entry_dict = history_entry_instance.to_dict()
# create an instance of HistoryEntry from a dict
history_entry_from_dict = HistoryEntry.from_dict(history_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


