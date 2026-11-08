# UsersActivityStreamSummaryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**notification_category** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**unread_count** | **int** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.users_activity_stream_summary_response import UsersActivityStreamSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UsersActivityStreamSummaryResponse from a JSON string
users_activity_stream_summary_response_instance = UsersActivityStreamSummaryResponse.from_json(json)
# print the JSON string representation of the object
print(UsersActivityStreamSummaryResponse.to_json())

# convert the object into a dict
users_activity_stream_summary_response_dict = users_activity_stream_summary_response_instance.to_dict()
# create an instance of UsersActivityStreamSummaryResponse from a dict
users_activity_stream_summary_response_from_dict = UsersActivityStreamSummaryResponse.from_dict(users_activity_stream_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


