# GradeChangeEvent



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the event. | [optional] 
**created_at** | **datetime** | timestamp of the event | [optional] 
**event_type** | **str** | GradeChange event type | [optional] 
**excused_after** | **bool** | Boolean indicating whether the submission was excused after the change. | [optional] 
**excused_before** | **bool** | Boolean indicating whether the submission was excused before the change. | [optional] 
**grade_after** | **str** | The grade after the change. | [optional] 
**grade_before** | **str** | The grade before the change. | [optional] 
**graded_anonymously** | **bool** | Boolean indicating whether the student name was visible when the grade was given. Could be null if the grade change record was created before this feature existed. | [optional] 
**version_number** | **int** | Version Number of the grade change submission. | [optional] 
**points_possible_before** | **float** | The assignment&#39;s points possible before the change. | [optional] 
**points_possible_after** | **float** | The assignment&#39;s points possible after the change. | [optional] 
**grade_current** | **str** | The current grade of the submission. Only included when the request includes current_grade. | [optional] 
**course_override_grade** | **bool** | True if the event changed a course override grade. Only included for override grade events. | [optional] 
**request_id** | **str** | The unique request id of the request during the grade change. | [optional] 
**links** | [**GradeChangeEventLinks**](GradeChangeEventLinks.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.grade_change_event import GradeChangeEvent

# TODO update the JSON string below
json = "{}"
# create an instance of GradeChangeEvent from a JSON string
grade_change_event_instance = GradeChangeEvent.from_json(json)
# print the JSON string representation of the object
print(GradeChangeEvent.to_json())

# convert the object into a dict
grade_change_event_dict = grade_change_event_instance.to_dict()
# create an instance of GradeChangeEvent from a dict
grade_change_event_from_dict = GradeChangeEvent.from_dict(grade_change_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


