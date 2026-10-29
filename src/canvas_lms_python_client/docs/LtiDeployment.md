# LtiDeployment

A deployment of an LTI tool in Canvas

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | the Canvas ID of the Lti_Deployment object | [optional] 
**registration_id** | **int** | the Canvas ID of the associated Lti_Registration object | [optional] 
**deployment_id** | **str** | The Deployment ID of this deployment which is shared with launched tools | [optional] 
**context_id** | **int** | The Canvas ID of the context this deployment is associated with | [optional] 
**context_type** | **str** | The type of context this deployment is associated with | [optional] 
**context_name** | **str** | The name of the context this deployment is associated with | [optional] 
**workflow_state** | **str** | The workflow state of the deployment | [optional] 
**context_controls** | [**List[LtiContextControl]**](LtiContextControl.md) | The context controls for this deployment. Only present in the LTI Context Controls - List All Context Controls endpoint. | [optional] 

## Example

```python
from canvas_lms_python_client.models.lti_deployment import LtiDeployment

# TODO update the JSON string below
json = "{}"
# create an instance of LtiDeployment from a JSON string
lti_deployment_instance = LtiDeployment.from_json(json)
# print the JSON string representation of the object
print(LtiDeployment.to_json())

# convert the object into a dict
lti_deployment_dict = lti_deployment_instance.to_dict()
# create an instance of LtiDeployment from a dict
lti_deployment_from_dict = LtiDeployment.from_dict(lti_deployment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


