# ListLtiRegistrationsResponse

The response for the List LTI Registrations API endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | The total number of LTI registrations across all pages | [optional] 
**data** | [**List[LtiRegistration]**](LtiRegistration.md) | The paginated list of LTI_Registrations | [optional] 

## Example

```python
from canvas_lms_python_client.models.list_lti_registrations_response import ListLtiRegistrationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListLtiRegistrationsResponse from a JSON string
list_lti_registrations_response_instance = ListLtiRegistrationsResponse.from_json(json)
# print the JSON string representation of the object
print(ListLtiRegistrationsResponse.to_json())

# convert the object into a dict
list_lti_registrations_response_dict = list_lti_registrations_response_instance.to_dict()
# create an instance of ListLtiRegistrationsResponse from a dict
list_lti_registrations_response_from_dict = ListLtiRegistrationsResponse.from_dict(list_lti_registrations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


