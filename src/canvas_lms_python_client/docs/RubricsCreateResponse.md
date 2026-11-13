# RubricsCreateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rubric** | **object** |  | [optional] 
**rubric_association** | **object** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.rubrics_create_response import RubricsCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RubricsCreateResponse from a JSON string
rubrics_create_response_instance = RubricsCreateResponse.from_json(json)
# print the JSON string representation of the object
print(RubricsCreateResponse.to_json())

# convert the object into a dict
rubrics_create_response_dict = rubrics_create_response_instance.to_dict()
# create an instance of RubricsCreateResponse from a dict
rubrics_create_response_from_dict = RubricsCreateResponse.from_dict(rubrics_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


