# canvas_lms_python_client.AccountsApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accounts_course_accounts**](AccountsApi.md#accounts_course_accounts) | **GET** /api/v1/course_accounts | List accounts for course admins
[**accounts_course_creation_accounts**](AccountsApi.md#accounts_course_creation_accounts) | **GET** /api/v1/course_creation_accounts | Get accounts that users can create courses in
[**accounts_courses_api**](AccountsApi.md#accounts_courses_api) | **GET** /api/v1/accounts/{account_id}/courses | List active courses in an account
[**accounts_environment**](AccountsApi.md#accounts_environment) | **GET** /api/v1/settings/environment | List environment settings
[**accounts_help_links**](AccountsApi.md#accounts_help_links) | **GET** /api/v1/accounts/{account_id}/help_links | Get help links
[**accounts_horizon_accounts**](AccountsApi.md#accounts_horizon_accounts) | **GET** /api/v1/horizon_accounts | List horizon accounts
[**accounts_index**](AccountsApi.md#accounts_index) | **GET** /api/v1/accounts | List accounts
[**accounts_manageable_accounts**](AccountsApi.md#accounts_manageable_accounts) | **GET** /api/v1/manageable_accounts | Get accounts that admins can manage
[**accounts_manually_created_courses_account**](AccountsApi.md#accounts_manually_created_courses_account) | **GET** /api/v1/manually_created_courses_account | Get the manually-created courses sub-account for the domain root account
[**accounts_permissions**](AccountsApi.md#accounts_permissions) | **GET** /api/v1/accounts/{account_id}/permissions | Permissions
[**accounts_remove_user**](AccountsApi.md#accounts_remove_user) | **DELETE** /api/v1/accounts/{account_id}/users/{user_id} | Delete a user from the root account
[**accounts_remove_users**](AccountsApi.md#accounts_remove_users) | **DELETE** /api/v1/accounts/{account_id}/users | Delete multiple users from the root account
[**accounts_restore_user**](AccountsApi.md#accounts_restore_user) | **PUT** /api/v1/accounts/{account_id}/users/{user_id}/restore | Restore a deleted user from a root account
[**accounts_show**](AccountsApi.md#accounts_show) | **GET** /api/v1/accounts/{id} | Get a single account
[**accounts_show_settings**](AccountsApi.md#accounts_show_settings) | **GET** /api/v1/accounts/{account_id}/settings | Settings
[**accounts_sub_accounts**](AccountsApi.md#accounts_sub_accounts) | **GET** /api/v1/accounts/{account_id}/sub_accounts | Get the sub-accounts of an account
[**accounts_terms_of_service**](AccountsApi.md#accounts_terms_of_service) | **GET** /api/v1/accounts/{account_id}/terms_of_service | Get the Terms of Service
[**accounts_update**](AccountsApi.md#accounts_update) | **PUT** /api/v1/accounts/{id} | Update an account
[**accounts_update_users**](AccountsApi.md#accounts_update_users) | **PUT** /api/v1/accounts/{account_id}/users/bulk_update | Update multiple users


# **accounts_course_accounts**
> List[Account] accounts_course_accounts(page=page, per_page=per_page)

List accounts for course admins

A paginated list of accounts that the current user can view through their
admin course enrollments. (Teacher, TA, or designer enrollments).
Only returns "id", "name", "workflow_state", "root_account_id" and "parent_account_id"

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.account import Account
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
    api_instance = canvas_lms_python_client.AccountsApi(api_client)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List accounts for course admins
        api_response = await api_instance.accounts_course_accounts(page=page, per_page=per_page)
        print("The response of AccountsApi->accounts_course_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->accounts_course_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[Account]**](Account.md)

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

# **accounts_course_creation_accounts**
> List[Account] accounts_course_creation_accounts(page=page, per_page=per_page)

Get accounts that users can create courses in

A paginated list of accounts where the current user has permission to create
courses.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.account import Account
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
    api_instance = canvas_lms_python_client.AccountsApi(api_client)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # Get accounts that users can create courses in
        api_response = await api_instance.accounts_course_creation_accounts(page=page, per_page=per_page)
        print("The response of AccountsApi->accounts_course_creation_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->accounts_course_creation_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[Account]**](Account.md)

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

# **accounts_courses_api**
> List[Course] accounts_courses_api(account_id, with_enrollments=with_enrollments, enrollment_type=enrollment_type, enrollment_workflow_state=enrollment_workflow_state, published=published, completed=completed, blueprint=blueprint, blueprint_associated=blueprint_associated, public=public, by_teachers=by_teachers, by_subaccounts=by_subaccounts, hide_enrollmentless_courses=hide_enrollmentless_courses, state_created_claimed_available_completed_deleted_all=state_created_claimed_available_completed_deleted_all, enrollment_term_id=enrollment_term_id, search_term=search_term, include=include, sort=sort, order=order, search_by=search_by, starts_before=starts_before, ends_after=ends_after, homeroom=homeroom, page=page, per_page=per_page)

List active courses in an account

Retrieve a paginated list of courses in this account.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.course import Course
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
    api_instance = canvas_lms_python_client.AccountsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    with_enrollments = True # bool | If true, include only courses with at least one enrollment.  If false, include only courses with no enrollments.  If not present, do not filter on course enrollment status. (optional)
    enrollment_type = ['enrollment_type_example'] # List[str] | If set, only return courses that have at least one user enrolled in in the course with one of the specified enrollment types. (optional)
    enrollment_workflow_state = ['enrollment_workflow_state_example'] # List[str] | If set, only return courses that have at least one user enrolled in in the course with one of the specified enrollment workflow states. (optional)
    published = True # bool | If true, include only published courses.  If false, exclude published courses.  If not present, do not filter on published status. (optional)
    completed = True # bool | If true, include only completed courses (these may be in state 'completed', or their enrollment term may have ended).  If false, exclude completed courses.  If not present, do not filter on completed status. (optional)
    blueprint = True # bool | If true, include only blueprint courses. If false, exclude them. If not present, do not filter on this basis. (optional)
    blueprint_associated = True # bool | If true, include only courses that inherit content from a blueprint course. If false, exclude them. If not present, do not filter on this basis. (optional)
    public = True # bool | If true, include only public courses. If false, exclude them. If not present, do not filter on this basis. (optional)
    by_teachers = [56] # List[int] | List of User IDs of teachers; if supplied, include only courses taught by one of the referenced users. (optional)
    by_subaccounts = [56] # List[int] | List of Account IDs; if supplied, include only courses associated with one of the referenced subaccounts. (optional)
    hide_enrollmentless_courses = True # bool | If present, only return courses that have at least one enrollment. Equivalent to 'with_enrollments=true'; retained for compatibility. (optional)
    state_created_claimed_available_completed_deleted_all = 'state_created_claimed_available_completed_deleted_all_example' # str | If set, only return courses that are in the given state(s). By default, all states but \"deleted\" are returned. (optional)
    enrollment_term_id = [56] # List[int] | If set, only includes courses from the specified terms. Can be either a single ID or an array of enrollment term IDs. (optional)
    search_term = 'search_term_example' # str | The partial course name, code, or full ID to match and return in the results list. Must be at least 3 characters. (optional)
    include = ['include_example'] # List[str] | - All explanations can be seen in the {api:CoursesController#index Course API index documentation} - \"sections\", \"needs_grading_count\" and \"total_scores\" are not valid options at the account level (optional)
    sort = 'sort_example' # str | The column to sort results by. (optional)
    order = 'order_example' # str | The order to sort the given column by. (optional)
    search_by = 'search_by_example' # str | The filter to search by. \"course\" searches for course names, course codes, and SIS IDs. \"teacher\" searches for teacher names (optional)
    starts_before = 'starts_before_example' # str | If set, only return courses that start before the value (inclusive) or their enrollment term starts before the value (inclusive) or both the course's start_at and the enrollment term's start_at are set to null. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ. (optional)
    ends_after = 'ends_after_example' # str | If set, only return courses that end after the value (inclusive) or their enrollment term ends after the value (inclusive) or both the course's end_at and the enrollment term's end_at are set to null. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ. (optional)
    homeroom = True # bool | If set, only return homeroom courses. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List active courses in an account
        api_response = await api_instance.accounts_courses_api(account_id, with_enrollments=with_enrollments, enrollment_type=enrollment_type, enrollment_workflow_state=enrollment_workflow_state, published=published, completed=completed, blueprint=blueprint, blueprint_associated=blueprint_associated, public=public, by_teachers=by_teachers, by_subaccounts=by_subaccounts, hide_enrollmentless_courses=hide_enrollmentless_courses, state_created_claimed_available_completed_deleted_all=state_created_claimed_available_completed_deleted_all, enrollment_term_id=enrollment_term_id, search_term=search_term, include=include, sort=sort, order=order, search_by=search_by, starts_before=starts_before, ends_after=ends_after, homeroom=homeroom, page=page, per_page=per_page)
        print("The response of AccountsApi->accounts_courses_api:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->accounts_courses_api: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **with_enrollments** | **bool**| If true, include only courses with at least one enrollment.  If false, include only courses with no enrollments.  If not present, do not filter on course enrollment status. | [optional] 
 **enrollment_type** | [**List[str]**](str.md)| If set, only return courses that have at least one user enrolled in in the course with one of the specified enrollment types. | [optional] 
 **enrollment_workflow_state** | [**List[str]**](str.md)| If set, only return courses that have at least one user enrolled in in the course with one of the specified enrollment workflow states. | [optional] 
 **published** | **bool**| If true, include only published courses.  If false, exclude published courses.  If not present, do not filter on published status. | [optional] 
 **completed** | **bool**| If true, include only completed courses (these may be in state &#39;completed&#39;, or their enrollment term may have ended).  If false, exclude completed courses.  If not present, do not filter on completed status. | [optional] 
 **blueprint** | **bool**| If true, include only blueprint courses. If false, exclude them. If not present, do not filter on this basis. | [optional] 
 **blueprint_associated** | **bool**| If true, include only courses that inherit content from a blueprint course. If false, exclude them. If not present, do not filter on this basis. | [optional] 
 **public** | **bool**| If true, include only public courses. If false, exclude them. If not present, do not filter on this basis. | [optional] 
 **by_teachers** | [**List[int]**](int.md)| List of User IDs of teachers; if supplied, include only courses taught by one of the referenced users. | [optional] 
 **by_subaccounts** | [**List[int]**](int.md)| List of Account IDs; if supplied, include only courses associated with one of the referenced subaccounts. | [optional] 
 **hide_enrollmentless_courses** | **bool**| If present, only return courses that have at least one enrollment. Equivalent to &#39;with_enrollments&#x3D;true&#39;; retained for compatibility. | [optional] 
 **state_created_claimed_available_completed_deleted_all** | **str**| If set, only return courses that are in the given state(s). By default, all states but \&quot;deleted\&quot; are returned. | [optional] 
 **enrollment_term_id** | [**List[int]**](int.md)| If set, only includes courses from the specified terms. Can be either a single ID or an array of enrollment term IDs. | [optional] 
 **search_term** | **str**| The partial course name, code, or full ID to match and return in the results list. Must be at least 3 characters. | [optional] 
 **include** | [**List[str]**](str.md)| - All explanations can be seen in the {api:CoursesController#index Course API index documentation} - \&quot;sections\&quot;, \&quot;needs_grading_count\&quot; and \&quot;total_scores\&quot; are not valid options at the account level | [optional] 
 **sort** | **str**| The column to sort results by. | [optional] 
 **order** | **str**| The order to sort the given column by. | [optional] 
 **search_by** | **str**| The filter to search by. \&quot;course\&quot; searches for course names, course codes, and SIS IDs. \&quot;teacher\&quot; searches for teacher names | [optional] 
 **starts_before** | **str**| If set, only return courses that start before the value (inclusive) or their enrollment term starts before the value (inclusive) or both the course&#39;s start_at and the enrollment term&#39;s start_at are set to null. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ. | [optional] 
 **ends_after** | **str**| If set, only return courses that end after the value (inclusive) or their enrollment term ends after the value (inclusive) or both the course&#39;s end_at and the enrollment term&#39;s end_at are set to null. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ. | [optional] 
 **homeroom** | **bool**| If set, only return homeroom courses. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[Course]**](Course.md)

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

# **accounts_environment**
> AccountsEnvironmentResponse accounts_environment()

List environment settings

Return a hash of global settings for the root account
This is the same information supplied to the web interface as +ENV.SETTINGS+.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.accounts_environment_response import AccountsEnvironmentResponse
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
    api_instance = canvas_lms_python_client.AccountsApi(api_client)

    try:
        # List environment settings
        api_response = await api_instance.accounts_environment()
        print("The response of AccountsApi->accounts_environment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->accounts_environment: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AccountsEnvironmentResponse**](AccountsEnvironmentResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | AccountsEnvironmentResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_help_links**
> HelpLinks accounts_help_links(account_id)

Get help links

Returns the help links for that account

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.help_links import HelpLinks
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
    api_instance = canvas_lms_python_client.AccountsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id

    try:
        # Get help links
        api_response = await api_instance.accounts_help_links(account_id)
        print("The response of AccountsApi->accounts_help_links:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->accounts_help_links: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 

### Return type

[**HelpLinks**](HelpLinks.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | HelpLinks |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_horizon_accounts**
> List[Account] accounts_horizon_accounts(include=include, page=page, per_page=per_page)

List horizon accounts

A paginated list of horizon accounts that the current user can view or manage.
Returns all accounts with the horizon_account setting enabled. If there are any
horizon accounts and the user has access to Site Admin, Site Admin will also be
included in the results.

Typically, students and even teachers will get an empty list in response,
only account admins can view the accounts that they are in.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.account import Account
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
    api_instance = canvas_lms_python_client.AccountsApi(api_client)
    include = ['include_example'] # List[str] | Array of additional information to include.  \"lti_guid\":: the 'tool_consumer_instance_guid' that will be sent for this account on LTI launches \"registration_settings\":: returns info about the privacy policy and terms of use \"services\":: returns services and whether they are enabled (requires account management permissions) \"course_count\":: returns the number of courses directly under each account \"sub_account_count\":: returns the number of sub-accounts directly under each account \"site_admin\":: returns true if the account is the Site Admin account (only included if true) (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List horizon accounts
        api_response = await api_instance.accounts_horizon_accounts(include=include, page=page, per_page=per_page)
        print("The response of AccountsApi->accounts_horizon_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->accounts_horizon_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | [**List[str]**](str.md)| Array of additional information to include.  \&quot;lti_guid\&quot;:: the &#39;tool_consumer_instance_guid&#39; that will be sent for this account on LTI launches \&quot;registration_settings\&quot;:: returns info about the privacy policy and terms of use \&quot;services\&quot;:: returns services and whether they are enabled (requires account management permissions) \&quot;course_count\&quot;:: returns the number of courses directly under each account \&quot;sub_account_count\&quot;:: returns the number of sub-accounts directly under each account \&quot;site_admin\&quot;:: returns true if the account is the Site Admin account (only included if true) | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[Account]**](Account.md)

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

# **accounts_index**
> List[Account] accounts_index(include=include, page=page, per_page=per_page)

List accounts

A paginated list of accounts that the current user can view or manage.
Typically, students and even teachers will get an empty list in response,
only account admins can view the accounts that they are in.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.account import Account
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
    api_instance = canvas_lms_python_client.AccountsApi(api_client)
    include = ['include_example'] # List[str] | Array of additional information to include.  \"lti_guid\":: the 'tool_consumer_instance_guid' that will be sent for this account on LTI launches \"registration_settings\":: returns info about the privacy policy and terms of use \"services\":: returns services and whether they are enabled (requires account management permissions) \"course_count\":: returns the number of courses directly under each account \"sub_account_count\":: returns the number of sub-accounts directly under each account (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List accounts
        api_response = await api_instance.accounts_index(include=include, page=page, per_page=per_page)
        print("The response of AccountsApi->accounts_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->accounts_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | [**List[str]**](str.md)| Array of additional information to include.  \&quot;lti_guid\&quot;:: the &#39;tool_consumer_instance_guid&#39; that will be sent for this account on LTI launches \&quot;registration_settings\&quot;:: returns info about the privacy policy and terms of use \&quot;services\&quot;:: returns services and whether they are enabled (requires account management permissions) \&quot;course_count\&quot;:: returns the number of courses directly under each account \&quot;sub_account_count\&quot;:: returns the number of sub-accounts directly under each account | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[Account]**](Account.md)

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

# **accounts_manageable_accounts**
> List[Account] accounts_manageable_accounts(page=page, per_page=per_page)

Get accounts that admins can manage

A paginated list of accounts where the current user has permission to create
or manage courses. List will be empty for students and teachers as only admins
can view which accounts they are in.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.account import Account
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
    api_instance = canvas_lms_python_client.AccountsApi(api_client)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # Get accounts that admins can manage
        api_response = await api_instance.accounts_manageable_accounts(page=page, per_page=per_page)
        print("The response of AccountsApi->accounts_manageable_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->accounts_manageable_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[Account]**](Account.md)

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

# **accounts_manually_created_courses_account**
> Account accounts_manually_created_courses_account()

Get the manually-created courses sub-account for the domain root account

Returns the sub-account that contains manually created courses for the domain root account.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.account import Account
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
    api_instance = canvas_lms_python_client.AccountsApi(api_client)

    try:
        # Get the manually-created courses sub-account for the domain root account
        api_response = await api_instance.accounts_manually_created_courses_account()
        print("The response of AccountsApi->accounts_manually_created_courses_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->accounts_manually_created_courses_account: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Account**](Account.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Account |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_permissions**
> AccountsPermissionsResponse accounts_permissions(account_id, permissions=permissions)

Permissions

Returns permission information for the calling user and the given account.
You may use `self` as the account id to check permissions against the domain root account.
The caller must have an account role or admin (teacher/TA/designer) enrollment in a course
in the account.

See also the {api:CoursesController#permissions Course} and {api:GroupsController#permissions Group}
counterparts.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.accounts_permissions_response import AccountsPermissionsResponse
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
    api_instance = canvas_lms_python_client.AccountsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    permissions = ['permissions_example'] # List[str] | List of permissions to check against the authenticated user. Permission names are documented in the {api:RoleOverridesController#manageable_permissions List assignable permissions} endpoint. (optional)

    try:
        # Permissions
        api_response = await api_instance.accounts_permissions(account_id, permissions=permissions)
        print("The response of AccountsApi->accounts_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->accounts_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **permissions** | [**List[str]**](str.md)| List of permissions to check against the authenticated user. Permission names are documented in the {api:RoleOverridesController#manageable_permissions List assignable permissions} endpoint. | [optional] 

### Return type

[**AccountsPermissionsResponse**](AccountsPermissionsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | AccountsPermissionsResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_remove_user**
> AccountsRemoveUserResponse accounts_remove_user(account_id, user_id)

Delete a user from the root account

Delete a user record from a Canvas root account. If a user is associated
with multiple root accounts (in a multi-tenant instance of Canvas), this
action will NOT remove them from the other accounts.

WARNING: This API will allow a user to remove themselves from the account.
If they do this, they won't be able to make API calls or log into Canvas at
that account.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.accounts_remove_user_response import AccountsRemoveUserResponse
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
    api_instance = canvas_lms_python_client.AccountsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # Delete a user from the root account
        api_response = await api_instance.accounts_remove_user(account_id, user_id)
        print("The response of AccountsApi->accounts_remove_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->accounts_remove_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **user_id** | **str**| Scope response to user_id | 

### Return type

[**AccountsRemoveUserResponse**](AccountsRemoveUserResponse.md)

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

# **accounts_remove_users**
> Progress accounts_remove_users(account_id)

Delete multiple users from the root account

Delete multiple users from a Canvas root account. If a user is associated
with multiple root accounts (in a multi-tenant instance of Canvas), this
action will NOT remove them from the other accounts.

WARNING: This API will allow a user to remove themselves from the account.
If they do this, they won't be able to make API calls or log into Canvas at
that account.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.progress import Progress
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
    api_instance = canvas_lms_python_client.AccountsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id

    try:
        # Delete multiple users from the root account
        api_response = await api_instance.accounts_remove_users(account_id)
        print("The response of AccountsApi->accounts_remove_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->accounts_remove_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 

### Return type

[**Progress**](Progress.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Progress |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_restore_user**
> User accounts_restore_user(account_id, user_id)

Restore a deleted user from a root account

Restore a user record along with the most recently deleted pseudonym
from a Canvas root account.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.user import User
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
    api_instance = canvas_lms_python_client.AccountsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # Restore a deleted user from a root account
        api_response = await api_instance.accounts_restore_user(account_id, user_id)
        print("The response of AccountsApi->accounts_restore_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->accounts_restore_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **user_id** | **str**| Scope response to user_id | 

### Return type

[**User**](User.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | User |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_show**
> Account accounts_show(id)

Get a single account

Retrieve information on an individual account, given by id or sis
sis_account_id.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.account import Account
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
    api_instance = canvas_lms_python_client.AccountsApi(api_client)
    id = 'id_example' # str | Scope response to id

    try:
        # Get a single account
        api_response = await api_instance.accounts_show(id)
        print("The response of AccountsApi->accounts_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->accounts_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 

### Return type

[**Account**](Account.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Account |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_show_settings**
> AccountsShowSettingsResponse accounts_show_settings(account_id)

Settings

Returns a JSON object containing a subset of settings for the specified account.
It's possible an empty set will be returned if no settings are applicable.
The caller must be an Account admin with the manage_account_settings permission.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.accounts_show_settings_response import AccountsShowSettingsResponse
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
    api_instance = canvas_lms_python_client.AccountsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id

    try:
        # Settings
        api_response = await api_instance.accounts_show_settings(account_id)
        print("The response of AccountsApi->accounts_show_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->accounts_show_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 

### Return type

[**AccountsShowSettingsResponse**](AccountsShowSettingsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | AccountsShowSettingsResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_sub_accounts**
> List[Account] accounts_sub_accounts(account_id, recursive=recursive, order=order, include=include, page=page, per_page=per_page)

Get the sub-accounts of an account

List accounts that are sub-accounts of the given account.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.account import Account
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
    api_instance = canvas_lms_python_client.AccountsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    recursive = True # bool | If true, the entire account tree underneath this account will be returned (though still paginated). If false, only direct sub-accounts of this account will be returned. Defaults to false. (optional)
    order = 'order_example' # str | Sorts the accounts by id or name. Only applies when recursive is false. Defaults to id. (optional)
    include = ['include_example'] # List[str] | Array of additional information to include.  \"course_count\":: returns the number of courses directly under each account \"sub_account_count\":: returns the number of sub-accounts directly under each account (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # Get the sub-accounts of an account
        api_response = await api_instance.accounts_sub_accounts(account_id, recursive=recursive, order=order, include=include, page=page, per_page=per_page)
        print("The response of AccountsApi->accounts_sub_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->accounts_sub_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **recursive** | **bool**| If true, the entire account tree underneath this account will be returned (though still paginated). If false, only direct sub-accounts of this account will be returned. Defaults to false. | [optional] 
 **order** | **str**| Sorts the accounts by id or name. Only applies when recursive is false. Defaults to id. | [optional] 
 **include** | [**List[str]**](str.md)| Array of additional information to include.  \&quot;course_count\&quot;:: returns the number of courses directly under each account \&quot;sub_account_count\&quot;:: returns the number of sub-accounts directly under each account | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[Account]**](Account.md)

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

# **accounts_terms_of_service**
> TermsOfService accounts_terms_of_service(account_id)

Get the Terms of Service

Returns the terms of service for that account

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.terms_of_service import TermsOfService
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
    api_instance = canvas_lms_python_client.AccountsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id

    try:
        # Get the Terms of Service
        api_response = await api_instance.accounts_terms_of_service(account_id)
        print("The response of AccountsApi->accounts_terms_of_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->accounts_terms_of_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 

### Return type

[**TermsOfService**](TermsOfService.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | TermsOfService |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_update**
> Account accounts_update(id, accounts_update_request=accounts_update_request)

Update an account

Update an existing account.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.account import Account
from canvas_lms_python_client.models.accounts_update_request import AccountsUpdateRequest
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
    api_instance = canvas_lms_python_client.AccountsApi(api_client)
    id = 'id_example' # str | Scope response to id
    accounts_update_request = canvas_lms_python_client.AccountsUpdateRequest() # AccountsUpdateRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/accounts/<account_id> \\   -X PUT \\   -H 'Authorization: Bearer <token>' \\   -d 'account[name]=New account name' \\   -d 'account[default_time_zone]=Mountain Time (US & Canada)' \\   -d 'account[default_storage_quota_mb]=450' ``` (optional)

    try:
        # Update an account
        api_response = await api_instance.accounts_update(id, accounts_update_request=accounts_update_request)
        print("The response of AccountsApi->accounts_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->accounts_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **accounts_update_request** | [**AccountsUpdateRequest**](AccountsUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/accounts/&lt;account_id&gt; \\   -X PUT \\   -H &#39;Authorization: Bearer &lt;token&gt;&#39; \\   -d &#39;account[name]&#x3D;New account name&#39; \\   -d &#39;account[default_time_zone]&#x3D;Mountain Time (US &amp; Canada)&#39; \\   -d &#39;account[default_storage_quota_mb]&#x3D;450&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**Account**](Account.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Account |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_update_users**
> Progress accounts_update_users(account_id, accounts_update_users_request=accounts_update_users_request)

Update multiple users

Updates multiple users in bulk.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.accounts_update_users_request import AccountsUpdateUsersRequest
from canvas_lms_python_client.models.progress import Progress
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
    api_instance = canvas_lms_python_client.AccountsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    accounts_update_users_request = canvas_lms_python_client.AccountsUpdateUsersRequest() # AccountsUpdateUsersRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/accounts/3/users/bulk_update \\   -X PUT \\   -H 'Authorization: Bearer <token>' \\   -d 'user_ids[]=1' \\   -d 'user_ids[]=2' \\   -d 'user[event]=suspend' ``` (optional)

    try:
        # Update multiple users
        api_response = await api_instance.accounts_update_users(account_id, accounts_update_users_request=accounts_update_users_request)
        print("The response of AccountsApi->accounts_update_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->accounts_update_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **accounts_update_users_request** | [**AccountsUpdateUsersRequest**](AccountsUpdateUsersRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/accounts/3/users/bulk_update \\   -X PUT \\   -H &#39;Authorization: Bearer &lt;token&gt;&#39; \\   -d &#39;user_ids[]&#x3D;1&#39; \\   -d &#39;user_ids[]&#x3D;2&#39; \\   -d &#39;user[event]&#x3D;suspend&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**Progress**](Progress.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Progress |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

