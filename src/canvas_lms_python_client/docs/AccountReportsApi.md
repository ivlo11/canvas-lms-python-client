# canvas_lms_python_client.AccountReportsApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_reports_abort**](AccountReportsApi.md#account_reports_abort) | **PUT** /api/v1/accounts/{account_id}/reports/{report}/{id}/abort | Abort a Report
[**account_reports_available_reports**](AccountReportsApi.md#account_reports_available_reports) | **GET** /api/v1/accounts/{account_id}/reports | List Available Reports
[**account_reports_create**](AccountReportsApi.md#account_reports_create) | **POST** /api/v1/accounts/{account_id}/reports/{report} | Start a Report
[**account_reports_destroy**](AccountReportsApi.md#account_reports_destroy) | **DELETE** /api/v1/accounts/{account_id}/reports/{report}/{id} | Delete a Report
[**account_reports_index**](AccountReportsApi.md#account_reports_index) | **GET** /api/v1/accounts/{account_id}/reports/{report} | Index of Reports
[**account_reports_show**](AccountReportsApi.md#account_reports_show) | **GET** /api/v1/accounts/{account_id}/reports/{report}/{id} | Status of a Report


# **account_reports_abort**
> Report account_reports_abort(account_id, id, report)

Abort a Report

Abort a report in progress

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.report import Report
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
    api_instance = canvas_lms_python_client.AccountReportsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id
    report = 'report_example' # str | Scope response to report

    try:
        # Abort a Report
        api_response = await api_instance.account_reports_abort(account_id, id, report)
        print("The response of AccountReportsApi->account_reports_abort:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountReportsApi->account_reports_abort: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 
 **report** | **str**| Scope response to report | 

### Return type

[**Report**](Report.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Report |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_reports_available_reports**
> List[AccountReportsAvailableReportsResponse] account_reports_available_reports(account_id, include=include)

List Available Reports

Returns a paginated list of reports for the current context.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.account_reports_available_reports_response import AccountReportsAvailableReportsResponse
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
    api_instance = canvas_lms_python_client.AccountReportsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    include = ['include_example'] # List[str] | Array of additional information to include.  \"description_html\":: an HTML description of the report, with example output \"parameters_html\":: an HTML form for the report parameters (optional)

    try:
        # List Available Reports
        api_response = await api_instance.account_reports_available_reports(account_id, include=include)
        print("The response of AccountReportsApi->account_reports_available_reports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountReportsApi->account_reports_available_reports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **include** | [**List[str]**](str.md)| Array of additional information to include.  \&quot;description_html\&quot;:: an HTML description of the report, with example output \&quot;parameters_html\&quot;:: an HTML form for the report parameters | [optional] 

### Return type

[**List[AccountReportsAvailableReportsResponse]**](AccountReportsAvailableReportsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_reports_create**
> Report account_reports_create(account_id, report, account_reports_create_request=account_reports_create_request)

Start a Report

Generates a report instance for the account. Note that "report" in the
request must match one of the available report names. To fetch a list of
available report names and parameters for each report (including whether or
not those parameters are required), see
{api:AccountReportsController#available_reports List Available Reports}.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.account_reports_create_request import AccountReportsCreateRequest
from canvas_lms_python_client.models.report import Report
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
    api_instance = canvas_lms_python_client.AccountReportsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    report = 'report_example' # str | Scope response to report
    account_reports_create_request = canvas_lms_python_client.AccountReportsCreateRequest() # AccountReportsCreateRequest | Request body parameters  **Example Request:** ``` curl -X POST \\      https://<canvas>/api/v1/accounts/1/reports/provisioning_csv \\      -H 'Authorization: Bearer <token>' \\      -H 'Content-Type: multipart/form-data' \\      -F 'parameters[users]=true' \\      -F 'parameters[courses]=true' \\      -F 'parameters[enrollments]=true' ``` (optional)

    try:
        # Start a Report
        api_response = await api_instance.account_reports_create(account_id, report, account_reports_create_request=account_reports_create_request)
        print("The response of AccountReportsApi->account_reports_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountReportsApi->account_reports_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **report** | **str**| Scope response to report | 
 **account_reports_create_request** | [**AccountReportsCreateRequest**](AccountReportsCreateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl -X POST \\      https://&lt;canvas&gt;/api/v1/accounts/1/reports/provisioning_csv \\      -H &#39;Authorization: Bearer &lt;token&gt;&#39; \\      -H &#39;Content-Type: multipart/form-data&#39; \\      -F &#39;parameters[users]&#x3D;true&#39; \\      -F &#39;parameters[courses]&#x3D;true&#39; \\      -F &#39;parameters[enrollments]&#x3D;true&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**Report**](Report.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Report |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_reports_destroy**
> Report account_reports_destroy(account_id, id, report)

Delete a Report

Deletes a generated report instance.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.report import Report
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
    api_instance = canvas_lms_python_client.AccountReportsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id
    report = 'report_example' # str | Scope response to report

    try:
        # Delete a Report
        api_response = await api_instance.account_reports_destroy(account_id, id, report)
        print("The response of AccountReportsApi->account_reports_destroy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountReportsApi->account_reports_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 
 **report** | **str**| Scope response to report | 

### Return type

[**Report**](Report.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Report |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_reports_index**
> List[Report] account_reports_index(account_id, report, page=page, per_page=per_page)

Index of Reports

Shows all reports that have been run for the account of a specific type.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.report import Report
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
    api_instance = canvas_lms_python_client.AccountReportsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    report = 'report_example' # str | Scope response to report
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # Index of Reports
        api_response = await api_instance.account_reports_index(account_id, report, page=page, per_page=per_page)
        print("The response of AccountReportsApi->account_reports_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountReportsApi->account_reports_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **report** | **str**| Scope response to report | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[Report]**](Report.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_reports_show**
> Report account_reports_show(account_id, id, report)

Status of a Report

Returns the status of a report.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.report import Report
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
    api_instance = canvas_lms_python_client.AccountReportsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id
    report = 'report_example' # str | Scope response to report

    try:
        # Status of a Report
        api_response = await api_instance.account_reports_show(account_id, id, report)
        print("The response of AccountReportsApi->account_reports_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountReportsApi->account_reports_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 
 **report** | **str**| Scope response to report | 

### Return type

[**Report**](Report.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Report |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

