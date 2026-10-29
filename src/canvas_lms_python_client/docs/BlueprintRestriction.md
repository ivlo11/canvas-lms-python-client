# BlueprintRestriction

A set of restrictions on editing for copied objects in associated courses

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **bool** | Restriction on main content (e.g. title, description). | [optional] 
**points** | **bool** | Restriction on points possible for assignments and graded learning objects | [optional] 
**due_dates** | **bool** | Restriction on due dates for assignments and graded learning objects | [optional] 
**availability_dates** | **bool** | Restriction on availability dates for an object | [optional] 

## Example

```python
from canvas_lms_python_client.models.blueprint_restriction import BlueprintRestriction

# TODO update the JSON string below
json = "{}"
# create an instance of BlueprintRestriction from a JSON string
blueprint_restriction_instance = BlueprintRestriction.from_json(json)
# print the JSON string representation of the object
print(BlueprintRestriction.to_json())

# convert the object into a dict
blueprint_restriction_dict = blueprint_restriction_instance.to_dict()
# create an instance of BlueprintRestriction from a dict
blueprint_restriction_from_dict = BlueprintRestriction.from_dict(blueprint_restriction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


