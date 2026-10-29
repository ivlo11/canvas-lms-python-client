# JwtsCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflows** | **List[str]** | Adds additional data to the JWT to be used by the consuming service workflow | [optional] 
**context_type** | **str** | The type of the context to generate the JWT for, in case the workflow requires it. Case insensitive. | [optional] 
**context_id** | **int** | The id of the context to generate the JWT for, in case the workflow requires it. | [optional] 
**context_uuid** | **str** | The uuid of the context to generate the JWT for, in case the workflow requires it. Note that context_id and context_uuid are mutually exclusive. If both are provided, an error will be returned. | [optional] 
**canvas_audience** | **bool** | Defaults to true. If false, the JWT will be signed, but not encrypted, for use in downstream services. The default encrypted behaviour can be used to talk to Canvas itself. | [optional] 

## Example

```python
from canvas_lms_python_client.models.jwts_create_request import JwtsCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of JwtsCreateRequest from a JSON string
jwts_create_request_instance = JwtsCreateRequest.from_json(json)
# print the JSON string representation of the object
print(JwtsCreateRequest.to_json())

# convert the object into a dict
jwts_create_request_dict = jwts_create_request_instance.to_dict()
# create an instance of JwtsCreateRequest from a dict
jwts_create_request_from_dict = JwtsCreateRequest.from_dict(jwts_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


