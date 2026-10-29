# NamesAndRoleMessage

Additional attributes which would appear in the LTI launch message were this member to click the specified resource link (`rlid` query parameter)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**https___purl_imsglobal_org_spec_lti_claim_message_type** | **str** | The type of LTI message being described. Always set to &#39;LtiResourceLinkRequest&#39; | [optional] 
**locale** | **str** | The member&#39;s preferred locale | [optional] 
**https___www_instructure_com_canvas_user_id** | **int** | The member&#39;s API ID | [optional] 
**https___www_instructure_com_canvas_user_login_id** | **str** | The member&#39;s primary login username | [optional] 
**https___purl_imsglobal_org_spec_lti_claim_custom** | **object** | Expanded LTI custom parameters that pertain to the member (as opposed to the Context) | [optional] 

## Example

```python
from canvas_lms_python_client.models.names_and_role_message import NamesAndRoleMessage

# TODO update the JSON string below
json = "{}"
# create an instance of NamesAndRoleMessage from a JSON string
names_and_role_message_instance = NamesAndRoleMessage.from_json(json)
# print the JSON string representation of the object
print(NamesAndRoleMessage.to_json())

# convert the object into a dict
names_and_role_message_dict = names_and_role_message_instance.to_dict()
# create an instance of NamesAndRoleMessage from a dict
names_and_role_message_from_dict = NamesAndRoleMessage.from_dict(names_and_role_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


