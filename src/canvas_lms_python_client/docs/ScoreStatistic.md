# ScoreStatistic

Used by Assignment model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min** | **int** | Min score | [optional] 
**max** | **int** | Max score | [optional] 
**mean** | **int** | Mean score | [optional] 
**upper_q** | **int** | Upper quartile score | [optional] 
**median** | **int** | Median score | [optional] 
**lower_q** | **int** | Lower quartile score | [optional] 

## Example

```python
from canvas_lms_python_client.models.score_statistic import ScoreStatistic

# TODO update the JSON string below
json = "{}"
# create an instance of ScoreStatistic from a JSON string
score_statistic_instance = ScoreStatistic.from_json(json)
# print the JSON string representation of the object
print(ScoreStatistic.to_json())

# convert the object into a dict
score_statistic_dict = score_statistic_instance.to_dict()
# create an instance of ScoreStatistic from a dict
score_statistic_from_dict = ScoreStatistic.from_dict(score_statistic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


