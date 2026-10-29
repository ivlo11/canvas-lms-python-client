# NeedsGradingCount

Used by Assignment model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**section_id** | **str** | The section ID | [optional] 
**needs_grading_count** | **int** | Number of submissions that need grading | [optional] 

## Example

```python
from canvas_lms_python_client.models.needs_grading_count import NeedsGradingCount

# TODO update the JSON string below
json = "{}"
# create an instance of NeedsGradingCount from a JSON string
needs_grading_count_instance = NeedsGradingCount.from_json(json)
# print the JSON string representation of the object
print(NeedsGradingCount.to_json())

# convert the object into a dict
needs_grading_count_dict = needs_grading_count_instance.to_dict()
# create an instance of NeedsGradingCount from a dict
needs_grading_count_from_dict = NeedsGradingCount.from_dict(needs_grading_count_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


