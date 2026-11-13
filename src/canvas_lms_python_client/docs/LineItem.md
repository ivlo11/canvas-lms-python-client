# LineItem



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The fully qualified URL for showing, updating, and deleting the Line Item | [optional] 
**score_maximum** | **float** | The maximum score of the Line Item | [optional] 
**label** | **str** | The label of the Line Item. | [optional] 
**tag** | **str** | Tag used to qualify a line Item beyond its ids | [optional] 
**resource_id** | **str** | A Tool Provider specified id for the Line Item. Multiple line items can share the same resourceId within a given context | [optional] 
**resource_link_id** | **str** | The resource link id the Line Item is attached to | [optional] 
**https___canvas_instructure_com_lti_submission_type** | **str** | The extension that defines the submission_type of the line_item. Only returns if set through the line_item create endpoint. | [optional] 
**https___canvas_instructure_com_lti_launch_url** | **str** | The launch url of the Line Item. Only returned if &#x60;include&#x3D;launch_url&#x60; query parameter is passed, and only for Show and List actions. | [optional] 
**end_date_time** | **str** |  | [optional] 
**start_date_time** | **str** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.line_item import LineItem

# TODO update the JSON string below
json = "{}"
# create an instance of LineItem from a JSON string
line_item_instance = LineItem.from_json(json)
# print the JSON string representation of the object
print(LineItem.to_json())

# convert the object into a dict
line_item_dict = line_item_instance.to_dict()
# create an instance of LineItem from a dict
line_item_from_dict = LineItem.from_dict(line_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


