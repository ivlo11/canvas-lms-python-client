# BlueprintSubscription

Associates a course with a blueprint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the blueprint course subscription | [optional] 
**template_id** | **int** | The ID of the blueprint template the associated course is subscribed to | [optional] 
**blueprint_course** | **object** | The blueprint course subscribed to | [optional] 

## Example

```python
from canvas_lms_python_client.models.blueprint_subscription import BlueprintSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of BlueprintSubscription from a JSON string
blueprint_subscription_instance = BlueprintSubscription.from_json(json)
# print the JSON string representation of the object
print(BlueprintSubscription.to_json())

# convert the object into a dict
blueprint_subscription_dict = blueprint_subscription_instance.to_dict()
# create an instance of BlueprintSubscription from a dict
blueprint_subscription_from_dict = BlueprintSubscription.from_dict(blueprint_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


