# openapi_client.ObjectApi

All URIs are relative to *https://storage-service.iran.liara.ir*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_object**](ObjectApi.md#delete_object) | **DELETE** /api/v1/buckets/{bucket}/objects/{prefix} | Delete Object
[**download_object**](ObjectApi.md#download_object) | **GET** /api/v1/buckets/{bucket}/download/${object} | Download Object
[**get_list_objects**](ObjectApi.md#get_list_objects) | **GET** /api/v1/buckets/{bucket}/objects/{prefix} | List Objects
[**get_stat_object**](ObjectApi.md#get_stat_object) | **GET** /api/v1/buckets/{bucket}/objects/statistics/{object} | Get Stat Object
[**upload_object**](ObjectApi.md#upload_object) | **GET** /api/v1/buckets/{bucket}/upload/{object} | Upload Object


# **delete_object**
> delete_object(bucket, prefix)

Delete Object

Delete an object from storage

### Example

* Api Key Authentication (jwt):
```python
import object_storage.openapi_client
from object_storage.openapi_client.rest import ApiException
from pprint import pprint

with object_storage.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = object_storage.openapi_client.ObjectApi(api_client)
    bucket = 'bucket_example' # str | 
    prefix = 'prefix_example'
    
    try:
        api_instance.delete_object(bucket, prefix)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**|  | 
 **prefix** | **str**|  | 

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

# **download_object**
> DownloadObject200Response download_object(bucket, object, expiry=expiry)

Download Object

Return presigned url for download object

### Example

* Api Key Authentication (jwt):
```python
import object_storage.openapi_client
from object_storage.openapi_client.models.download_object200_response import DownloadObject200Response
from object_storage.openapi_client.rest import ApiException
from pprint import pprint

with object_storage.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = object_storage.openapi_client.ObjectApi(api_client)
    bucket = 'bucket_example' 
    object = 'object_example' 
    expiry = 'expiry_example'
    
    try:
        api_response: DownloadObject200Response = api_instance.download_object(bucket, object, expiry=expiry)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**|  | 
 **object** | **str**| specify object path | 
 **expiry** | **str**| example: 2 days 7 hours 45 minutes | [optional] 

### Return type

[**DownloadObject200Response**](DownloadObject200Response.md)

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

# **get_list_objects**
> Objects get_list_objects(bucket, prefix, number=number, page=page)

List Objects

Return list of objects ( max:50, min:1 )

### Example

* Api Key Authentication (jwt):
```python
import object_storage.openapi_client
from object_storage.openapi_client.models.objects import Objects
from object_storage.openapi_client.rest import ApiException
from pprint import pprint

with object_storage.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = object_storage.openapi_client.ObjectApi(api_client)
    bucket = 'bucket_example'  
    prefix = 'prefix_example'  
    number = 'number_example' 
    page = 'page_example'
    
    try:
        api_response: Objects = api_instance.get_list_objects(bucket, prefix, number=number, page=page)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**|  | 
 **prefix** | **str**|  | 
 **number** | **str**| specify number of object ( max: 50, min: 1 ) | [optional] 
 **page** | **str**|  | [optional] 

### Return type

[**Objects**](Objects.md)

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

# **get_stat_object**
> Stat get_stat_object(bucket, object)

Get Stat Object

### Example

* Api Key Authentication (jwt):
```python
import object_storage.openapi_client
from object_storage.openapi_client.models.stat import Stat
from object_storage.openapi_client.rest import ApiException
from pprint import pprint

with object_storage.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = object_storage.openapi_client.ObjectApi(api_client)
    bucket = 'bucket_example'
    object = 'object_example'
    
    try:
        api_response: Stat = api_instance.get_stat_object(bucket, object)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**|  | 
 **object** | **str**|  | 

### Return type

[**Stat**](Stat.md)

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

# **upload_object**
> DownloadObject200Response upload_object(bucket, object)

Upload Object

Return presigned url for download object

### Example

* Api Key Authentication (jwt):
```python
import object_storage.openapi_client
from object_storage.openapi_client.models.download_object200_response import DownloadObject200Response
from object_storage.openapi_client.rest import ApiException
from pprint import pprint

with object_storage.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = object_storage.openapi_client.ObjectApi(api_client)
    bucket = 'bucket_example'
    object = 'object_example'
    
    try:
        api_response: DownloadObject200Response = api_instance.upload_object(bucket, object)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**|  | 
 **object** | **str**| specify object path | 

### Return type

[**DownloadObject200Response**](DownloadObject200Response.md)

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

