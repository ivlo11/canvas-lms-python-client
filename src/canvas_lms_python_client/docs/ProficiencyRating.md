# ProficiencyRating



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description of the rating | [optional] 
**points** | **float** | A non-negative number of points for the rating | [optional] 
**mastery** | **bool** | Indicates the rating where mastery is first achieved | [optional] 
**color** | **str** | The hex color code of the rating | [optional] 

## Example

```python
from canvas_lms_python_client.models.proficiency_rating import ProficiencyRating

# TODO update the JSON string below
json = "{}"
# create an instance of ProficiencyRating from a JSON string
proficiency_rating_instance = ProficiencyRating.from_json(json)
# print the JSON string representation of the object
print(ProficiencyRating.to_json())

# convert the object into a dict
proficiency_rating_dict = proficiency_rating_instance.to_dict()
# create an instance of ProficiencyRating from a dict
proficiency_rating_from_dict = ProficiencyRating.from_dict(proficiency_rating_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


