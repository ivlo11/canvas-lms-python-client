# ContextExternalTool

An external tool configured for a specific context

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for the external tool | [optional] 
**name** | **str** | The name of the external tool | [optional] 
**description** | **str** | A description of the external tool | [optional] 
**url** | **str** | The launch URL for the external tool | [optional] 
**domain** | **str** | The domain to match links against. Note that this doesn&#39;t contain the protocol. | [optional] 
**consumer_key** | **str** | The consumer key used by the tool (The associated shared secret is not returned) | [optional] 
**created_at** | **str** | Timestamp of the tool&#39;s creation | [optional] 
**updated_at** | **str** | Timestamp of the tool&#39;s last update | [optional] 
**privacy_level** | **str** | How much user information to send to the external tool | [optional] 
**custom_fields** | **object** | Custom fields that will be sent to the tool consumer | [optional] 
**workflow_state** | **str** | The current state of the external tool | [optional] 
**is_rce_favorite** | **bool** | Boolean determining whether this tool should be in a preferred location in the RCE. Only present if the tool can be an RCE favorite. | [optional] 
**is_top_nav_favorite** | **bool** | Boolean determining whether this tool should have a dedicated button in Top Navigation. Only present if the tool can be a top nav favorite. | [optional] 
**selection_width** | **int** | The pixel width of the iFrame that the tool will be rendered in | [optional] 
**selection_height** | **int** | The pixel height of the iFrame that the tool will be rendered in | [optional] 
**icon_url** | **str** | The URL for the tool icon | [optional] 
**not_selectable** | **bool** | Whether the tool is not selectable from assignment and modules | [optional] 
**version** | **str** | The LTI version of the tool | [optional] 
**unified_tool_id** | **str** | The unique identifier for the tool in LearnPlatform | [optional] 
**developer_key_id** | **int** | The developer key id associated with this tool. Only present for LTI 1.3 tools. | [optional] 
**lti_registration_id** | **int** | The LTI registration id associated with this tool. Only present for LTI 1.3 tools. | [optional] 
**deployment_id** | **str** | The unique identifier for the deployment of the tool | [optional] 
**allow_membership_service_access** | **bool** | Whether the tool can access the membership service. Only present if the feature is enabled. | [optional] 
**prefer_sis_email** | **bool** | Whether to send the SIS email address in launches | [optional] 
**estimated_duration** | [**EstimatedDuration**](EstimatedDuration.md) |  | [optional] 
**account_navigation** | [**ContextExternalToolPlacement**](ContextExternalToolPlacement.md) |  | [optional] 
**analytics_hub** | [**ContextExternalToolPlacement**](ContextExternalToolPlacement.md) |  | [optional] 
**assignment_edit** | [**ContextExternalToolPlacement**](ContextExternalToolPlacement.md) |  | [optional] 
**assignment_group_menu** | [**ContextExternalToolPlacement**](ContextExternalToolPlacement.md) |  | [optional] 
**assignment_index_menu** | [**ContextExternalToolPlacement**](ContextExternalToolPlacement.md) |  | [optional] 
**assignment_menu** | [**ContextExternalToolPlacement**](ContextExternalToolPlacement.md) |  | [optional] 
**assignment_selection** | [**ContextExternalToolPlacement**](ContextExternalToolPlacement.md) |  | [optional] 
**assignment_view** | [**ContextExternalToolPlacement**](ContextExternalToolPlacement.md) |  | [optional] 
**collaboration** | [**ContextExternalToolPlacement**](ContextExternalToolPlacement.md) |  | [optional] 
**conference_selection** | [**ContextExternalToolPlacement**](ContextExternalToolPlacement.md) |  | [optional] 
**course_assignments_menu** | [**ContextExternalToolPlacement**](ContextExternalToolPlacement.md) |  | [optional] 
**course_home_sub_navigation** | [**ContextExternalToolPlacement**](ContextExternalToolPlacement.md) |  | [optional] 
**course_navigation** | [**ContextExternalToolPlacement**](ContextExternalToolPlacement.md) |  | [optional] 
**course_settings_sub_navigation** | [**ContextExternalToolPlacement**](ContextExternalToolPlacement.md) |  | [optional] 
**discussion_topic_index_menu** | [**ContextExternalToolPlacement**](ContextExternalToolPlacement.md) |  | [optional] 
**discussion_topic_menu** | [**ContextExternalToolPlacement**](ContextExternalToolPlacement.md) |  | [optional] 
**editor_button** | [**ContextExternalToolPlacement**](ContextExternalToolPlacement.md) |  | [optional] 
**file_index_menu** | [**ContextExternalToolPlacement**](ContextExternalToolPlacement.md) |  | [optional] 
**file_menu** | [**ContextExternalToolPlacement**](ContextExternalToolPlacement.md) |  | [optional] 
**global_navigation** | [**ContextExternalToolPlacement**](ContextExternalToolPlacement.md) |  | [optional] 
**homework_submission** | [**ContextExternalToolPlacement**](ContextExternalToolPlacement.md) |  | [optional] 
**link_selection** | [**ContextExternalToolPlacement**](ContextExternalToolPlacement.md) |  | [optional] 
**migration_selection** | [**ContextExternalToolPlacement**](ContextExternalToolPlacement.md) |  | [optional] 
**module_group_menu** | [**ContextExternalToolPlacement**](ContextExternalToolPlacement.md) |  | [optional] 
**module_index_menu** | [**ContextExternalToolPlacement**](ContextExternalToolPlacement.md) |  | [optional] 
**module_index_menu_modal** | [**ContextExternalToolPlacement**](ContextExternalToolPlacement.md) |  | [optional] 
**module_menu_modal** | [**ContextExternalToolPlacement**](ContextExternalToolPlacement.md) |  | [optional] 
**module_menu** | [**ContextExternalToolPlacement**](ContextExternalToolPlacement.md) |  | [optional] 
**page_index_menu** | [**ContextExternalToolPlacement**](ContextExternalToolPlacement.md) |  | [optional] 
**page_menu** | [**ContextExternalToolPlacement**](ContextExternalToolPlacement.md) |  | [optional] 
**post_grades** | [**ContextExternalToolPlacement**](ContextExternalToolPlacement.md) |  | [optional] 
**quiz_index_menu** | [**ContextExternalToolPlacement**](ContextExternalToolPlacement.md) |  | [optional] 
**quiz_menu** | [**ContextExternalToolPlacement**](ContextExternalToolPlacement.md) |  | [optional] 
**resource_selection** | [**ContextExternalToolPlacement**](ContextExternalToolPlacement.md) |  | [optional] 
**similarity_detection** | [**ContextExternalToolPlacement**](ContextExternalToolPlacement.md) |  | [optional] 
**student_context_card** | [**ContextExternalToolPlacement**](ContextExternalToolPlacement.md) |  | [optional] 
**submission_type_selection** | [**ContextExternalToolPlacement**](ContextExternalToolPlacement.md) |  | [optional] 
**tool_configuration** | [**ContextExternalToolPlacement**](ContextExternalToolPlacement.md) |  | [optional] 
**top_navigation** | [**ContextExternalToolPlacement**](ContextExternalToolPlacement.md) |  | [optional] 
**user_navigation** | [**ContextExternalToolPlacement**](ContextExternalToolPlacement.md) |  | [optional] 
**wiki_index_menu** | [**ContextExternalToolPlacement**](ContextExternalToolPlacement.md) |  | [optional] 
**wiki_page_menu** | [**ContextExternalToolPlacement**](ContextExternalToolPlacement.md) |  | [optional] 
**activity_asset_processor** | [**ContextExternalToolPlacement**](ContextExternalToolPlacement.md) |  | [optional] 
**activity_asset_processor_contribution** | [**ContextExternalToolPlacement**](ContextExternalToolPlacement.md) |  | [optional] 
**message_settings** | [**List[ContextExternalToolMessageSettings]**](ContextExternalToolMessageSettings.md) | Configuration for placementless message types (currently only LtiEulaRequest). | [optional] 

## Example

```python
from canvas_lms_python_client.models.context_external_tool import ContextExternalTool

# TODO update the JSON string below
json = "{}"
# create an instance of ContextExternalTool from a JSON string
context_external_tool_instance = ContextExternalTool.from_json(json)
# print the JSON string representation of the object
print(ContextExternalTool.to_json())

# convert the object into a dict
context_external_tool_dict = context_external_tool_instance.to_dict()
# create an instance of ContextExternalTool from a dict
context_external_tool_from_dict = ContextExternalTool.from_dict(context_external_tool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


