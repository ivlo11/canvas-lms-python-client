# CourseGradingPeriod

A grading period of the course's term, as included with include[]=grading_periods

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for the grading period. | [optional] 
**title** | **str** | The title for the grading period. | [optional] 
**start_date** | **datetime** | The start date of the grading period. | [optional] 
**end_date** | **datetime** | The end date of the grading period. | [optional] 
**workflow_state** | **str** | The state of the grading period: active or deleted. | [optional] 

## Example

```python
from canvas_lms_python_client.models.course_grading_period import CourseGradingPeriod

# TODO update the JSON string below
json = "{}"
# create an instance of CourseGradingPeriod from a JSON string
course_grading_period_instance = CourseGradingPeriod.from_json(json)
# print the JSON string representation of the object
print(CourseGradingPeriod.to_json())

# convert the object into a dict
course_grading_period_dict = course_grading_period_instance.to_dict()
# create an instance of CourseGradingPeriod from a dict
course_grading_period_from_dict = CourseGradingPeriod.from_dict(course_grading_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


