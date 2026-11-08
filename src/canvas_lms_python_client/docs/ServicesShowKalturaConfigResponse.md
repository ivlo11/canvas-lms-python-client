# ServicesShowKalturaConfigResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**partner_id** | **str** |  | [optional] 
**resource_domain** | **str** |  | [optional] 
**rtmp_domain** | **str** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.services_show_kaltura_config_response import ServicesShowKalturaConfigResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ServicesShowKalturaConfigResponse from a JSON string
services_show_kaltura_config_response_instance = ServicesShowKalturaConfigResponse.from_json(json)
# print the JSON string representation of the object
print(ServicesShowKalturaConfigResponse.to_json())

# convert the object into a dict
services_show_kaltura_config_response_dict = services_show_kaltura_config_response_instance.to_dict()
# create an instance of ServicesShowKalturaConfigResponse from a dict
services_show_kaltura_config_response_from_dict = ServicesShowKalturaConfigResponse.from_dict(services_show_kaltura_config_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


