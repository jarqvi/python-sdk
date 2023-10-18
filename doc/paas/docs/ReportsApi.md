# openapi_client.ReportsApi

All URIs are relative to *https://api.iran.liara.ir*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_app_cpu_reports**](ReportsApi.md#get_app_cpu_reports) | **GET** /v1/projects/{name}/metrics/cpu | Get cpu reports of app
[**get_app_memory_reports**](ReportsApi.md#get_app_memory_reports) | **GET** /v1/projects/{name}/metrics/memory | Get memory reports of app
[**get_app_network_receive_reports**](ReportsApi.md#get_app_network_receive_reports) | **GET** /v1/projects/{name}/metrics/network-receive | Get network-receive reports of app
[**get_app_summary_reports**](ReportsApi.md#get_app_summary_reports) | **GET** /v1/projects/{name}/metrics/summary | Get summary reports of app
[**get_network_transmit_reports**](ReportsApi.md#get_network_transmit_reports) | **GET** /v1/projects/{name}/metrics/network-transmit | Get network-transmit reports of app


# **get_app_cpu_reports**
> Reports get_app_cpu_reports(name, since)

Get cpu reports of app

get cpu reports of app that user owns

### Example

* Api Key Authentication (jwt):
```python
import paas.openapi_client
from paas.openapi_client.models.reports import Reports
from paas.openapi_client.rest import ApiException
from pprint import pprint

with paas.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = paas.openapi_client.ReportsApi(api_client)
    name = 'name_example'
    since = 3.4 
    
    try:
        api_response: Reports = api_instance.get_app_cpu_reports(name, since)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of your app | 
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
**404** | App does not exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_memory_reports**
> Reports get_app_memory_reports(name, since)

Get memory reports of app

get memory reports of app that user owns

### Example

* Api Key Authentication (jwt):
```python
import paas.openapi_client
from paas.openapi_client.models.reports import Reports
from paas.openapi_client.rest import ApiException
from pprint import pprint

with paas.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = paas.openapi_client.ReportsApi(api_client)
    name = 'name_example'
    since = 3.4 
    
    try:
        api_response: Reports = api_instance.get_app_memory_reports(name, since)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of your app | 
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
**404** | App does not exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_network_receive_reports**
> Reports get_app_network_receive_reports(name, since)

Get network-receive reports of app

get network-receive reports of app that user owns

### Example

* Api Key Authentication (jwt):
```python
import paas.openapi_client
from paas.openapi_client.models.reports import Reports
from paas.openapi_client.rest import ApiException
from pprint import pprint

with paas.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = paas.openapi_client.ReportsApi(api_client)
    name = 'name_example'
    since = 3.4 
    
    try:
        api_response: Reports = api_instance.get_app_network_receive_reports(name, since)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of your app | 
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
**404** | App does not exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_summary_reports**
> GetAppSummaryReports200Response get_app_summary_reports(name)

Get summary reports of app

get summary reports of app that user owns

### Example

* Api Key Authentication (jwt):
```python
import paas.openapi_client
from paas.openapi_client.models.get_app_summary_reports200_response import GetAppSummaryReports200Response
from paas.openapi_client.rest import ApiException
from pprint import pprint

with paas.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = paas.openapi_client.ReportsApi(api_client)
    name = 'name_example'
    
    try:
        api_response: GetAppSummaryReports200Response = api_instance.get_app_summary_reports(name)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of your app | 

### Return type

[**GetAppSummaryReports200Response**](GetAppSummaryReports200Response.md)

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

# **get_network_transmit_reports**
> Reports get_network_transmit_reports(name, since)

Get network-transmit reports of app

get network-transmit reports of app that user owns

### Example

* Api Key Authentication (jwt):
```python
import paas.openapi_client
from paas.openapi_client.models.reports import Reports
from paas.openapi_client.rest import ApiException
from pprint import pprint

with paas.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = paas.openapi_client.ReportsApi(api_client)
    name = 'name_example' 
    since = 3.4 
    
    try:
        api_response: Reports = api_instance.get_network_transmit_reports(name, since)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of your app | 
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
**404** | App does not exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

