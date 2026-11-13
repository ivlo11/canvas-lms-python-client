# CoursesActivityStreamSummaryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**notification_category** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**unread_count** | **int** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.courses_activity_stream_summary_response import CoursesActivityStreamSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CoursesActivityStreamSummaryResponse from a JSON string
courses_activity_stream_summary_response_instance = CoursesActivityStreamSummaryResponse.from_json(json)
# print the JSON string representation of the object
print(CoursesActivityStreamSummaryResponse.to_json())

# convert the object into a dict
courses_activity_stream_summary_response_dict = courses_activity_stream_summary_response_instance.to_dict()
# create an instance of CoursesActivityStreamSummaryResponse from a dict
courses_activity_stream_summary_response_from_dict = CoursesActivityStreamSummaryResponse.from_dict(courses_activity_stream_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


