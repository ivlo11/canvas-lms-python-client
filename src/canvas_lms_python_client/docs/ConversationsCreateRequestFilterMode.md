# ConversationsCreateRequestFilterMode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**and_or** | **str** | Used when generating \&quot;visible\&quot; in the API response. See the explanation under the {api:ConversationsController#index index API action} | [optional] 

## Example

```python
from canvas_lms_python_client.models.conversations_create_request_filter_mode import ConversationsCreateRequestFilterMode

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationsCreateRequestFilterMode from a JSON string
conversations_create_request_filter_mode_instance = ConversationsCreateRequestFilterMode.from_json(json)
# print the JSON string representation of the object
print(ConversationsCreateRequestFilterMode.to_json())

# convert the object into a dict
conversations_create_request_filter_mode_dict = conversations_create_request_filter_mode_instance.to_dict()
# create an instance of ConversationsCreateRequestFilterMode from a dict
conversations_create_request_filter_mode_from_dict = ConversationsCreateRequestFilterMode.from_dict(conversations_create_request_filter_mode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


