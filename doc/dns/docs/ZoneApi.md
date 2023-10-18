# openapi_client.ZoneApi

All URIs are relative to *https://dns-service.iran.liara.ir*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_zone**](ZoneApi.md#create_zone) | **POST** /api/v1/zones | Create Zone
[**delete_zone**](ZoneApi.md#delete_zone) | **DELETE** /api/v1/zones/{zone} | Delete Zone
[**get_list_zones**](ZoneApi.md#get_list_zones) | **GET** /api/v1/zones | List all zones
[**get_zone**](ZoneApi.md#get_zone) | **GET** /api/v1/zones/{zone} | Get Zone


# **create_zone**
> CreateZone create_zone(zone_struct)

Create Zone

creates a new zone on dns server

### Example

* Api Key Authentication (jwt):
```python
import dns.openapi_client
from dns.openapi_client.models.create_zone import CreateZone
from dns.openapi_client.models.create_zone_request import CreateZoneRequest
from dns.openapi_client.rest import ApiException
from pprint import pprint

with dns.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = dns.openapi_client.ZoneApi(api_client)
    zone_struct: CreateZoneRequest = dns.openapi_client.CreateZoneRequest(name = "example.com")
    
    try:
        api_response: CreateZone = api_instance.create_zone(zone_struct)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_struct** | [**CreateZoneRequest**](CreateZoneRequest.md)| The zone to create | 

### Return type

[**CreateZone**](CreateZone.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Missing authentication |  -  |
**409** | Conflict |  -  |
**500** | server does not response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_zone**
> Submitted delete_zone(zone)

Delete Zone

Deletes this zone, all dns records

### Example

* Api Key Authentication (jwt):
```python
import dns.openapi_client
from dns.openapi_client.models.submitted import Submitted
from dns.openapi_client.rest import ApiException
from pprint import pprint

with dns.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = dns.openapi_client.ZoneApi(api_client)
    zone = 'example.com'
    
    try:
        api_response: Submitted = api_instance.delete_zone(zone)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone** | **str**| The name of the zone to delete | 

### Return type

[**Submitted**](Submitted.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Your request has been submitted. |  -  |
**204** | Zone deleted. |  -  |
**401** | Missing authentication |  -  |
**404** | Zone does not exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_zones**
> Zones get_list_zones()

List all zones

list all zones that user owns

### Example

* Api Key Authentication (jwt):
```python
import dns.openapi_client
from dns.openapi_client.models.zones import Zones
from dns.openapi_client.rest import ApiException
from pprint import pprint

with dns.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = dns.openapi_client.ZoneApi(api_client)
    try:
        api_response: Zones = api_instance.get_list_zones()
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters
This endpoint does not need any parameter.

### Return type

[**Zones**](Zones.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An server |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zone**
> CreateZone get_zone(zone)

Get Zone

Get this zone, all dns records

### Example

* Api Key Authentication (jwt):
```python
import dns.openapi_client
from dns.openapi_client.models.create_zone import CreateZone
from dns.openapi_client.rest import ApiException
from pprint import pprint

with dns.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = dns.openapi_client.ZoneApi(api_client)
    zone = 'example.com'
    
    try:
        api_response: CreateZone = api_instance.get_zone(zone)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone** | **str**| The name of the zone | 

### Return type

[**CreateZone**](CreateZone.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | zone details |  -  |
**401** | Missing authentication |  -  |
**404** | Zone does not exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

