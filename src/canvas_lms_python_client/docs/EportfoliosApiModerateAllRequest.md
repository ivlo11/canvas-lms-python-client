# EportfoliosApiModerateAllRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spam_status** | **str** | The spam status for all the ePortfolios | [optional] 

## Example

```python
from canvas_lms_python_client.models.eportfolios_api_moderate_all_request import EportfoliosApiModerateAllRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EportfoliosApiModerateAllRequest from a JSON string
eportfolios_api_moderate_all_request_instance = EportfoliosApiModerateAllRequest.from_json(json)
# print the JSON string representation of the object
print(EportfoliosApiModerateAllRequest.to_json())

# convert the object into a dict
eportfolios_api_moderate_all_request_dict = eportfolios_api_moderate_all_request_instance.to_dict()
# create an instance of EportfoliosApiModerateAllRequest from a dict
eportfolios_api_moderate_all_request_from_dict = EportfoliosApiModerateAllRequest.from_dict(eportfolios_api_moderate_all_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


