# EstimatedDuration

An estimated duration for completing a learning activity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for the estimated duration | [optional] 
**duration** | **str** | The estimated duration in ISO 8601 format | [optional] 
**created_at** | **str** | Timestamp of when the estimated duration was created | [optional] 
**updated_at** | **str** | Timestamp of when the estimated duration was last updated | [optional] 

## Example

```python
from canvas_lms_python_client.models.estimated_duration import EstimatedDuration

# TODO update the JSON string below
json = "{}"
# create an instance of EstimatedDuration from a JSON string
estimated_duration_instance = EstimatedDuration.from_json(json)
# print the JSON string representation of the object
print(EstimatedDuration.to_json())

# convert the object into a dict
estimated_duration_dict = estimated_duration_instance.to_dict()
# create an instance of EstimatedDuration from a dict
estimated_duration_from_dict = EstimatedDuration.from_dict(estimated_duration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


