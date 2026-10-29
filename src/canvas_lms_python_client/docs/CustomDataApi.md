# canvas_lms_python_client.CustomDataApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**custom_data_delete_data**](CustomDataApi.md#custom_data_delete_data) | **DELETE** /api/v1/users/{user_id}/custom_data(/*scope) | Delete custom data
[**custom_data_get_data**](CustomDataApi.md#custom_data_get_data) | **GET** /api/v1/users/{user_id}/custom_data(/*scope) | Load custom data
[**custom_data_set_data**](CustomDataApi.md#custom_data_set_data) | **PUT** /api/v1/users/{user_id}/custom_data(/*scope) | Store custom data


# **custom_data_delete_data**
> custom_data_delete_data(user_id, ns)

Delete custom data

Delete custom user data.

Arbitrary JSON data can be stored for a User.  This API call
deletes that data for a given scope.  Without a scope, all custom_data is deleted.
See {api:UsersController#set_custom_data Store Custom Data} for details and
examples of storage and retrieval.

As an example, we'll store some data, then delete a subset of it.

Example {api:UsersController#set_custom_data PUT} with valid JSON data:
  curl 'https://<canvas>/api/v1/users/<user_id>/custom_data' \
    -X PUT \
    -F 'ns=com.my-organization.canvas-app' \
    -F 'data[fruit][apple]=so tasty' \
    -F 'data[fruit][kiwi]=a bit sour' \
    -F 'data[veggies][root][onion]=tear-jerking' \
    -H 'Authorization: Bearer <token>'

Response:
  !!!javascript
  {
    "data": {
      "fruit": {
        "apple": "so tasty",
        "kiwi": "a bit sour"
      },
      "veggies": {
        "root": {
          "onion": "tear-jerking"
        }
      }
    }
  }

Example DELETE:
  curl 'https://<canvas>/api/v1/users/<user_id>/custom_data/fruit/kiwi' \
    -X DELETE \
    -F 'ns=com.my-organization.canvas-app' \
    -H 'Authorization: Bearer <token>'

Response:
  !!!javascript
  {
    "data": "a bit sour"
  }

Example {api:UsersController#get_custom_data GET} following the above DELETE:
  curl 'https://<canvas>/api/v1/users/<user_id>/custom_data' \
    -X GET \
    -F 'ns=com.my-organization.canvas-app' \
    -H 'Authorization: Bearer <token>'

Response:
  !!!javascript
  {
    "data": {
      "fruit": {
        "apple": "so tasty"
      },
      "veggies": {
        "root": {
          "onion": "tear-jerking"
        }
      }
    }
  }

Note that hashes left empty after a DELETE will get removed from the custom_data store.
For example, following the previous commands, if we delete /custom_data/veggies/root/onion,
then the entire /custom_data/veggies scope will be removed.

Example DELETE that empties a parent scope:
  curl 'https://<canvas>/api/v1/users/<user_id>/custom_data/veggies/root/onion' \
    -X DELETE \
    -F 'ns=com.my-organization.canvas-app' \
    -H 'Authorization: Bearer <token>'

Response:
  !!!javascript
  {
    "data": "tear-jerking"
  }

Example {api:UsersController#get_custom_data GET} following the above DELETE:
  curl 'https://<canvas>/api/v1/users/<user_id>/custom_data' \
    -X GET \
    -F 'ns=com.my-organization.canvas-app' \
    -H 'Authorization: Bearer <token>'

Response:
  !!!javascript
  {
    "data": {
      "fruit": {
        "apple": "so tasty"
      }
    }
  }

On success, this endpoint returns an object containing the data that was deleted.

Responds with status code 400 if the namespace parameter, +ns+, is missing or invalid,
or if the specified scope does not contain any data.

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
    api_instance = canvas_lms_python_client.CustomDataApi(api_client)
    user_id = 'user_id_example' # str | Scope response to user_id
    ns = 'ns_example' # str | The namespace from which to delete the data.  This should be something other Canvas API apps aren't likely to use, such as a reverse DNS for your organization.

    try:
        # Delete custom data
        await api_instance.custom_data_delete_data(user_id, ns)
    except Exception as e:
        print("Exception when calling CustomDataApi->custom_data_delete_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Scope response to user_id | 
 **ns** | **str**| The namespace from which to delete the data.  This should be something other Canvas API apps aren&#39;t likely to use, such as a reverse DNS for your organization. | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Delete custom data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_data_get_data**
> custom_data_get_data(user_id, ns)

Load custom data

Load custom user data.

Arbitrary JSON data can be stored for a User.  This API call
retrieves that data for a (optional) given scope.
See {api:UsersController#set_custom_data Store Custom Data} for details and
examples.

On success, this endpoint returns an object containing the data that was requested.

Responds with status code 400 if the namespace parameter, +ns+, is missing or invalid,
or if the specified scope does not contain any data.

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
    api_instance = canvas_lms_python_client.CustomDataApi(api_client)
    user_id = 'user_id_example' # str | Scope response to user_id
    ns = 'ns_example' # str | The namespace from which to retrieve the data.  This should be something other Canvas API apps aren't likely to use, such as a reverse DNS for your organization.

    try:
        # Load custom data
        await api_instance.custom_data_get_data(user_id, ns)
    except Exception as e:
        print("Exception when calling CustomDataApi->custom_data_get_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Scope response to user_id | 
 **ns** | **str**| The namespace from which to retrieve the data.  This should be something other Canvas API apps aren&#39;t likely to use, such as a reverse DNS for your organization. | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Load custom data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_data_set_data**
> custom_data_set_data(user_id, custom_data_set_data_request=custom_data_set_data_request)

Store custom data

Store arbitrary user data as JSON.

Arbitrary JSON data can be stored for a User.
A typical scenario would be an external site/service that registers users in Canvas
and wants to capture additional info about them.  The part of the URL that follows
+/custom_data/+ defines the scope of the request, and it reflects the structure of
the JSON data to be stored or retrieved.

The value +self+ may be used for +user_id+ to store data associated with the calling user.
In order to access another user's custom data, you must be an account administrator with
permission to manage users.

A namespace parameter, +ns+, is used to prevent custom_data collisions between
different apps.  This parameter is required for all custom_data requests.

A request with Content-Type multipart/form-data or Content-Type
application/x-www-form-urlencoded can only be used to store strings.

Example PUT with multipart/form-data data:
  curl 'https://<canvas>/api/v1/users/<user_id>/custom_data/telephone' \
    -X PUT \
    -F 'ns=com.my-organization.canvas-app' \
    -F 'data=555-1234' \
    -H 'Authorization: Bearer <token>'

Response:
  !!!javascript
  {
    "data": "555-1234"
  }

Subscopes (or, generated scopes) can also be specified by passing values to
+data+[+subscope+].

Example PUT specifying subscopes:
  curl 'https://<canvas>/api/v1/users/<user_id>/custom_data/body/measurements' \
    -X PUT \
    -F 'ns=com.my-organization.canvas-app' \
    -F 'data[waist]=32in' \
    -F 'data[inseam]=34in' \
    -F 'data[chest]=40in' \
    -H 'Authorization: Bearer <token>'

Response:
  !!!javascript
  {
    "data": {
      "chest": "40in",
      "waist": "32in",
      "inseam": "34in"
    }
  }

Following such a request, subsets of the stored data to be retrieved directly from a subscope.

Example {api:UsersController#get_custom_data GET} from a generated scope
  curl 'https://<canvas>/api/v1/users/<user_id>/custom_data/body/measurements/chest' \
    -X GET \
    -F 'ns=com.my-organization.canvas-app' \
    -H 'Authorization: Bearer <token>'

Response:
  !!!javascript
  {
    "data": "40in"
  }

If you want to store more than just strings (i.e. numbers, arrays, hashes, true, false,
and/or null), you must make a request with Content-Type application/json as in the following
example.

Example PUT with JSON data:
  curl 'https://<canvas>/api/v1/users/<user_id>/custom_data' \
    -H 'Content-Type: application/json' \
    -X PUT \
    -d '{
          "ns": "com.my-organization.canvas-app",
          "data": {
            "a-number": 6.02e23,
            "a-bool": true,
            "a-string": "true",
            "a-hash": {"a": {"b": "ohai"}},
            "an-array": [1, "two", null, false]
          }
        }' \
    -H 'Authorization: Bearer <token>'

Response:
  !!!javascript
  {
    "data": {
      "a-number": 6.02e+23,
      "a-bool": true,
      "a-string": "true",
      "a-hash": {
        "a": {
          "b": "ohai"
        }
      },
      "an-array": [1, "two", null, false]
    }
  }

If the data is an Object (as it is in the above example), then subsets of the data can
be accessed by including the object's (possibly nested) keys in the scope of a GET request.

Example {api:UsersController#get_custom_data GET} with a generated scope:
  curl 'https://<canvas>/api/v1/users/<user_id>/custom_data/a-hash/a/b' \
    -X GET \
    -F 'ns=com.my-organization.canvas-app' \
    -H 'Authorization: Bearer <token>'

Response:
  !!!javascript
  {
    "data": "ohai"
  }


On success, this endpoint returns an object containing the data that was stored.

Responds with status code 200 if the scope already contained data, and it was overwritten
by the data specified in the request.

Responds with status code 201 if the scope was previously empty, and the data specified
in the request was successfully stored there.

Responds with status code 400 if the namespace parameter, +ns+, is missing or invalid, or if
the +data+ parameter is missing.

Responds with status code 409 if the requested scope caused a conflict and data was not stored.
This happens when storing data at the requested scope would cause data at an outer scope
to be lost.  e.g., if +/custom_data+ was +{"fashion_app": {"hair": "blonde"}}+, but
you tried to +`PUT /custom_data/fashion_app/hair/style -F data=buzz`+, then for the request
to succeed,the value of +/custom_data/fashion_app/hair+ would have to become a hash, and its
old string value would be lost.  In this situation, an error object is returned with the
following format:

  !!!javascript
  {
    "message": "write conflict for custom_data hash",
    "conflict_scope": "fashion_app/hair",
    "type_at_conflict": "String",
    "value_at_conflict": "blonde"
  }

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.custom_data_set_data_request import CustomDataSetDataRequest
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
    api_instance = canvas_lms_python_client.CustomDataApi(api_client)
    user_id = 'user_id_example' # str | Scope response to user_id
    custom_data_set_data_request = canvas_lms_python_client.CustomDataSetDataRequest() # CustomDataSetDataRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/users/<user_id>/custom_data/food_app' \\   -X PUT \\   -F 'ns=com.my-organization.canvas-app' \\   -F 'data[weight]=81kg' \\   -F 'data[favorites][meat]=pork belly' \\   -F 'data[favorites][dessert]=pistachio ice cream' \\   -H 'Authorization: Bearer <token>' ``` (optional)

    try:
        # Store custom data
        await api_instance.custom_data_set_data(user_id, custom_data_set_data_request=custom_data_set_data_request)
    except Exception as e:
        print("Exception when calling CustomDataApi->custom_data_set_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Scope response to user_id | 
 **custom_data_set_data_request** | [**CustomDataSetDataRequest**](CustomDataSetDataRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/users/&lt;user_id&gt;/custom_data/food_app&#39; \\   -X PUT \\   -F &#39;ns&#x3D;com.my-organization.canvas-app&#39; \\   -F &#39;data[weight]&#x3D;81kg&#39; \\   -F &#39;data[favorites][meat]&#x3D;pork belly&#39; \\   -F &#39;data[favorites][dessert]&#x3D;pistachio ice cream&#39; \\   -H &#39;Authorization: Bearer &lt;token&gt;&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Store custom data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

