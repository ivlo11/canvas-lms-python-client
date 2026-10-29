# Favorite



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context_id** | **int** | The ID of the object the Favorite refers to | [optional] 
**context_type** | **str** | The type of the object the Favorite refers to (currently, only &#39;Course&#39; is supported) | [optional] 

## Example

```python
from canvas_lms_python_client.models.favorite import Favorite

# TODO update the JSON string below
json = "{}"
# create an instance of Favorite from a JSON string
favorite_instance = Favorite.from_json(json)
# print the JSON string representation of the object
print(Favorite.to_json())

# convert the object into a dict
favorite_dict = favorite_instance.to_dict()
# create an instance of Favorite from a dict
favorite_from_dict = Favorite.from_dict(favorite_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


