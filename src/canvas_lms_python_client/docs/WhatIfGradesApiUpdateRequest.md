# WhatIfGradesApiUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**student_entered_score** | **float** | The score the student wants to test | [optional] 

## Example

```python
from canvas_lms_python_client.models.what_if_grades_api_update_request import WhatIfGradesApiUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WhatIfGradesApiUpdateRequest from a JSON string
what_if_grades_api_update_request_instance = WhatIfGradesApiUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(WhatIfGradesApiUpdateRequest.to_json())

# convert the object into a dict
what_if_grades_api_update_request_dict = what_if_grades_api_update_request_instance.to_dict()
# create an instance of WhatIfGradesApiUpdateRequest from a dict
what_if_grades_api_update_request_from_dict = WhatIfGradesApiUpdateRequest.from_dict(what_if_grades_api_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


