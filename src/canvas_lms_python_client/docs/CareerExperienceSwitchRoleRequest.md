# CareerExperienceSwitchRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** | The role to switch to. | 

## Example

```python
from canvas_lms_python_client.models.career_experience_switch_role_request import CareerExperienceSwitchRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CareerExperienceSwitchRoleRequest from a JSON string
career_experience_switch_role_request_instance = CareerExperienceSwitchRoleRequest.from_json(json)
# print the JSON string representation of the object
print(CareerExperienceSwitchRoleRequest.to_json())

# convert the object into a dict
career_experience_switch_role_request_dict = career_experience_switch_role_request_instance.to_dict()
# create an instance of CareerExperienceSwitchRoleRequest from a dict
career_experience_switch_role_request_from_dict = CareerExperienceSwitchRoleRequest.from_dict(career_experience_switch_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


