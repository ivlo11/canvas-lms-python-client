# canvas_lms_python_client.TermsApiApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**terms_api_index**](TermsApiApi.md#terms_api_index) | **GET** /api/v1/accounts/{account_id}/terms | List enrollment terms
[**terms_api_show**](TermsApiApi.md#terms_api_show) | **GET** /api/v1/accounts/{account_id}/terms/{id} | Retrieve enrollment term


# **terms_api_index**
> EnrollmentTermsList terms_api_index(account_id, workflow_state=workflow_state, include=include, term_name=term_name, page=page, per_page=per_page)

List enrollment terms

An object with a paginated list of all of the terms in the account.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.enrollment_terms_list import EnrollmentTermsList
from canvas_lms_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://canvas.instructure.com
# See configuration.py for a list of all supported configuration parameters.
configuration = canvas_lms_python_client.Configuration(
    host = "https://canvas.instructure.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (token): bearer
configuration = canvas_lms_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with canvas_lms_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = canvas_lms_python_client.TermsApiApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    workflow_state = ['workflow_state_example'] # List[str] | If set, only returns terms that are in the given state. Defaults to 'active'. (optional)
    include = ['include_example'] # List[str] | Array of additional information to include.  \"overrides\":: term start/end dates overridden for different enrollment types \"course_count\":: the number of courses in each term (optional)
    term_name = 'term_name_example' # str | If set, only returns terms that match the given search keyword. Search keyword is matched against term name. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List enrollment terms
        api_response = await api_instance.terms_api_index(account_id, workflow_state=workflow_state, include=include, term_name=term_name, page=page, per_page=per_page)
        print("The response of TermsApiApi->terms_api_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TermsApiApi->terms_api_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **workflow_state** | [**List[str]**](str.md)| If set, only returns terms that are in the given state. Defaults to &#39;active&#39;. | [optional] 
 **include** | [**List[str]**](str.md)| Array of additional information to include.  \&quot;overrides\&quot;:: term start/end dates overridden for different enrollment types \&quot;course_count\&quot;:: the number of courses in each term | [optional] 
 **term_name** | **str**| If set, only returns terms that match the given search keyword. Search keyword is matched against term name. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**EnrollmentTermsList**](EnrollmentTermsList.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | EnrollmentTermsList |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terms_api_show**
> EnrollmentTerm terms_api_show(account_id, id)

Retrieve enrollment term

Retrieves the details for an enrollment term in the account. Includes overrides by default.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.enrollment_term import EnrollmentTerm
from canvas_lms_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://canvas.instructure.com
# See configuration.py for a list of all supported configuration parameters.
configuration = canvas_lms_python_client.Configuration(
    host = "https://canvas.instructure.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (token): bearer
configuration = canvas_lms_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with canvas_lms_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = canvas_lms_python_client.TermsApiApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id

    try:
        # Retrieve enrollment term
        api_response = await api_instance.terms_api_show(account_id, id)
        print("The response of TermsApiApi->terms_api_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TermsApiApi->terms_api_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**EnrollmentTerm**](EnrollmentTerm.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | EnrollmentTerm |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

