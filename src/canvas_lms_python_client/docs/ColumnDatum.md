# ColumnDatum

ColumnDatum objects contain the entry for a column for each user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | [optional] 
**user_id** | **int** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.column_datum import ColumnDatum

# TODO update the JSON string below
json = "{}"
# create an instance of ColumnDatum from a JSON string
column_datum_instance = ColumnDatum.from_json(json)
# print the JSON string representation of the object
print(ColumnDatum.to_json())

# convert the object into a dict
column_datum_dict = column_datum_instance.to_dict()
# create an instance of ColumnDatum from a dict
column_datum_from_dict = ColumnDatum.from_dict(column_datum_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


