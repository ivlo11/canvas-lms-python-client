# FilesApiQuotaResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quota** | **int** |  | [optional] 
**quota_used** | **int** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.files_api_quota_response import FilesApiQuotaResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FilesApiQuotaResponse from a JSON string
files_api_quota_response_instance = FilesApiQuotaResponse.from_json(json)
# print the JSON string representation of the object
print(FilesApiQuotaResponse.to_json())

# convert the object into a dict
files_api_quota_response_dict = files_api_quota_response_instance.to_dict()
# create an instance of FilesApiQuotaResponse from a dict
files_api_quota_response_from_dict = FilesApiQuotaResponse.from_dict(files_api_quota_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


