# CareerExperienceEnabledResponse

Object response with `enabled` (from the Canvas `@returns`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.career_experience_enabled_response import CareerExperienceEnabledResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CareerExperienceEnabledResponse from a JSON string
career_experience_enabled_response_instance = CareerExperienceEnabledResponse.from_json(json)
# print the JSON string representation of the object
print(CareerExperienceEnabledResponse.to_json())

# convert the object into a dict
career_experience_enabled_response_dict = career_experience_enabled_response_instance.to_dict()
# create an instance of CareerExperienceEnabledResponse from a dict
career_experience_enabled_response_from_dict = CareerExperienceEnabledResponse.from_dict(career_experience_enabled_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


