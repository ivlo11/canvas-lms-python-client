# CoursesApiSettingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_final_grade_override** | **bool** |  | [optional] 
**allow_student_anonymous_discussion_topics** | **bool** |  | [optional] 
**allow_student_discussion_editing** | **bool** |  | [optional] 
**allow_student_discussion_reporting** | **bool** |  | [optional] 
**allow_student_discussion_topics** | **bool** |  | [optional] 
**allow_student_forum_attachments** | **bool** |  | [optional] 
**allow_student_organized_groups** | **bool** |  | [optional] 
**banner_image** | **object** |  | [optional] 
**banner_image_id** | **object** |  | [optional] 
**banner_image_url** | **object** |  | [optional] 
**conditional_release** | **bool** |  | [optional] 
**course_color** | **object** |  | [optional] 
**default_discussion_settings** | **object** |  | [optional] 
**default_due_time** | **str** |  | [optional] 
**default_student_gradebook_view** | **bool** |  | [optional] 
**filter_speed_grader_by_student_group** | **bool** |  | [optional] 
**friendly_name** | **object** |  | [optional] 
**grade_passback_setting** | **object** |  | [optional] 
**grading_standard_enabled** | **bool** |  | [optional] 
**grading_standard_id** | **int** |  | [optional] 
**hide_distribution_graphs** | **bool** |  | [optional] 
**hide_final_grades** | **bool** |  | [optional] 
**hide_sections_on_course_users_page** | **bool** |  | [optional] 
**home_page_announcement_limit** | **object** |  | [optional] 
**homeroom_course** | **bool** |  | [optional] 
**image** | **object** |  | [optional] 
**image_id** | **object** |  | [optional] 
**image_url** | **object** |  | [optional] 
**lock_all_announcements** | **bool** |  | [optional] 
**restrict_quantitative_data** | **bool** |  | [optional] 
**restrict_student_future_view** | **bool** |  | [optional] 
**restrict_student_past_view** | **bool** |  | [optional] 
**show_announcements_on_home_page** | **bool** |  | [optional] 
**syllabus_course_summary** | **bool** |  | [optional] 
**usage_rights_required** | **bool** |  | [optional] 
**use_default_discussion_settings** | **bool** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.courses_api_settings_response import CoursesApiSettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CoursesApiSettingsResponse from a JSON string
courses_api_settings_response_instance = CoursesApiSettingsResponse.from_json(json)
# print the JSON string representation of the object
print(CoursesApiSettingsResponse.to_json())

# convert the object into a dict
courses_api_settings_response_dict = courses_api_settings_response_instance.to_dict()
# create an instance of CoursesApiSettingsResponse from a dict
courses_api_settings_response_from_dict = CoursesApiSettingsResponse.from_dict(courses_api_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


