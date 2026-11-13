# ConferencesIndexResponse

Object response with `conferences` (from the Canvas `@returns`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conferences** | [**List[Conference]**](Conference.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.conferences_index_response import ConferencesIndexResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConferencesIndexResponse from a JSON string
conferences_index_response_instance = ConferencesIndexResponse.from_json(json)
# print the JSON string representation of the object
print(ConferencesIndexResponse.to_json())

# convert the object into a dict
conferences_index_response_dict = conferences_index_response_instance.to_dict()
# create an instance of ConferencesIndexResponse from a dict
conferences_index_response_from_dict = ConferencesIndexResponse.from_dict(conferences_index_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


