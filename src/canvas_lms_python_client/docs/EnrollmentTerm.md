# EnrollmentTerm



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for the enrollment term. | [optional] 
**sis_term_id** | **str** | The SIS id of the term. Only included if the user has permission to view SIS information. | [optional] 
**sis_import_id** | **int** | the unique identifier for the SIS import. This field is only included if the user has permission to manage SIS information. | [optional] 
**name** | **str** | The name of the term. | [optional] 
**start_at** | **datetime** | The datetime of the start of the term. | [optional] 
**end_at** | **datetime** | The datetime of the end of the term. | [optional] 
**workflow_state** | **str** | The state of the term. Can be &#39;active&#39; or &#39;deleted&#39;. | [optional] 
**overrides** | **object** | Term date overrides for specific enrollment types | [optional] 
**course_count** | **int** | The number of courses in the term (available via include) | [optional] 

## Example

```python
from canvas_lms_python_client.models.enrollment_term import EnrollmentTerm

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentTerm from a JSON string
enrollment_term_instance = EnrollmentTerm.from_json(json)
# print the JSON string representation of the object
print(EnrollmentTerm.to_json())

# convert the object into a dict
enrollment_term_dict = enrollment_term_instance.to_dict()
# create an instance of EnrollmentTerm from a dict
enrollment_term_from_dict = EnrollmentTerm.from_dict(enrollment_term_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


