# openapi_client.DnsRecordApi

All URIs are relative to *https://dns-service.iran.liara.ir*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dns_record**](DnsRecordApi.md#create_dns_record) | **POST** /api/v1/zones/{zone}/dns-records | Create dns record
[**delete_dns_record**](DnsRecordApi.md#delete_dns_record) | **DELETE** /api/v1/zones/{zone}/dns-records/{id} | delete dns record
[**edit_dns_record**](DnsRecordApi.md#edit_dns_record) | **PUT** /api/v1/zones/{zone}/dns-records/{id} | edit dns record
[**get_dns_record**](DnsRecordApi.md#get_dns_record) | **GET** /api/v1/zones/{zone}/dns-records/{id} | Get dns record
[**get_list_dns_records**](DnsRecordApi.md#get_list_dns_records) | **GET** /api/v1/zones/{zone}/dns-records | Get all dns record


# **create_dns_record**
> DnsRecordResponse create_dns_record(zone, dns_record)

Create dns record

Creates a new dns record, returns the dns record on creation

### Example

* Api Key Authentication (jwt):
```python
import dns.openapi_client
from dns.openapi_client.models.dns_record_response import DnsRecordResponse
from dns.openapi_client.models.dns_record import DnsRecord
from dns.openapi_client.rest import ApiException
from pprint import pprint

with dns.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = dns.openapi_client.DnsRecordApi(api_client)
    zone = 'example.com'
    dns_record: DnsRecord = dns.openapi_client.DnsRecord(
        name = "test", type = "A", ttl = 3600, contents = [{
            "ip": "1.2.3.4"
        }]
    )
    
    try:
        api_response: DnsRecordResponse = api_instance.create_dns_record(zone, dns_record)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone** | **str**| The name of the zone to delete | 
 **dns_record** | [**DnsRecord**](DnsRecord.md)|  | 

### Return type

[**DnsRecordResponse**](DnsRecordResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful operation |  -  |
**400** | Bad request |  -  |
**401** | Missing authentication |  -  |
**404** | Zone does not exists. |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dns_record**
> delete_dns_record(zone, id)

delete dns record

Delete dns record from this zone

### Example

* Api Key Authentication (jwt):
```python
import dns.openapi_client
from dns.openapi_client.rest import ApiException

with dns.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = dns.openapi_client.DnsRecordApi(api_client)
    zone = 'example.com'
    id = 'example-id'
    
    try:
        api_instance.delete_dns_record(zone, id)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone** | **str**| The name of the zone to delete dns record | 
 **id** | **str**| The id of dns record to delete its data | 

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
**204** | Successful operation |  -  |
**400** | Bad request |  -  |
**401** | Missing authentication |  -  |
**404** | Zone does not exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_dns_record**
> DnsRecordResponse edit_dns_record(zone, id, dns_record)

edit dns record

you can not edit type of dns record

### Example

* Api Key Authentication (jwt):
```python
import dns.openapi_client
from dns.openapi_client.models.dns_record_response import DnsRecordResponse
from dns.openapi_client.models.dns_record import DnsRecord
from dns.openapi_client.rest import ApiException
from pprint import pprint

with dns.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = dns.openapi_client.DnsRecordApi(api_client)
    zone = 'example.com'
    id = 'example-id'
    dns_record: DnsRecord = dns.openapi_client.DnsRecord(
        name = "tesst", type = "A", ttl = 7200, contents = [{
            "ip": "4.3.2.1"
        }]
    )
    
    try:
        api_response: DnsRecordResponse = api_instance.edit_dns_record(zone, id, dns_record)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone** | **str**| The name of the zone to edit dns record | 
 **id** | **str**| The id of dns record to edit its data | 
 **dns_record** | [**DnsRecord**](DnsRecord.md)|  | 

### Return type

[**DnsRecordResponse**](DnsRecordResponse.md)

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
**404** | Zone does not exists. |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dns_record**
> DnsRecordResponse get_dns_record(zone, id)

Get dns record

Get Dns Record data on this zone

### Example

* Api Key Authentication (jwt):
```python
import dns.openapi_client
from dns.openapi_client.models.dns_record_response import DnsRecordResponse
from dns.openapi_client.rest import ApiException
from pprint import pprint

with dns.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = dns.openapi_client.DnsRecordApi(api_client)
    zone = 'example.com'
    id = 'example-id'
    
    try:
        api_response: DnsRecordResponse = api_instance.get_dns_record(zone, id)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone** | **str**| The name of the zone to see dns record | 
 **id** | **str**| The id of dns record to see its data | 

### Return type

[**DnsRecordResponse**](DnsRecordResponse.md)

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
**404** | Zone or dns record Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_dns_records**
> AllDnsRecordResponse get_list_dns_records(zone)

Get all dns record

Get all Dns Records on this zone

### Example

* Api Key Authentication (jwt):
```python
import dns.openapi_client
from dns.openapi_client.models.all_dns_record_response import AllDnsRecordResponse
from dns.openapi_client.rest import ApiException
from pprint import pprint

with dns.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = dns.openapi_client.DnsRecordApi(api_client)
    zone = 'example.com'
    
    try:
        api_response: AllDnsRecordResponse = api_instance.get_list_dns_records(zone)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone** | **str**| The name of the zone to see all dns records | 

### Return type

[**AllDnsRecordResponse**](AllDnsRecordResponse.md)

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
**404** | Zone Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

