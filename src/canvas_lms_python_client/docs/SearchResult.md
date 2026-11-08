# SearchResult

Reference to an object that matches a smart search

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_id** | **int** | The ID of the matching object. | [optional] 
**content_type** | **str** | The type of the matching object. | [optional] 
**title** | **str** | The title of the matching object. | [optional] 
**body** | **str** | The body of the matching object. | [optional] 
**html_url** | **str** | The Canvas URL of the matching object. | [optional] 
**distance** | **float** | The distance between the search query and the result. Smaller numbers indicate closer matches. | [optional] 
**due_date** | **str** |  | [optional] 
**modules** | **List[object]** |  | [optional] 
**published** | **bool** |  | [optional] 
**readable_type** | **str** |  | [optional] 
**relevance** | **int** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.search_result import SearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResult from a JSON string
search_result_instance = SearchResult.from_json(json)
# print the JSON string representation of the object
print(SearchResult.to_json())

# convert the object into a dict
search_result_dict = search_result_instance.to_dict()
# create an instance of SearchResult from a dict
search_result_from_dict = SearchResult.from_dict(search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


