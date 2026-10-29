# ContextSearchResponse

The response for the Search Accounts and Courses API endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | [**List[SearchableAccount]**](SearchableAccount.md) | Accounts that match the search query. Limited to 100. | [optional] 
**courses** | [**List[SearchableCourse]**](SearchableCourse.md) | Courses that match the search query. Limited to 100. | [optional] 

## Example

```python
from canvas_lms_python_client.models.context_search_response import ContextSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContextSearchResponse from a JSON string
context_search_response_instance = ContextSearchResponse.from_json(json)
# print the JSON string representation of the object
print(ContextSearchResponse.to_json())

# convert the object into a dict
context_search_response_dict = context_search_response_instance.to_dict()
# create an instance of ContextSearchResponse from a dict
context_search_response_from_dict = ContextSearchResponse.from_dict(context_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


