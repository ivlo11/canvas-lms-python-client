# LockInfo



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_string** | **str** | Asset string for the object causing the lock | [optional] 
**unlock_at** | **datetime** | (Optional) Time at which this was/will be unlocked. Must be before the due date. | [optional] 
**lock_at** | **datetime** | (Optional) Time at which this was/will be locked. Must be after the due date. | [optional] 
**context_module** | [**LockInfoContextModule**](LockInfoContextModule.md) |  | [optional] 
**manually_locked** | **bool** |  | [optional] 
**can_view** | **bool** |  | [optional] 
**missing_permission** | **str** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.lock_info import LockInfo

# TODO update the JSON string below
json = "{}"
# create an instance of LockInfo from a JSON string
lock_info_instance = LockInfo.from_json(json)
# print the JSON string representation of the object
print(LockInfo.to_json())

# convert the object into a dict
lock_info_dict = lock_info_instance.to_dict()
# create an instance of LockInfo from a dict
lock_info_from_dict = LockInfo.from_dict(lock_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


