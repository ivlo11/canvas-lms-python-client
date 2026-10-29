# ExceptionRecord

Lists associated courses that did not receive a change propagated from a blueprint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**course_id** | **int** | The ID of the associated course | [optional] 
**conflicting_changes** | **List[object]** | A list of change classes in the associated course&#39;s copy of the item that prevented a blueprint change from being applied. One or more of [&#39;content&#39;, &#39;points&#39;, &#39;due_dates&#39;, &#39;availability_dates&#39;]. | [optional] 

## Example

```python
from canvas_lms_python_client.models.exception_record import ExceptionRecord

# TODO update the JSON string below
json = "{}"
# create an instance of ExceptionRecord from a JSON string
exception_record_instance = ExceptionRecord.from_json(json)
# print the JSON string representation of the object
print(ExceptionRecord.to_json())

# convert the object into a dict
exception_record_dict = exception_record_instance.to_dict()
# create an instance of ExceptionRecord from a dict
exception_record_from_dict = ExceptionRecord.from_dict(exception_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


