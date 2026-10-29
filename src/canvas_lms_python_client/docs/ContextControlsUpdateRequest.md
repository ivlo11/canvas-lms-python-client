# ContextControlsUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **bool** | the new value for this control&#39;s availability | 
**comment** | **str** | A comment to add the to the change-log entry explaining why the changes were made. | [optional] 

## Example

```python
from canvas_lms_python_client.models.context_controls_update_request import ContextControlsUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ContextControlsUpdateRequest from a JSON string
context_controls_update_request_instance = ContextControlsUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(ContextControlsUpdateRequest.to_json())

# convert the object into a dict
context_controls_update_request_dict = context_controls_update_request_instance.to_dict()
# create an instance of ContextControlsUpdateRequest from a dict
context_controls_update_request_from_dict = ContextControlsUpdateRequest.from_dict(context_controls_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


