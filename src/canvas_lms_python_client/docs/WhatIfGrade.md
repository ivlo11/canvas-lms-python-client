# WhatIfGrade


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grade** | **float** | The grade for the course | [optional] 
**total** | **float** | The total points earned in the course | [optional] 
**possible** | **float** | The total points possible for the course | [optional] 
**dropped** | **List[object]** | The dropped grades for the course | [optional] 

## Example

```python
from canvas_lms_python_client.models.what_if_grade import WhatIfGrade

# TODO update the JSON string below
json = "{}"
# create an instance of WhatIfGrade from a JSON string
what_if_grade_instance = WhatIfGrade.from_json(json)
# print the JSON string representation of the object
print(WhatIfGrade.to_json())

# convert the object into a dict
what_if_grade_dict = what_if_grade_instance.to_dict()
# create an instance of WhatIfGrade from a dict
what_if_grade_from_dict = WhatIfGrade.from_dict(what_if_grade_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


