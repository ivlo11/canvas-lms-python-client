# CoursesBatchUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**course_ids** | **List[str]** | List of ids of courses to update. At most 500 courses may be updated in one call. | 
**event** | **str** | The action to take on each course.  Must be one of &#39;offer&#39;, &#39;conclude&#39;, &#39;delete&#39;, or &#39;undelete&#39;. * &#39;offer&#39; makes a course visible to students. This action is also called \&quot;publish\&quot; on the web site. * &#39;conclude&#39; prevents future enrollments and makes a course read-only for all participants. The course still appears   in prior-enrollment lists. * &#39;delete&#39; completely removes the course from the web site (including course menus and prior-enrollment lists).   All enrollments are deleted. Course content may be physically deleted at a future date. * &#39;undelete&#39; attempts to recover a course that has been deleted. (Recovery is not guaranteed; please conclude   rather than delete a course if there is any possibility the course will be used again.) The recovered course   will be unpublished. Deleted enrollments will not be recovered. | 

## Example

```python
from canvas_lms_python_client.models.courses_batch_update_request import CoursesBatchUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CoursesBatchUpdateRequest from a JSON string
courses_batch_update_request_instance = CoursesBatchUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(CoursesBatchUpdateRequest.to_json())

# convert the object into a dict
courses_batch_update_request_dict = courses_batch_update_request_instance.to_dict()
# create an instance of CoursesBatchUpdateRequest from a dict
courses_batch_update_request_from_dict = CoursesBatchUpdateRequest.from_dict(courses_batch_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


