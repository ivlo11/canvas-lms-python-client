# InstAccessToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | The InstAccess token itself -- a signed, encrypted JWT | [optional] 

## Example

```python
from canvas_lms_python_client.models.inst_access_token import InstAccessToken

# TODO update the JSON string below
json = "{}"
# create an instance of InstAccessToken from a JSON string
inst_access_token_instance = InstAccessToken.from_json(json)
# print the JSON string representation of the object
print(InstAccessToken.to_json())

# convert the object into a dict
inst_access_token_dict = inst_access_token_instance.to_dict()
# create an instance of InstAccessToken from a dict
inst_access_token_from_dict = InstAccessToken.from_dict(inst_access_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


