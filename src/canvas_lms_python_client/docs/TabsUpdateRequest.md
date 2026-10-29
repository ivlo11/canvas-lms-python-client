# TabsUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **int** | The new position of the tab, 1-based | [optional] 
**hidden** | **bool** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.tabs_update_request import TabsUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TabsUpdateRequest from a JSON string
tabs_update_request_instance = TabsUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(TabsUpdateRequest.to_json())

# convert the object into a dict
tabs_update_request_dict = tabs_update_request_instance.to_dict()
# create an instance of TabsUpdateRequest from a dict
tabs_update_request_from_dict = TabsUpdateRequest.from_dict(tabs_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


