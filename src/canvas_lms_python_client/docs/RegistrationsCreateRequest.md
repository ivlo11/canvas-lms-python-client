# RegistrationsCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the tool. If one isn&#39;t provided, it will be inferred from the configuration&#39;s title. | [optional] 
**admin_nickname** | **str** | A friendly nickname set by admins to override the tool name | [optional] 
**vendor** | **str** | The vendor of the tool | [optional] 
**description** | **str** | A description of the tool. Cannot exceed 2048 bytes. | [optional] 
**configuration** | **str** | The LTI 1.3 configuration for the tool | 
**unified_tool_id** | **str** | The unique identifier for the tool, used for analytics. If not provided, one will be generated. | [optional] 
**lock_deploying** | **bool** | When true, no new deployments of this registration can be created. | [optional] 
**workflow_state** | **str** | \&quot;on\&quot;/\&quot;off\&quot;/\&quot;allow\&quot; set the account binding state directly (binding vocabulary). \&quot;active\&quot;/\&quot;inactive\&quot; set the registration state directly (registration vocabulary). All five values update both the binding and the registration to equivalent states. \&quot;allow\&quot; is only valid for Site Admin registrations. Defaults to \&quot;off\&quot;. | [optional] 
**overlay** | [**RegistrationsCreateRequestOverlay**](RegistrationsCreateRequestOverlay.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.registrations_create_request import RegistrationsCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RegistrationsCreateRequest from a JSON string
registrations_create_request_instance = RegistrationsCreateRequest.from_json(json)
# print the JSON string representation of the object
print(RegistrationsCreateRequest.to_json())

# convert the object into a dict
registrations_create_request_dict = registrations_create_request_instance.to_dict()
# create an instance of RegistrationsCreateRequest from a dict
registrations_create_request_from_dict = RegistrationsCreateRequest.from_dict(registrations_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


