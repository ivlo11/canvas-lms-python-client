# CatalogCourse

A course in the public course catalog. This is the raw course record, not the Course object the Courses API returns: it has conclude_at instead of end_at and storage_quota in bytes, and includes columns the Courses API doesn't.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the course. | 
**name** | **str** | The full name of the course. | 
**account_id** | **int** | The ID of the account the course belongs to. | [optional] 
**group_weighting_scheme** | **str** | How assignment groups are weighted: \&quot;equal\&quot; or \&quot;percent\&quot;. | [optional] 
**workflow_state** | **str** | The state of the course. The catalog lists only \&quot;available\&quot; courses. | [optional] 
**start_at** | **datetime** | The start date of the course. | [optional] 
**conclude_at** | **datetime** | The end date of the course. | [optional] 
**grading_standard_id** | **int** | The ID of the grading standard the course uses. | [optional] 
**is_public** | **bool** | Whether the course is public. | [optional] 
**allow_student_wiki_edits** | **bool** | Whether students can edit wiki pages. | [optional] 
**created_at** | **datetime** | When the course was created. | [optional] 
**updated_at** | **datetime** | When the course was last updated. | [optional] 
**show_public_context_messages** | **bool** | Whether public context messages are shown. | [optional] 
**syllabus_body** | **str** | The course syllabus, as HTML. | [optional] 
**allow_student_forum_attachments** | **bool** | Whether students can attach files to discussions. | [optional] 
**default_wiki_editing_roles** | **str** | The roles that can edit wiki pages by default. | [optional] 
**wiki_id** | **int** | The ID of the course&#39;s wiki. | [optional] 
**allow_student_organized_groups** | **bool** | Whether students can organize their own groups. | [optional] 
**course_code** | **str** | The course code. | [optional] 
**default_view** | **str** | The type of page users see first in the course. | [optional] 
**abstract_course_id** | **int** | The ID of the abstract course the course belongs to. | [optional] 
**root_account_id** | **int** | The ID of the root account. | [optional] 
**enrollment_term_id** | **int** | The ID of the course&#39;s enrollment term. | [optional] 
**sis_source_id** | **str** | The SIS ID of the course. | [optional] 
**sis_batch_id** | **int** | The ID of the SIS import that last changed the course. | [optional] 
**open_enrollment** | **bool** | Whether the course is open for enrollment. | [optional] 
**storage_quota** | **int** | The course&#39;s storage quota, in bytes. | [optional] 
**tab_configuration** | **List[object]** | The course&#39;s navigation tab settings. | [optional] 
**allow_wiki_comments** | **bool** | Whether wiki comments are allowed. | [optional] 
**turnitin_comments** | **str** | Comments shown to students on Turnitin submissions. | [optional] 
**self_enrollment** | **bool** | Whether users can enroll themselves. | [optional] 
**license** | **str** | The license for the course&#39;s content. | [optional] 
**indexed** | **bool** | Whether the course appears in the public course catalog. | [optional] 
**restrict_enrollments_to_course_dates** | **bool** | Whether enrollments are limited to the course dates. | [optional] 
**template_course_id** | **int** | The ID of the template course the course was created from. | [optional] 
**locale** | **str** | The course&#39;s language. | [optional] 
**settings** | **object** | Course settings, keyed by name. | [optional] 
**replacement_course_id** | **int** | The ID of the course that replaces this one. | [optional] 
**stuck_sis_fields** | **List[str]** | The fields that SIS imports won&#39;t change. | [optional] 
**public_description** | **str** | The course&#39;s public description. | [optional] 
**self_enrollment_code** | **str** | The code users enter to enroll themselves. | [optional] 
**self_enrollment_limit** | **int** | The maximum number of users who can enroll themselves. | [optional] 
**integration_id** | **str** | The integration ID of the course. | [optional] 
**time_zone** | **str** | The course&#39;s time zone, as an IANA name. | [optional] 
**lti_context_id** | **str** | The course&#39;s LTI context ID. | [optional] 
**turnitin_id** | **int** | The course&#39;s Turnitin ID. | [optional] 
**show_announcements_on_home_page** | **bool** | Whether recent announcements show on the home page. | [optional] 
**home_page_announcement_limit** | **int** | The number of announcements shown on the home page. | [optional] 
**latest_outcome_import_id** | **int** | The ID of the latest outcome import. | [optional] 
**grade_passback_setting** | **str** | The grade passback setting. | [optional] 
**template** | **bool** | Whether the course is a blueprint for new courses. | [optional] 
**homeroom_course** | **bool** | Whether the course is a homeroom course. | [optional] 
**sync_enrollments_from_homeroom** | **bool** | Whether enrollments sync from the homeroom course. | [optional] 
**homeroom_course_id** | **int** | The ID of the homeroom course enrollments sync from. | [optional] 
**deleted_at** | **datetime** | When the course was deleted. | [optional] 
**archived_at** | **datetime** | When the course was archived. | [optional] 
**horizon_course** | **bool** | Whether the course is a Canvas Career course. | [optional] 
**content_library** | **bool** | Whether the course is a content library. | [optional] 
**career_learning_library_only** | **bool** | Whether the course is a Canvas Career learning library only. | [optional] 

## Example

```python
from canvas_lms_python_client.models.catalog_course import CatalogCourse

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogCourse from a JSON string
catalog_course_instance = CatalogCourse.from_json(json)
# print the JSON string representation of the object
print(CatalogCourse.to_json())

# convert the object into a dict
catalog_course_dict = catalog_course_instance.to_dict()
# create an instance of CatalogCourse from a dict
catalog_course_from_dict = CatalogCourse.from_dict(catalog_course_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


