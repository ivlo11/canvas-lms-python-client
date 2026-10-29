# EportfoliosApiModerateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spam_status** | **str** | The spam status for the ePortfolio | [optional] 

## Example

```python
from canvas_lms_python_client.models.eportfolios_api_moderate_request import EportfoliosApiModerateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EportfoliosApiModerateRequest from a JSON string
eportfolios_api_moderate_request_instance = EportfoliosApiModerateRequest.from_json(json)
# print the JSON string representation of the object
print(EportfoliosApiModerateRequest.to_json())

# convert the object into a dict
eportfolios_api_moderate_request_dict = eportfolios_api_moderate_request_instance.to_dict()
# create an instance of EportfoliosApiModerateRequest from a dict
eportfolios_api_moderate_request_from_dict = EportfoliosApiModerateRequest.from_dict(eportfolios_api_moderate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


