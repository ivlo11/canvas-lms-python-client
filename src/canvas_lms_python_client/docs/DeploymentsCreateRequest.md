# DeploymentsCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**for_subaccount_id** | **int** | (optional) If provided, the deployment will be created in the specified subaccount. | [optional] 
**for_course_id** | **int** | (optional) If provided, the deployment will be created in the specified course. | [optional] 
**available** | **bool** | (optional) If provided, sets the availability of the created deployment. Defaults to true. | [optional] 

## Example

```python
from canvas_lms_python_client.models.deployments_create_request import DeploymentsCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentsCreateRequest from a JSON string
deployments_create_request_instance = DeploymentsCreateRequest.from_json(json)
# print the JSON string representation of the object
print(DeploymentsCreateRequest.to_json())

# convert the object into a dict
deployments_create_request_dict = deployments_create_request_instance.to_dict()
# create an instance of DeploymentsCreateRequest from a dict
deployments_create_request_from_dict = DeploymentsCreateRequest.from_dict(deployments_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


