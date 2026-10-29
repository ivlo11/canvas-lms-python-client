# PseudonymsCreateRequestUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | [Required, String] The ID of the user to create the login for. | 
**existing_user_id** | **str** | [String] A Canvas User ID to identify a user in a trusted account (alternative to &#x60;id&#x60;, &#x60;existing_sis_user_id&#x60;, or &#x60;existing_integration_id&#x60;). This parameter is not available in OSS Canvas. | [optional] 
**existing_integration_id** | **str** | [String] An Integration ID to identify a user in a trusted account (alternative to &#x60;id&#x60;, &#x60;existing_user_id&#x60;, or &#x60;existing_sis_user_id&#x60;). This parameter is not available in OSS Canvas. | [optional] 
**existing_sis_user_id** | **str** | [String] An SIS User ID to identify a user in a trusted account (alternative to &#x60;id&#x60;, &#x60;existing_integration_id&#x60;, or &#x60;existing_user_id&#x60;). This parameter is not available in OSS Canvas. | [optional] 
**trusted_account** | **str** | [String] The domain of the account to search for the user. This field is required when identifying a user in a trusted account. This parameter is not available in OSS Canvas. | [optional] 

## Example

```python
from canvas_lms_python_client.models.pseudonyms_create_request_user import PseudonymsCreateRequestUser

# TODO update the JSON string below
json = "{}"
# create an instance of PseudonymsCreateRequestUser from a JSON string
pseudonyms_create_request_user_instance = PseudonymsCreateRequestUser.from_json(json)
# print the JSON string representation of the object
print(PseudonymsCreateRequestUser.to_json())

# convert the object into a dict
pseudonyms_create_request_user_dict = pseudonyms_create_request_user_instance.to_dict()
# create an instance of PseudonymsCreateRequestUser from a dict
pseudonyms_create_request_user_from_dict = PseudonymsCreateRequestUser.from_dict(pseudonyms_create_request_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


