# CompletionRequirement



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | one of &#39;must_view&#39;, &#39;must_submit&#39;, &#39;must_contribute&#39;, &#39;min_score&#39;, &#39;min_percentage&#39;, &#39;must_mark_done&#39; | [optional] 
**min_score** | **int** | minimum score required to complete (only present when type &#x3D;&#x3D; &#39;min_score&#39;) | [optional] 
**min_percentage** | **int** | minimum percentage required to complete (only present when type &#x3D;&#x3D; &#39;min_percentage&#39;) | [optional] 
**completed** | **bool** | whether the calling user has met this requirement (Optional; present only if the caller is a student or if the optional parameter &#39;student_id&#39; is included) | [optional] 

## Example

```python
from canvas_lms_python_client.models.completion_requirement import CompletionRequirement

# TODO update the JSON string below
json = "{}"
# create an instance of CompletionRequirement from a JSON string
completion_requirement_instance = CompletionRequirement.from_json(json)
# print the JSON string representation of the object
print(CompletionRequirement.to_json())

# convert the object into a dict
completion_requirement_dict = completion_requirement_instance.to_dict()
# create an instance of CompletionRequirement from a dict
completion_requirement_from_dict = CompletionRequirement.from_dict(completion_requirement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


