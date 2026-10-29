# ExperienceSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_app** | **str** | The current active experience. One of: &#39;academic&#39;, &#39;career_learner&#39;, &#39;career_learning_provider&#39;. | [optional] 
**available_apps** | **List[str]** | List of available experiences for the user. Can include: &#39;academic&#39;, &#39;career_learner&#39;, &#39;career_learning_provider&#39;. | [optional] 

## Example

```python
from canvas_lms_python_client.models.experience_summary import ExperienceSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ExperienceSummary from a JSON string
experience_summary_instance = ExperienceSummary.from_json(json)
# print the JSON string representation of the object
print(ExperienceSummary.to_json())

# convert the object into a dict
experience_summary_dict = experience_summary_instance.to_dict()
# create an instance of ExperienceSummary from a dict
experience_summary_from_dict = ExperienceSummary.from_dict(experience_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


