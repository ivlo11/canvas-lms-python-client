# ContentSharesAddUsersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**receiver_ids** | **List[str]** | IDs of users to share the content with. | [optional] 

## Example

```python
from canvas_lms_python_client.models.content_shares_add_users_request import ContentSharesAddUsersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ContentSharesAddUsersRequest from a JSON string
content_shares_add_users_request_instance = ContentSharesAddUsersRequest.from_json(json)
# print the JSON string representation of the object
print(ContentSharesAddUsersRequest.to_json())

# convert the object into a dict
content_shares_add_users_request_dict = content_shares_add_users_request_instance.to_dict()
# create an instance of ContentSharesAddUsersRequest from a dict
content_shares_add_users_request_from_dict = ContentSharesAddUsersRequest.from_dict(content_shares_add_users_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


