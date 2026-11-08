# LiveAssessmentsAssessmentsIndexResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assessments** | [**List[Assessment]**](Assessment.md) |  | [optional] 
**links** | **object** |  | [optional] 
**meta** | **object** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.live_assessments_assessments_index_response import LiveAssessmentsAssessmentsIndexResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LiveAssessmentsAssessmentsIndexResponse from a JSON string
live_assessments_assessments_index_response_instance = LiveAssessmentsAssessmentsIndexResponse.from_json(json)
# print the JSON string representation of the object
print(LiveAssessmentsAssessmentsIndexResponse.to_json())

# convert the object into a dict
live_assessments_assessments_index_response_dict = live_assessments_assessments_index_response_instance.to_dict()
# create an instance of LiveAssessmentsAssessmentsIndexResponse from a dict
live_assessments_assessments_index_response_from_dict = LiveAssessmentsAssessmentsIndexResponse.from_dict(live_assessments_assessments_index_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


