# CourseQuizExtensionsCreateResponse

Paginated `quiz_extensions` list response (from the Canvas example response).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quiz_extensions** | [**List[QuizExtension]**](QuizExtension.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.course_quiz_extensions_create_response import CourseQuizExtensionsCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CourseQuizExtensionsCreateResponse from a JSON string
course_quiz_extensions_create_response_instance = CourseQuizExtensionsCreateResponse.from_json(json)
# print the JSON string representation of the object
print(CourseQuizExtensionsCreateResponse.to_json())

# convert the object into a dict
course_quiz_extensions_create_response_dict = course_quiz_extensions_create_response_instance.to_dict()
# create an instance of CourseQuizExtensionsCreateResponse from a dict
course_quiz_extensions_create_response_from_dict = CourseQuizExtensionsCreateResponse.from_dict(course_quiz_extensions_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


