# QuizExtensionsCreateResponse

Paginated `quiz_extensions` list response (from the Canvas example response).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quiz_extensions** | [**List[QuizExtension]**](QuizExtension.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.quiz_extensions_create_response import QuizExtensionsCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QuizExtensionsCreateResponse from a JSON string
quiz_extensions_create_response_instance = QuizExtensionsCreateResponse.from_json(json)
# print the JSON string representation of the object
print(QuizExtensionsCreateResponse.to_json())

# convert the object into a dict
quiz_extensions_create_response_dict = quiz_extensions_create_response_instance.to_dict()
# create an instance of QuizExtensionsCreateResponse from a dict
quiz_extensions_create_response_from_dict = QuizExtensionsCreateResponse.from_dict(quiz_extensions_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


