# CoursesCreateRequestCourse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | [String] The name of the course. If omitted, the course will be named \&quot;Unnamed Course.\&quot; | [optional] 
**course_code** | **str** | [String] The course code for the course. | [optional] 
**start_at** | **str** | [DateTime] Course start date in ISO8601 format, e.g. 2011-01-01T01:00Z This value is ignored unless &#39;restrict_enrollments_to_course_dates&#39; is set to true. | [optional] 
**end_at** | **str** | [DateTime] Course end date in ISO8601 format. e.g. 2011-01-01T01:00Z This value is ignored unless &#39;restrict_enrollments_to_course_dates&#39; is set to true. | [optional] 
**license** | **str** | [String] The name of the licensing. Should be one of the following abbreviations (a descriptive name is included in parenthesis for reference): - &#39;private&#39; (Private Copyrighted) - &#39;cc_by_nc_nd&#39; (CC Attribution Non-Commercial No Derivatives) - &#39;cc_by_nc_sa&#39; (CC Attribution Non-Commercial Share Alike) - &#39;cc_by_nc&#39; (CC Attribution Non-Commercial) - &#39;cc_by_nd&#39; (CC Attribution No Derivatives) - &#39;cc_by_sa&#39; (CC Attribution Share Alike) - &#39;cc_by&#39; (CC Attribution) - &#39;public_domain&#39; (Public Domain). | [optional] 
**is_public** | **bool** | [Boolean] Set to true if course is public to both authenticated and unauthenticated users. | [optional] 
**is_public_to_auth_users** | **bool** | [Boolean] Set to true if course is public only to authenticated users. | [optional] 
**public_syllabus** | **bool** | [Boolean] Set to true to make the course syllabus public. | [optional] 
**public_syllabus_to_auth** | **bool** | [Boolean] Set to true to make the course syllabus public for authenticated users. | [optional] 
**public_description** | **str** | [String] A publicly visible description of the course. | [optional] 
**allow_student_wiki_edits** | **bool** | [Boolean] If true, students will be able to modify the course wiki. | [optional] 
**allow_wiki_comments** | **bool** | [Boolean] If true, course members will be able to comment on wiki pages. | [optional] 
**allow_student_forum_attachments** | **bool** | [Boolean] If true, students can attach files to forum posts. | [optional] 
**open_enrollment** | **bool** | [Boolean] Set to true if the course is open enrollment. | [optional] 
**self_enrollment** | **bool** | [Boolean] Set to true if the course is self enrollment. | [optional] 
**restrict_enrollments_to_course_dates** | **bool** | [Boolean] Set to true to restrict user enrollments to the start and end dates of the course. This value must be set to true in order to specify a course start date and/or end date. | [optional] 
**term_id** | **str** | [String] The unique ID of the term to create to course in. | [optional] 
**sis_course_id** | **str** | [String] The unique SIS identifier. | [optional] 
**integration_id** | **str** | [String] The unique Integration identifier. | [optional] 
**hide_final_grades** | **bool** | [Boolean] If this option is set to true, the totals in student grades summary will be hidden. | [optional] 
**apply_assignment_group_weights** | **bool** | [Boolean] Set to true to weight final grade based on assignment groups percentages. | [optional] 
**default_view** | **str** | [String, \&quot;feed\&quot;|\&quot;wiki\&quot;|\&quot;modules\&quot;|\&quot;syllabus\&quot;|\&quot;assignments\&quot;] The type of page that users will see when they first visit the course * &#39;feed&#39; Recent Activity Dashboard * &#39;modules&#39; Course Modules/Sections Page * &#39;assignments&#39; Course Assignments List * &#39;syllabus&#39; Course Syllabus Page other types may be added in the future | [optional] 
**syllabus_body** | **str** | [String] The syllabus body for the course | [optional] 
**grading_standard_id** | **int** | [Integer] The grading standard id to set for the course.  If no value is provided for this argument the current grading_standard will be un-set from this course. | [optional] 
**grade_passback_setting** | **str** | [String] Optional. The grade_passback_setting for the course. Only &#39;nightly_sync&#39;, &#39;disabled&#39;, and &#39;&#39; are allowed | [optional] 
**course_format** | **str** | [String] Optional. Specifies the format of the course. (Should be &#39;on_campus&#39;, &#39;online&#39;, or &#39;blended&#39;) | [optional] 
**post_manually** | **bool** | [Boolean] Default is false. When true, all grades in the course must be posted manually, and will not be automatically posted. When false, all grades in the course will be automatically posted. | [optional] 

## Example

```python
from canvas_lms_python_client.models.courses_create_request_course import CoursesCreateRequestCourse

# TODO update the JSON string below
json = "{}"
# create an instance of CoursesCreateRequestCourse from a JSON string
courses_create_request_course_instance = CoursesCreateRequestCourse.from_json(json)
# print the JSON string representation of the object
print(CoursesCreateRequestCourse.to_json())

# convert the object into a dict
courses_create_request_course_dict = courses_create_request_course_instance.to_dict()
# create an instance of CoursesCreateRequestCourse from a dict
courses_create_request_course_from_dict = CoursesCreateRequestCourse.from_dict(courses_create_request_course_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


