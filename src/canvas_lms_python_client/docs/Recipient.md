# Recipient

A user or a context (course, section, group, or a synthetic group of a course's users) that the current user can send messages to. Users carry full_name, pronouns, common_courses and common_groups; contexts carry type \"context\", user_count or item_count, permissions and context_name.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | The unique identifier for the user (an integer), or for the context (a string prefixed by its type, for example \&quot;course_5\&quot; or \&quot;group_1\&quot;). | [optional] 
**name** | **str** | The name of the context or short name of the user. | [optional] 
**full_name** | **str** | Only set for users. The full name of the user. | [optional] 
**pronouns** | **str** | Only set for users. The user&#39;s pronouns, if any. | [optional] 
**avatar_url** | **str** | Avatar image url for the user/context. | [optional] 
**type** | **str** | Only set for contexts: \&quot;context\&quot;. | [optional] 
**user_count** | **int** | Only set for contexts. The number of users in the context. | [optional] 
**item_count** | **int** | Only set for synthetic contexts that group sections or groups (for example \&quot;course_5_groups\&quot;). The number of items in the group. | [optional] 
**context_name** | **str** | Only set for some contexts. The name of the context&#39;s parent course. | [optional] 
**permissions** | **object** | Only set for contexts. The requested permissions the current user has in the context. | [optional] 
**common_courses** | **object** | Only set for users. Course ids the user shares with the current user, mapped to the user&#39;s enrollment types. | [optional] 
**common_groups** | **object** | Only set for users. Group ids the user shares with the current user, mapped to the user&#39;s roles. | [optional] 

## Example

```python
from canvas_lms_python_client.models.recipient import Recipient

# TODO update the JSON string below
json = "{}"
# create an instance of Recipient from a JSON string
recipient_instance = Recipient.from_json(json)
# print the JSON string representation of the object
print(Recipient.to_json())

# convert the object into a dict
recipient_dict = recipient_instance.to_dict()
# create an instance of Recipient from a dict
recipient_from_dict = Recipient.from_dict(recipient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


