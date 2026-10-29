# EnrollmentTermsList



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enrollment_terms** | [**List[EnrollmentTerm]**](EnrollmentTerm.md) | a paginated list of all terms in the account | [optional] 

## Example

```python
from canvas_lms_python_client.models.enrollment_terms_list import EnrollmentTermsList

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentTermsList from a JSON string
enrollment_terms_list_instance = EnrollmentTermsList.from_json(json)
# print the JSON string representation of the object
print(EnrollmentTermsList.to_json())

# convert the object into a dict
enrollment_terms_list_dict = enrollment_terms_list_instance.to_dict()
# create an instance of EnrollmentTermsList from a dict
enrollment_terms_list_from_dict = EnrollmentTermsList.from_dict(enrollment_terms_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


