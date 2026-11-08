# LatePolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**LatePolicyId**](LatePolicyId.md) |  | [optional] 
**course_id** | **int** | the unique identifier for the course | [optional] 
**missing_submission_deduction_enabled** | **bool** | whether to enable missing submission deductions | [optional] 
**missing_submission_deduction** | **float** | amount of percentage points to deduct | [optional] 
**late_submission_deduction_enabled** | **bool** | whether to enable late submission deductions | [optional] 
**late_submission_deduction** | **float** | amount of percentage points to deduct per late_submission_interval | [optional] 
**late_submission_interval** | **str** | time interval for late submission deduction | [optional] 
**late_submission_minimum_percent_enabled** | **bool** | whether to enable late submission minimum percent | [optional] 
**late_submission_minimum_percent** | **float** | the minimum score a submission can receive in percentage points | [optional] 
**created_at** | **datetime** | the time at which this late policy was originally created | [optional] 
**updated_at** | **datetime** | the time at which this late policy was last modified in any way | [optional] 

## Example

```python
from canvas_lms_python_client.models.late_policy import LatePolicy

# TODO update the JSON string below
json = "{}"
# create an instance of LatePolicy from a JSON string
late_policy_instance = LatePolicy.from_json(json)
# print the JSON string representation of the object
print(LatePolicy.to_json())

# convert the object into a dict
late_policy_dict = late_policy_instance.to_dict()
# create an instance of LatePolicy from a dict
late_policy_from_dict = LatePolicy.from_dict(late_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


