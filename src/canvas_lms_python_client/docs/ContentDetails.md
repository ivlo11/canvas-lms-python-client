# ContentDetails



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**points_possible** | **int** |  | [optional] 
**due_at** | **datetime** |  | [optional] 
**unlock_at** | **datetime** |  | [optional] 
**lock_at** | **datetime** |  | [optional] 
**locked_for_user** | **bool** |  | [optional] 
**lock_explanation** | **str** |  | [optional] 
**lock_info** | [**LockInfo**](LockInfo.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.content_details import ContentDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ContentDetails from a JSON string
content_details_instance = ContentDetails.from_json(json)
# print the JSON string representation of the object
print(ContentDetails.to_json())

# convert the object into a dict
content_details_dict = content_details_instance.to_dict()
# create an instance of ContentDetails from a dict
content_details_from_dict = ContentDetails.from_dict(content_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


