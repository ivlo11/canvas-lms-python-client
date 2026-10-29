# EPortfolioPage



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The database ID of the ePortfolio | [optional] 
**eportfolio_id** | **int** | The ePortfolio ID to which the entry belongs | [optional] 
**position** | **int** | The positional order of the entry in the list | [optional] 
**name** | **str** | The name of the ePortfolio | [optional] 
**content** | **str** | The user entered content of the entry | [optional] 
**created_at** | **datetime** | The creation timestamp for the ePortfolio | [optional] 
**updated_at** | **datetime** | The timestamp of the last time any of the ePortfolio attributes changed | [optional] 

## Example

```python
from canvas_lms_python_client.models.e_portfolio_page import EPortfolioPage

# TODO update the JSON string below
json = "{}"
# create an instance of EPortfolioPage from a JSON string
e_portfolio_page_instance = EPortfolioPage.from_json(json)
# print the JSON string representation of the object
print(EPortfolioPage.to_json())

# convert the object into a dict
e_portfolio_page_dict = e_portfolio_page_instance.to_dict()
# create an instance of EPortfolioPage from a dict
e_portfolio_page_from_dict = EPortfolioPage.from_dict(e_portfolio_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


