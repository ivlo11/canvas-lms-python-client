# PeerReviewSubmissionComments

The submission comments associated with this Peer Review if the submission_comment include parameter is provided (see submissions API) (optional)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from canvas_lms_python_client.models.peer_review_submission_comments import PeerReviewSubmissionComments

# TODO update the JSON string below
json = "{}"
# create an instance of PeerReviewSubmissionComments from a JSON string
peer_review_submission_comments_instance = PeerReviewSubmissionComments.from_json(json)
# print the JSON string representation of the object
print(PeerReviewSubmissionComments.to_json())

# convert the object into a dict
peer_review_submission_comments_dict = peer_review_submission_comments_instance.to_dict()
# create an instance of PeerReviewSubmissionComments from a dict
peer_review_submission_comments_from_dict = PeerReviewSubmissionComments.from_dict(peer_review_submission_comments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


