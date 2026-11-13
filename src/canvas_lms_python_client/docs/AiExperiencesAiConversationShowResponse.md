# AiExperiencesAiConversationShowResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**llm_conversation_id** | **str** |  | [optional] 
**messages** | **List[object]** |  | [optional] 
**progress** | **object** |  | [optional] 
**student** | **object** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**user_id** | **int** |  | [optional] 
**workflow_state** | **str** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.ai_experiences_ai_conversation_show_response import AiExperiencesAiConversationShowResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AiExperiencesAiConversationShowResponse from a JSON string
ai_experiences_ai_conversation_show_response_instance = AiExperiencesAiConversationShowResponse.from_json(json)
# print the JSON string representation of the object
print(AiExperiencesAiConversationShowResponse.to_json())

# convert the object into a dict
ai_experiences_ai_conversation_show_response_dict = ai_experiences_ai_conversation_show_response_instance.to_dict()
# create an instance of AiExperiencesAiConversationShowResponse from a dict
ai_experiences_ai_conversation_show_response_from_dict = AiExperiencesAiConversationShowResponse.from_dict(ai_experiences_ai_conversation_show_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


