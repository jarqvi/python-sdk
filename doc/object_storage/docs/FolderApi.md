# openapi_client.FolderApi

All URIs are relative to *https://storage-service.iran.liara.ir*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_folder**](FolderApi.md#create_folder) | **POST** /api/v1/buckets/{bucket}/folders | Create Folder
[**delete_folder**](FolderApi.md#delete_folder) | **DELETE** /api/v1/buckets/{bucket}/folders | Delete Folder


# **create_folder**
> CreateFolder201Response create_folder(bucket, body)

Create Folder

Create Folder in Bucket

### Example

* Api Key Authentication (jwt):
```python
import object_storage.openapi_client
from object_storage.openapi_client.models.create_folder import CreateFolder
from object_storage.openapi_client.models.create_folder201_response import CreateFolder201Response
from object_storage.openapi_client.rest import ApiException
from pprint import pprint

with object_storage.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = object_storage.openapi_client.FolderApi(api_client)
    bucket = 'bucket_example' 
    body: CreateFolder = object_storage.openapi_client.CreateFolder(
        path = 'path_example'
    )
    
    try:
        api_response: CreateFolder201Response = api_instance.create_folder(bucket, body)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**|  | 
 **body** | [**CreateFolder**](CreateFolder.md)|  | 

### Return type

[**CreateFolder201Response**](CreateFolder201Response.md)

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
**409** | Conflict |  -  |
**500** | server does not response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_folder**
> delete_folder(bucket, path)

Delete Folder

Delete Folder in Bucket

### Example

* Api Key Authentication (jwt):
```python
import object_storage.openapi_client
from object_storage.openapi_client.rest import ApiException
from pprint import pprint

with object_storage.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = object_storage.openapi_client.FolderApi(api_client)
    bucket = 'bucket_example' 
    path = 'path_example'
    
    try:
        api_instance.delete_folder(bucket, path)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**|  | 
 **path** | **str**|  | 

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

