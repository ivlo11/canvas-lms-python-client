# SubmissionsApiBulkUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grade_data** | [**SubmissionsApiBulkUpdateRequestGradeData**](SubmissionsApiBulkUpdateRequestGradeData.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.submissions_api_bulk_update_request import SubmissionsApiBulkUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SubmissionsApiBulkUpdateRequest from a JSON string
submissions_api_bulk_update_request_instance = SubmissionsApiBulkUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(SubmissionsApiBulkUpdateRequest.to_json())

# convert the object into a dict
submissions_api_bulk_update_request_dict = submissions_api_bulk_update_request_instance.to_dict()
# create an instance of SubmissionsApiBulkUpdateRequest from a dict
submissions_api_bulk_update_request_from_dict = SubmissionsApiBulkUpdateRequest.from_dict(submissions_api_bulk_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


