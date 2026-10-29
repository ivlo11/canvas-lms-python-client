# MigrationIssuesUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_state** | **str** | Set the workflow_state of the issue. | 

## Example

```python
from canvas_lms_python_client.models.migration_issues_update_request import MigrationIssuesUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MigrationIssuesUpdateRequest from a JSON string
migration_issues_update_request_instance = MigrationIssuesUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(MigrationIssuesUpdateRequest.to_json())

# convert the object into a dict
migration_issues_update_request_dict = migration_issues_update_request_instance.to_dict()
# create an instance of MigrationIssuesUpdateRequest from a dict
migration_issues_update_request_from_dict = MigrationIssuesUpdateRequest.from_dict(migration_issues_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


