# Login

A user's login (pseudonym) on an account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique, numeric ID for the login. | 
**user_id** | **int** | The unique ID of the login&#39;s user. | 
**account_id** | **int** | The ID of the login&#39;s account. | 
**unique_id** | **str** | The unique ID for the login. | 
**sis_user_id** | **str** | The login&#39;s unique SIS ID. Only included if the caller can read SIS data. | [optional] 
**integration_id** | **str** | The login&#39;s unique integration ID. Only included if the caller can read SIS data. | [optional] 
**authentication_provider_id** | **int** | The ID of the authentication provider that this login is associated with. | [optional] 
**authentication_provider_type** | **str** | The type of the authentication provider that this login is associated with. Only included when the login has a provider. | [optional] 
**created_at** | **datetime** | When the login was created. | [optional] 
**workflow_state** | **str** | The current status of the login. | [optional] 
**declared_user_type** | **str** | The declared intention for this user&#39;s role. | [optional] 

## Example

```python
from canvas_lms_python_client.models.login import Login

# TODO update the JSON string below
json = "{}"
# create an instance of Login from a JSON string
login_instance = Login.from_json(json)
# print the JSON string representation of the object
print(Login.to_json())

# convert the object into a dict
login_dict = login_instance.to_dict()
# create an instance of Login from a dict
login_from_dict = Login.from_dict(login_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


