# StudyAssistCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompt** | **str** | Short prompt (e.g. \&quot;Summarize\&quot;). Blank returns chips. | [optional] 
**state** | **str** | Content state with courseID, and one of pageID or fileID. | [optional] 
**regenerate** | **bool** | If true, bypasses the LLM response cache. | [optional] 

## Example

```python
from canvas_lms_python_client.models.study_assist_create_request import StudyAssistCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StudyAssistCreateRequest from a JSON string
study_assist_create_request_instance = StudyAssistCreateRequest.from_json(json)
# print the JSON string representation of the object
print(StudyAssistCreateRequest.to_json())

# convert the object into a dict
study_assist_create_request_dict = study_assist_create_request_instance.to_dict()
# create an instance of StudyAssistCreateRequest from a dict
study_assist_create_request_from_dict = StudyAssistCreateRequest.from_dict(study_assist_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


