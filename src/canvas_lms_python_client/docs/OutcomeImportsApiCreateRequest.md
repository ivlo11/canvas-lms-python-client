# OutcomeImportsApiCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**import_type** | **str** | Choose the data format for reading outcome data. With a standard Canvas install, this option can only be &#39;instructure_csv&#39;, and if unprovided, will be assumed to be so. Can be part of the query string. | [optional] 
**attachment** | **str** | There are two ways to post outcome import data - either via a multipart/form-data form-field-style attachment, or via a non-multipart raw post request.  &#39;attachment&#39; is required for multipart/form-data style posts. Assumed to be outcome data from a file upload form field named &#39;attachment&#39;.  Examples:   curl -F attachment&#x3D;@&lt;filename&gt; -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; \\       &#39;https://&lt;canvas&gt;/api/v1/accounts/&lt;account_id&gt;/outcome_imports?import_type&#x3D;instructure_csv&#39;   curl -F attachment&#x3D;@&lt;filename&gt; -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; \\       &#39;https://&lt;canvas&gt;/api/v1/courses/&lt;course_id&gt;/outcome_imports?import_type&#x3D;instructure_csv&#39;  If you decide to do a raw post, you can skip the &#39;attachment&#39; argument, but you will then be required to provide a suitable Content-Type header. You are encouraged to also provide the &#39;extension&#39; argument.  Examples:   curl -H &#39;Content-Type: text/csv&#39; --data-binary @&lt;filename&gt;.csv \\       -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; \\       &#39;https://&lt;canvas&gt;/api/v1/accounts/&lt;account_id&gt;/outcome_imports?import_type&#x3D;instructure_csv&#39;    curl -H &#39;Content-Type: text/csv&#39; --data-binary @&lt;filename&gt;.csv \\       -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; \\       &#39;https://&lt;canvas&gt;/api/v1/courses/&lt;course_id&gt;/outcome_imports?import_type&#x3D;instructure_csv&#39; | [optional] 
**extension** | **str** | Recommended for raw post request style imports. This field will be used to distinguish between csv and other file format extensions that would usually be provided with the filename in the multipart post request scenario. If not provided, this value will be inferred from the Content-Type, falling back to csv-file format if all else fails. | [optional] 

## Example

```python
from canvas_lms_python_client.models.outcome_imports_api_create_request import OutcomeImportsApiCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OutcomeImportsApiCreateRequest from a JSON string
outcome_imports_api_create_request_instance = OutcomeImportsApiCreateRequest.from_json(json)
# print the JSON string representation of the object
print(OutcomeImportsApiCreateRequest.to_json())

# convert the object into a dict
outcome_imports_api_create_request_dict = outcome_imports_api_create_request_instance.to_dict()
# create an instance of OutcomeImportsApiCreateRequest from a dict
outcome_imports_api_create_request_from_dict = OutcomeImportsApiCreateRequest.from_dict(outcome_imports_api_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


