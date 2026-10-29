# SubmissionsApiBulkUpdateRequestGradeData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**student_id** | **str** | [file_ids][] [Integer] See documentation for the comment[] arguments in the {api:SubmissionsApiController#update Submissions Update} documentation | [optional] 
**assignment_id** | **str** | [&lt;student_id&gt;] [Integer] Specifies which assignment to grade.  This argument is not necessary when using the assignment-specific endpoints. | [optional] 

## Example

```python
from canvas_lms_python_client.models.submissions_api_bulk_update_request_grade_data import SubmissionsApiBulkUpdateRequestGradeData

# TODO update the JSON string below
json = "{}"
# create an instance of SubmissionsApiBulkUpdateRequestGradeData from a JSON string
submissions_api_bulk_update_request_grade_data_instance = SubmissionsApiBulkUpdateRequestGradeData.from_json(json)
# print the JSON string representation of the object
print(SubmissionsApiBulkUpdateRequestGradeData.to_json())

# convert the object into a dict
submissions_api_bulk_update_request_grade_data_dict = submissions_api_bulk_update_request_grade_data_instance.to_dict()
# create an instance of SubmissionsApiBulkUpdateRequestGradeData from a dict
submissions_api_bulk_update_request_grade_data_from_dict = SubmissionsApiBulkUpdateRequestGradeData.from_dict(submissions_api_bulk_update_request_grade_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


