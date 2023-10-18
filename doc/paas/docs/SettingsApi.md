# openapi_client.SettingsApi

All URIs are relative to *https://api.iran.liara.ir*

Method | HTTP request | Description
------------- | ------------- | -------------
[**default_subdomain**](SettingsApi.md#default_subdomain) | **POST** /v1/projects/{id}/default-subdomain/{status} | Default subdomain
[**ip_static**](SettingsApi.md#ip_static) | **POST** /v1/projects/{id}/fixed-ip/{status} | IP static
[**update_envs**](SettingsApi.md#update_envs) | **POST** /v1/projects/update-envs | Update envs
[**zero_downtime**](SettingsApi.md#zero_downtime) | **POST** /v1/projects/{id}/zero-downtime/{status} | Zero downtime


# **default_subdomain**
> default_subdomain(id, status)

Default subdomain

default subdomain that user owns

### Example

* Api Key Authentication (jwt):
```python
import paas.openapi_client
from paas.openapi_client.rest import ApiException
from pprint import pprint

with paas.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = paas.openapi_client.SettingsApi(api_client)
    id = 'id_example'
    status = 'status_example'
    
    try:
        api_instance.default_subdomain(id, status)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **status** | **str**| disable or enable | 

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

# **ip_static**
> IpStatic200Response ip_static(id, status)

IP static

ip static that user owns

### Example

* Api Key Authentication (jwt):
```python
import paas.openapi_client
from paas.openapi_client.models.ip_static200_response import IpStatic200Response
from paas.openapi_client.rest import ApiException
from pprint import pprint

with paas.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = paas.openapi_client.SettingsApi(api_client)
    id = 'id_example'
    status = 'status_example'
    
    try:
        api_response: IpStatic200Response = api_instance.ip_static(id, status)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **status** | **str**| disable or enable | 

### Return type

[**IpStatic200Response**](IpStatic200Response.md)

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
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_envs**
> UpdateEnvs200Response update_envs(update_envs)

Update envs

update envs that user owns

### Example

* Api Key Authentication (jwt):
```python
import paas.openapi_client
from paas.openapi_client.models.update_envs import UpdateEnvs
from paas.openapi_client.models.update_envs200_response import UpdateEnvs200Response
from paas.openapi_client.rest import ApiException
from pprint import pprint

with paas.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = paas.openapi_client.SettingsApi(api_client)
    update_envs: UpdateEnvs = paas.openapi_client.UpdateEnvs()
    update_envs.project = 'project_example'
    update_envs.variables = [
        {
            "key": "key_example",
            "value": "value_example"
        }
    ]
    
    try:
        api_response: UpdateEnvs200Response = api_instance.update_envs(update_envs)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_envs** | [**UpdateEnvs**](UpdateEnvs.md)|  | 

### Return type

[**UpdateEnvs200Response**](UpdateEnvs200Response.md)

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

# **zero_downtime**
> zero_downtime(id, status)

Zero downtime

zero downtime that user owns

### Example

* Api Key Authentication (jwt):
```python
import paas.openapi_client
from paas.openapi_client.rest import ApiException
from pprint import pprint

with paas.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = paas.openapi_client.SettingsApi(api_client)
    id = 'id_example'
    status = 'status_example'
    
    try:
        api_instance.zero_downtime(id, status)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **status** | **str**| disable or enable | 

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

