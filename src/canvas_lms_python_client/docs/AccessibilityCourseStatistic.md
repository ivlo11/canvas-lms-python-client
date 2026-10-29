# AccessibilityCourseStatistic

Per-course accessibility issue counts for a user's active teacher/designer courses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the accessibility course statistic record | [optional] 
**course_id** | **int** | The ID of the course | [optional] 
**course_name** | **str** | The name of the course | [optional] 
**course_code** | **str** | The course code (short name) of the course | [optional] 
**published** | **bool** | Whether the course is published | [optional] 
**active_issue_count** | **int** | The number of active accessibility issues in the course | [optional] 
**resolved_issue_count** | **int** | The number of resolved accessibility issues in the course | [optional] 
**closed_issue_count** | **int** | The number of closed accessibility issues in the course | [optional] 
**workflow_state** | **str** | The workflow state of the statistic record | [optional] 
**created_at** | **datetime** | The date and time the record was created | [optional] 
**updated_at** | **datetime** | The date and time the record was last updated | [optional] 

## Example

```python
from canvas_lms_python_client.models.accessibility_course_statistic import AccessibilityCourseStatistic

# TODO update the JSON string below
json = "{}"
# create an instance of AccessibilityCourseStatistic from a JSON string
accessibility_course_statistic_instance = AccessibilityCourseStatistic.from_json(json)
# print the JSON string representation of the object
print(AccessibilityCourseStatistic.to_json())

# convert the object into a dict
accessibility_course_statistic_dict = accessibility_course_statistic_instance.to_dict()
# create an instance of AccessibilityCourseStatistic from a dict
accessibility_course_statistic_from_dict = AccessibilityCourseStatistic.from_dict(accessibility_course_statistic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


