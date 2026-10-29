# Progress



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | the ID of the Progress object | [optional] 
**context_id** | **int** | the context owning the job. | [optional] 
**context_type** | **str** |  | [optional] 
**user_id** | **int** | the id of the user who started the job | [optional] 
**tag** | **str** | the type of operation | [optional] 
**completion** | **int** | percent completed | [optional] 
**workflow_state** | **str** | the state of the job one of &#39;queued&#39;, &#39;running&#39;, &#39;completed&#39;, &#39;failed&#39; | [optional] 
**created_at** | **datetime** | the time the job was created | [optional] 
**updated_at** | **datetime** | the time the job was last updated | [optional] 
**message** | **str** | optional details about the job | [optional] 
**results** | **object** | optional results of the job. omitted when job is still pending | [optional] 
**url** | **str** | url where a progress update can be retrieved | [optional] 

## Example

```python
from canvas_lms_python_client.models.progress import Progress

# TODO update the JSON string below
json = "{}"
# create an instance of Progress from a JSON string
progress_instance = Progress.from_json(json)
# print the JSON string representation of the object
print(Progress.to_json())

# convert the object into a dict
progress_dict = progress_instance.to_dict()
# create an instance of Progress from a dict
progress_from_dict = Progress.from_dict(progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


