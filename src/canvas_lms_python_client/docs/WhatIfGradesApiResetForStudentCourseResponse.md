# WhatIfGradesApiResetForStudentCourseResponse

Object response with `grades` (from the Canvas `@returns`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grades** | [**List[Grades]**](Grades.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.what_if_grades_api_reset_for_student_course_response import WhatIfGradesApiResetForStudentCourseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WhatIfGradesApiResetForStudentCourseResponse from a JSON string
what_if_grades_api_reset_for_student_course_response_instance = WhatIfGradesApiResetForStudentCourseResponse.from_json(json)
# print the JSON string representation of the object
print(WhatIfGradesApiResetForStudentCourseResponse.to_json())

# convert the object into a dict
what_if_grades_api_reset_for_student_course_response_dict = what_if_grades_api_reset_for_student_course_response_instance.to_dict()
# create an instance of WhatIfGradesApiResetForStudentCourseResponse from a dict
what_if_grades_api_reset_for_student_course_response_from_dict = WhatIfGradesApiResetForStudentCourseResponse.from_dict(what_if_grades_api_reset_for_student_course_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


