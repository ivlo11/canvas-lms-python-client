# CareerExperienceSwitchExperienceResponse

Object response with `experience` (from the Canvas `@returns`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**experience** | **str** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.career_experience_switch_experience_response import CareerExperienceSwitchExperienceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CareerExperienceSwitchExperienceResponse from a JSON string
career_experience_switch_experience_response_instance = CareerExperienceSwitchExperienceResponse.from_json(json)
# print the JSON string representation of the object
print(CareerExperienceSwitchExperienceResponse.to_json())

# convert the object into a dict
career_experience_switch_experience_response_dict = career_experience_switch_experience_response_instance.to_dict()
# create an instance of CareerExperienceSwitchExperienceResponse from a dict
career_experience_switch_experience_response_from_dict = CareerExperienceSwitchExperienceResponse.from_dict(career_experience_switch_experience_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


