# MigrationIssue



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | the unique identifier for the issue | [optional] 
**content_migration_url** | **str** | API url to the content migration | [optional] 
**description** | **str** | Description of the issue for the end-user | [optional] 
**workflow_state** | **str** | Current state of the issue: active, resolved | [optional] 
**fix_issue_html_url** | **str** | HTML Url to the Canvas page to investigate the issue | [optional] 
**issue_type** | **str** | Severity of the issue: todo, warning, error | [optional] 
**error_report_html_url** | **str** | Link to a Canvas error report if present (If the requesting user has permissions) | [optional] 
**error_message** | **str** | Site administrator error message (If the requesting user has permissions) | [optional] 
**created_at** | **datetime** | timestamp | [optional] 
**updated_at** | **datetime** | timestamp | [optional] 

## Example

```python
from canvas_lms_python_client.models.migration_issue import MigrationIssue

# TODO update the JSON string below
json = "{}"
# create an instance of MigrationIssue from a JSON string
migration_issue_instance = MigrationIssue.from_json(json)
# print the JSON string representation of the object
print(MigrationIssue.to_json())

# convert the object into a dict
migration_issue_dict = migration_issue_instance.to_dict()
# create an instance of MigrationIssue from a dict
migration_issue_from_dict = MigrationIssue.from_dict(migration_issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


