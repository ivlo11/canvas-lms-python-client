# LtiOverlayVersion

A single version of a tool's configuration overlay

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**root_account_id** | **int** | The Canvas id of the root account | [optional] 
**created_at** | **str** | Timestamp of the version&#39;s creation | [optional] 
**updated_at** | **str** | Timestamp of the version&#39;s last update | [optional] 
**caused_by_reset** | **bool** | Whether or not this change was caused by a reset of the tool&#39;s configuration | [optional] 
**created_by** | [**LtiRegistrationCreatedBy**](LtiRegistrationCreatedBy.md) |  | [optional] 
**diff** | **List[List[object]]** | A list of changes made in this version compared to the previous version | [optional] 
**lti_overlay_id** | **int** | The id of the overlay this version is for | [optional] 
**account_id** | **int** | The id of the account this version is for | [optional] 

## Example

```python
from canvas_lms_python_client.models.lti_overlay_version import LtiOverlayVersion

# TODO update the JSON string below
json = "{}"
# create an instance of LtiOverlayVersion from a JSON string
lti_overlay_version_instance = LtiOverlayVersion.from_json(json)
# print the JSON string representation of the object
print(LtiOverlayVersion.to_json())

# convert the object into a dict
lti_overlay_version_dict = lti_overlay_version_instance.to_dict()
# create an instance of LtiOverlayVersion from a dict
lti_overlay_version_from_dict = LtiOverlayVersion.from_dict(lti_overlay_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


