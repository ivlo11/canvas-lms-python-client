# Proficiency



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ratings** | **List[object]** | An array of proficiency ratings. See the ProficiencyRating specification above. | [optional] 

## Example

```python
from canvas_lms_python_client.models.proficiency import Proficiency

# TODO update the JSON string below
json = "{}"
# create an instance of Proficiency from a JSON string
proficiency_instance = Proficiency.from_json(json)
# print the JSON string representation of the object
print(Proficiency.to_json())

# convert the object into a dict
proficiency_dict = proficiency_instance.to_dict()
# create an instance of Proficiency from a dict
proficiency_from_dict = Proficiency.from_dict(proficiency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


