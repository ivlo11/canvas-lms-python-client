# AnonymousUserDisplay

This mini-object is returned in place of UserDisplay when returning student data for anonymous assignments, and includes an anonymous ID to identify a user within the scope of a single assignment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anonymous_id** | **str** | A unique short ID identifying this user within the scope of a particular assignment. | [optional] 
**avatar_image_url** | **str** | A URL to retrieve a generic avatar. | [optional] 
**display_name** | **str** | The anonymized display name for the student. | [optional] 

## Example

```python
from canvas_lms_python_client.models.anonymous_user_display import AnonymousUserDisplay

# TODO update the JSON string below
json = "{}"
# create an instance of AnonymousUserDisplay from a JSON string
anonymous_user_display_instance = AnonymousUserDisplay.from_json(json)
# print the JSON string representation of the object
print(AnonymousUserDisplay.to_json())

# convert the object into a dict
anonymous_user_display_dict = anonymous_user_display_instance.to_dict()
# create an instance of AnonymousUserDisplay from a dict
anonymous_user_display_from_dict = AnonymousUserDisplay.from_dict(anonymous_user_display_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


