# LiveAssessmentsAssessmentsCreateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assessments** | [**List[Assessment]**](Assessment.md) |  | [optional] 
**links** | **object** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.live_assessments_assessments_create_response import LiveAssessmentsAssessmentsCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LiveAssessmentsAssessmentsCreateResponse from a JSON string
live_assessments_assessments_create_response_instance = LiveAssessmentsAssessmentsCreateResponse.from_json(json)
# print the JSON string representation of the object
print(LiveAssessmentsAssessmentsCreateResponse.to_json())

# convert the object into a dict
live_assessments_assessments_create_response_dict = live_assessments_assessments_create_response_instance.to_dict()
# create an instance of LiveAssessmentsAssessmentsCreateResponse from a dict
live_assessments_assessments_create_response_from_dict = LiveAssessmentsAssessmentsCreateResponse.from_dict(live_assessments_assessments_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


