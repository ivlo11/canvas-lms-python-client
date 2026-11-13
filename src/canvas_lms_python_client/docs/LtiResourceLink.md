# LtiResourceLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The Canvas identifier for the LTI Resource Link. | [optional] 
**context_id** | **int** | The Canvas identifier for the context that the LTI Resource Link is associated with. | [optional] 
**context_type** | **str** | The type of the context that the LTI Resource Link is associated with. | [optional] 
**context_external_tool_id** | **int** | The Canvas identifier for the LTI 1.3 External Tool that the LTI Resource Link was originally installed from. Note that this tool may have been deleted or reinstalled and may not be the tool that would be launched for this url. | [optional] 
**resource_type** | **str** | The type of Canvas content for the resource link. Included for convenience. | [optional] 
**canvas_launch_url** | **str** | The Canvas URL that launches the LTI Resource Link. Suitable for use in Canvas rich content | [optional] 
**resource_link_uuid** | **str** | The LTI identifier for the LTI Resource Link, included as the resource_link_id when this link is launched | [optional] 
**lookup_uuid** | **str** | A unique identifier for the LTI Resource Link, present in the rich content representation. Remains the same across content migration. | [optional] 
**title** | **str** | The title of the LTI Resource Link. Usually tool-provided, or matches the assignment name | [optional] 
**url** | **str** | The tool URL to which the LTI Resource Link will launch | [optional] 
**lti_1_1_id** | **str** | The LTI 1.1 identifier for the LTI Resource Link, included in lti1p1 migration claim when launched. Only present if tool was migrated from 1.1 to 1.3. | [optional] 
**created_at** | **str** | Timestamp of the resource link&#39;s creation | [optional] 
**updated_at** | **str** | Timestamp of the resource link&#39;s last update | [optional] 
**workflow_state** | **str** | The state of the resource link | [optional] 
**associated_content_type** | **str** | Type of the associated content this resource link belongs to if present. Now only supports &#x60;ModuleItems&#x60;, later may be extend others | [optional] 
**associated_content_id** | **int** | The Canvas identifier of the associated content, e.g. ModuleItem related to this link. Present if associated_content_type is present | [optional] 
**custom** | **object** |  | [optional] 
**root_account_id** | **int** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.lti_resource_link import LtiResourceLink

# TODO update the JSON string below
json = "{}"
# create an instance of LtiResourceLink from a JSON string
lti_resource_link_instance = LtiResourceLink.from_json(json)
# print the JSON string representation of the object
print(LtiResourceLink.to_json())

# convert the object into a dict
lti_resource_link_dict = lti_resource_link_instance.to_dict()
# create an instance of LtiResourceLink from a dict
lti_resource_link_from_dict = LtiResourceLink.from_dict(lti_resource_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


