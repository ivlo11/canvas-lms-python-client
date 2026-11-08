# EpubExportsIndexResponse

Object response with `courses` (from the Canvas `@returns`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**courses** | [**List[CourseEpubExport]**](CourseEpubExport.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.epub_exports_index_response import EpubExportsIndexResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EpubExportsIndexResponse from a JSON string
epub_exports_index_response_instance = EpubExportsIndexResponse.from_json(json)
# print the JSON string representation of the object
print(EpubExportsIndexResponse.to_json())

# convert the object into a dict
epub_exports_index_response_dict = epub_exports_index_response_instance.to_dict()
# create an instance of EpubExportsIndexResponse from a dict
epub_exports_index_response_from_dict = EpubExportsIndexResponse.from_dict(epub_exports_index_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


