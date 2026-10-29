# AiExperiencesCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The title of the AI experience. | 
**description** | **str** | The description of the AI experience. | [optional] 
**facts** | **str** | The AI facts for the experience. | [optional] 
**learning_objective** | **str** | The learning objectives for this experience. | 
**pedagogical_guidance** | **str** | The pedagogical guidance for the experience. | 
**workflow_state** | **str** | The initial state of the experience. Defaults to &#39;unpublished&#39;. Allowed values: published, unpublished | [optional] 

## Example

```python
from canvas_lms_python_client.models.ai_experiences_create_request import AiExperiencesCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiExperiencesCreateRequest from a JSON string
ai_experiences_create_request_instance = AiExperiencesCreateRequest.from_json(json)
# print the JSON string representation of the object
print(AiExperiencesCreateRequest.to_json())

# convert the object into a dict
ai_experiences_create_request_dict = ai_experiences_create_request_instance.to_dict()
# create an instance of AiExperiencesCreateRequest from a dict
ai_experiences_create_request_from_dict = AiExperiencesCreateRequest.from_dict(ai_experiences_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


