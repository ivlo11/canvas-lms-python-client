# AiExperiencesUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The title of the AI experience. | [optional] 
**description** | **str** | The description of the AI experience. | [optional] 
**facts** | **str** | The AI facts for the experience. | [optional] 
**learning_objective** | **str** | The learning objectives for this experience. | 
**pedagogical_guidance** | **str** | The pedagogical guidance for the experience. | 
**workflow_state** | **str** | The state of the experience. Allowed values: published, unpublished | [optional] 

## Example

```python
from canvas_lms_python_client.models.ai_experiences_update_request import AiExperiencesUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiExperiencesUpdateRequest from a JSON string
ai_experiences_update_request_instance = AiExperiencesUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(AiExperiencesUpdateRequest.to_json())

# convert the object into a dict
ai_experiences_update_request_dict = ai_experiences_update_request_instance.to_dict()
# create an instance of AiExperiencesUpdateRequest from a dict
ai_experiences_update_request_from_dict = AiExperiencesUpdateRequest.from_dict(ai_experiences_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


