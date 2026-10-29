# ContextControlsCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | The Canvas ID of the Account that owns this. One of account_id or course_id must be present. Can also be a string. | [optional] 
**course_id** | **int** | The Canvas ID of the Course that owns this. One of account_id or course_id must be present. Can also be a string. | [optional] 
**deployment_id** | **int** | The Canvas ID of the ContextExternalTool that owns this, representing an LTI deployment. If absent, this ContextControl will be associated with the Deployment of this Registration at the Root Account level. If that is not present, this request will fail. | [optional] 
**available** | **bool** | The state of this tool in this context. &#x60;true&#x60; shows the tool in this context and all contexts below it. &#x60;false&#x60; disables the tool for this context and all contexts below it. Defaults to true. | [optional] 
**comment** | **str** | A comment to add the to the change-log entry explaining why the changes were made. | [optional] 

## Example

```python
from canvas_lms_python_client.models.context_controls_create_request import ContextControlsCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ContextControlsCreateRequest from a JSON string
context_controls_create_request_instance = ContextControlsCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ContextControlsCreateRequest.to_json())

# convert the object into a dict
context_controls_create_request_dict = context_controls_create_request_instance.to_dict()
# create an instance of ContextControlsCreateRequest from a dict
context_controls_create_request_from_dict = ContextControlsCreateRequest.from_dict(context_controls_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


