# BookmarksCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the bookmark | [optional] 
**url** | **str** | The url of the bookmark | [optional] 
**position** | **int** | The position of the bookmark. Defaults to the bottom. | [optional] 
**data** | **str** | The data associated with the bookmark | [optional] 

## Example

```python
from canvas_lms_python_client.models.bookmarks_create_request import BookmarksCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BookmarksCreateRequest from a JSON string
bookmarks_create_request_instance = BookmarksCreateRequest.from_json(json)
# print the JSON string representation of the object
print(BookmarksCreateRequest.to_json())

# convert the object into a dict
bookmarks_create_request_dict = bookmarks_create_request_instance.to_dict()
# create an instance of BookmarksCreateRequest from a dict
bookmarks_create_request_from_dict = BookmarksCreateRequest.from_dict(bookmarks_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


