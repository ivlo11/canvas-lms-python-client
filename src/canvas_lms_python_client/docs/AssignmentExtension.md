# AssignmentExtension


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignment_id** | **int** | The ID of the Assignment the extension belongs to. | 
**user_id** | **int** | The ID of the Student that needs the assignment extension. | 
**extra_attempts** | **int** | Number of times the student is allowed to re-submit the assignment | [optional] 

## Example

```python
from canvas_lms_python_client.models.assignment_extension import AssignmentExtension

# TODO update the JSON string below
json = "{}"
# create an instance of AssignmentExtension from a JSON string
assignment_extension_instance = AssignmentExtension.from_json(json)
# print the JSON string representation of the object
print(AssignmentExtension.to_json())

# convert the object into a dict
assignment_extension_dict = assignment_extension_instance.to_dict()
# create an instance of AssignmentExtension from a dict
assignment_extension_from_dict = AssignmentExtension.from_dict(assignment_extension_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


