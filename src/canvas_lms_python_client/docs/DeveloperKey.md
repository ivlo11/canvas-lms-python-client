# DeveloperKey

a Canvas API key (or LTI 1.3 registration)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The Canvas ID of the DeveloperKey object | [optional] 
**name** | **str** | The display name | [optional] 
**created_at** | **datetime** | Timestamp of the key&#39;s creation | [optional] 
**updated_at** | **datetime** | Timestamp of the key&#39;s last update | [optional] 
**workflow_state** | **str** | The state of the key | [optional] 
**is_lti_key** | **bool** | True if key represents an LTI 1.3 Registration. False for Canvas API keys | [optional] 
**email** | **str** | Contact email configured for key | [optional] 
**icon_url** | **str** | URL for a small icon to display in key list | [optional] 
**notes** | **str** | User-provided notes about key | [optional] 
**vendor_code** | **str** | User-specified code representing the vendor that uses the key | [optional] 
**account_name** | **str** | The name of the account that owns the key | [optional] 
**visible** | **bool** | True for all keys except Site Admin-level keys, which default to false. Controls visibility in the Inherited tab. | [optional] 
**scopes** | **List[str]** | List of API endpoints key is allowed to access (API keys), or LTI 1.3 scopes (LTI keys) | [optional] 
**redirect_uri** | **str** | Deprecated in favor of redirect_uris. Do not use. | [optional] 
**redirect_uris** | **List[str]** | List of URLs used during OAuth2 flow to validate given redirect URI (API keys), or to redirect to after login (LTI keys) | [optional] 
**access_token_count** | **int** | (API keys only) The number of active access tokens associated with the key | [optional] 
**last_used_at** | **datetime** | (API keys only) The last time an access token for this key was used in an API request | [optional] 
**test_cluster_only** | **bool** | (API keys only) If true, key is only usable in non-production environments (test, beta). Avoids problems with beta refresh. | [optional] 
**allow_includes** | **bool** | (API keys only) If true, allows &#x60;includes&#x60; parameters in API requests that match the scopes of this key | [optional] 
**require_scopes** | **bool** | (API keys only) If true, then token requests with this key must include scopes | [optional] 
**client_credentials_audience** | **str** | (API keys only) Used in OAuth2 client credentials flow to specify the audience for the access token | [optional] 
**api_key** | **str** | (API keys only) The client secret used in the OAuth authorization_code flow. | [optional] 
**tool_configuration** | [**LtiToolConfiguration**](LtiToolConfiguration.md) |  | [optional] 
**public_jwk** | **object** | (LTI keys only) The tool&#39;s public JWK in JSON format. Discouraged in favor of a url hosting a JWK set. | [optional] 
**public_jwk_url** | **str** | (LTI keys only) The tool-hosted URL containing its public JWK keyset. Canvas may cache JWKs up to 5 minutes. | [optional] 
**lti_registration** | **object** | (LTI keys only) The LTI IMS Registration object for this key, if key was created via Dynamic Registration. | [optional] 
**is_lti_registration** | **bool** | (LTI keys only) Returns true if key was created via Dynamic Registration. | [optional] 
**user_name** | **str** | Unused. | [optional] 
**user_id** | **str** | Unused. | [optional] 
**unified_tool_id** | **str** | Correlates an API key to a product configuration. | [optional] 

## Example

```python
from canvas_lms_python_client.models.developer_key import DeveloperKey

# TODO update the JSON string below
json = "{}"
# create an instance of DeveloperKey from a JSON string
developer_key_instance = DeveloperKey.from_json(json)
# print the JSON string representation of the object
print(DeveloperKey.to_json())

# convert the object into a dict
developer_key_dict = developer_key_instance.to_dict()
# create an instance of DeveloperKey from a dict
developer_key_from_dict = DeveloperKey.from_dict(developer_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


