# CourseProgress



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requirement_count** | **int** | total number of requirements from all modules | [optional] 
**requirement_completed_count** | **int** | total number of requirements the user has completed from all modules | [optional] 
**next_requirement_url** | **str** | url to next module item that has an unmet requirement. null if the user has completed the course or the current module does not require sequential progress | [optional] 
**completed_at** | **datetime** | date the course was completed. null if the course has not been completed by this user | [optional] 

## Example

```python
from canvas_lms_python_client.models.course_progress import CourseProgress

# TODO update the JSON string below
json = "{}"
# create an instance of CourseProgress from a JSON string
course_progress_instance = CourseProgress.from_json(json)
# print the JSON string representation of the object
print(CourseProgress.to_json())

# convert the object into a dict
course_progress_dict = course_progress_instance.to_dict()
# create an instance of CourseProgress from a dict
course_progress_from_dict = CourseProgress.from_dict(course_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


