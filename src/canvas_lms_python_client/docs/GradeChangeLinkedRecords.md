# GradeChangeLinkedRecords

The records referenced by the events on a page of grade change events

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_views** | [**List[PageView]**](PageView.md) | The page views during the events | [optional] 
**assignments** | [**List[Assignment]**](Assignment.md) | The assignments associated with the events | [optional] 
**courses** | [**List[Course]**](Course.md) | The courses associated with the events | [optional] 
**users** | [**List[User]**](User.md) | The students and graders associated with the events | [optional] 

## Example

```python
from canvas_lms_python_client.models.grade_change_linked_records import GradeChangeLinkedRecords

# TODO update the JSON string below
json = "{}"
# create an instance of GradeChangeLinkedRecords from a JSON string
grade_change_linked_records_instance = GradeChangeLinkedRecords.from_json(json)
# print the JSON string representation of the object
print(GradeChangeLinkedRecords.to_json())

# convert the object into a dict
grade_change_linked_records_dict = grade_change_linked_records_instance.to_dict()
# create an instance of GradeChangeLinkedRecords from a dict
grade_change_linked_records_from_dict = GradeChangeLinkedRecords.from_dict(grade_change_linked_records_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


