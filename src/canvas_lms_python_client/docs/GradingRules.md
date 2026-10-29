# GradingRules



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**drop_lowest** | **int** | Number of lowest scores to be dropped for each user. | [optional] 
**drop_highest** | **int** | Number of highest scores to be dropped for each user. | [optional] 
**never_drop** | **List[int]** | Assignment IDs that should never be dropped. | [optional] 

## Example

```python
from canvas_lms_python_client.models.grading_rules import GradingRules

# TODO update the JSON string below
json = "{}"
# create an instance of GradingRules from a JSON string
grading_rules_instance = GradingRules.from_json(json)
# print the JSON string representation of the object
print(GradingRules.to_json())

# convert the object into a dict
grading_rules_dict = grading_rules_instance.to_dict()
# create an instance of GradingRules from a dict
grading_rules_from_dict = GradingRules.from_dict(grading_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


