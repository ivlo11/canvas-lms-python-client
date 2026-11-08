# ErrorsCreateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**logged** | **bool** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.errors_create_response import ErrorsCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorsCreateResponse from a JSON string
errors_create_response_instance = ErrorsCreateResponse.from_json(json)
# print the JSON string representation of the object
print(ErrorsCreateResponse.to_json())

# convert the object into a dict
errors_create_response_dict = errors_create_response_instance.to_dict()
# create an instance of ErrorsCreateResponse from a dict
errors_create_response_from_dict = ErrorsCreateResponse.from_dict(errors_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


