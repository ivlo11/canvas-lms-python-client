# TemporaryEnrollmentPairing

A pairing unique to that enrollment period given to a recipient of that temporary enrollment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | the ID of the temporary enrollment pairing | [optional] 
**workflow_state** | **str** | The current status of the temporary enrollment pairing | [optional] 
**created_at** | **str** |  | [optional] 
**created_by_id** | **int** |  | [optional] 
**deleted_by_id** | **int** |  | [optional] 
**ending_enrollment_state** | **str** |  | [optional] 
**root_account_id** | **int** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.temporary_enrollment_pairing import TemporaryEnrollmentPairing

# TODO update the JSON string below
json = "{}"
# create an instance of TemporaryEnrollmentPairing from a JSON string
temporary_enrollment_pairing_instance = TemporaryEnrollmentPairing.from_json(json)
# print the JSON string representation of the object
print(TemporaryEnrollmentPairing.to_json())

# convert the object into a dict
temporary_enrollment_pairing_dict = temporary_enrollment_pairing_instance.to_dict()
# create an instance of TemporaryEnrollmentPairing from a dict
temporary_enrollment_pairing_from_dict = TemporaryEnrollmentPairing.from_dict(temporary_enrollment_pairing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


