# PollsCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**polls_question** | **str** | The title of the poll. | 
**polls_description** | **str** | A brief description or instructions for the poll. | [optional] 

## Example

```python
from canvas_lms_python_client.models.polls_create_request import PollsCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PollsCreateRequest from a JSON string
polls_create_request_instance = PollsCreateRequest.from_json(json)
# print the JSON string representation of the object
print(PollsCreateRequest.to_json())

# convert the object into a dict
polls_create_request_dict = polls_create_request_instance.to_dict()
# create an instance of PollsCreateRequest from a dict
polls_create_request_from_dict = PollsCreateRequest.from_dict(polls_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


