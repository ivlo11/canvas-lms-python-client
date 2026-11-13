# CoursesDestroyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conclude** | **bool** |  | [optional] 
**delete** | **bool** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.courses_destroy_response import CoursesDestroyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CoursesDestroyResponse from a JSON string
courses_destroy_response_instance = CoursesDestroyResponse.from_json(json)
# print the JSON string representation of the object
print(CoursesDestroyResponse.to_json())

# convert the object into a dict
courses_destroy_response_dict = courses_destroy_response_instance.to_dict()
# create an instance of CoursesDestroyResponse from a dict
courses_destroy_response_from_dict = CoursesDestroyResponse.from_dict(courses_destroy_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


