# WhatIfGradesApiUpdateResponse

Object response with `grades`, `submission` (from the Canvas `@returns`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grades** | [**List[Grades]**](Grades.md) |  | [optional] 
**submission** | [**WhatIfSubmission**](WhatIfSubmission.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.what_if_grades_api_update_response import WhatIfGradesApiUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WhatIfGradesApiUpdateResponse from a JSON string
what_if_grades_api_update_response_instance = WhatIfGradesApiUpdateResponse.from_json(json)
# print the JSON string representation of the object
print(WhatIfGradesApiUpdateResponse.to_json())

# convert the object into a dict
what_if_grades_api_update_response_dict = what_if_grades_api_update_response_instance.to_dict()
# create an instance of WhatIfGradesApiUpdateResponse from a dict
what_if_grades_api_update_response_from_dict = WhatIfGradesApiUpdateResponse.from_dict(what_if_grades_api_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


