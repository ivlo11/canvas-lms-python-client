# NoticeHandler

A notice handler for a particular tool deployment and notice type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**handler** | **str** | URL to receive the notice | [optional] 
**notice_type** | **str** | The type of notice | [optional] 
**max_batch_size** | **int** | The maximum number of notices to include in a single batch, or &#39;null&#39; if not set. | [optional] 

## Example

```python
from canvas_lms_python_client.models.notice_handler import NoticeHandler

# TODO update the JSON string below
json = "{}"
# create an instance of NoticeHandler from a JSON string
notice_handler_instance = NoticeHandler.from_json(json)
# print the JSON string representation of the object
print(NoticeHandler.to_json())

# convert the object into a dict
notice_handler_dict = notice_handler_instance.to_dict()
# create an instance of NoticeHandler from a dict
notice_handler_from_dict = NoticeHandler.from_dict(notice_handler_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


