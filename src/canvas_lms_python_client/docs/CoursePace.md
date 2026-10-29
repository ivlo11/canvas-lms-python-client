# CoursePace



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | the ID of the course pace | [optional] 
**course_id** | **int** | the ID of the course | [optional] 
**user_id** | **int** | the ID of the user for this course pace | [optional] 
**workflow_state** | **str** | the state of the course pace | [optional] 
**exclude_weekends** | **bool** | boolean value depending on exclude weekends setting | [optional] 
**selected_days_to_skip** | **List[int]** | array of strings representing the days of the work week | [optional] 
**hard_end_dates** | **bool** | set if the end date is set from course | [optional] 
**created_at** | **datetime** | date when course pace is created | [optional] 
**end_date** | **datetime** | course end date | [optional] 
**updated_at** | **datetime** | date when course pace is updated | [optional] 
**published_at** | **datetime** | date when course pace is published | [optional] 
**root_account_id** | **int** | the root account ID for this course pace | [optional] 
**start_date** | **datetime** | course start date | [optional] 
**modules** | **List[object]** | list of modules and items for this course pace | [optional] 
**progress** | [**Progress**](Progress.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.course_pace import CoursePace

# TODO update the JSON string below
json = "{}"
# create an instance of CoursePace from a JSON string
course_pace_instance = CoursePace.from_json(json)
# print the JSON string representation of the object
print(CoursePace.to_json())

# convert the object into a dict
course_pace_dict = course_pace_instance.to_dict()
# create an instance of CoursePace from a dict
course_pace_from_dict = CoursePace.from_dict(course_pace_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


