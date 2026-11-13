# MasteryDistributionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**outcome_distributions** | **object** |  | [optional] 
**students** | **List[object]** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.mastery_distribution_response import MasteryDistributionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MasteryDistributionResponse from a JSON string
mastery_distribution_response_instance = MasteryDistributionResponse.from_json(json)
# print the JSON string representation of the object
print(MasteryDistributionResponse.to_json())

# convert the object into a dict
mastery_distribution_response_dict = mastery_distribution_response_instance.to_dict()
# create an instance of MasteryDistributionResponse from a dict
mastery_distribution_response_from_dict = MasteryDistributionResponse.from_dict(mastery_distribution_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


