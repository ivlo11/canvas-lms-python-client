# ProvisionalGradesStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**needs_provisional_grade** | **bool** |  | [optional] 
**provisional_grades** | **List[object]** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.provisional_grades_status_response import ProvisionalGradesStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProvisionalGradesStatusResponse from a JSON string
provisional_grades_status_response_instance = ProvisionalGradesStatusResponse.from_json(json)
# print the JSON string representation of the object
print(ProvisionalGradesStatusResponse.to_json())

# convert the object into a dict
provisional_grades_status_response_dict = provisional_grades_status_response_instance.to_dict()
# create an instance of ProvisionalGradesStatusResponse from a dict
provisional_grades_status_response_from_dict = ProvisionalGradesStatusResponse.from_dict(provisional_grades_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


