# canvas_lms_python_client.OutcomeResultsApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**outcome_results_contributing_scores**](OutcomeResultsApi.md#outcome_results_contributing_scores) | **GET** /api/v1/courses/{course_id}/outcomes/{outcome_id}/contributing_scores | Get contributing scores
[**outcome_results_enqueue_outcome_rollup_calculation**](OutcomeResultsApi.md#outcome_results_enqueue_outcome_rollup_calculation) | **POST** /api/v1/enqueue_outcome_rollup_calculation | Enqueue a delayed Outcome Rollup Calculation Job
[**outcome_results_index**](OutcomeResultsApi.md#outcome_results_index) | **GET** /api/v1/courses/{course_id}/outcome_results | Get outcome results
[**outcome_results_mastery_distribution**](OutcomeResultsApi.md#outcome_results_mastery_distribution) | **GET** /api/v1/courses/{course_id}/outcome_mastery_distribution | Get mastery distribution
[**outcome_results_outcome_order**](OutcomeResultsApi.md#outcome_results_outcome_order) | **POST** /api/v1/courses/{course_id}/assign_outcome_order | Set outcome ordering for LMGB
[**outcome_results_rollups**](OutcomeResultsApi.md#outcome_results_rollups) | **GET** /api/v1/courses/{course_id}/outcome_rollups | Get outcome result rollups


# **outcome_results_contributing_scores**
> OutcomeResultsContributingScoresResponse outcome_results_contributing_scores(course_id, outcome_id, user_ids=user_ids, only_assignment_alignments=only_assignment_alignments, show_unpublished_assignments=show_unpublished_assignments)

Get contributing scores

Gets the contributing scores for a specific outcome and set of users.
Contributing scores are the individual assignment/quiz scores that
contributed to the outcome score for each user.

Returns all alignments for the outcome in the course context.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.outcome_results_contributing_scores_response import OutcomeResultsContributingScoresResponse
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
    api_instance = canvas_lms_python_client.OutcomeResultsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    outcome_id = 'outcome_id_example' # str | Scope response to outcome_id
    user_ids = [56] # List[int] | If specified, only the users whose ids are given will be included in the results. It is an error to specify an id for a user who is not a student in the context. (optional)
    only_assignment_alignments = True # bool | If specified, only assignment alignments will be included in the results. (optional)
    show_unpublished_assignments = True # bool | If true, unpublished assignments will be included in the results. Defaults to false. (optional)

    try:
        # Get contributing scores
        api_response = await api_instance.outcome_results_contributing_scores(course_id, outcome_id, user_ids=user_ids, only_assignment_alignments=only_assignment_alignments, show_unpublished_assignments=show_unpublished_assignments)
        print("The response of OutcomeResultsApi->outcome_results_contributing_scores:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutcomeResultsApi->outcome_results_contributing_scores: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **outcome_id** | **str**| Scope response to outcome_id | 
 **user_ids** | [**List[int]**](int.md)| If specified, only the users whose ids are given will be included in the results. It is an error to specify an id for a user who is not a student in the context. | [optional] 
 **only_assignment_alignments** | **bool**| If specified, only assignment alignments will be included in the results. | [optional] 
 **show_unpublished_assignments** | **bool**| If true, unpublished assignments will be included in the results. Defaults to false. | [optional] 

### Return type

[**OutcomeResultsContributingScoresResponse**](OutcomeResultsContributingScoresResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | OutcomeResultsContributingScoresResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **outcome_results_enqueue_outcome_rollup_calculation**
> RollupJob outcome_results_enqueue_outcome_rollup_calculation(outcome_results_enqueue_outcome_rollup_calculation_request=outcome_results_enqueue_outcome_rollup_calculation_request)

Enqueue a delayed Outcome Rollup Calculation Job

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.outcome_results_enqueue_outcome_rollup_calculation_request import OutcomeResultsEnqueueOutcomeRollupCalculationRequest
from canvas_lms_python_client.models.rollup_job import RollupJob
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
    api_instance = canvas_lms_python_client.OutcomeResultsApi(api_client)
    outcome_results_enqueue_outcome_rollup_calculation_request = canvas_lms_python_client.OutcomeResultsEnqueueOutcomeRollupCalculationRequest() # OutcomeResultsEnqueueOutcomeRollupCalculationRequest | Request body parameters (optional)

    try:
        # Enqueue a delayed Outcome Rollup Calculation Job
        api_response = await api_instance.outcome_results_enqueue_outcome_rollup_calculation(outcome_results_enqueue_outcome_rollup_calculation_request=outcome_results_enqueue_outcome_rollup_calculation_request)
        print("The response of OutcomeResultsApi->outcome_results_enqueue_outcome_rollup_calculation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutcomeResultsApi->outcome_results_enqueue_outcome_rollup_calculation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **outcome_results_enqueue_outcome_rollup_calculation_request** | [**OutcomeResultsEnqueueOutcomeRollupCalculationRequest**](OutcomeResultsEnqueueOutcomeRollupCalculationRequest.md)| Request body parameters | [optional] 

### Return type

[**RollupJob**](RollupJob.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | RollupJob |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **outcome_results_index**
> OutcomeResultsIndexResponse outcome_results_index(course_id, user_ids=user_ids, outcome_ids=outcome_ids, include=include, include_hidden=include_hidden, page=page, per_page=per_page)

Get outcome results

Gets the outcome results for users and outcomes in the specified context.

used in sLMGB

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.outcome_results_index_response import OutcomeResultsIndexResponse
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
    api_instance = canvas_lms_python_client.OutcomeResultsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    user_ids = [56] # List[int] | If specified, only the users whose ids are given will be included in the results. SIS ids can be used, prefixed by \"sis_user_id:\". It is an error to specify an id for a user who is not a student in the context. (optional)
    outcome_ids = [56] # List[int] | If specified, only the outcomes whose ids are given will be included in the results. it is an error to specify an id for an outcome which is not linked to the context. (optional)
    include = ['include_example'] # List[str] | Specify additional collections to be side loaded with the result. \"alignments\" includes only the alignments referenced by the returned results. \"outcomes.alignments\" includes all alignments referenced by outcomes in the context. (optional)
    include_hidden = True # bool | If true, results that are hidden from the learning mastery gradebook and student rollup scores will be included (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # Get outcome results
        api_response = await api_instance.outcome_results_index(course_id, user_ids=user_ids, outcome_ids=outcome_ids, include=include, include_hidden=include_hidden, page=page, per_page=per_page)
        print("The response of OutcomeResultsApi->outcome_results_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutcomeResultsApi->outcome_results_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **user_ids** | [**List[int]**](int.md)| If specified, only the users whose ids are given will be included in the results. SIS ids can be used, prefixed by \&quot;sis_user_id:\&quot;. It is an error to specify an id for a user who is not a student in the context. | [optional] 
 **outcome_ids** | [**List[int]**](int.md)| If specified, only the outcomes whose ids are given will be included in the results. it is an error to specify an id for an outcome which is not linked to the context. | [optional] 
 **include** | [**List[str]**](str.md)| Specify additional collections to be side loaded with the result. \&quot;alignments\&quot; includes only the alignments referenced by the returned results. \&quot;outcomes.alignments\&quot; includes all alignments referenced by outcomes in the context. | [optional] 
 **include_hidden** | **bool**| If true, results that are hidden from the learning mastery gradebook and student rollup scores will be included | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**OutcomeResultsIndexResponse**](OutcomeResultsIndexResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | OutcomeResultsIndexResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **outcome_results_mastery_distribution**
> MasteryDistributionResponse outcome_results_mastery_distribution(course_id, exclude=exclude, outcome_ids=outcome_ids, student_ids=student_ids, include=include, only_assignment_alignments=only_assignment_alignments, show_unpublished_assignments=show_unpublished_assignments, add_defaults=add_defaults)

Get mastery distribution

Returns the distribution of student scores across mastery levels for all outcomes.
This endpoint fetches data for ALL students (not paginated) to provide accurate
distribution statistics for charts and analytics.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.mastery_distribution_response import MasteryDistributionResponse
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
    api_instance = canvas_lms_python_client.OutcomeResultsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    exclude = ['exclude_example'] # List[str] | Optionally restrict which results are included: - \"missing_user_rollups\": exclude students without any scores - \"missing_outcome_results\": exclude outcomes without any results (optional)
    outcome_ids = ['outcome_ids_example'] # List[str] | Optionally restrict to specific outcome IDs (optional)
    student_ids = ['student_ids_example'] # List[str] | Optionally restrict to specific student IDs. If not provided, all students will be included. (optional)
    include = ['include_example'] # List[str] | Optionally include additional data: - \"alignment_distributions\": include contributing score distributions for alignments (optional)
    only_assignment_alignments = True # bool | If true and alignment_distributions is included, only include assignment alignments. Default: false. (optional)
    show_unpublished_assignments = True # bool | If true, include unpublished assignments in alignment distributions. Default: false. (optional)
    add_defaults = True # bool | If defaults are requested, then color and mastery level defaults will be added to outcome ratings in the result. This will only take effect if the Account Level Mastery Scales FF is DISABLED (optional)

    try:
        # Get mastery distribution
        api_response = await api_instance.outcome_results_mastery_distribution(course_id, exclude=exclude, outcome_ids=outcome_ids, student_ids=student_ids, include=include, only_assignment_alignments=only_assignment_alignments, show_unpublished_assignments=show_unpublished_assignments, add_defaults=add_defaults)
        print("The response of OutcomeResultsApi->outcome_results_mastery_distribution:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutcomeResultsApi->outcome_results_mastery_distribution: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **exclude** | [**List[str]**](str.md)| Optionally restrict which results are included: - \&quot;missing_user_rollups\&quot;: exclude students without any scores - \&quot;missing_outcome_results\&quot;: exclude outcomes without any results | [optional] 
 **outcome_ids** | [**List[str]**](str.md)| Optionally restrict to specific outcome IDs | [optional] 
 **student_ids** | [**List[str]**](str.md)| Optionally restrict to specific student IDs. If not provided, all students will be included. | [optional] 
 **include** | [**List[str]**](str.md)| Optionally include additional data: - \&quot;alignment_distributions\&quot;: include contributing score distributions for alignments | [optional] 
 **only_assignment_alignments** | **bool**| If true and alignment_distributions is included, only include assignment alignments. Default: false. | [optional] 
 **show_unpublished_assignments** | **bool**| If true, include unpublished assignments in alignment distributions. Default: false. | [optional] 
 **add_defaults** | **bool**| If defaults are requested, then color and mastery level defaults will be added to outcome ratings in the result. This will only take effect if the Account Level Mastery Scales FF is DISABLED | [optional] 

### Return type

[**MasteryDistributionResponse**](MasteryDistributionResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | MasteryDistributionResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **outcome_results_outcome_order**
> outcome_results_outcome_order(course_id)

Set outcome ordering for LMGB

Saves the ordering of outcomes in LMGB for a user

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
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
    api_instance = canvas_lms_python_client.OutcomeResultsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id

    try:
        # Set outcome ordering for LMGB
        await api_instance.outcome_results_outcome_order(course_id)
    except Exception as e:
        print("Exception when calling OutcomeResultsApi->outcome_results_outcome_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Set outcome ordering for LMGB |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **outcome_results_rollups**
> OutcomeResultsRollupsResponse outcome_results_rollups(course_id, aggregate=aggregate, aggregate_stat=aggregate_stat, user_ids=user_ids, outcome_ids=outcome_ids, include=include, exclude=exclude, sort_by=sort_by, sort_outcome_id=sort_outcome_id, sort_order=sort_order, add_defaults=add_defaults, contributing_scores=contributing_scores, page=page, per_page=per_page)

Get outcome result rollups

Gets the outcome rollups for the users and outcomes in the specified
context.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.outcome_results_rollups_response import OutcomeResultsRollupsResponse
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
    api_instance = canvas_lms_python_client.OutcomeResultsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    aggregate = 'aggregate_example' # str | If specified, instead of returning one rollup for each user, all the user rollups will be combined into one rollup for the course that will contain the average (or median, see below) rollup score for each outcome. (optional)
    aggregate_stat = 'aggregate_stat_example' # str | If aggregate rollups requested, then this value determines what statistic is used for the aggregate. Defaults to \"mean\" if this value is not specified. (optional)
    user_ids = [56] # List[int] | If specified, only the users whose ids are given will be included in the results or used in an aggregate result. it is an error to specify an id for a user who is not a student in the context (optional)
    outcome_ids = [56] # List[int] | If specified, only the outcomes whose ids are given will be included in the results. it is an error to specify an id for an outcome which is not linked to the context. (optional)
    include = ['include_example'] # List[str] | Specify additional collections to be side loaded with the result. (optional)
    exclude = ['exclude_example'] # List[str] | Specify additional values to exclude. \"missing_user_rollups\" excludes rollups for users without results. \"missing_outcome_results\" excludes outcomes without results. (optional)
    sort_by = 'sort_by_example' # str | If specified, sorts outcome result rollups. \"student\" sorting will sort by a user's sortable name. \"outcome\" sorting will sort by the given outcome's rollup score. The latter requires specifying the \"sort_outcome_id\" parameter. By default, the sort order is ascending. (optional)
    sort_outcome_id = 56 # int | If outcome sorting requested, then this determines which outcome to use for rollup score sorting. (optional)
    sort_order = 'sort_order_example' # str | If sorting requested, then this allows changing the default sort order of ascending to descending. (optional)
    add_defaults = True # bool | If defaults are requested, then color and mastery level defaults will be added to outcome ratings in the rollup. This will only take effect if the Account Level Mastery Scales FF is DISABLED (optional)
    contributing_scores = True # bool | **DEPRECATED**: This parameter is deprecated. Use the separate GET /api/v1/courses/:course_id/outcomes/:outcome_id/contributing_scores endpoint instead to fetch contributing scores for a specific outcome. If contributing scores are requested, then each individual outcome score will also include all graded artifacts that contributed to the outcome score (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # Get outcome result rollups
        api_response = await api_instance.outcome_results_rollups(course_id, aggregate=aggregate, aggregate_stat=aggregate_stat, user_ids=user_ids, outcome_ids=outcome_ids, include=include, exclude=exclude, sort_by=sort_by, sort_outcome_id=sort_outcome_id, sort_order=sort_order, add_defaults=add_defaults, contributing_scores=contributing_scores, page=page, per_page=per_page)
        print("The response of OutcomeResultsApi->outcome_results_rollups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutcomeResultsApi->outcome_results_rollups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **aggregate** | **str**| If specified, instead of returning one rollup for each user, all the user rollups will be combined into one rollup for the course that will contain the average (or median, see below) rollup score for each outcome. | [optional] 
 **aggregate_stat** | **str**| If aggregate rollups requested, then this value determines what statistic is used for the aggregate. Defaults to \&quot;mean\&quot; if this value is not specified. | [optional] 
 **user_ids** | [**List[int]**](int.md)| If specified, only the users whose ids are given will be included in the results or used in an aggregate result. it is an error to specify an id for a user who is not a student in the context | [optional] 
 **outcome_ids** | [**List[int]**](int.md)| If specified, only the outcomes whose ids are given will be included in the results. it is an error to specify an id for an outcome which is not linked to the context. | [optional] 
 **include** | [**List[str]**](str.md)| Specify additional collections to be side loaded with the result. | [optional] 
 **exclude** | [**List[str]**](str.md)| Specify additional values to exclude. \&quot;missing_user_rollups\&quot; excludes rollups for users without results. \&quot;missing_outcome_results\&quot; excludes outcomes without results. | [optional] 
 **sort_by** | **str**| If specified, sorts outcome result rollups. \&quot;student\&quot; sorting will sort by a user&#39;s sortable name. \&quot;outcome\&quot; sorting will sort by the given outcome&#39;s rollup score. The latter requires specifying the \&quot;sort_outcome_id\&quot; parameter. By default, the sort order is ascending. | [optional] 
 **sort_outcome_id** | **int**| If outcome sorting requested, then this determines which outcome to use for rollup score sorting. | [optional] 
 **sort_order** | **str**| If sorting requested, then this allows changing the default sort order of ascending to descending. | [optional] 
 **add_defaults** | **bool**| If defaults are requested, then color and mastery level defaults will be added to outcome ratings in the rollup. This will only take effect if the Account Level Mastery Scales FF is DISABLED | [optional] 
 **contributing_scores** | **bool**| **DEPRECATED**: This parameter is deprecated. Use the separate GET /api/v1/courses/:course_id/outcomes/:outcome_id/contributing_scores endpoint instead to fetch contributing scores for a specific outcome. If contributing scores are requested, then each individual outcome score will also include all graded artifacts that contributed to the outcome score | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**OutcomeResultsRollupsResponse**](OutcomeResultsRollupsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | OutcomeResultsRollupsResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

