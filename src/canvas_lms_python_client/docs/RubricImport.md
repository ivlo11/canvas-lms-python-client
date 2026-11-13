# RubricImport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** |  | [optional] 
**attachment_id** | **object** |  | [optional] 
**course_id** | **int** |  | [optional] 
**created_at** | **str** |  | [optional] 
**error_count** | **int** |  | [optional] 
**error_data** | **object** |  | [optional] 
**id** | **int** |  | [optional] 
**progress** | **int** |  | [optional] 
**root_account_id** | **int** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**user** | **object** |  | [optional] 
**user_id** | **int** |  | [optional] 
**workflow_state** | **str** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.rubric_import import RubricImport

# TODO update the JSON string below
json = "{}"
# create an instance of RubricImport from a JSON string
rubric_import_instance = RubricImport.from_json(json)
# print the JSON string representation of the object
print(RubricImport.to_json())

# convert the object into a dict
rubric_import_dict = rubric_import_instance.to_dict()
# create an instance of RubricImport from a dict
rubric_import_from_dict = RubricImport.from_dict(rubric_import_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


