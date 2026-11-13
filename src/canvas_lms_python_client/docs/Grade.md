# Grade



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**html_url** | **str** | The URL to the Canvas web UI page for the user&#39;s grades, if this is a student enrollment. | [optional] 
**current_grade** | **str** | The user&#39;s current grade in the class. Only included if user has permissions to view this grade. | [optional] 
**final_grade** | **str** | The user&#39;s final grade for the class. Only included if user has permissions to view this grade. | [optional] 
**current_score** | **float** | The user&#39;s current score in the class. Only included if user has permissions to view this score. | [optional] 
**final_score** | **float** | The user&#39;s final score for the class. Only included if user has permissions to view this score. | [optional] 
**current_points** | **float** | The total points the user has earned in the class. Only included if user has permissions to view this score and &#39;current_points&#39; is passed in the request&#39;s &#39;include&#39; parameter. | [optional] 
**unposted_current_grade** | **str** | The user&#39;s current grade in the class including muted/unposted assignments. Only included if user has permissions to view this grade, typically teachers, TAs, and admins. | [optional] 
**unposted_final_grade** | **str** | The user&#39;s final grade for the class including muted/unposted assignments. Only included if user has permissions to view this grade, typically teachers, TAs, and admins.. | [optional] 
**unposted_current_score** | **float** | The user&#39;s current score in the class including muted/unposted assignments. Only included if user has permissions to view this score, typically teachers, TAs, and admins.. | [optional] 
**unposted_final_score** | **float** | The user&#39;s final score for the class including muted/unposted assignments. Only included if user has permissions to view this score, typically teachers, TAs, and admins.. | [optional] 
**unposted_current_points** | **float** | The total points the user has earned in the class, including muted/unposted assignments. Only included if user has permissions to view this score (typically teachers, TAs, and admins) and &#39;current_points&#39; is passed in the request&#39;s &#39;include&#39; parameter. | [optional] 
**override_grade** | **str** |  | [optional] 
**override_score** | **float** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.grade import Grade

# TODO update the JSON string below
json = "{}"
# create an instance of Grade from a JSON string
grade_instance = Grade.from_json(json)
# print the JSON string representation of the object
print(Grade.to_json())

# convert the object into a dict
grade_dict = grade_instance.to_dict()
# create an instance of Grade from a dict
grade_from_dict = Grade.from_dict(grade_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


