# PeerReviewAssessor

The User object for the assessor if the user include parameter is provided (see user API) (optional)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from canvas_lms_python_client.models.peer_review_assessor import PeerReviewAssessor

# TODO update the JSON string below
json = "{}"
# create an instance of PeerReviewAssessor from a JSON string
peer_review_assessor_instance = PeerReviewAssessor.from_json(json)
# print the JSON string representation of the object
print(PeerReviewAssessor.to_json())

# convert the object into a dict
peer_review_assessor_dict = peer_review_assessor_instance.to_dict()
# create an instance of PeerReviewAssessor from a dict
peer_review_assessor_from_dict = PeerReviewAssessor.from_dict(peer_review_assessor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


