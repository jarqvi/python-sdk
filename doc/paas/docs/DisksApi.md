# openapi_client.DisksApi

All URIs are relative to *https://api.iran.liara.ir*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_backup**](DisksApi.md#create_backup) | **POST** /v1/projects/{id}/disks/{name}/backups | Create backup disk
[**create_disk**](DisksApi.md#create_disk) | **POST** /v1/projects/{name}/disks | Create a disk
[**create_ftp**](DisksApi.md#create_ftp) | **POST** /v1/projects/{name}/disks/{dname}/ftp | Create ftp
[**delete_disk**](DisksApi.md#delete_disk) | **DELETE** /v1/projects/{id}/disks/{name} | Delete a disk
[**delete_ftp**](DisksApi.md#delete_ftp) | **DELETE** /v1/ftp/{fname} | Delete a ftp
[**download_backup**](DisksApi.md#download_backup) | **POST** /v1/projects/{id}/disks/{dname}/backups/manual/{bname}/download | Download backup disk
[**get_backups**](DisksApi.md#get_backups) | **GET** /v1/projects/{id}/disks/{name}/backups | Get backups disk
[**get_disks**](DisksApi.md#get_disks) | **GET** /v1/projects/{id}/disks | Get disks
[**get_ftps**](DisksApi.md#get_ftps) | **GET** /v1/projects/{name}/disks/{dname}/ftp | Get ftps
[**resize_disk**](DisksApi.md#resize_disk) | **POST** /v1/projects/{name}/disks/{dname}/resize | Resize disk


# **create_backup**
> create_backup(id, name)

Create backup disk

create backup disk that user owns

### Example

* Api Key Authentication (jwt):
```python
import paas.openapi_client
from paas.openapi_client.rest import ApiException
from pprint import pprint

with paas.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = paas.openapi_client.DisksApi(api_client)
    id = 'id_example'
    name = 'name_example'

    try:
        api_instance.create_backup(id, name)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of your app | 
 **name** | **str**| The name of your disk | 

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
**404** | App does not exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_disk**
> create_disk(name, disk)

Create a disk

create a disk that user owns

### Example

* Api Key Authentication (jwt):
```python
import paas.openapi_client
from paas.openapi_client.models.create_disk_request import CreateDiskRequest
from paas.openapi_client.rest import ApiException
from pprint import pprint

with paas.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = paas.openapi_client.DisksApi(api_client)
    name = 'name_example'
    disk: CreateDiskRequest = paas.openapi_client.CreateDiskRequest()
    disk.name = 'name_example' 
    disk.size = 'size_example' 

    try:
        api_instance.create_disk(name, disk)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of your app | 
 **disk** | [**CreateDiskRequest**](CreateDiskRequest.md)| The disk of your app | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful operation |  -  |
**400** | Bad request |  -  |
**401** | Missing authentication |  -  |
**404** | App does not exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ftp**
> CreateFtp200Response create_ftp(name, dname, create_ftp)

Create ftp

create ftp that user owns

### Example

* Api Key Authentication (jwt):
```python
import paas.openapi_client
from paas.openapi_client.models.create_ftp200_response import CreateFtp200Response
from paas.openapi_client.models.create_ftp_request import CreateFtpRequest
from paas.openapi_client.rest import ApiException
from pprint import pprint

with paas.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = paas.openapi_client.DisksApi(api_client)
    name = 'name_example' 
    dname = 'dname_example'
    create_ftp: CreateFtpRequest = paas.openapi_client.CreateFtpRequest()
    create_ftp.username = 'username_example'
    create_ftp.read_only = True

    try:
        api_response: CreateFtp200Response = api_instance.create_ftp(name, dname, create_ftp)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of your app | 
 **dname** | **str**| The name of your disk | 
 **create_ftp** | [**CreateFtpRequest**](CreateFtpRequest.md)| The plan of your app | 

### Return type

[**CreateFtp200Response**](CreateFtp200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request |  -  |
**401** | Missing authentication |  -  |
**404** | App does not exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_disk**
> delete_disk(id, name)

Delete a disk

delete a disk that user owns

### Example

* Api Key Authentication (jwt):
```python
import paas.openapi_client
from paas.openapi_client.rest import ApiException
from pprint import pprint

with paas.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = paas.openapi_client.DisksApi(api_client)
    id = 'id_example'
    name = 'name_example' 

    try:
        api_instance.delete_disk(id, name)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of your app | 
 **name** | **str**| The name of your disk of app | 

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
**404** | App does not exists. |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ftp**
> delete_ftp(fname)

Delete a ftp

delete a ftp that user owns

### Example

* Api Key Authentication (jwt):
```python
import paas.openapi_client
from paas.openapi_client.rest import ApiException
from pprint import pprint

with paas.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = paas.openapi_client.DisksApi(api_client)
    fname = 'fname_example'

    try:
        api_instance.delete_ftp(fname)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fname** | **str**| The name of your ftp | 

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
**404** | App does not exists. |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_backup**
> DownloadBackup200Response download_backup(id, dname, bname)

Download backup disk

download backup disk that user owns

### Example

* Api Key Authentication (jwt):
```python
import paas.openapi_client
from paas.openapi_client.models.download_backup200_response import DownloadBackup200Response
from paas.openapi_client.rest import ApiException
from pprint import pprint

with paas.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = paas.openapi_client.DisksApi(api_client)
    id = 'id_example'
    dname = 'dname_example'
    bname = 'bname_example'

    try:
        api_response: DownloadBackup200Response = api_instance.download_backup(id, dname, bname)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of your app | 
 **dname** | **str**| The name of your disk | 
 **bname** | **str**| The name of your backup | 

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
**404** | App does not exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_backups**
> GetDiskBackup get_backups(id, name)

Get backups disk

get backups disk that user owns

### Example

* Api Key Authentication (jwt):
```python
import paas.openapi_client
from paas.openapi_client.models.get_disk_backup import GetDiskBackup
from paas.openapi_client.rest import ApiException
from pprint import pprint

with paas.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = paas.openapi_client.DisksApi(api_client)
    id = 'id_example'
    name = 'name_example'

    try:
        api_response: GetDiskBackup = api_instance.get_backups(id, name)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of your app | 
 **name** | **str**| The name of your disk | 

### Return type

[**GetDiskBackup**](GetDiskBackup.md)

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
**404** | App does not exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_disks**
> GetDisks get_disks(id)

Get disks

get disks that user owns

### Example

* Api Key Authentication (jwt):
```python
import paas.openapi_client
from paas.openapi_client.models.get_disks import GetDisks
from paas.openapi_client.rest import ApiException
from pprint import pprint

with paas.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = paas.openapi_client.DisksApi(api_client)
    id = 'id_example'

    try:
        api_response: GetDisks = api_instance.get_disks(id)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of your app | 

### Return type

[**GetDisks**](GetDisks.md)

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
**404** | App does not exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ftps**
> GetFtps200Response get_ftps(name, dname)

Get ftps

get ftps that user owns

### Example

* Api Key Authentication (jwt):
```python
import paas.openapi_client
from paas.openapi_client.models.get_ftps200_response import GetFtps200Response
from paas.openapi_client.rest import ApiException
from pprint import pprint

with paas.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = paas.openapi_client.DisksApi(api_client)
    name = 'name_example'
    dname = 'dname_example'

    try:
        api_response: GetFtps200Response = api_instance.get_ftps(name, dname)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of your app | 
 **dname** | **str**| The name of your disk | 

### Return type

[**GetFtps200Response**](GetFtps200Response.md)

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
**404** | App does not exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resize_disk**
> resize_disk(name, dname, resize_disk)

Resize disk

resize disk that user owns

### Example

* Api Key Authentication (jwt):
```python
import paas.openapi_client
from paas.openapi_client.models.resize_disk_request import ResizeDiskRequest
from paas.openapi_client.rest import ApiException
from pprint import pprint

with paas.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = paas.openapi_client.DisksApi(api_client)
    name = 'name_example'
    dname = 'dname_example'
    resize_disk: ResizeDiskRequest = paas.openapi_client.ResizeDiskRequest()
    resize_disk.size = 'size_example'
    
    try:
        api_instance.resize_disk(name, dname, resize_disk)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of your app | 
 **dname** | **str**| The name of your disk | 
 **resize_disk** | [**ResizeDiskRequest**](ResizeDiskRequest.md)| The size of your disk | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request |  -  |
**401** | Missing authentication |  -  |
**404** | App does not exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

