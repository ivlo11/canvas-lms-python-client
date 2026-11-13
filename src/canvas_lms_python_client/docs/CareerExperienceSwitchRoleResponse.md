# CareerExperienceSwitchRoleResponse

Object response with `role` (from the Canvas `@returns`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.career_experience_switch_role_response import CareerExperienceSwitchRoleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CareerExperienceSwitchRoleResponse from a JSON string
career_experience_switch_role_response_instance = CareerExperienceSwitchRoleResponse.from_json(json)
# print the JSON string representation of the object
print(CareerExperienceSwitchRoleResponse.to_json())

# convert the object into a dict
career_experience_switch_role_response_dict = career_experience_switch_role_response_instance.to_dict()
# create an instance of CareerExperienceSwitchRoleResponse from a dict
career_experience_switch_role_response_from_dict = CareerExperienceSwitchRoleResponse.from_dict(career_experience_switch_role_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


