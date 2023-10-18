# openapi_client.ReportsApi

All URIs are relative to *https://api.iran.liara.ir*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_database_cpu_reports**](ReportsApi.md#get_database_cpu_reports) | **GET** /v1/databases/{id}/metrics/cpu | Get cpu reports of database
[**get_database_memory_reports**](ReportsApi.md#get_database_memory_reports) | **GET** /v1/databases/{id}/metrics/memory | Get memory reports of database
[**get_database_network_receive_reports**](ReportsApi.md#get_database_network_receive_reports) | **GET** /v1/databases/{id}/metrics/network-receive | Get network-receive reports of database
[**get_database_network_transmit_reports**](ReportsApi.md#get_database_network_transmit_reports) | **GET** /v1/databases/{id}/metrics/network-transmit | Get network-transmit reports of database
[**get_database_summary_reports**](ReportsApi.md#get_database_summary_reports) | **GET** /v1/databases/{id}/metrics/summary | Get summary reports of database


# **get_database_cpu_reports**
> Reports get_database_cpu_reports(id, since)

Get cpu reports of database

get cpu reports of database that user owns

### Example

* Api Key Authentication (jwt):
```python
import dbaas.openapi_client
from dbaas.openapi_client.models.reports import Reports
from dbaas.openapi_client.rest import ApiException
from pprint import pprint

with dbaas.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = dbaas.openapi_client.ReportsApi(api_client)
    id = 'id_example'
    since = 3.4 
    
    try:
        api_response: Reports = api_instance.get_database_cpu_reports(id, since)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The name of your database | 
 **since** | **float**| The since of your cpu reports | 

### Return type

[**Reports**](Reports.md)

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
**404** | Database does not exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_database_memory_reports**
> Reports get_database_memory_reports(id, since)

Get memory reports of database

get memory reports of database that user owns

### Example

* Api Key Authentication (jwt):
```python
import dbaas.openapi_client
from dbaas.openapi_client.models.reports import Reports
from dbaas.openapi_client.rest import ApiException
from pprint import pprint

with dbaas.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = dbaas.openapi_client.ReportsApi(api_client)
    id = 'id_example'
    since = 3.4 
    
    try:
        api_response: Reports = api_instance.get_database_memory_reports(id, since)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The name of your database | 
 **since** | **float**| The since of your memory reports | 

### Return type

[**Reports**](Reports.md)

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
**404** | Database does not exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_database_network_receive_reports**
> Reports get_database_network_receive_reports(id, since)

Get network-receive reports of database

get network-receive reports of database that user owns

### Example

* Api Key Authentication (jwt):
```python
import dbaas.openapi_client
from dbaas.openapi_client.models.reports import Reports
from dbaas.openapi_client.rest import ApiException
from pprint import pprint

with dbaas.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = dbaas.openapi_client.ReportsApi(api_client)
    id = 'id_example'
    since = 3.4 
    
    try:
        api_response: Reports = api_instance.get_database_network_receive_reports(id, since)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The name of your database | 
 **since** | **float**| The since of your network-receive reports | 

### Return type

[**Reports**](Reports.md)

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
**404** | Database does not exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_database_network_transmit_reports**
> Reports get_database_network_transmit_reports(id, since)

Get network-transmit reports of database

get network-transmit reports of database that user owns

### Example

* Api Key Authentication (jwt):
```python
import dbaas.openapi_client
from dbaas.openapi_client.models.reports import Reports
from dbaas.openapi_client.rest import ApiException
from pprint import pprint

with dbaas.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = dbaas.openapi_client.ReportsApi(api_client)
    id = 'id_example'
    since = 3.4 
    
    try:
        api_response: Reports = api_instance.get_database_network_transmit_reports(id, since)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The name of your database | 
 **since** | **float**| The since of your network-transmit reports | 

### Return type

[**Reports**](Reports.md)

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
**404** | Database does not exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_database_summary_reports**
> GetDatabaseSummaryReports200Response get_database_summary_reports(id)

Get summary reports of database

get summary reports of database that user owns

### Example

* Api Key Authentication (jwt):
```python
import dbaas.openapi_client
from dbaas.openapi_client.models.get_database_summary_reports200_response import GetDatabaseSummaryReports200Response
from dbaas.openapi_client.rest import ApiException
from pprint import pprint

with dbaas.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = dbaas.openapi_client.ReportsApi(api_client)
    id = 'id_example'
    
    try:
        api_response: GetDatabaseSummaryReports200Response = api_instance.get_database_summary_reports(id)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The name of your database | 

### Return type

[**GetDatabaseSummaryReports200Response**](GetDatabaseSummaryReports200Response.md)

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
**404** | Database does not exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

