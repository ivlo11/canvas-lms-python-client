# ErrorsCreateRequestError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | **str** | [Required, String] The summary of the problem | 
**url** | **str** | [Optional, String] URL from which the report was issued | [optional] 
**email** | **str** | [Optional, String] Email address for the reporting user | [optional] 
**comments** | **str** | [Optional, String] The long version of the story from the user one what they experienced | [optional] 
**http_env** | **str** | [Optional, SerializedHash] A collection of metadata about the users&#39; environment.  If not provided, canvas will collect it based on information found in the request. (Doesn&#39;t have to be HTTPENV info, could be anything JSON object that can be serialized as a hash, a mobile app might include relevant metadata for itself) | [optional] 

## Example

```python
from canvas_lms_python_client.models.errors_create_request_error import ErrorsCreateRequestError

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorsCreateRequestError from a JSON string
errors_create_request_error_instance = ErrorsCreateRequestError.from_json(json)
# print the JSON string representation of the object
print(ErrorsCreateRequestError.to_json())

# convert the object into a dict
errors_create_request_error_dict = errors_create_request_error_instance.to_dict()
# create an instance of ErrorsCreateRequestError from a dict
errors_create_request_error_from_dict = ErrorsCreateRequestError.from_dict(errors_create_request_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


