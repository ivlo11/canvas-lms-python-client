# canvas_lms_python_client.AssessmentQuestionBanksApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assessment_question_banks_index**](AssessmentQuestionBanksApi.md#assessment_question_banks_index) | **GET** /api/v1/question_banks | List question banks
[**assessment_question_banks_questions**](AssessmentQuestionBanksApi.md#assessment_question_banks_questions) | **GET** /api/v1/question_banks/{id}/questions | List assessment questions for a question bank
[**assessment_question_banks_show**](AssessmentQuestionBanksApi.md#assessment_question_banks_show) | **GET** /api/v1/question_banks/{id} | Get a single question bank


# **assessment_question_banks_index**
> List[AssessmentQuestionBank] assessment_question_banks_index(context_type, context_id, include_question_count=include_question_count)

List question banks

Returns the paginated list of question banks for a given context.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.assessment_question_bank import AssessmentQuestionBank
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
    api_instance = canvas_lms_python_client.AssessmentQuestionBanksApi(api_client)
    context_type = 'context_type_example' # str | The type of context. Must be either \"Course\" or \"Account\".
    context_id = 56 # int | The id of the context.
    include_question_count = True # bool | Whether to include the number of questions in each bank. (optional)

    try:
        # List question banks
        api_response = await api_instance.assessment_question_banks_index(context_type, context_id, include_question_count=include_question_count)
        print("The response of AssessmentQuestionBanksApi->assessment_question_banks_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssessmentQuestionBanksApi->assessment_question_banks_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context_type** | **str**| The type of context. Must be either \&quot;Course\&quot; or \&quot;Account\&quot;. | 
 **context_id** | **int**| The id of the context. | 
 **include_question_count** | **bool**| Whether to include the number of questions in each bank. | [optional] 

### Return type

[**List[AssessmentQuestionBank]**](AssessmentQuestionBank.md)

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

# **assessment_question_banks_questions**
> List[AssessmentQuestion] assessment_question_banks_questions(id, page=page, per_page=per_page)

List assessment questions for a question bank

Returns the paginated list of assessment questions in this bank.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.assessment_question import AssessmentQuestion
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
    api_instance = canvas_lms_python_client.AssessmentQuestionBanksApi(api_client)
    id = 'id_example' # str | The question bank unique identifier.
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List assessment questions for a question bank
        api_response = await api_instance.assessment_question_banks_questions(id, page=page, per_page=per_page)
        print("The response of AssessmentQuestionBanksApi->assessment_question_banks_questions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssessmentQuestionBanksApi->assessment_question_banks_questions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The question bank unique identifier. | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[AssessmentQuestion]**](AssessmentQuestion.md)

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

# **assessment_question_banks_show**
> AssessmentQuestionBank assessment_question_banks_show(id, include_question_count=include_question_count)

Get a single question bank

Returns the question bank with the given id

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.assessment_question_bank import AssessmentQuestionBank
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
    api_instance = canvas_lms_python_client.AssessmentQuestionBanksApi(api_client)
    id = 'id_example' # str | The question bank unique identifier.
    include_question_count = True # bool | Whether to include the number of questions in the bank. (optional)

    try:
        # Get a single question bank
        api_response = await api_instance.assessment_question_banks_show(id, include_question_count=include_question_count)
        print("The response of AssessmentQuestionBanksApi->assessment_question_banks_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssessmentQuestionBanksApi->assessment_question_banks_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The question bank unique identifier. | 
 **include_question_count** | **bool**| Whether to include the number of questions in the bank. | [optional] 

### Return type

[**AssessmentQuestionBank**](AssessmentQuestionBank.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | AssessmentQuestionBank |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

