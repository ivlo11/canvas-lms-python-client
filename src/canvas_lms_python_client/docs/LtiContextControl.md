# LtiContextControl

Represent availability of an LTI registration in a specific context

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | the Canvas ID of the Lti_ContextControl object | [optional] 
**course_id** | **int** | the Canvas ID of the Course that owns this. one of this or account_id will always be present | [optional] 
**account_id** | **int** | the Canvas ID of the Account that owns this. one of this or course_id will always be present | [optional] 
**deployment_id** | **int** | the Canvas ID of the ContextExternalTool that owns this, representing an LTI deployment | [optional] 
**available** | **bool** | The state of this tool in this context. &#x60;true&#x60; means the tool is available in this context and in all contexts below it. | [optional] 
**path** | **str** | A representation of the account hierarchy for the context that owns this object. Used for checking availability during LTI operations. | [optional] 
**display_path** | **List[str]** | For UI display. Names of the accounts in the context&#39;s hierarchy. Excludes the root, and the current account if context is an account. | [optional] 
**context_name** | **str** | For UI display. The name of the context this object is associated with | [optional] 
**depth** | **int** | For UI display. The depth of ContextControls for this particular deployment account chain, which can be different from the number of accounts in the chain. | [optional] 
**course_count** | **int** | For UI display. The number of courses in this account and all nested subaccounts. 0 when context is a Course. | [optional] 
**child_control_count** | **int** | For UI display. The number of controls for accounts below this one, including all nested subaccounts. 0 when context is a Course. | [optional] 
**subaccount_count** | **int** | For UI display. The number of subaccounts for this account. Includes all nested subaccounts. 0 when context is a Course. | [optional] 
**workflow_state** | **str** | The state of the object | [optional] 
**created_at** | **str** | Timestamp of the object&#39;s creation | [optional] 
**updated_at** | **str** | Timestamp of the object&#39;s last update | [optional] 
**created_by** | [**User**](User.md) |  | [optional] 
**updated_by** | [**User**](User.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.lti_context_control import LtiContextControl

# TODO update the JSON string below
json = "{}"
# create an instance of LtiContextControl from a JSON string
lti_context_control_instance = LtiContextControl.from_json(json)
# print the JSON string representation of the object
print(LtiContextControl.to_json())

# convert the object into a dict
lti_context_control_dict = lti_context_control_instance.to_dict()
# create an instance of LtiContextControl from a dict
lti_context_control_from_dict = LtiContextControl.from_dict(lti_context_control_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


