# ApiRegistration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **int** |  | [optional] 
**company_name** | **str** |  | [optional] 
**global_product_id** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**tool_id** | **int** |  | [optional] 
**tool_name** | **str** |  | [optional] 
**unified_tool_id** | **str** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.api_registration import ApiRegistration

# TODO update the JSON string below
json = "{}"
# create an instance of ApiRegistration from a JSON string
api_registration_instance = ApiRegistration.from_json(json)
# print the JSON string representation of the object
print(ApiRegistration.to_json())

# convert the object into a dict
api_registration_dict = api_registration_instance.to_dict()
# create an instance of ApiRegistration from a dict
api_registration_from_dict = ApiRegistration.from_dict(api_registration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


