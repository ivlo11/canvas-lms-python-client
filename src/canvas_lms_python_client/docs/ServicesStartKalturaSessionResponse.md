# ServicesStartKalturaSessionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kaltura_setting** | **object** |  | [optional] 
**ks** | **str** |  | [optional] 
**partner_id** | **str** |  | [optional] 
**server_time** | **int** |  | [optional] 
**subp_id** | **str** |  | [optional] 
**uid** | **str** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.services_start_kaltura_session_response import ServicesStartKalturaSessionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ServicesStartKalturaSessionResponse from a JSON string
services_start_kaltura_session_response_instance = ServicesStartKalturaSessionResponse.from_json(json)
# print the JSON string representation of the object
print(ServicesStartKalturaSessionResponse.to_json())

# convert the object into a dict
services_start_kaltura_session_response_dict = services_start_kaltura_session_response_instance.to_dict()
# create an instance of ServicesStartKalturaSessionResponse from a dict
services_start_kaltura_session_response_from_dict = ServicesStartKalturaSessionResponse.from_dict(services_start_kaltura_session_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


