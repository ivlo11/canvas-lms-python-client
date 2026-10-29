# Migrator



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The value to pass to the create endpoint | [optional] 
**requires_file_upload** | **bool** | Whether this endpoint requires a file upload | [optional] 
**name** | **str** | Description of the package type expected | [optional] 
**required_settings** | **List[str]** | A list of fields this system requires | [optional] 

## Example

```python
from canvas_lms_python_client.models.migrator import Migrator

# TODO update the JSON string below
json = "{}"
# create an instance of Migrator from a JSON string
migrator_instance = Migrator.from_json(json)
# print the JSON string representation of the object
print(Migrator.to_json())

# convert the object into a dict
migrator_dict = migrator_instance.to_dict()
# create an instance of Migrator from a dict
migrator_from_dict = Migrator.from_dict(migrator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


