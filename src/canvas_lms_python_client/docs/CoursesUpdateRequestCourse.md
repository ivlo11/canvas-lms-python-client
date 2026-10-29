# CoursesUpdateRequestCourse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | [Integer] The unique ID of the account to move the course to. | [optional] 
**name** | **str** | [String] The name of the course. If omitted, the course will be named \&quot;Unnamed Course.\&quot; | [optional] 
**course_code** | **str** | [String] The course code for the course. | [optional] 
**start_at** | **str** | [DateTime] Course start date in ISO8601 format, e.g. 2011-01-01T01:00Z This value is ignored unless &#39;restrict_enrollments_to_course_dates&#39; is set to true, or the course is already published. | [optional] 
**end_at** | **str** | [DateTime] Course end date in ISO8601 format. e.g. 2011-01-01T01:00Z This value is ignored unless &#39;restrict_enrollments_to_course_dates&#39; is set to true. | [optional] 
**license** | **str** | [String] The name of the licensing. Should be one of the following abbreviations (a descriptive name is included in parenthesis for reference): - &#39;private&#39; (Private Copyrighted) - &#39;cc_by_nc_nd&#39; (CC Attribution Non-Commercial No Derivatives) - &#39;cc_by_nc_sa&#39; (CC Attribution Non-Commercial Share Alike) - &#39;cc_by_nc&#39; (CC Attribution Non-Commercial) - &#39;cc_by_nd&#39; (CC Attribution No Derivatives) - &#39;cc_by_sa&#39; (CC Attribution Share Alike) - &#39;cc_by&#39; (CC Attribution) - &#39;public_domain&#39; (Public Domain). | [optional] 
**is_public** | **bool** | [Boolean] Set to true if course is public to both authenticated and unauthenticated users. | [optional] 
**is_public_to_auth_users** | **bool** | [Boolean] Set to true if course is public only to authenticated users. | [optional] 
**public_syllabus** | **bool** | [Boolean] Set to true to make the course syllabus public. | [optional] 
**public_syllabus_to_auth** | **bool** | [Boolean] Set to true to make the course syllabus to public for authenticated users. | [optional] 
**public_description** | **str** | [String] A publicly visible description of the course. | [optional] 
**allow_student_wiki_edits** | **bool** | [Boolean] If true, students will be able to modify the course wiki. | [optional] 
**allow_wiki_comments** | **bool** | [Boolean] If true, course members will be able to comment on wiki pages. | [optional] 
**allow_student_forum_attachments** | **bool** | [Boolean] If true, students can attach files to forum posts. | [optional] 
**open_enrollment** | **bool** | [Boolean] Set to true if the course is open enrollment. | [optional] 
**self_enrollment** | **bool** | [Boolean] Set to true if the course is self enrollment. | [optional] 
**restrict_enrollments_to_course_dates** | **bool** | [Boolean] Set to true to restrict user enrollments to the start and end dates of the course. Setting this value to false will remove the course end date (if it exists), as well as the course start date (if the course is unpublished). | [optional] 
**term_id** | **int** | [Integer] The unique ID of the term to create to course in. | [optional] 
**sis_course_id** | **str** | [String] The unique SIS identifier. | [optional] 
**integration_id** | **str** | [String] The unique Integration identifier. | [optional] 
**hide_final_grades** | **bool** | [Boolean] If this option is set to true, the totals in student grades summary will be hidden. | [optional] 
**apply_assignment_group_weights** | **bool** | [Boolean] Set to true to weight final grade based on assignment groups percentages. | [optional] 
**storage_quota_mb** | **int** | [Integer] Set the storage quota for the course, in megabytes. The caller must have the \&quot;Manage storage quotas\&quot; account permission. | [optional] 
**event** | **str** | [String, \&quot;claim\&quot;|\&quot;offer\&quot;|\&quot;conclude\&quot;|\&quot;delete\&quot;|\&quot;undelete\&quot;] The action to take on each course. * &#39;claim&#39; makes a course no longer visible to students. This action is also called \&quot;unpublish\&quot; on the web site.   A course cannot be unpublished if students have received graded submissions. * &#39;offer&#39; makes a course visible to students. This action is also called \&quot;publish\&quot; on the web site. * &#39;conclude&#39; prevents future enrollments and makes a course read-only for all participants. The course still appears   in prior-enrollment lists. * &#39;delete&#39; completely removes the course from the web site (including course menus and prior-enrollment lists).   All enrollments are deleted. Course content may be physically deleted at a future date. * &#39;undelete&#39; attempts to recover a course that has been deleted. This action requires account administrative rights.   (Recovery is not guaranteed; please conclude rather than delete a course if there is any possibility the course   will be used again.) The recovered course will be unpublished. Deleted enrollments will not be recovered. | [optional] 
**default_view** | **str** | [String, \&quot;feed\&quot;|\&quot;wiki\&quot;|\&quot;modules\&quot;|\&quot;syllabus\&quot;|\&quot;assignments\&quot;] The type of page that users will see when they first visit the course * &#39;feed&#39; Recent Activity Dashboard * &#39;wiki&#39; Wiki Front Page * &#39;modules&#39; Course Modules/Sections Page * &#39;assignments&#39; Course Assignments List * &#39;syllabus&#39; Course Syllabus Page other types may be added in the future | [optional] 
**syllabus_body** | **str** | [String] The syllabus body for the course | [optional] 
**syllabus_course_summary** | **bool** | [Boolean] Optional. Indicates whether the Course Summary (consisting of the course&#39;s assignments and calendar events) is displayed on the syllabus page. Defaults to +true+. | [optional] 
**grading_standard_id** | **int** | [Integer] The grading standard id to set for the course.  If no value is provided for this argument the current grading_standard will be un-set from this course. | [optional] 
**grade_passback_setting** | **str** | [String] Optional. The grade_passback_setting for the course. Only &#39;nightly_sync&#39; and &#39;&#39; are allowed | [optional] 
**course_format** | **str** | [String] Optional. Specifies the format of the course. (Should be either &#39;on_campus&#39; or &#39;online&#39;) | [optional] 
**image_id** | **int** | [Integer] This is a file ID corresponding to an image file in the course that will be used as the course image. This will clear the course&#39;s image_url setting if set.  If you attempt to provide image_url and image_id in a request it will fail. | [optional] 
**image_url** | **str** | [String] This is a URL to an image to be used as the course image. This will clear the course&#39;s image_id setting if set.  If you attempt to provide image_url and image_id in a request it will fail. | [optional] 
**remove_image** | **bool** | [Boolean] If this option is set to true, the course image url and course image ID are both set to nil | [optional] 
**remove_banner_image** | **bool** | [Boolean] If this option is set to true, the course banner image url and course banner image ID are both set to nil | [optional] 
**blueprint** | **bool** | [Boolean] Sets the course as a blueprint course. | [optional] 
**blueprint_restrictions** | **str** | [BlueprintRestriction] Sets a default set to apply to blueprint course objects when restricted, unless _use_blueprint_restrictions_by_object_type_ is enabled. See the {api:Blueprint_Courses:BlueprintRestriction Blueprint Restriction} documentation | [optional] 
**use_blueprint_restrictions_by_object_type** | **bool** | [Boolean] When enabled, the _blueprint_restrictions_ parameter will be ignored in favor of the _blueprint_restrictions_by_object_type_ parameter | [optional] 
**blueprint_restrictions_by_object_type** | **str** | [multiple BlueprintRestrictions] Allows setting multiple {api:Blueprint_Courses:BlueprintRestriction Blueprint Restriction} to apply to blueprint course objects of the matching type when restricted. The possible object types are \&quot;assignment\&quot;, \&quot;attachment\&quot;, \&quot;discussion_topic\&quot;, \&quot;quiz\&quot; and \&quot;wiki_page\&quot;. Example usage:   course[blueprint_restrictions_by_object_type][assignment][content]&#x3D;1 | [optional] 
**homeroom_course** | **bool** | [Boolean] Sets the course as a homeroom course. The setting takes effect only when the course is associated with a Canvas for Elementary-enabled account. | [optional] 
**sync_enrollments_from_homeroom** | **str** | [String] Syncs enrollments from the homeroom that is set in homeroom_course_id. The setting only takes effect when the course is associated with a Canvas for Elementary-enabled account and sync_enrollments_from_homeroom is enabled. | [optional] 
**homeroom_course_id** | **str** | [String] Sets the Homeroom Course id to be used with sync_enrollments_from_homeroom. The setting only takes effect when the course is associated with a Canvas for Elementary-enabled account and sync_enrollments_from_homeroom is enabled. | [optional] 
**template** | **bool** | [Boolean] Enable or disable the course as a template that can be selected by an account | [optional] 
**course_color** | **str** | [String] Sets a color in hex code format to be associated with the course. The setting takes effect only when the course is associated with a Canvas for Elementary-enabled account. | [optional] 
**friendly_name** | **str** | [String] Set a friendly name for the course. If this is provided and the course is associated with a Canvas for Elementary account, it will be shown instead of the course name. This setting takes priority over course nicknames defined by individual users. | [optional] 
**enable_course_paces** | **bool** | [Boolean] Enable or disable Course Pacing for the course. This setting only has an effect when the Course Pacing feature flag is enabled for the sub-account. Otherwise, Course Pacing are always disabled. | [optional] 
**conditional_release** | **bool** | [Boolean] Enable or disable individual learning paths for students based on assessment | [optional] 
**post_manually** | **bool** | [Boolean] When true, all grades in the course will be posted manually. When false, all grades in the course will be automatically posted. Use with caution as this setting will override any assignment level post policy. | [optional] 

## Example

```python
from canvas_lms_python_client.models.courses_update_request_course import CoursesUpdateRequestCourse

# TODO update the JSON string below
json = "{}"
# create an instance of CoursesUpdateRequestCourse from a JSON string
courses_update_request_course_instance = CoursesUpdateRequestCourse.from_json(json)
# print the JSON string representation of the object
print(CoursesUpdateRequestCourse.to_json())

# convert the object into a dict
courses_update_request_course_dict = courses_update_request_course_instance.to_dict()
# create an instance of CoursesUpdateRequestCourse from a dict
courses_update_request_course_from_dict = CoursesUpdateRequestCourse.from_dict(courses_update_request_course_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


