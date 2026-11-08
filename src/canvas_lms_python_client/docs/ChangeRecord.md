# ChangeRecord

Describes a learning object change propagated to associated courses from a blueprint course

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **int** | The ID of the learning object that was changed in the blueprint course. | [optional] 
**asset_type** | **str** | The type of the learning object that was changed in the blueprint course.  One of &#39;assignment&#39;, &#39;attachment&#39;, &#39;discussion_topic&#39;, &#39;external_tool&#39;, &#39;quiz&#39;, &#39;wiki_page&#39;, &#39;syllabus&#39;, or &#39;settings&#39;.  For &#39;syllabus&#39; or &#39;settings&#39;, the asset_id is the course id. | [optional] 
**asset_name** | **str** | The name of the learning object that was changed in the blueprint course. | [optional] 
**change_type** | **str** | The type of change; one of &#39;created&#39;, &#39;updated&#39;, &#39;deleted&#39; | [optional] 
**html_url** | **str** | The URL of the changed object | [optional] 
**locked** | **bool** | Whether the object is locked in the blueprint | [optional] 
**exceptions** | **List[object]** | A list of ExceptionRecords for linked courses that did not receive this update. | [optional] 
**locale** | **str** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.change_record import ChangeRecord

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeRecord from a JSON string
change_record_instance = ChangeRecord.from_json(json)
# print the JSON string representation of the object
print(ChangeRecord.to_json())

# convert the object into a dict
change_record_dict = change_record_instance.to_dict()
# create an instance of ChangeRecord from a dict
change_record_from_dict = ChangeRecord.from_dict(change_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


