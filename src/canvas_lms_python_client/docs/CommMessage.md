# CommMessage



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the CommMessage. | [optional] 
**created_at** | **datetime** | The date and time this message was created | [optional] 
**sent_at** | **datetime** | The date and time this message was sent | [optional] 
**workflow_state** | **str** | The workflow state of the message. Possible values: &#39;created&#39; : The message has been created, but not yet processed. &#39;staged&#39; : The message is queued for sending. &#39;sending&#39; : The message is being sent currently. &#39;sent&#39; : The message has been successfully sent. &#39;bounced&#39; : An error occurred during the sending of the message.&#39;dashboard&#39; : The message has been sent to the dashboard. &#39;closed&#39; :  The message has been sent and closed, typically for dashboard messages or messages sent to deleted users. &#39;cancelled&#39; : The message was cancelled before it could be sent. | [optional] 
**var_from** | **str** | The address that was put in the &#39;from&#39; field of the message | [optional] 
**from_name** | **str** | The display name for the from address | [optional] 
**to** | **str** | The address the message was sent to: | [optional] 
**reply_to** | **str** | The reply_to header of the message | [optional] 
**subject** | **str** | The message subject | [optional] 
**body** | **str** | The plain text body of the message | [optional] 
**html_body** | **str** | The HTML body of the message. | [optional] 

## Example

```python
from canvas_lms_python_client.models.comm_message import CommMessage

# TODO update the JSON string below
json = "{}"
# create an instance of CommMessage from a JSON string
comm_message_instance = CommMessage.from_json(json)
# print the JSON string representation of the object
print(CommMessage.to_json())

# convert the object into a dict
comm_message_dict = comm_message_instance.to_dict()
# create an instance of CommMessage from a dict
comm_message_from_dict = CommMessage.from_dict(comm_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


