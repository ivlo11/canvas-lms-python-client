# UserProgress

A user's display fields with their progress in the course.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the user. | [optional] 
**anonymous_id** | **str** | The anonymous ID of the user, for use in anonymous grading. | [optional] 
**display_name** | **str** | The name of the user, as it should be displayed. | [optional] 
**avatar_image_url** | **str** | The URL of the user&#39;s avatar image. | [optional] 
**html_url** | **str** | The URL of the user&#39;s page in the course. | [optional] 
**pronouns** | **str** | The user&#39;s pronouns, if pronouns are enabled. | [optional] 
**fake_student** | **bool** | Optional: true if the user is the course&#39;s test student. Only included for test students. | [optional] 
**progress** | [**CourseProgress**](CourseProgress.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.user_progress import UserProgress

# TODO update the JSON string below
json = "{}"
# create an instance of UserProgress from a JSON string
user_progress_instance = UserProgress.from_json(json)
# print the JSON string representation of the object
print(UserProgress.to_json())

# convert the object into a dict
user_progress_dict = user_progress_instance.to_dict()
# create an instance of UserProgress from a dict
user_progress_from_dict = UserProgress.from_dict(user_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


