# Bookmark



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**position** | **int** |  | [optional] 
**data** | **object** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.bookmark import Bookmark

# TODO update the JSON string below
json = "{}"
# create an instance of Bookmark from a JSON string
bookmark_instance = Bookmark.from_json(json)
# print the JSON string representation of the object
print(Bookmark.to_json())

# convert the object into a dict
bookmark_dict = bookmark_instance.to_dict()
# create an instance of Bookmark from a dict
bookmark_from_dict = Bookmark.from_dict(bookmark_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


