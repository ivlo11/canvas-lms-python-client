# Tab



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**html_url** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**hidden** | **bool** | only included if true | [optional] 
**visibility** | **str** | possible values are: public, members, admins, and none | [optional] 
**position** | **int** | 1 based | [optional] 

## Example

```python
from canvas_lms_python_client.models.tab import Tab

# TODO update the JSON string below
json = "{}"
# create an instance of Tab from a JSON string
tab_instance = Tab.from_json(json)
# print the JSON string representation of the object
print(Tab.to_json())

# convert the object into a dict
tab_dict = tab_instance.to_dict()
# create an instance of Tab from a dict
tab_from_dict = Tab.from_dict(tab_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


