# Result



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The fully qualified URL for showing the Result | [optional] 
**user_id** | **str** | The lti_user_id or the Canvas user_id | [optional] 
**result_score** | **float** | The score of the result as defined by Canvas, scaled to the resultMaximum | [optional] 
**result_maximum** | **float** | Maximum possible score for this result; 1 is the default value and will be assumed if not specified otherwise. Minimum value of 0 required. | [optional] 
**comment** | **str** | Comment visible to the student about the result. | [optional] 
**score_of** | **str** | URL of the line item this belongs to | [optional] 
**assessed_at** | **str** |  | [optional] 
**links** | **object** |  | [optional] 
**passed** | **bool** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.result import Result

# TODO update the JSON string below
json = "{}"
# create an instance of Result from a JSON string
result_instance = Result.from_json(json)
# print the JSON string representation of the object
print(Result.to_json())

# convert the object into a dict
result_dict = result_instance.to_dict()
# create an instance of Result from a dict
result_from_dict = Result.from_dict(result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


