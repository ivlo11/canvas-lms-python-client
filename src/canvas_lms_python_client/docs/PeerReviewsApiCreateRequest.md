# PeerReviewsApiCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | user_id to assign as reviewer on this assignment | 

## Example

```python
from canvas_lms_python_client.models.peer_reviews_api_create_request import PeerReviewsApiCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PeerReviewsApiCreateRequest from a JSON string
peer_reviews_api_create_request_instance = PeerReviewsApiCreateRequest.from_json(json)
# print the JSON string representation of the object
print(PeerReviewsApiCreateRequest.to_json())

# convert the object into a dict
peer_reviews_api_create_request_dict = peer_reviews_api_create_request_instance.to_dict()
# create an instance of PeerReviewsApiCreateRequest from a dict
peer_reviews_api_create_request_from_dict = PeerReviewsApiCreateRequest.from_dict(peer_reviews_api_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


