# ContentSharesUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**read_state** | **str** | Read state for the content share | [optional] 

## Example

```python
from canvas_lms_python_client.models.content_shares_update_request import ContentSharesUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ContentSharesUpdateRequest from a JSON string
content_shares_update_request_instance = ContentSharesUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(ContentSharesUpdateRequest.to_json())

# convert the object into a dict
content_shares_update_request_dict = content_shares_update_request_instance.to_dict()
# create an instance of ContentSharesUpdateRequest from a dict
content_shares_update_request_from_dict = ContentSharesUpdateRequest.from_dict(content_shares_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


