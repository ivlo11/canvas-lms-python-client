# GroupCategoriesImportTagsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachment** | **str** | There are two ways to post differentiation tag import data - either via a multipart/form-data form-field-style attachment, or via a non-multipart raw post request.  &#39;attachment&#39; is required for multipart/form-data style posts. Assumed to be tag data from a file upload form field named &#39;attachment&#39;.  Examples:   curl -F attachment&#x3D;@&lt;filename&gt; -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; \\       &#39;https://&lt;canvas&gt;/api/v1/group_categories/import_tags&#39;  If you decide to do a raw post, you can skip the &#39;attachment&#39; argument, but you will then be required to provide a suitable Content-Type header. You are encouraged to also provide the &#39;extension&#39; argument.  Examples:   curl -H &#39;Content-Type: text/csv&#39; --data-binary @&lt;filename&gt;.csv \\       -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; \\       &#39;https://&lt;canvas&gt;/api/v1/group_categories_tags&#39; | [optional] 

## Example

```python
from canvas_lms_python_client.models.group_categories_import_tags_request import GroupCategoriesImportTagsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GroupCategoriesImportTagsRequest from a JSON string
group_categories_import_tags_request_instance = GroupCategoriesImportTagsRequest.from_json(json)
# print the JSON string representation of the object
print(GroupCategoriesImportTagsRequest.to_json())

# convert the object into a dict
group_categories_import_tags_request_dict = group_categories_import_tags_request_instance.to_dict()
# create an instance of GroupCategoriesImportTagsRequest from a dict
group_categories_import_tags_request_from_dict = GroupCategoriesImportTagsRequest.from_dict(group_categories_import_tags_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


