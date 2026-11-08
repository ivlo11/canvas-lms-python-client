# ProvisionalGradesBulkSelectResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anonymous_id** | **str** |  | [optional] 
**assignment_id** | **int** |  | [optional] 
**selected_provisional_grade_id** | **int** |  | [optional] 
**student_id** | **int** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.provisional_grades_bulk_select_response import ProvisionalGradesBulkSelectResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProvisionalGradesBulkSelectResponse from a JSON string
provisional_grades_bulk_select_response_instance = ProvisionalGradesBulkSelectResponse.from_json(json)
# print the JSON string representation of the object
print(ProvisionalGradesBulkSelectResponse.to_json())

# convert the object into a dict
provisional_grades_bulk_select_response_dict = provisional_grades_bulk_select_response_instance.to_dict()
# create an instance of ProvisionalGradesBulkSelectResponse from a dict
provisional_grades_bulk_select_response_from_dict = ProvisionalGradesBulkSelectResponse.from_dict(provisional_grades_bulk_select_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


