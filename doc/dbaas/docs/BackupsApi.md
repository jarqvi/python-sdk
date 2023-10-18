# openapi_client.BackupsApi

All URIs are relative to *https://api.iran.liara.ir*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_backup**](BackupsApi.md#create_backup) | **POST** /v1/databases/{id}/backups | Backup a database
[**download_backup**](BackupsApi.md#download_backup) | **POST** /v1/databases/{id}/backups/{name}/download | Download a backup
[**get_list_backups**](BackupsApi.md#get_list_backups) | **GET** /v1/databases/{id}/backups | Get all backups


# **create_backup**
> create_backup(id)

Backup a database

backup a database that user owns

### Example

* Api Key Authentication (jwt):
```python
import dbaas.openapi_client
from dbaas.openapi_client.rest import ApiException
from pprint import pprint

with dbaas.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = dbaas.openapi_client.BackupsApi(api_client)
    id = 'id_example' 
    
    try:
        api_instance.create_backup(id)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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
**200** | Successful operation |  -  |
**400** | Bad request |  -  |
**401** | Missing authentication |  -  |
**404** | Database not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_backup**
> DownloadBackup200Response download_backup(id, name)

Download a backup

download a backup that user owns

### Example

* Api Key Authentication (jwt):
```python
import dbaas.openapi_client
from dbaas.openapi_client.models.download_backup200_response import DownloadBackup200Response
from dbaas.openapi_client.rest import ApiException
from pprint import pprint

with dbaas.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = dbaas.openapi_client.BackupsApi(api_client)
    id = 'id_example'
    name = 'name_example'
    
    try:
        api_response: DownloadBackup200Response = api_instance.download_backup(id, name)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of your database | 
 **name** | **str**| The name of your backup | 

### Return type

[**DownloadBackup200Response**](DownloadBackup200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request |  -  |
**401** | Missing authentication |  -  |
**404** | Database not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_backups**
> GetListBackups200Response get_list_backups(id)

Get all backups

get all backups that user owns

### Example

* Api Key Authentication (jwt):
```python
import dbaas.openapi_client
from dbaas.openapi_client.models.get_list_backups200_response import GetListBackups200Response
from dbaas.openapi_client.rest import ApiException
from pprint import pprint

with dbaas.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = dbaas.openapi_client.BackupsApi(api_client)
    id = 'id_example'
    
    try:
        api_response: GetListBackups200Response = api_instance.get_list_backups(id)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**GetListBackups200Response**](GetListBackups200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request |  -  |
**401** | Missing authentication |  -  |
**404** | Database not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

