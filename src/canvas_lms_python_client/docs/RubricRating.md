# RubricRating


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**criterion_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**long_description** | **str** |  | [optional] 
**points** | **int** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.rubric_rating import RubricRating

# TODO update the JSON string below
json = "{}"
# create an instance of RubricRating from a JSON string
rubric_rating_instance = RubricRating.from_json(json)
# print the JSON string representation of the object
print(RubricRating.to_json())

# convert the object into a dict
rubric_rating_dict = rubric_rating_instance.to_dict()
# create an instance of RubricRating from a dict
rubric_rating_from_dict = RubricRating.from_dict(rubric_rating_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


