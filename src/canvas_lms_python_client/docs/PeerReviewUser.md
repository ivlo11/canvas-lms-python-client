# PeerReviewUser

the User object for the owner of the asset if the user include parameter is provided (see user API) (optional)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from canvas_lms_python_client.models.peer_review_user import PeerReviewUser

# TODO update the JSON string below
json = "{}"
# create an instance of PeerReviewUser from a JSON string
peer_review_user_instance = PeerReviewUser.from_json(json)
# print the JSON string representation of the object
print(PeerReviewUser.to_json())

# convert the object into a dict
peer_review_user_dict = peer_review_user_instance.to_dict()
# create an instance of PeerReviewUser from a dict
peer_review_user_from_dict = PeerReviewUser.from_dict(peer_review_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


