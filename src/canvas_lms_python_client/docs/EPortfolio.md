# EPortfolio



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The database ID of the ePortfolio | [optional] 
**user_id** | **int** | The user ID to which the ePortfolio belongs | [optional] 
**name** | **str** | The name of the ePortfolio | [optional] 
**public** | **bool** | Whether or not the ePortfolio is visible without authentication | [optional] 
**created_at** | **datetime** | The creation timestamp for the ePortfolio | [optional] 
**updated_at** | **datetime** | The timestamp of the last time any of the ePortfolio attributes changed | [optional] 
**workflow_state** | **str** | The state of the ePortfolio. Either &#39;active&#39; or &#39;deleted&#39; | [optional] 
**deleted_at** | **datetime** | The timestamp when the ePortfolio was deleted, or else null | [optional] 
**spam_status** | **str** | A flag indicating whether the ePortfolio has been       flagged or moderated as spam. One of &#39;flagged_as_possible_spam&#39;,       &#39;marked_as_safe&#39;, &#39;marked_as_spam&#39;, or null | [optional] 

## Example

```python
from canvas_lms_python_client.models.e_portfolio import EPortfolio

# TODO update the JSON string below
json = "{}"
# create an instance of EPortfolio from a JSON string
e_portfolio_instance = EPortfolio.from_json(json)
# print the JSON string representation of the object
print(EPortfolio.to_json())

# convert the object into a dict
e_portfolio_dict = e_portfolio_instance.to_dict()
# create an instance of EPortfolio from a dict
e_portfolio_from_dict = EPortfolio.from_dict(e_portfolio_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


