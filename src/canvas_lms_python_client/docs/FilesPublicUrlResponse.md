# FilesPublicUrlResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_url** | **str** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.files_public_url_response import FilesPublicUrlResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FilesPublicUrlResponse from a JSON string
files_public_url_response_instance = FilesPublicUrlResponse.from_json(json)
# print the JSON string representation of the object
print(FilesPublicUrlResponse.to_json())

# convert the object into a dict
files_public_url_response_dict = files_public_url_response_instance.to_dict()
# create an instance of FilesPublicUrlResponse from a dict
files_public_url_response_from_dict = FilesPublicUrlResponse.from_dict(files_public_url_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


