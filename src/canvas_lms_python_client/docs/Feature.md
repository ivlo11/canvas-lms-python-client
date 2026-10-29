# Feature



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature** | **str** | The symbolic name of the feature, used in FeatureFlags | [optional] 
**display_name** | **str** | The user-visible name of the feature | [optional] 
**applies_to** | **str** | The type of object the feature applies to (RootAccount, Account, Course, or User):  * RootAccount features may only be controlled by flags on root accounts.  * Account features may be controlled by flags on accounts and their parent accounts.  * Course features may be controlled by flags on courses and their parent accounts.  * User features may be controlled by flags on users and site admin only. | [optional] 
**feature_flag** | [**FeatureFlag**](FeatureFlag.md) |  | [optional] 
**root_opt_in** | **bool** | If true, a feature that is &#39;allowed&#39; globally will be &#39;off&#39; by default in root accounts. Otherwise, root accounts inherit the global &#39;allowed&#39; setting, which allows sub-accounts and courses to turn features on with no root account action. | [optional] 
**beta** | **bool** | Whether the feature is a feature preview. If true, opting in includes ongoing updates outside the regular release schedule. | [optional] 
**early_access_program** | **bool** | Indicates the feature is part of the Early Access Program. | [optional] 
**autoexpand** | **bool** | Whether the details of the feature are autoexpanded on page load vs. the user clicking to expand. | [optional] 
**release_notes_url** | **str** | A URL to the release notes describing the feature | [optional] 

## Example

```python
from canvas_lms_python_client.models.feature import Feature

# TODO update the JSON string below
json = "{}"
# create an instance of Feature from a JSON string
feature_instance = Feature.from_json(json)
# print the JSON string representation of the object
print(Feature.to_json())

# convert the object into a dict
feature_dict = feature_instance.to_dict()
# create an instance of Feature from a dict
feature_from_dict = Feature.from_dict(feature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


