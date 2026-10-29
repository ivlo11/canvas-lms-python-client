# QuizIPFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A unique name for the filter. | 
**account** | **str** | Name of the Account (or Quiz) the IP filter is defined in. | 
**filter** | **str** | An IP address (or range mask) this filter embodies. | 

## Example

```python
from canvas_lms_python_client.models.quiz_ip_filter import QuizIPFilter

# TODO update the JSON string below
json = "{}"
# create an instance of QuizIPFilter from a JSON string
quiz_ip_filter_instance = QuizIPFilter.from_json(json)
# print the JSON string representation of the object
print(QuizIPFilter.to_json())

# convert the object into a dict
quiz_ip_filter_dict = quiz_ip_filter_instance.to_dict()
# create an instance of QuizIPFilter from a dict
quiz_ip_filter_from_dict = QuizIPFilter.from_dict(quiz_ip_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


