# NamesAndRoleMembership

A member of a LTI Context in one or more roles

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Membership state | [optional] 
**name** | **str** | Member&#39;s full name. Only included if tool privacy level is &#x60;public&#x60; or &#x60;name_only&#x60;. | [optional] 
**picture** | **str** | URL to the member&#39;s avatar. Only included if tool privacy level is &#x60;public&#x60;. | [optional] 
**given_name** | **str** | Member&#39;s &#39;first&#39; name. Only included if tool privacy level is &#x60;public&#x60; or &#x60;name_only&#x60;. | [optional] 
**family_name** | **str** | Member&#39;s &#39;last&#39; name. Only included if tool privacy level is &#x60;public&#x60; or &#x60;name_only&#x60;. | [optional] 
**email** | **str** | Member&#39;s email address. Only included if tool privacy level is &#x60;public&#x60; or &#x60;email_only&#x60;. | [optional] 
**lis_person_sourcedid** | **str** | Member&#39;s primary SIS identifier. Only included if tool privacy level is &#x60;public&#x60; or &#x60;name_only&#x60;. | [optional] 
**user_id** | **str** | Member&#39;s unique LTI identifier. | [optional] 
**roles** | **List[str]** | Member&#39;s roles in the current Context, expressed as LTI/LIS URNs. | [optional] 
**message** | [**List[NamesAndRoleMessage]**](NamesAndRoleMessage.md) | Only present when the request specifies a &#x60;rlid&#x60; query parameter. Contains additional attributes which would appear in the LTI launch message were this member to click the link referenced by the &#x60;rlid&#x60; query parameter | [optional] 

## Example

```python
from canvas_lms_python_client.models.names_and_role_membership import NamesAndRoleMembership

# TODO update the JSON string below
json = "{}"
# create an instance of NamesAndRoleMembership from a JSON string
names_and_role_membership_instance = NamesAndRoleMembership.from_json(json)
# print the JSON string representation of the object
print(NamesAndRoleMembership.to_json())

# convert the object into a dict
names_and_role_membership_dict = names_and_role_membership_instance.to_dict()
# create an instance of NamesAndRoleMembership from a dict
names_and_role_membership_from_dict = NamesAndRoleMembership.from_dict(names_and_role_membership_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


