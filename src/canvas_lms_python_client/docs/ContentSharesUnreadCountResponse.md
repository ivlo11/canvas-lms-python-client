# ContentSharesUnreadCountResponse

Object response with `unread_count` (from the Canvas `@returns`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unread_count** | **int** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.content_shares_unread_count_response import ContentSharesUnreadCountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContentSharesUnreadCountResponse from a JSON string
content_shares_unread_count_response_instance = ContentSharesUnreadCountResponse.from_json(json)
# print the JSON string representation of the object
print(ContentSharesUnreadCountResponse.to_json())

# convert the object into a dict
content_shares_unread_count_response_dict = content_shares_unread_count_response_instance.to_dict()
# create an instance of ContentSharesUnreadCountResponse from a dict
content_shares_unread_count_response_from_dict = ContentSharesUnreadCountResponse.from_dict(content_shares_unread_count_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


