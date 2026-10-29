# ResultLinks

Unique identifiers of objects associated with a result

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **str** | A unique identifier for the user to whom this result applies | [optional] 
**assessor** | **str** | A unique identifier for the user who created this result | [optional] 
**assessment** | **str** | A unique identifier for the assessment that this result is for | [optional] 

## Example

```python
from canvas_lms_python_client.models.result_links import ResultLinks

# TODO update the JSON string below
json = "{}"
# create an instance of ResultLinks from a JSON string
result_links_instance = ResultLinks.from_json(json)
# print the JSON string representation of the object
print(ResultLinks.to_json())

# convert the object into a dict
result_links_dict = result_links_instance.to_dict()
# create an instance of ResultLinks from a dict
result_links_from_dict = ResultLinks.from_dict(result_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


