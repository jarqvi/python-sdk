# openapi_client.KeyApi

All URIs are relative to *https://storage-service.iran.liara.ir*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_key**](KeyApi.md#create_key) | **POST** /api/v1/keys | Create Keys
[**delete_key**](KeyApi.md#delete_key) | **DELETE** /api/v1/keys/{key} | Delete Key
[**get_key**](KeyApi.md#get_key) | **GET** /api/v1/keys/{key} | Get Key
[**get_list_keys**](KeyApi.md#get_list_keys) | **GET** /api/v1/keys | Get List of Keys
[**revoke_secret_key**](KeyApi.md#revoke_secret_key) | **PATCH** /api/v1/keys/{key}/revoke | Revoke secret key
[**update_key**](KeyApi.md#update_key) | **PATCH** /api/v1/keys/{key} | Update key


# **create_key**
> CreateKey201Response create_key(body)

Create Keys

Create access and secret key

### Example

* Api Key Authentication (jwt):
```python
import object_storage.openapi_client
from object_storage.openapi_client.models.create_key import CreateKey
from object_storage.openapi_client.models.create_key201_response import CreateKey201Response
from object_storage.openapi_client.rest import ApiException
from pprint import pprint

with object_storage.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = object_storage.openapi_client.FolderApi(api_client)
    body: CreateKey = object_storage.openapi_client.CreateKey(
        buckets = 'buckets_example',
        description = 'description_example'
    )
    
    try:
        api_response: CreateKey201Response = api_instance.create_key(body)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateKey**](CreateKey.md)| Declare Buckets for access key | 

### Return type

[**CreateKey201Response**](CreateKey201Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Missing authentication |  -  |
**404** | Not Found |  -  |
**500** | server does not response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_key**
> delete_key(key)

Delete Key

Delete access key

### Example

* Api Key Authentication (jwt):
```python
import object_storage.openapi_client
from object_storage.openapi_client.rest import ApiException
from pprint import pprint

with object_storage.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = object_storage.openapi_client.FolderApi(api_client)
    key = 'key_example'
    
    try:
        api_instance.delete_key(key)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Missing authentication |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**500** | server does not response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_key**
> get_key(key)

Get Key

Get a key

### Example

* Api Key Authentication (jwt):
```python
import object_storage.openapi_client
from object_storage.openapi_client.rest import ApiException
from pprint import pprint

with object_storage.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = object_storage.openapi_client.FolderApi(api_client)
    key = 'key_example'
    
    try:
        api_instance.get_key(key)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Missing authentication |  -  |
**404** | Not Found |  -  |
**500** | server does not response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_keys**
> Keys get_list_keys()

Get List of Keys

### Example

* Api Key Authentication (jwt):
```python
import object_storage.openapi_client
from object_storage.openapi_client.models.keys import Keys
from object_storage.openapi_client.rest import ApiException
from pprint import pprint

with object_storage.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = object_storage.openapi_client.FolderApi(api_client)
    
    try:
        api_response: Keys = api_instance.get_list_keys()
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters
This endpoint does not need any parameter.

### Return type

[**Keys**](Keys.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Missing authentication |  -  |
**404** | Not Found |  -  |
**500** | server does not response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_secret_key**
> RevokeSecretKey200Response revoke_secret_key(key)

Revoke secret key

Revoke secret key

### Example

* Api Key Authentication (jwt):
```python
import object_storage.openapi_client
from object_storage.openapi_client.models.revoke_secret_key200_response import RevokeSecretKey200Response
from object_storage.openapi_client.rest import ApiException
from pprint import pprint

with object_storage.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = object_storage.openapi_client.FolderApi(api_client)
    key = 'key_example' 
    
    try:
        api_response: RevokeSecretKey200Response = api_instance.revoke_secret_key(key)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | 

### Return type

[**RevokeSecretKey200Response**](RevokeSecretKey200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Missing authentication |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**500** | server does not response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_key**
> CreateBucket201Response update_key(key, body)

Update key

Update buckets of key ( redefine )

### Example

* Api Key Authentication (jwt):
```python
import object_storage.openapi_client
from object_storage.openapi_client.models.create_bucket201_response import CreateBucket201Response
from object_storage.openapi_client.models.create_key import CreateKey
from object_storage.openapi_client.rest import ApiException
from pprint import pprint

with object_storage.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = object_storage.openapi_client.FolderApi(api_client)
    key = 'key_example' 
    body: CreateKey = object_storage.openapi_client.CreateKey(
        buckets = [
            {}
        ],
        description = 'description_example'
    )
    
    try:
        api_response: CreateBucket201Response = api_instance.update_key(key, body)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | 
 **body** | [**CreateKey**](CreateKey.md)| Declare Buckets for access key | 

### Return type

[**CreateBucket201Response**](CreateBucket201Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Missing authentication |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**500** | server does not response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

