# AiExperiencesIndexResponse

Object response with `can_manage`, `experiences` (from the Canvas `@returns`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_manage** | **bool** |  | [optional] 
**experiences** | [**List[AiExperience]**](AiExperience.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.ai_experiences_index_response import AiExperiencesIndexResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AiExperiencesIndexResponse from a JSON string
ai_experiences_index_response_instance = AiExperiencesIndexResponse.from_json(json)
# print the JSON string representation of the object
print(AiExperiencesIndexResponse.to_json())

# convert the object into a dict
ai_experiences_index_response_dict = ai_experiences_index_response_instance.to_dict()
# create an instance of AiExperiencesIndexResponse from a dict
ai_experiences_index_response_from_dict = AiExperiencesIndexResponse.from_dict(ai_experiences_index_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


