# OutcomeGroupsApiImportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_outcome_group_id** | **int** | The ID of the source outcome group. | 
**var_async** | **bool** | If true, perform action asynchronously.  In that case, this endpoint will return a Progress object instead of an OutcomeGroup. Use the {api:ProgressController#show progress endpoint} to query the status of the operation.  The imported outcome group id and url will be returned in the results of the Progress object as \&quot;outcome_group_id\&quot; and \&quot;outcome_group_url\&quot; | [optional] 

## Example

```python
from canvas_lms_python_client.models.outcome_groups_api_import_request import OutcomeGroupsApiImportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OutcomeGroupsApiImportRequest from a JSON string
outcome_groups_api_import_request_instance = OutcomeGroupsApiImportRequest.from_json(json)
# print the JSON string representation of the object
print(OutcomeGroupsApiImportRequest.to_json())

# convert the object into a dict
outcome_groups_api_import_request_dict = outcome_groups_api_import_request_instance.to_dict()
# create an instance of OutcomeGroupsApiImportRequest from a dict
outcome_groups_api_import_request_from_dict = OutcomeGroupsApiImportRequest.from_dict(outcome_groups_api_import_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


