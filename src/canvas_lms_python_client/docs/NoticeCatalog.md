# NoticeCatalog

Set of notice handlers (one per notice type) for an LTI tool deployment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | The LTI tool&#39;s client ID (global developer key ID) | [optional] 
**deployment_id** | **str** | String that identifies the Platform-Tool integration governing the notices | [optional] 
**notice_handlers** | [**List[NoticeHandler]**](NoticeHandler.md) | List of notice handlers for the tool | [optional] 

## Example

```python
from canvas_lms_python_client.models.notice_catalog import NoticeCatalog

# TODO update the JSON string below
json = "{}"
# create an instance of NoticeCatalog from a JSON string
notice_catalog_instance = NoticeCatalog.from_json(json)
# print the JSON string representation of the object
print(NoticeCatalog.to_json())

# convert the object into a dict
notice_catalog_dict = notice_catalog_instance.to_dict()
# create an instance of NoticeCatalog from a dict
notice_catalog_from_dict = NoticeCatalog.from_dict(notice_catalog_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


