# AnonymousProvisionalGradesStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**needs_provisional_grade** | **bool** |  | [optional] 
**provisional_grades** | **List[object]** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.anonymous_provisional_grades_status_response import AnonymousProvisionalGradesStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AnonymousProvisionalGradesStatusResponse from a JSON string
anonymous_provisional_grades_status_response_instance = AnonymousProvisionalGradesStatusResponse.from_json(json)
# print the JSON string representation of the object
print(AnonymousProvisionalGradesStatusResponse.to_json())

# convert the object into a dict
anonymous_provisional_grades_status_response_dict = anonymous_provisional_grades_status_response_instance.to_dict()
# create an instance of AnonymousProvisionalGradesStatusResponse from a dict
anonymous_provisional_grades_status_response_from_dict = AnonymousProvisionalGradesStatusResponse.from_dict(anonymous_provisional_grades_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


