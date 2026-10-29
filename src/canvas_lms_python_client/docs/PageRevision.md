# PageRevision



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**revision_id** | **int** | an identifier for this revision of the page | [optional] 
**updated_at** | **datetime** | the time when this revision was saved | [optional] 
**latest** | **bool** | whether this is the latest revision or not | [optional] 
**edited_by** | [**User**](User.md) |  | [optional] 
**url** | **str** | the following fields are not included in the index action and may be omitted from the show action via summary&#x3D;1 the historic url of the page | [optional] 
**title** | **str** | the historic page title | [optional] 
**body** | **str** | the historic page contents | [optional] 

## Example

```python
from canvas_lms_python_client.models.page_revision import PageRevision

# TODO update the JSON string below
json = "{}"
# create an instance of PageRevision from a JSON string
page_revision_instance = PageRevision.from_json(json)
# print the JSON string representation of the object
print(PageRevision.to_json())

# convert the object into a dict
page_revision_dict = page_revision_instance.to_dict()
# create an instance of PageRevision from a dict
page_revision_from_dict = PageRevision.from_dict(page_revision_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


