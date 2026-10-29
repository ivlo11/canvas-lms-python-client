# ContentSharesCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**receiver_ids** | **List[str]** | IDs of users to share the content with. | 
**content_type** | **str** | Type of content you are sharing. | 
**content_id** | **int** | The id of the content that you are sharing | 

## Example

```python
from canvas_lms_python_client.models.content_shares_create_request import ContentSharesCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ContentSharesCreateRequest from a JSON string
content_shares_create_request_instance = ContentSharesCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ContentSharesCreateRequest.to_json())

# convert the object into a dict
content_shares_create_request_dict = content_shares_create_request_instance.to_dict()
# create an instance of ContentSharesCreateRequest from a dict
content_shares_create_request_from_dict = ContentSharesCreateRequest.from_dict(content_shares_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


