# LtiSubscriptionsCreateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**root_account_id** | **str** |  | [optional] 
**foo** | **str** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.lti_subscriptions_create_response import LtiSubscriptionsCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LtiSubscriptionsCreateResponse from a JSON string
lti_subscriptions_create_response_instance = LtiSubscriptionsCreateResponse.from_json(json)
# print the JSON string representation of the object
print(LtiSubscriptionsCreateResponse.to_json())

# convert the object into a dict
lti_subscriptions_create_response_dict = lti_subscriptions_create_response_instance.to_dict()
# create an instance of LtiSubscriptionsCreateResponse from a dict
lti_subscriptions_create_response_from_dict = LtiSubscriptionsCreateResponse.from_dict(lti_subscriptions_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


