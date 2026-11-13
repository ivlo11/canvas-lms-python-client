# QuizPermissions

Permissions the user has for the quiz

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**read** | **bool** | whether the user can view the quiz | [optional] 
**submit** | **bool** | whether the user may submit a submission for the quiz | [optional] 
**create** | **bool** | whether the user may create a new quiz | [optional] 
**manage** | **bool** | whether the user may edit, update, or delete the quiz | [optional] 
**read_statistics** | **bool** | whether the user may view quiz statistics for this quiz | [optional] 
**review_grades** | **bool** | whether the user may review grades for all quiz submissions for this quiz | [optional] 
**update** | **bool** | whether the user may update the quiz | [optional] 
**delete** | **bool** |  | [optional] 
**grade** | **bool** |  | [optional] 
**manage_assign_to** | **bool** |  | [optional] 
**preview** | **bool** |  | [optional] 
**view_answer_audits** | **bool** |  | [optional] 
**attach_submission_comment_files** | **bool** |  | [optional] 
**manage_files_add** | **bool** |  | [optional] 
**manage_files_delete** | **bool** |  | [optional] 
**manage_files_edit** | **bool** |  | [optional] 
**read_own_submission** | **bool** |  | [optional] 
**set_grading_scheme** | **bool** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.quiz_permissions import QuizPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of QuizPermissions from a JSON string
quiz_permissions_instance = QuizPermissions.from_json(json)
# print the JSON string representation of the object
print(QuizPermissions.to_json())

# convert the object into a dict
quiz_permissions_dict = quiz_permissions_instance.to_dict()
# create an instance of QuizPermissions from a dict
quiz_permissions_from_dict = QuizPermissions.from_dict(quiz_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


