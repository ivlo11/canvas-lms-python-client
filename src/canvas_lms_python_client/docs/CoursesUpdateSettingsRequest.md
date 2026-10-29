# CoursesUpdateSettingsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_final_grade_override** | **bool** | Let student final grades for a grading period or the total grades for the course be overridden | [optional] 
**allow_student_discussion_topics** | **bool** | Let students create discussion topics | [optional] 
**allow_student_forum_attachments** | **bool** | Let students attach files to discussions | [optional] 
**allow_student_discussion_editing** | **bool** | Let students edit or delete their own discussion replies | [optional] 
**allow_student_organized_groups** | **bool** | Let students organize their own groups | [optional] 
**allow_student_discussion_reporting** | **bool** | Let students report offensive discussion content | [optional] 
**allow_student_anonymous_discussion_topics** | **bool** | Let students create anonymous discussion topics | [optional] 
**filter_speed_grader_by_student_group** | **bool** | Filter SpeedGrader to only the selected student group | [optional] 
**hide_final_grades** | **bool** | Hide totals in student grades summary | [optional] 
**hide_distribution_graphs** | **bool** | Hide grade distribution graphs from students | [optional] 
**hide_sections_on_course_users_page** | **bool** | Disallow students from viewing students in sections they do not belong to | [optional] 
**lock_all_announcements** | **bool** | Disable comments on announcements | [optional] 
**usage_rights_required** | **bool** | Copyright and license information must be provided for files before they are published. | [optional] 
**restrict_student_past_view** | **bool** | Restrict students from viewing courses after end date | [optional] 
**restrict_student_future_view** | **bool** | Restrict students from viewing courses before start date | [optional] 
**show_announcements_on_home_page** | **bool** | Show the most recent announcements on the Course home page (if a Wiki, defaults to five announcements, configurable via home_page_announcement_limit). Canvas for Elementary subjects ignore this setting. | [optional] 
**home_page_announcement_limit** | **int** | Limit the number of announcements on the home page if enabled via show_announcements_on_home_page | [optional] 
**syllabus_course_summary** | **bool** | Show the course summary (list of assignments and calendar events) on the syllabus page. Default is true. | [optional] 
**default_due_time** | **str** | Set the default due time for assignments. This is the time that will be pre-selected in the Canvas user interface when setting a due date for an assignment. It does not change when any existing assignment is due. It should be given in 24-hour HH:MM:SS format. The default is \&quot;23:59:59\&quot;. Use \&quot;inherit\&quot; to inherit the account setting. | [optional] 
**conditional_release** | **bool** | Enable or disable individual learning paths for students based on assessment | [optional] 

## Example

```python
from canvas_lms_python_client.models.courses_update_settings_request import CoursesUpdateSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CoursesUpdateSettingsRequest from a JSON string
courses_update_settings_request_instance = CoursesUpdateSettingsRequest.from_json(json)
# print the JSON string representation of the object
print(CoursesUpdateSettingsRequest.to_json())

# convert the object into a dict
courses_update_settings_request_dict = courses_update_settings_request_instance.to_dict()
# create an instance of CoursesUpdateSettingsRequest from a dict
courses_update_settings_request_from_dict = CoursesUpdateSettingsRequest.from_dict(courses_update_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


