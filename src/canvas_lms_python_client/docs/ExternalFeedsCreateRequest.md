# ExternalFeedsCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The url to the external rss or atom feed | 
**header_match** | **bool** | If given, only feed entries that contain this string in their title will be imported | [optional] 
**verbosity** | **str** | Defaults to \&quot;full\&quot; | [optional] 

## Example

```python
from canvas_lms_python_client.models.external_feeds_create_request import ExternalFeedsCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalFeedsCreateRequest from a JSON string
external_feeds_create_request_instance = ExternalFeedsCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ExternalFeedsCreateRequest.to_json())

# convert the object into a dict
external_feeds_create_request_dict = external_feeds_create_request_instance.to_dict()
# create an instance of ExternalFeedsCreateRequest from a dict
external_feeds_create_request_from_dict = ExternalFeedsCreateRequest.from_dict(external_feeds_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


