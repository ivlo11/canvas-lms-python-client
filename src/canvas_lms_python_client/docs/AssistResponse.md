# AssistResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chips** | **List[object]** |  | [optional] 
**response** | **str** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.assist_response import AssistResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AssistResponse from a JSON string
assist_response_instance = AssistResponse.from_json(json)
# print the JSON string representation of the object
print(AssistResponse.to_json())

# convert the object into a dict
assist_response_dict = assist_response_instance.to_dict()
# create an instance of AssistResponse from a dict
assist_response_from_dict = AssistResponse.from_dict(assist_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


