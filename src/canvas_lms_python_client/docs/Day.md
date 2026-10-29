# Day



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | the date represented by this entry | [optional] 
**graders** | **int** | an array of the graders who were responsible for the submissions in this response. the submissions are grouped according to the person who graded them and the assignment they were submitted for. | [optional] 

## Example

```python
from canvas_lms_python_client.models.day import Day

# TODO update the JSON string below
json = "{}"
# create an instance of Day from a JSON string
day_instance = Day.from_json(json)
# print the JSON string representation of the object
print(Day.to_json())

# convert the object into a dict
day_dict = day_instance.to_dict()
# create an instance of Day from a dict
day_from_dict = Day.from_dict(day_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


