# RubricsDestroyResponse

Object response with `rubric` (from the Canvas `@returns`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rubric** | [**Rubric**](Rubric.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.rubrics_destroy_response import RubricsDestroyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RubricsDestroyResponse from a JSON string
rubrics_destroy_response_instance = RubricsDestroyResponse.from_json(json)
# print the JSON string representation of the object
print(RubricsDestroyResponse.to_json())

# convert the object into a dict
rubrics_destroy_response_dict = rubrics_destroy_response_instance.to_dict()
# create an instance of RubricsDestroyResponse from a dict
rubrics_destroy_response_from_dict = RubricsDestroyResponse.from_dict(rubrics_destroy_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


