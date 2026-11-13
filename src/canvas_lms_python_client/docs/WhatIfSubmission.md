# WhatIfSubmission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the submission | [optional] 
**student_entered_score** | **str** | The score the student wants to test | [optional] 

## Example

```python
from canvas_lms_python_client.models.what_if_submission import WhatIfSubmission

# TODO update the JSON string below
json = "{}"
# create an instance of WhatIfSubmission from a JSON string
what_if_submission_instance = WhatIfSubmission.from_json(json)
# print the JSON string representation of the object
print(WhatIfSubmission.to_json())

# convert the object into a dict
what_if_submission_dict = what_if_submission_instance.to_dict()
# create an instance of WhatIfSubmission from a dict
what_if_submission_from_dict = WhatIfSubmission.from_dict(what_if_submission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


