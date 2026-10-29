# AiExperience

An AI Experience for interactive learning

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the AI experience | [optional] 
**title** | **str** | The title for the AI experience | [optional] 
**description** | **str** | The description of the AI experience | [optional] 
**facts** | **str** | The AI facts for the experience (optional) | [optional] 
**learning_objective** | **str** | The learning objectives for this experience | [optional] 
**pedagogical_guidance** | **str** | The pedagogical guidance for the experience | [optional] 
**workflow_state** | **str** | The current published state of the AI experience | [optional] 
**course_id** | **int** | The course this experience belongs to | [optional] 

## Example

```python
from canvas_lms_python_client.models.ai_experience import AiExperience

# TODO update the JSON string below
json = "{}"
# create an instance of AiExperience from a JSON string
ai_experience_instance = AiExperience.from_json(json)
# print the JSON string representation of the object
print(AiExperience.to_json())

# convert the object into a dict
ai_experience_dict = ai_experience_instance.to_dict()
# create an instance of AiExperience from a dict
ai_experience_from_dict = AiExperience.from_dict(ai_experience_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


