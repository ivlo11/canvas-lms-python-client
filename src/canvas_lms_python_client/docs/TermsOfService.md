# TermsOfService



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Terms Of Service id | [optional] 
**terms_type** | **str** | The given type for the Terms of Service | [optional] 
**passive** | **bool** | Boolean dictating if the user must accept Terms of Service | [optional] 
**account_id** | **int** | The id of the root account that owns the Terms of Service | [optional] 
**content** | **str** | Content of the Terms of Service | [optional] 
**self_registration_type** | **str** | The type of self registration allowed | [optional] 

## Example

```python
from canvas_lms_python_client.models.terms_of_service import TermsOfService

# TODO update the JSON string below
json = "{}"
# create an instance of TermsOfService from a JSON string
terms_of_service_instance = TermsOfService.from_json(json)
# print the JSON string representation of the object
print(TermsOfService.to_json())

# convert the object into a dict
terms_of_service_dict = terms_of_service_instance.to_dict()
# create an instance of TermsOfService from a dict
terms_of_service_from_dict = TermsOfService.from_dict(terms_of_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


