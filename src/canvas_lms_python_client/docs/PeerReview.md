# PeerReview



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assessor_id** | **int** | The assessors user id | [optional] 
**asset_id** | **int** | The id for the asset associated with this Peer Review | [optional] 
**asset_type** | **str** | The type of the asset | [optional] 
**id** | **int** | The id of the Peer Review | [optional] 
**user_id** | **int** | The user id for the owner of the asset | [optional] 
**workflow_state** | **str** | The state of the Peer Review, either &#39;assigned&#39; or &#39;completed&#39; | [optional] 
**user** | **str** | the User object for the owner of the asset if the user include parameter is provided (see user API) (optional) | [optional] 
**assessor** | **str** | The User object for the assessor if the user include parameter is provided (see user API) (optional) | [optional] 
**submission_comments** | **str** | The submission comments associated with this Peer Review if the submission_comment include parameter is provided (see submissions API) (optional) | [optional] 

## Example

```python
from canvas_lms_python_client.models.peer_review import PeerReview

# TODO update the JSON string below
json = "{}"
# create an instance of PeerReview from a JSON string
peer_review_instance = PeerReview.from_json(json)
# print the JSON string representation of the object
print(PeerReview.to_json())

# convert the object into a dict
peer_review_dict = peer_review_instance.to_dict()
# create an instance of PeerReview from a dict
peer_review_from_dict = PeerReview.from_dict(peer_review_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


