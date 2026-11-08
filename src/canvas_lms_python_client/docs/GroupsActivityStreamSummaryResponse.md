# GroupsActivityStreamSummaryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**notification_category** | **object** |  | [optional] 
**type** | **str** |  | [optional] 
**unread_count** | **int** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.groups_activity_stream_summary_response import GroupsActivityStreamSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GroupsActivityStreamSummaryResponse from a JSON string
groups_activity_stream_summary_response_instance = GroupsActivityStreamSummaryResponse.from_json(json)
# print the JSON string representation of the object
print(GroupsActivityStreamSummaryResponse.to_json())

# convert the object into a dict
groups_activity_stream_summary_response_dict = groups_activity_stream_summary_response_instance.to_dict()
# create an instance of GroupsActivityStreamSummaryResponse from a dict
groups_activity_stream_summary_response_from_dict = GroupsActivityStreamSummaryResponse.from_dict(groups_activity_stream_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


