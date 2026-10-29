# ExternalFeed



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the feed | [optional] 
**display_name** | **str** | The title of the feed, pulled from the feed itself. If the feed hasn&#39;t yet been pulled, a temporary name will be synthesized based on the URL | [optional] 
**url** | **str** | The HTTP/HTTPS URL to the feed | [optional] 
**header_match** | **str** | If not null, only feed entries whose title contains this string will trigger new posts in Canvas | [optional] 
**created_at** | **datetime** | When this external feed was added to Canvas | [optional] 
**verbosity** | **str** | The verbosity setting determines how much of the feed&#39;s content is imported into Canvas as part of the posting. &#39;link_only&#39; means that only the title and a link to the item. &#39;truncate&#39; means that a summary of the first portion of the item body will be used. &#39;full&#39; means that the full item body will be used. | [optional] 

## Example

```python
from canvas_lms_python_client.models.external_feed import ExternalFeed

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalFeed from a JSON string
external_feed_instance = ExternalFeed.from_json(json)
# print the JSON string representation of the object
print(ExternalFeed.to_json())

# convert the object into a dict
external_feed_dict = external_feed_instance.to_dict()
# create an instance of ExternalFeed from a dict
external_feed_from_dict = ExternalFeed.from_dict(external_feed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


