# RecordAlreadyExistsCreateRequestLatePolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**missing_submission_deduction_enabled** | **bool** | [Boolean] Whether to enable the missing submission deduction late policy. | [optional] 
**missing_submission_deduction** | **float** | [Number] How many percentage points to deduct from a missing submission. | [optional] 
**late_submission_deduction_enabled** | **bool** | [Boolean] Whether to enable the late submission deduction late policy. | [optional] 
**late_submission_deduction** | **float** | [Number] How many percentage points to deduct per the late submission interval. | [optional] 
**late_submission_interval** | **str** | [String] The interval for late policies. | [optional] 
**late_submission_minimum_percent_enabled** | **bool** | [Boolean] Whether to enable the late submission minimum percent for a late policy. | [optional] 
**late_submission_minimum_percent** | **float** | [Number] The minimum grade a submissions can have in percentage points. | [optional] 

## Example

```python
from canvas_lms_python_client.models.record_already_exists_create_request_late_policy import RecordAlreadyExistsCreateRequestLatePolicy

# TODO update the JSON string below
json = "{}"
# create an instance of RecordAlreadyExistsCreateRequestLatePolicy from a JSON string
record_already_exists_create_request_late_policy_instance = RecordAlreadyExistsCreateRequestLatePolicy.from_json(json)
# print the JSON string representation of the object
print(RecordAlreadyExistsCreateRequestLatePolicy.to_json())

# convert the object into a dict
record_already_exists_create_request_late_policy_dict = record_already_exists_create_request_late_policy_instance.to_dict()
# create an instance of RecordAlreadyExistsCreateRequestLatePolicy from a dict
record_already_exists_create_request_late_policy_from_dict = RecordAlreadyExistsCreateRequestLatePolicy.from_dict(record_already_exists_create_request_late_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


